"""
Flask Web Application for Azure AI Bot
Provides a shareable web interface to interact with the Azure AI agent
"""
from flask import Flask, render_template, request, jsonify, session
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MessageRole
import uuid
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24).hex())

# Azure AI Project endpoint (configurable via environment variable)
myEndpoint = os.environ.get(
    'AZURE_AI_ENDPOINT',
    "https://foundarydec251219.services.ai.azure.com/api/projects/proj-default"
)

# Initialize the AI Project Client with DefaultAzureCredential
project_client = AIProjectClient(
    endpoint=myEndpoint,
    credential=DefaultAzureCredential(),
)

# Agent name (configurable via environment variable)
myAgent = os.environ.get('AZURE_AI_AGENT_NAME', 'bot')

# Get the agent
try:
    agent = project_client.agents.get_agent(myAgent)
    print(f"Successfully connected to agent: {agent.name}")
except Exception as e:
    print(f"Warning: Could not retrieve agent on startup: {e}")
    agent = None


@app.route('/')
def home():
    """Home page with chat interface"""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        # Check if agent is available
        if agent is None:
            return jsonify({'error': 'Agent is not available. Please check your Azure configuration.'}), 503
        
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Get or create thread ID for this session
        if 'thread_id' not in session:
            thread = project_client.agents.create_thread()
            session['thread_id'] = thread.id
        
        thread_id = session['thread_id']
        
        # Add user message to thread
        project_client.agents.create_message(
            thread_id=thread_id,
            role=MessageRole.USER,
            content=user_message
        )
        
        # Run the agent
        run = project_client.agents.create_and_process_run(
            thread_id=thread_id,
            assistant_id=agent.id
        )
        
        # Get the latest messages
        messages = project_client.agents.list_messages(thread_id=thread_id)
        
        # Find the assistant's response
        assistant_message = None
        for msg in messages:
            if msg.role == MessageRole.ASSISTANT:
                assistant_message = msg.content[0].text.value
                break
        
        return jsonify({
            'response': assistant_message or 'No response from agent',
            'thread_id': thread_id
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset the conversation"""
    session.pop('thread_id', None)
    return jsonify({'status': 'reset'})


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'agent': agent.name if agent else 'not connected',
        'endpoint': myEndpoint
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

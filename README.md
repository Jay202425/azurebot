# azurebot

Azure Bot using Azure AI Projects Agent

## Overview

This project implements a bot using Azure AI Projects with the Azure Agent service. It uses `DefaultAzureCredential` for authentication and connects to an Azure AI Project to retrieve an existing agent.

## Prerequisites

- Python 3.8 or higher
- Azure subscription with AI Projects enabled
- Proper Azure credentials configured (via environment variables, Azure CLI, managed identity, etc.)

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Web Application (Recommended for Sharing)

Run the Flask web application to get a shareable link:

```bash
python app.py
```

The web application will start on `http://localhost:5000` (or the port specified in the `PORT` environment variable).

**Features:**
- 🌐 Web-based chat interface
- 💬 Real-time conversation with Azure AI agent
- 🔄 Session management with conversation threads
- 📱 Responsive design for mobile and desktop
- 🔗 Shareable link for clients

**Deployment:**

For production deployment, you can deploy to:
- **Azure App Service**: Use the Azure Portal or Azure CLI
- **Azure Container Instances**: Containerize with Docker
- **Any cloud platform**: AWS, GCP, Heroku, etc.

Example for local testing:
```bash
export PORT=8080
python app.py
```

### Option 2: Command Line

Run the bot from command line:

```bash
python bot.py
```

## Configuration

The bot is configured to:
- Connect to the Azure AI Project endpoint: `https://foundarydec251219.services.ai.azure.com/api/projects/proj-default`
- Retrieve an existing agent named "bot"
- Use `DefaultAzureCredential` for authentication

## Authentication

The bot uses `DefaultAzureCredential` which attempts authentication through multiple methods in the following order:
1. Environment variables
2. Managed Identity
3. Visual Studio Code
4. Azure CLI
5. Azure PowerShell
6. Interactive browser

Ensure you have one of these authentication methods configured before running the bot.

## Files

- `app.py` - Flask web application with chat interface (for shareable link)
- `bot.py` - Command-line bot implementation
- `templates/index.html` - Web chat interface UI
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore patterns for Python projects

## Deployment to Azure App Service

To deploy the web application to Azure App Service:

1. Create an Azure App Service:
```bash
az webapp up --name your-bot-name --runtime PYTHON:3.11
```

2. Configure authentication (Managed Identity recommended):
```bash
az webapp identity assign --name your-bot-name --resource-group your-resource-group
```

3. Set environment variables:
```bash
az webapp config appsettings set --name your-bot-name --resource-group your-resource-group --settings FLASK_SECRET_KEY=your-secret-key
```

4. Your bot will be available at: `https://your-bot-name.azurewebsites.net`

## Security Notes

- The `FLASK_SECRET_KEY` should be set to a secure random value in production
- Ensure proper authentication is configured for Azure AI Projects
- Consider adding rate limiting and authentication for production deployments
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

Run the bot:

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

- `bot.py` - Main bot implementation
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore patterns for Python projects
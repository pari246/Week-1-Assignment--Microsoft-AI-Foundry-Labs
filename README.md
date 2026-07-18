# 🚀 Microsoft AI Foundry Labs

A beginner-friendly collection of Microsoft AI Foundry labs demonstrating how to build Generative AI applications using Azure AI Foundry, GPT-5.2, the OpenAI SDK, Web Search, and File Search.

This repository follows Microsoft's AI Foundry learning exercises while adding detailed explanations, screenshots (optional), and fully commented Python code to make the labs easier for beginners.

---

# 📚 Labs Included

## Lab 1 – Prepare for an AI Development Project

In this lab you will learn how to:

- Create an Azure AI Foundry Project
- Deploy GPT-5.2
- Test prompts in the AI Playground
- View Project Endpoints
- Install the Foundry Toolkit for Visual Studio Code
- Connect VS Code to your AI Foundry Project

---

## Lab 2 – Create a Generative AI App Using Tools

In this lab you will learn how to:

- Connect Python to Azure AI Foundry
- Authenticate using Azure CLI
- Create an OpenAI Client
- Create a Vector Store
- Upload PDF brochures
- Use File Search
- Use Web Search
- Build an interactive AI chatbot

---

# 📋 Prerequisites

Before starting ensure you have:

- Azure Subscription
- Azure CLI
- Git
- Visual Studio Code
- Python 3.13.x
- Microsoft AI Foundry Access

---

# 💻 Software Installation

## Install Python

Download:

https://www.python.org/downloads/

Verify

```bash
python --version
```

Expected

```
Python 3.13.x
```

---

## Install Git

Download

https://git-scm.com/downloads

Verify

```bash
git --version
```

---

## Install Azure CLI

Download

https://learn.microsoft.com/cli/azure/install-azure-cli

Verify

```bash
az version
```

---

## Install VS Code

https://code.visualstudio.com/

Install extensions

- Python
- Foundry Toolkit

---

# 📁 Project Structure

```
AI-Foundry-Labs
│
├── README.md
├── requirements.txt
├── .env.example
│
├── 01_create_foundry_project.py
├── 02_test_gpt52_model.py
├── 03_view_project_details.py
├── 04_tools_chat_app.py
├── 05_cleanup_resources.py
```

---

# ☁️ Lab 1 – Create an AI Foundry Project

Open

https://ai.azure.com

Login using your Azure Account.

---

## Step 1

Click

```
New Project
```

---

## Step 2

Fill in

Project Name

```
AIFoundryLab
```

Resource

```
AIFoundryLab-resource
```

Choose

- Azure Subscription
- Resource Group
- Region

Recommended Regions

- East US
- Sweden Central
- West Europe

Click

```
Create
```

Wait until deployment completes.

---

# 🤖 Deploy GPT-5.2

Navigate

```
Discover
```

↓

```
Models
```

Search

```
gpt-5.2
```

Click

```
Deploy
```

Use default settings.

After deployment

Open

```
Model Playground
```

---

# Test the Model

System Instructions

```
You are an AI assistant that can provide information and advice about AI software development.
```

Prompt

```
Describe three key considerations when developing applications with Large Language Models.
```

Expected Output

- Prompt Engineering
- Safety
- Cost Optimization

---

# 🔑 Collect Your Endpoints

Navigate to

```
Home
```

Record

- Azure OpenAI Endpoint
- Project Endpoint
- API Key
- Deployment Name

Example

```
Deployment Name

gpt-5-2
```

---

# Install Foundry Toolkit

Open

Visual Studio Code

Go to

Extensions

Search

```
Foundry Toolkit
```

Install

Restart VS Code.

---

# Connect VS Code

Open

Foundry Toolkit

Sign into Azure

Select your project

Expand

```
Models
```

Verify

```
gpt-5.2
```

appears.

---

# 🚀 Lab 2

The second lab builds a complete chatbot using

- GPT-5.2
- File Search
- Web Search
- Azure OpenAI SDK

Python source files are included in this repository.

---

# Install Python Packages

```bash
pip install -r requirements.txt
```

---

# Login to Azure

```bash
az login
```

---

# Run the Chatbot

```bash
python 04_tools_chat_app.py
```

---

# Example Questions

```
What's happening in New York next month?
```

```
What hotels does Margie's Travel offer?
```

```
What travel packages are available?
```

---

# Cleanup

After completing the labs

Go to

Azure Portal

↓

Resource Groups

↓

Delete Resource Group

This prevents unnecessary Azure charges.

---

# Technologies Used

- Microsoft AI Foundry
- Azure OpenAI
- GPT-5.2
- OpenAI SDK
- Azure Identity
- Python
- Visual Studio Code

---

# Learning Outcomes

After completing this repository you will be able to

- Create AI Foundry Projects
- Deploy GPT Models
- Connect Python to Azure AI
- Authenticate with Azure CLI
- Use OpenAI SDK
- Create Vector Stores
- Use File Search
- Use Web Search
- Build AI Chat Applications

---

# Author

Created for Microsoft AI Foundry Learning Labs.

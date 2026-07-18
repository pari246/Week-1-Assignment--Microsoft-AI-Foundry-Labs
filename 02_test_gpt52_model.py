"""
=========================================================
Microsoft AI Foundry Lab 2
File: 02_test_gpt52_model.py

Description
-----------
This script connects to your Azure AI Foundry deployment
using Microsoft Entra ID authentication (Azure CLI login)
and sends prompts to your GPT-5.2 model.

Prerequisites
-------------
1. az login
2. .env file configured
3. GPT-5.2 deployed
4. Packages installed:
   pip install -r requirements.txt
=========================================================
"""

from dotenv import load_dotenv
import os

from openai import OpenAI
from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider,
)

# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT")


# ---------------------------------------------------------
# Validate configuration
# ---------------------------------------------------------

if not AZURE_OPENAI_ENDPOINT:
    raise ValueError(
        "AZURE_OPENAI_ENDPOINT not found in .env file."
    )

if not MODEL_DEPLOYMENT:
    raise ValueError(
        "MODEL_DEPLOYMENT not found in .env file."
    )


# ---------------------------------------------------------
# Create Azure Authentication Token
# ---------------------------------------------------------

print("\nAuthenticating with Azure...")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default",
)

print("Authentication successful.\n")


# ---------------------------------------------------------
# Create OpenAI Client
# ---------------------------------------------------------

client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=token_provider,
)

print("Connected to Azure AI Foundry.")
print(f"Deployment : {MODEL_DEPLOYMENT}")
print("-" * 60)


# ---------------------------------------------------------
# System Instructions
# ---------------------------------------------------------

SYSTEM_PROMPT = """
You are an AI assistant that provides helpful information
about Artificial Intelligence, Microsoft Azure,
and AI software development.

Provide concise, beginner-friendly explanations.
"""


# ---------------------------------------------------------
# Interactive Chat Loop
# ---------------------------------------------------------

print("AI Chat Started")
print("Type 'quit' to exit.\n")

previous_response_id = None

while True:

    user_input = input("You : ")

    if user_input.lower() == "quit":
        print("\nGoodbye!")
        break

    try:

        response = client.responses.create(

            model=MODEL_DEPLOYMENT,

            instructions=SYSTEM_PROMPT,

            input=user_input,

            previous_response_id=previous_response_id,

        )

        print("\nAssistant:\n")

        print(response.output_text)

        print("\n" + "-" * 60)

        previous_response_id = response.id

    except Exception as ex:

        print("\nAn error occurred.\n")

        print(ex)

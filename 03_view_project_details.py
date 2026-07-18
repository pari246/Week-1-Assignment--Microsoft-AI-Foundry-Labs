"""
==============================================================
Microsoft AI Foundry Lab 3

File:
03_view_project_details.py

Description
-----------
Displays the current Azure AI Foundry project configuration.

This script helps verify that:

• Environment variables are configured
• Azure CLI authentication works
• Azure OpenAI endpoint is valid
• Deployment name is available

Author:
GitHub Learning Project
==============================================================
"""

import os
from dotenv import load_dotenv

# ---------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("MODEL_DEPLOYMENT")


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Display Configuration
# ---------------------------------------------------------

print_section("Azure AI Foundry Configuration")

print(f"Azure OpenAI Endpoint : {AZURE_OPENAI_ENDPOINT}")
print(f"Model Deployment      : {MODEL_DEPLOYMENT}")

print_section("Configuration Validation")

if AZURE_OPENAI_ENDPOINT:
    print("✅ Azure OpenAI Endpoint Found")
else:
    print("❌ Azure OpenAI Endpoint Missing")

if MODEL_DEPLOYMENT:
    print("✅ Model Deployment Found")
else:
    print("❌ Model Deployment Missing")

print_section("Next Steps")

print("""
1. Verify the Azure OpenAI endpoint matches the value shown
   on the Azure AI Foundry Home page.

2. Verify the deployment name matches your GPT-5.2 deployment.

3. Ensure you have already run:

       az login

4. Continue to the next lab:

       python 04_tools_chat_app.py
""")

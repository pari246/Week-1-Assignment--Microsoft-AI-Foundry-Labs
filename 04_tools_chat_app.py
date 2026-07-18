"""
=================================================================
Microsoft AI Foundry Lab 4

File:
04_tools_chat_app.py

Description:
-------------
A Generative AI chatbot application using Azure AI Foundry.

Features:
---------
✓ Azure AI Foundry GPT-5.2 model
✓ Microsoft Entra ID authentication
✓ OpenAI Responses API
✓ Vector Store creation
✓ PDF document upload
✓ File Search tool
✓ Web Search tool
✓ Multi-turn conversation

Scenario:
---------
Margie's Travel AI Assistant

The assistant can:
- Answer questions about travel brochures
- Search uploaded documents
- Provide current travel information
- Recommend destinations

=================================================================
"""


import os
import glob

from dotenv import load_dotenv

from openai import OpenAI

from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider
)


# ===============================================================
# Load Configuration
# ===============================================================


load_dotenv()


AZURE_OPENAI_ENDPOINT = os.getenv(
    "AZURE_OPENAI_ENDPOINT"
)

MODEL_DEPLOYMENT = os.getenv(
    "MODEL_DEPLOYMENT"
)


if not AZURE_OPENAI_ENDPOINT:
    raise ValueError(
        "Missing AZURE_OPENAI_ENDPOINT in .env file"
    )


if not MODEL_DEPLOYMENT:
    raise ValueError(
        "Missing MODEL_DEPLOYMENT in .env file"
    )


# ===============================================================
# Connect to Azure AI Foundry
# ===============================================================


print("\nConnecting to Azure AI Foundry...")


token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)


client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=token_provider
)


print("✅ Connected successfully")


# ===============================================================
# Create Vector Store
# ===============================================================


print("\nCreating knowledge base...")


vector_store = client.vector_stores.create(
    name="margies-travel-brochures"
)


# ===============================================================
# Upload Travel Documents
# ===============================================================


print("\nUploading brochures...")


files = glob.glob(
    "brochures/*.pdf"
)


if not files:

    print(
        """
No PDF files found.

Please add PDF brochures inside:

brochures/

Example:

brochures/newyork.pdf
brochures/paris.pdf

"""
    )

    exit()


file_streams = []


for file in files:

    file_streams.append(
        open(file, "rb")
    )


file_upload = client.vector_stores.file_batches.upload_and_poll(

    vector_store_id=vector_store.id,

    files=file_streams

)


for file in file_streams:
    file.close()



print(
    f"""
✅ Knowledge base created

Files uploaded:
{file_upload.file_counts.completed}

"""
)


# ===============================================================
# AI Assistant Instructions
# ===============================================================


instructions = """

You are Margie's Travel AI Assistant.

Your responsibilities:

1. Answer questions about Margie's Travel services.

2. Use uploaded brochures when answering
   travel package questions.

3. Use web search for:
   - Current events
   - Weather
   - Recent travel information
   - Local recommendations

4. If information is unavailable,
   clearly explain that.

Provide helpful and friendly travel advice.

"""


# ===============================================================
# Chat Application
# ===============================================================


print("=" * 60)

print(
"""
Margie's Travel AI Assistant

Ask questions about:
- Travel packages
- Destinations
- Hotels
- Current travel information

Type 'quit' to exit.

"""
)

print("=" * 60)


previous_response_id = None



while True:


    user_question = input(
        "\nYou: "
    )


    if user_question.lower() == "quit":

        print(
            "\nThank you for using Margie's Travel AI."
        )

        break



    try:


        response = client.responses.create(

            model=MODEL_DEPLOYMENT,


            instructions=instructions,


            input=user_question,


            previous_response_id=
                previous_response_id,


            tools=[


                {


                    "type":
                    "file_search",


                    "vector_store_ids":
                    [
                        vector_store.id
                    ]

                },


                {


                    "type":
                    "web_search"

                }


            ]

        )


        print(
            "\nAssistant:"
        )


        print(
            response.output_text
        )


        previous_response_id = response.id



    except Exception as error:


        print(
            "\nError occurred:"
        )


        print(error)

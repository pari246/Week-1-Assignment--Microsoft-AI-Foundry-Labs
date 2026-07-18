"""
===========================================================
Microsoft AI Foundry Lab 1
File: 01_create_foundry_project.py

Purpose:
--------
This script helps beginners verify that their local
development environment is ready for Microsoft AI Foundry.

It checks:

1. Python installation
2. Azure CLI installation
3. Git installation
4. Azure login status
5. Installed Python packages

Author:
GitHub Learning Project
===========================================================
"""

import platform
import subprocess
import sys


def run_command(command):
    """
    Executes a shell command and returns its output.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return None

    except Exception:
        return None


def check_python():
    """Check Python version."""
    print("=" * 60)
    print("Checking Python Installation")
    print("=" * 60)

    version = platform.python_version()

    print(f"Python Version : {version}")

    major, minor, *_ = version.split(".")

    if int(major) == 3 and int(minor) >= 13:
        print("✅ Python version is compatible.")
    else:
        print("⚠ Python 3.13 or newer is recommended.")


def check_git():
    """Check Git installation."""
    print("\n" + "=" * 60)
    print("Checking Git")
    print("=" * 60)

    output = run_command("git --version")

    if output:
        print(f"✅ {output}")
    else:
        print("❌ Git is not installed.")


def check_azure_cli():
    """Check Azure CLI."""
    print("\n" + "=" * 60)
    print("Checking Azure CLI")
    print("=" * 60)

    output = run_command("az version")

    if output:
        print("✅ Azure CLI Installed")
    else:
        print("❌ Azure CLI not found.")


def check_azure_login():
    """Check Azure authentication."""
    print("\n" + "=" * 60)
    print("Checking Azure Login")
    print("=" * 60)

    output = run_command("az account show")

    if output:
        print("✅ Logged into Azure")
    else:
        print("❌ Not logged in.")
        print("\nRun:")
        print("    az login")


def check_packages():
    """Check required Python packages."""

    print("\n" + "=" * 60)
    print("Checking Required Packages")
    print("=" * 60)

    packages = [
        "openai",
        "azure.identity",
        "dotenv",
        "requests"
    ]

    for package in packages:
        try:
            __import__(package)

            print(f"✅ {package}")

        except ImportError:

            print(f"❌ {package}")


def print_next_steps():
    """Display what the learner should do next."""

    print("\n" + "=" * 60)
    print("Environment Check Complete")
    print("=" * 60)

    print("""
Next Steps

1. Open https://ai.azure.com

2. Create a Microsoft AI Foundry Project

3. Deploy GPT-5.2

4. Copy your:

   • Azure OpenAI Endpoint
   • Deployment Name

5. Update the .env file

6. Run:

    python 02_test_gpt52_model.py
""")


def main():

    print("\n")
    print("=" * 60)
    print("Microsoft AI Foundry Environment Checker")
    print("=" * 60)

    check_python()
    check_git()
    check_azure_cli()
    check_azure_login()
    check_packages()

    print_next_steps()


if __name__ == "__main__":
    main()

"""
=================================================================
Microsoft AI Foundry Labs

File:
05_cleanup_resources.py

Description:
-------------
Azure AI Foundry cleanup helper.

This script helps you safely remove Azure resources created
during the AI Foundry labs.

It performs:

✓ Azure login verification
✓ Displays current subscription
✓ Lists resource groups
✓ Allows optional resource group deletion

Important:
-----------
Deleting a resource group permanently removes all resources
inside it, including:

- Azure AI Foundry resources
- Azure OpenAI deployments
- Storage resources
- Other Azure services

Use carefully.

=================================================================
"""


import subprocess
import json


# ===============================================================
# Helper Function
# ===============================================================


def run_command(command):
    """
    Execute Azure CLI commands.
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



# ===============================================================
# Check Azure Login
# ===============================================================


def check_login():

    print("=" * 60)

    print(
        "Checking Azure Login"
    )

    print("=" * 60)


    account = run_command(
        "az account show"
    )


    if account:

        print(
            "✅ Azure login detected"
        )

        return True


    else:

        print(
            """
❌ Azure login not found.

Please run:

az login

"""
        )

        return False



# ===============================================================
# Show Subscription
# ===============================================================


def show_subscription():

    print("\nAzure Subscription Information")

    print("-" * 60)


    result = run_command(
        "az account show --output json"
    )


    if result:


        data = json.loads(result)


        print(
            f"Subscription Name : {data['name']}"
        )


        print(
            f"Subscription ID   : {data['id']}"
        )


    else:

        print(
            "Unable to retrieve subscription details"
        )



# ===============================================================
# List Resource Groups
# ===============================================================


def list_resource_groups():

    print("\nAvailable Resource Groups")

    print("-" * 60)


    groups = run_command(
        "az group list --output table"
    )


    if groups:

        print(groups)


    else:

        print(
            "No resource groups found."
        )



# ===============================================================
# Delete Resource Group
# ===============================================================


def delete_resource_group():


    print("\n")

    resource_group = input(
        """
Enter the resource group name to delete.

Leave blank to cancel:

> """
    )


    if not resource_group:


        print(
            "Cleanup cancelled."
        )

        return



    confirmation = input(

        f"""
WARNING:

You are about to permanently delete:

{resource_group}

All resources inside this group will be removed.

Type DELETE to continue:

> """

    )


    if confirmation != "DELETE":

        print(
            "Deletion cancelled."
        )

        return



    print(
        "\nDeleting resource group..."
    )


    result = run_command(

        f"az group delete --name {resource_group} --yes"

    )


    if result is not None:


        print(
            """
✅ Resource group deletion started.

Azure may take several minutes
to complete the cleanup.
"""
        )


    else:


        print(
            """
❌ Unable to delete resource group.

Check Azure permissions.
"""
        )



# ===============================================================
# Main Program
# ===============================================================


def main():


    print(
        """
==============================================================
Microsoft AI Foundry Cleanup Tool
==============================================================
"""
    )


    if not check_login():

        return


    show_subscription()

    list_resource_groups()


    answer = input(

        """
Would you like to delete a resource group?

(y/n):

> """

    )


    if answer.lower() == "y":

        delete_resource_group()


    else:

        print(
            """
Cleanup skipped.

You can manually delete resources from:

https://portal.azure.com

Resource Groups
>
Select Resource Group
>
Delete
"""
        )



if __name__ == "__main__":

    main()

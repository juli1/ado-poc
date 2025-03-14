import requests
import base64
import os

# Configuration
config = {
    "organization": "julien-ado",
    "project": "test-ado",
    "repository": "test-ado",
    "path": "program.py",  # e.g., '/src/main.py'
    "branch": "main",  # or another branch name
    # Personal Access Token (PAT) for authentication
    "pat": os.environ['ADO_TOKEN']
}

def get_code_from_azure_devops():
    """
    Retrieves a code snippet from an Azure DevOps repository.
    """
    # Create the API URL
    api_url = f"https://dev.azure.com/{config['organization']}/{config['project']}/_apis/git/repositories/{config['repository']}/items"

    # Query parameters
    params = {
        "path": config["path"],
        "versionDescriptor.version": config["branch"],
        "includeContent": "true",  # Explicitly request content
        "api-version": "6.0"
    }

    # Create the authorization header with PAT
    auth_token = base64.b64encode(f":{config['pat']}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_token}",
        # Request the raw content directly
        "Accept": "application/octet-stream"  # This is key for getting raw file content
    }

    try:
        # Make the API request
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # With application/octet-stream, the response content is directly the file content
        print("Code snippet retrieved successfully:")

        # For text files
        if response.headers.get('Content-Type', '').startswith(('text/', 'application/json')):
            content = response.text
            print(content)
        # For binary files
        else:
            content = response.content
            print(f"Retrieved binary content of size {len(content)} bytes")
            print(content)
        return content
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        if response.content:
            print(f"Error details: {response.json()}")
    except requests.exceptions.RequestException as err:
        print(f"Error retrieving code from Azure DevOps: {err}")

    return None

if __name__ == "__main__":
    get_code_from_azure_devops()
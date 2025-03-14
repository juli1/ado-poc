import requests
import base64
import json
import os

def add_pull_request_comment(organization, project, repository_id, pull_request_id, comment_content, file_path, line_number, pat):
    """
    Adds a comment to specific code in a pull request in Azure DevOps.

    Args:
        organization (str): Azure DevOps organization name
        project (str): Project name
        repository_id (str): Repository ID or name
        pull_request_id (int): Pull Request ID
        comment_content (str): The content of the comment
        file_path (str): Path to the file being commented on
        line_number (int): Line number to comment on
        pat (str): Personal Access Token for authentication

    Returns:
        dict: The API response data if successful, None otherwise
    """
    # Create the API URL for adding comments to a pull request
    api_url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories/{repository_id}/pullRequests/{pull_request_id}/threads?api-version=6.0"

    # Create the authorization header with PAT
    auth_token = base64.b64encode(f":{pat}".encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_token}",
        "Content-Type": "application/json"
    }

    # Create the request payload for a comment on file content
    payload = {
        "comments": [
            {
                "parentCommentId": 0,
                "content": comment_content,
                "commentType": "text"
            }
        ],
        "status": "active",
        "threadContext": {
            "filePath": "/program2.py",  # Path to the file you're commenting on
            "rightFileStart": {
                "line": 1,  # Line number to comment on
                "offset": 1   # Column offset
            },
            "rightFileEnd": {
                "line": 1,
                "offset": 5  # Arbitrary end column (covers most lines)
            }
        }
    }

    try:
        # Make the API request
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise exception for HTTP errors

        print(f"Comment added successfully to Pull Request #{pull_request_id}")
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        if hasattr(response, 'content'):
            print(f"Error details: {response.content}")
    except requests.exceptions.RequestException as err:
        print(f"Error adding comment to Pull Request: {err}")

    return None

# Example usage
if __name__ == "__main__":
    # Configuration
    config = {
        "organization": "julien-ado",
        "project": "test-ado",
        "repository": "test-ado",
        "path": "program.py",  # e.g., '/src/main.py'
        "pull_request_id": 1,  # Replace with your PR ID
        "comment_content": "Consider using a more descriptive variable name here.",
        "file_path": "program2.py",  # Path to the file in the repository
        "line_number": 1,  # Line number to comment on
        "pat": os.environ['ADO_TOKEN']
    }

    # Call the function with the configuration
    result = add_pull_request_comment(
        config["organization"],
        config["project"],
        config["repository"],
        config["pull_request_id"],
        config["comment_content"],
        config["file_path"],
        config["line_number"],
        config["pat"]
    )
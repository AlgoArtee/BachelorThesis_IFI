import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
load_dotenv()

def get_jira_auth():
    email = os.getenv('EMAIL')
    api_token = os.getenv('JIRA_API_TOKEN')
    if not email or not api_token:
        raise Exception("JIRA email or API token is not set!")
    return HTTPBasicAuth(email, api_token)

def get_gpt_auth():
    api_key = os.getenv('GPT_API_KEY')
    api_endpoint = os.getenv('GPT_API_ENDPOINT')
    if not api_key or not api_endpoint:
        raise Exception("GPT API key or endpoint is not set!")
    return {
        'api_key': api_key,
        'api_endpoint': api_endpoint
    }

def get_gitlab_auth():
    private_token = os.getenv('GITLAB_API_TOKEN')
    if not private_token:
        raise Exception("GitLab private token is not set!")
    return private_token
# Add more functions for other services as needed
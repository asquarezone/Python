from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth

import requests
load_dotenv()

BASE_URL = os.getenv('BASE_URL','http://localhost:8080')

def get_default_headers():
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    return headers

def get_cred() -> tuple[str]:
    
    return (os.getenv('USERNAME'), os.getenv('PASSWORD'))

def get_auth() -> HTTPBasicAuth:
    creds = get_cred()
    auth = HTTPBasicAuth(
        username=creds[0],
        password=creds[1]
    )
    return auth

def check_myself():
    response = requests.get(
        f"{BASE_URL}/rest/api/2/myself",
        auth=get_auth(),
        headers=get_default_headers())
    print(response)

def change_progress(issue_id="EXP-4", status_id="11"):
    url= f"{BASE_URL}/rest/api/2/issue/{issue_id}/transitions"
    data = {
        "transition": { "id": status_id }
    }
    response = requests.post(
        url=url,
        auth=get_auth(),
        headers=get_default_headers(),
        json=data
    )
    print(response)


def main():
    print("Hello from jira-client!")


if __name__ == "__main__":
    change_progress("EXP-4", "11")

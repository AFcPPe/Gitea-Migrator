import os
import requests
import subprocess

# Constants
BASE_URL = ""
AUTH_TOKEN = "token "
GIT_USERNAME = ""
GIT_PASSWORD = ""

# Headers for API requests
headers = {
    "Authorization": AUTH_TOKEN,
    "Content-Type": "application/json"
}

# Function to create organization
def create_org(org_name):
    url = f"{BASE_URL}/api/v1/orgs"
    payload = {
        "full_name": org_name,
        "repo_admin_change_team_access": False,
        "username": org_name,
        "visibility": "private",
    }
    response = requests.post(url, json=payload, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

# Function to create repository
def create_repo(org_name, repo_name):
    url = f"{BASE_URL}/api/v1/orgs/{org_name}/repos"
    payload = {
        "auto_init": True,
        "default_branch": "master",
        "name": repo_name,
        "object_format_name": "sha1",
        "private": True,
        "template": False,
        "trust_model": "default"
    }
    response = requests.post(url, json=payload, headers=headers,verify=False)
    response.raise_for_status()
    return response.json()

# Function to push repository to new git server
def push_repo(org_name, repo_name, repo_path):
    remote_url = f"https://{GIT_USERNAME}:{GIT_PASSWORD}@git.moa.com/{org_name}/{repo_name}.git"
    commands = [
        ["git", "--git-dir", repo_path, "remote", "add", "origin", remote_url],
        ["git", "--git-dir", repo_path, "push", "--all", "--force", "origin"],
        ["git", "--git-dir", repo_path, "push", "--tags", "--force", "origin"]
    ]
    for command in commands:
        try:
            subprocess.run(command, check=True)
        except Exception as e:
            print(e)

# Main function to process all repositories
def migrate_repos(base_path):
    for org in os.listdir(base_path):
        org_path = os.path.join(base_path, org)
        if not os.path.isdir(org_path):
            continue

        # Create organization
        try:
            create_org(org)
        except Exception as e:
            print(e)


        for repo in os.listdir(org_path):
            if not repo.endswith(".git"):
                continue

            repo_name = repo[:-4]  # Remove .git extension
            repo_path = os.path.join(org_path, repo)
            
            # Create repository
            try:
                create_repo(org, repo_name)
            except Exception as e:
                print(e)
            
            # Push repository
            try:
                push_repo(org, repo_name, repo_path)
            except Exception as e:
                print(e)


# Run the migration
migrate_repos("./repos")

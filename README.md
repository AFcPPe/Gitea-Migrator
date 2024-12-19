# Gitea-Migrator

Gitea-Migrator is a simple script designed to facilitate the batch migration of local Git repositories to a Gitea server. It leverages the Gitea API and command-line tools to automate the process, making it easier to manage multiple repositories.

## Prerequisites

- Python 3.x installed on your machine.
- Git installed and accessible via command line.

## Setup

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/AFcPPe/Gitea-Migrator.git
   cd Gitea-Migrator
   ```

2. Install required Python packages.
   
   ```bash
   pip install requests
   ```

## Configuration

Before running the script, you need to configure the following constants in the script:

- `BASE_URL`: The base URL of your Gitea server (e.g., `https://gitea.example.com`).
- `AUTH_TOKEN`: Your Gitea API token for authentication (REMENBER TO PREPEND `token`  AND A SPACE).
- `GIT_USERNAME`: Your Gitea username.
- `GIT_PASSWORD`: Your Gitea password.

These constants are typically found at the top of the script file. Modify them to match your Gitea server settings.

```python
BASE_URL = "https://gitea.example.com"
AUTH_TOKEN = "your_api_token"
GIT_USERNAME = "your_username"
GIT_PASSWORD = "your_password"
```

## Usage

Once you have configured the constants, you can run the script to start migrating your local repositories to Gitea.

```bash
python main.py
```

The script will iterate through your local repositories and push them to the specified Gitea server.

# 

# GitHub API Python Script

A Python script for interacting with the GitHub API using the PyGithub library.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Get a GitHub Personal Access Token:
   - Go to https://github.com/settings/tokens
   - Generate a new token with appropriate permissions (at least `public_repo` scope)

3. Set the token as an environment variable:
```bash
# Windows (PowerShell)
$env:GITHUB_TOKEN="your_token_here"

# Windows (CMD)
set GITHUB_TOKEN=your_token_here

# Linux/Mac
export GITHUB_TOKEN="your_token_here"
```

Or pass it directly when initializing:
```python
github_api = GitHubAPI(token='your_token_here')
```

## Usage

Run the script:
```bash
python github_api.py
```

Or import and use the `GitHubAPI` class in your own code:
```python
from github_api import GitHubAPI

github_api = GitHubAPI()
user_info = github_api.get_user_info()
repos = github_api.get_repositories()
```

## Features

- Get authenticated user information
- List repositories for a user
- Get detailed repository information
- Search for repositories

## Note

The original file `from github import Github.py` has been replaced with `github_api.py` which follows Python naming conventions and includes a complete implementation.


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

3. Set the token as an environment variable in .env file like:
GITHUB_TOKEN =

Or pass it directly when initializing:
```python
auth = Auth.Token("xxx")
```

## Usage

Run the script:
```bash
python github_api.py
```
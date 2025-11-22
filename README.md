# GitHub API Python Script

A simple Python script that gets information from GitHub repositories using the GitHub API.

## What it does

- Shows how many stars a repository has
- Shows how many open issues a repository has
- Lists all open issues with their numbers and titles

## Setup

1. Install Poetry (if you don't have it):
  
   pip install poetry
   2. Install the project dependencies:
   poetry install
   3. Get a GitHub Personal Access Token:
   - Go to https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Give it a name and select the `public_repo` scope
   - Click "Generate token" and copy it

4. Create a `.env` file in the project root:
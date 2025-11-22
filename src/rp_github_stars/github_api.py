from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}"
}

repo_url = "https://api.github.com/repos/torvalds/linux"
r = requests.get(repo_url, headers=headers)
repo_data = r.json()

print(f"Stargazers count: {repo_data['stargazers_count']}")
print(f"Open issues count: {repo_data['open_issues_count']}")

issues_url = "https://api.github.com/repos/torvalds/linux/issues"
issues_params = {"state": "open"}
issues_response = requests.get(issues_url, headers=headers, params=issues_params)
issues = issues_response.json()

for x in issues:
    print(f"#{x['number']}: {x['title']}")
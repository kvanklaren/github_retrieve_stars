from github import Github, Auth
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

auth = Auth.Token(token)
g = Github(auth=auth)

repo = g.get_repo("torvalds/linux")
print(repo.stargazers_count)

issues = repo.get_issues(state="open")
for i in issues:
    print(f"#{i.number}: {i.title}")

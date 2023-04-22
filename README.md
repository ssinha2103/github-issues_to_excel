# GitHub Issue Extractor

GitHub Issue Extractor is a Python utility that helps you extract issues from a specific GitHub repository and milestone. This tool utilizes the GitHub API and requires an access token for authentication. 

## Features
- Extract issues from a specific GitHub repository
- Filter issues by milestone number
- Requires a GitHub access token for authentication

## Prerequisites
- Python 3.x
- `requests` library

## Installation
1. Clone the repository:
    `git clone https://github.com/ssinha2103/github-issues_to_excel`
2. Install the required dependencies:
    `pip install -r requirements.txt`


## Usage
To use the GitHub Issue Extractor, simply import the class and create an instance with the required parameters:

```python
from github_issue_extractor import GitHubIssueExtractor

milestone_number = 1
access_token = "your_access_token_here"
repo_name = "repository_name"
owner = "repository_owner"

extractor = GitHubIssueExtractor(milestone_number, access_token, repo_name, owner)
extractor.run()

```
Replace the values of `milestone_number`, `access_token`, `repo_name`, and `owner` with your desired settings.

## Parameters
1. `milestone_number`: The milestone number you want to filter issues by.
2. `access_token`: Your GitHub personal access token for authentication. Follow [these instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a personal access token.
3. `repo_name`: The name of the repository from which you want to extract issues.
4. `owner`: The username of the repository owner.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
from github_issue_extractor import GitHubIssueExtractor

if __name__ == '__main__':
    milestone_number = "1"
    access_token = "your-access-token"
    repo_name = "your-repo-name"
    owner = "your-owner-name"

    extractor = GitHubIssueExtractor(milestone_number, access_token, repo_name, owner)
    extractor.run()

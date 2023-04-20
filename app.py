import os
import requests
import openpyxl


def run(milestone_number, access_token, repo_name="issues-codex", owner="urbanpiper"):

    # Make a GET request to the GitHub API to fetch the issues with the specified milestone, including the Authorization
    # header
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo_name}/issues?milestone={milestone_number}&state=all", headers={"Authorization": f"Token {access_token}"})

    # Parse the JSON response to extract the relevant information for each issue
    issues = response.json()

    # Write the extracted information to an Excel file with proper headers
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append(["Number", "Title", "Body", "User", "State", "Assignee", "Created At", "Updated At", "Labels"])
    for issue in issues:
        issue_number = issue["number"]
        issue_title = issue["title"]
        issue_body = issue["body"]
        issue_user = issue["user"]["login"]
        issue_state = issue["state"]
        issue_assignee = issue["assignee"]["login"] if issue["assignee"] else ""
        issue_created_at = issue["created_at"]
        issue_updated_at = issue["updated_at"]
        issue_labels = ",".join([label["name"] for label in issue["labels"]])
        worksheet.append(
            [issue_number, issue_title, issue_body, issue_user, issue_state, issue_assignee, issue_created_at,
             issue_updated_at, issue_labels])

        # Get the path of the user's Downloads folder
        downloads_folder = os.path.expanduser("~/Downloads")

        # Save the Excel file to the Downloads folder with a filename based on the milestone number
        filename = f"{repo_name}-{milestone_number}.xlsx"
        file_path = os.path.join(downloads_folder, filename)
        workbook.save(file_path)

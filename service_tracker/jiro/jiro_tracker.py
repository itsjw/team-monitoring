import os
import requests

from jira import JIRA
from requests.auth import HTTPBasicAuth


USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
ASSIGNEE = os.environ.get("ASSIGNEE")

jira = JIRA(basic_auth=(USERNAME, PASSWORD), options={'server': 'https://pm.maddevs.co/'})


def dayly_issue_by_user(username, password, assignee):
    issues = []
    all_proj_issues_by_assignee = jira.search_issues('assignee = {} AND  updated  > startOfDay()'.format(assignee))
    for key in all_proj_issues_by_assignee:
        issues.append(key)
        return issues


def worklog_by_issue(username, password, issues):
    worklogs = []
    auth = HTTPBasicAuth(username=username, password=password)
    for issue in issues:
        worklog = requests.get('https://pm.maddevs.co/rest/api/2/issue/{}/worklog'.format(issue), auth=auth).json()
        worklogs.append(worklog)


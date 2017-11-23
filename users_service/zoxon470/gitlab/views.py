# -*- coding: utf-8 -*-

import os
import requests

from jira import JIRA
from requests.auth import HTTPBasicAuth
from datetime import datetime

JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
JIRA_PASSWORD = os.environ.get('JIRA_PASSWORD')
JIRA_ASSIGNEE = os.environ.get('JIRA_ASSIGNEE')


# autentification per jiralib and api
jira = JIRA(basic_auth=(JIRA_USERNAME, JIRA_PASSWORD), options={'server': 'https://pm.maddevs.co/'})
auth = HTTPBasicAuth(username=JIRA_USERNAME, password=JIRA_PASSWORD)
current_day = datetime.today().strftime("%Y-%m-%d")


class JIRATimeSpent():
    print('class')
    def time_tracked_per_day(self):
        print("Grabbing user info for {}".format(JIRA_ASSIGNEE))
        # getting all issues updated by user since start of the day
        issues = []
        search_categorys = 'assignee = {0} AND  updated  > startOfDay()'.format(JIRA_ASSIGNEE)
        all_proj_issues_by_assignee = jira.search_issues(search_categorys)
        for key in all_proj_issues_by_assignee:
            issues.append(key)

            # getting all worklog info per person
            for issue in issues:
                worklog_url = 'https://pm.maddevs.co/rest/api/2/issue/{0}/worklog'.format(issue)
                worklog_info = requests.get(worklog_url, auth=auth).json()

                # getting updated time of issue and adding them all
                all_issues_per_day = 0
                for item in worklog_info['worklogs']:
                    time_per_track = item['timeSpentSeconds']
                    all_issues_per_day += time_per_track
                    return all_issues_per_day

    def time_tracked_per_week(self):
        print("Grabbing user info for {}".format(JIRA_ASSIGNEE))
        issues = []
        search_categorys = 'assignee = {0} AND  updated  <=  endOfWeek()'.format(JIRA_ASSIGNEE)

        all_proj_issues_by_assignee = jira.search_issues(search_categorys)
        print(all_proj_issues_by_assignee)
        for key, value in all_proj_issues_by_assignee.items():
            print("KEY - %s VALUE - %s" % (key, value))
            #print(key)
            issues.append(key)
            #print(issues)

            # getting all worklog info per person
            for issue in issues:
                worklog_url = 'https://pm.maddevs.co/rest/api/2/issue/{0}/worklog'.format(issue)
                worklog_info = requests.get(worklog_url, auth=auth).json()
                # print (worklog_url)

                # getting updated time of issue and adding them all
                all_issues_per_week = 0
                for item in worklog_info['worklogs']:
                    # print(item)
                    time_per_track = item['timeSpentSeconds']
                    all_issues_per_week += time_per_track
                    print(all_issues_per_week)
                    return all_issues_per_week

    def time_tracked_per_month(self):
        print("Grabbing user info for {}".format(JIRA_ASSIGNEE))
        issues = []
        search_categorys = 'assignee = {0} AND  updated  <=  endOfMonth()'.format(JIRA_ASSIGNEE)
        all_proj_issues_by_assignee = jira.search_issues(search_categorys)
        print(type(all_proj_issues_by_assignee))
        print(all_proj_issues_by_assignee)
        for key in all_proj_issues_by_assignee:
            print(key)
            issues.append(key)
            print(issues)

            # getting all worklog info per person
            for issue in issues:
                worklog_url = 'https://pm.maddevs.co/rest/api/2/issue/{0}/worklog'.format(issue)
                worklog_info = requests.get(worklog_url, auth=auth).json()
                # print (worklog_url)

                # getting updated time of issue and adding them all
                all_issues_per_month = 0
                for item in worklog_info['worklogs']:
                    # print(item)
                    time_per_track = item['timeSpentSeconds']
                    all_issues_per_month += time_per_track
                    print(all_issues_per_month)
                    return all_issues_per_month

# -*- coding: utf-8 -*-
import json
import os
import requests

from jira import JIRA
from requests.auth import HTTPBasicAuth
from datetime import datetime


class JIRATimeSpent():
    def __init__(self):
        self.JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
        self.JIRA_PASSWORD = os.environ.get('JIRA_PASSWORD')
        self.JIRA_ASSIGNEE = os.environ.get('JIRA_ASSIGNEE')
        self.SERVER = 'https://pm.maddevs.co/'

        # autentification per jiralib and api
        self.jira_api_auth = JIRA(basic_auth=(self.JIRA_USERNAME, self.JIRA_PASSWORD), options={'server': self.SERVER})
        self.jira_http_auth = HTTPBasicAuth(username=self.JIRA_USERNAME, password=self.JIRA_PASSWORD)
        self.current_day = datetime.today().strftime("%Y-%m-%d")

    def time_tracked_per_day(self):
        print("Grabbing user info for {}".format(self.JIRA_ASSIGNEE))
        # getting all issues updated by user since start of the day
        search_categorys = 'worklogAuthor = {0} AND worklogDate >= startOfDay()'.format(self.JIRA_ASSIGNEE)
        all_proj_issues_by_assignee = self.jira_api_auth.search_issues(search_categorys)
        keys = sorted([project.key for project in all_proj_issues_by_assignee])
        if not keys:
            return "there are no issues for today"

        # getting all worklog info per person
        for issue in keys:
            print("hmm, issue!")
            worklog_url = 'https://pm.maddevs.co/rest/api/2/issue/{0}/worklog'.format(issue)
            worklog_info = requests.get(worklog_url, auth=self.jira_http_auth).json()

            # getting updated time of issue and adding them all
            all_issues_per_day = []
            for item in worklog_info['worklogs']:
                print('one more time log')
                item_format = "%Y-%m-%dT%H:%M:%S.%f+0000"
                worklog_date = datetime.strptime(item['updated'], item_format).strftime("%Y-%m-%d")
                if worklog_date == self.current_day:
                    time_per_track = item['timeSpentSeconds']
                    all_issues_per_day.append(time_per_track)

            return all_issues_per_day

    def time_tracked_per_week(self):
        print("Grabbing user info for {}".format(self.JIRA_ASSIGNEE))
        issues = []
        search_categorys = 'worklogAuthor = {0} AND worklogDate <=  endOfWeek()'.format(self.JIRA_ASSIGNEE)
        all_proj_issues_by_assignee = self.jira_api_auth.search_issues(search_categorys)
        keys = sorted([project.key for project in all_proj_issues_by_assignee])
        if not keys:
            return "there are no issues for this week"

        # getting all worklog info per person
        for issue in keys:
            print("hmm, issue!")
            worklog_url = 'https://pm.maddevs.co/rest/api/2/issue/{0}/worklog'.format(issue)
            worklog_info = requests.get(worklog_url, auth=self.jira_http_auth).json()

            # getting updated time of issue and adding them all
            all_issues_per_week = []
            for item in worklog_info['worklogs']:
                print('one more time log')
                item_format = "%Y-%m-%dT%H:%M:%S.%f+0000"
                worklog_date = datetime.strptime(item['updated'], item_format).strftime("%Y-%m-%d")
                if worklog_date == self.current_day:

                    time_per_track = item['timeSpentSeconds']
                    all_issues_per_week.append(time_per_track)

            return all_issues_per_week


    def time_tracked_per_month(self):
        print("Grabbing user info for {}".format(self.JIRA_ASSIGNEE))
        issues = []
        search_categorys = 'worklogAuthor = {0} AND worklogDate  <=  endOfMonth()'.format(self.JIRA_ASSIGNEE)
        all_proj_issues_by_assignee = self.jira_api_auth.search_issues(search_categorys)
        keys = sorted([project.key for project in all_proj_issues_by_assignee])
        if not keys:
            return "there are no issues for this month"

        # getting all worklog info per person
        for issue in keys:
            print("hmm, issue!")
            worklog_url = 'https://pm.maddevs.co/rest/api/2/issue/{0}/worklog'.format(issue)
            worklog_info = requests.get(worklog_url, auth=self.jira_http_auth).json()

            # getting updated time of issue and adding them all
            all_issues_per_day = []
            for item in worklog_info['worklogs']:
                print('one more time log')
                item_format = "%Y-%m-%dT%H:%M:%S.%f+0000"
                worklog_date = datetime.strptime(item['updated'], item_format).strftime("%Y-%m-%d")
                if worklog_date == self.current_day:
                    time_per_track = item['timeSpentSeconds']
                    all_issues_per_day.append(time_per_track)

            return all_issues_per_day

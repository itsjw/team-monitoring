# -*- coding: utf-8 -*-

import os
import requests

from datetime import datetime, timedelta

from urllib3.connectionpool import xrange

GITLAB_TOKEN = os.environ.get('GITLAB_TOKEN')
GITLAB_ASSIGNEE = os.environ.get('GITLAB_ASSIGNEE')


class GitlabCommitTracked():
    def __init__(self, user_id):
        self.user_id = user_id

    def getting_user_id(self):
        print("Grabbing user info for {}".format(GITLAB_ASSIGNEE))
        resp = requests.get("https://gitlab.com/api/v4/users?username={}".format(GITLAB_ASSIGNEE))
        user_id = resp.json()[0].get('id', 0)
        if user_id == 0:
            return "user {} not found".format(GITLAB_ASSIGNEE)
        return self.user_id

    def get_commits_per_day(self):
        print("Grabbing events data...")
        params = {
            "private_token": GITLAB_TOKEN,
            "before": datetime.now().strftime("%Y-%m-%d"),
            "after": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
        }
        r = requests.get("https://gitlab.com/api/v4/users/{}/events".format(self.user_id), params=params)
        messages = []
        for i in xrange(7):
            day = datetime.now() - timedelta(i)
            commits = 0
            for event in r.json():
                commit_date = datetime.strptime(event.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ")
                if (day - commit_date).days == 0:
                    commits += 1


    def get_commits_per_week(self):
        print("Grabbing events data...")
        params = {
            "private_token": GITLAB_TOKEN,
            "before": datetime.now().strftime("%Y-%m-%d"),
            "after": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
        }
        r = requests.get("https://gitlab.com/api/v4/users/{}/events".format(self.user_id), params=params)
        messages = []
        for i in xrange(7):
            day = datetime.now() - timedelta(i)
            commits = 0
            for event in r.json():
                commit_date = datetime.strptime(event.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ")
                if (day - commit_date).days == 0:
                    commits += 1

    def time_commits_per_month(self):
        print("Grabbing events data...")
        params = {
            "private_token": GITLAB_TOKEN,
            "before": datetime.now().strftime("%Y-%m-%d"),
            "after": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        }
        r = requests.get("https://gitlab.com/api/v4/users/{}/events".format(self.user_id), params=params)
        messages = []
        for i in xrange(7):
            day = datetime.now() - timedelta(i)
            commits = 0
            for event in r.json():
                commit_date = datetime.strptime(event.get("created_at"), "%Y-%m-%dT%H:%M:%S.%fZ")
                if (day - commit_date).days == 0:
                    commits += 1

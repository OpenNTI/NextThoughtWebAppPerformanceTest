# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import urllib.parse
from random import randrange
from random import sample
import time

USER_CREDENTIALS = list(range(1, 1000000))
ASSIGNMENT_INFO = [
    {
        "course_uid": "120-Orientation",
        "assignment_name": "Professional Development Test"
    },
]

class UserBehavior(SequentialTaskSet):
    user_id = 0
    version = None
    course_ntiid = None
    course_uid = None
    course_instance_link = None
    overview_summary_link = None
    overview_content_link = None
    assignment_name = None
    assignment_target_ntiid = None
    savepoint_link = None
    commence_link = None
    submit_link = None
    metadata_attempts_link = None
    assignment_parts = None
    final_answer = None


    def on_start(self):
        index_val = USER_CREDENTIALS.pop()
        index = index_val % len(ASSIGNMENT_INFO)
        print(index_val, index)
        print(f'starting {self.user_id} {self.course_uid} {self.assignment_name}')


    @task()
    def task_000027_GET_dataserver2_logon_ping(self):
        url = f'/_ops/ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
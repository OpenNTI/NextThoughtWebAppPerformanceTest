# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import urllib.parse
from random import randrange
from random import sample
import time

USER_CREDENTIALS = list(range(1, 1000))
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
        self.user_id = f'stress.tester{index_val}'
        self.course_uid = ASSIGNMENT_INFO[index]['course_uid']
        self.assignment_name = ASSIGNMENT_INFO[index]['assignment_name']
        print(f'starting {self.user_id} {self.course_uid} {self.assignment_name}')

    @task()
    def task_000002_GET_login(self):
        url = f'/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    ### Additional tasks can go here ###

    @task()
    def task_000027_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000028_GET_login_resources_images_0bcdabaa0b82ea3349f95d9a90a66551_png(self):
        url = f'/login/resources/images/0bcdabaa0b82ea3349f95d9a90a66551.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000034_GET_favicon_ico(self):
        url = f'/favicon.ico'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000035_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000036_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '143',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryHBvB2tr9viCiZ39B',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundaryHBvB2tr9viCiZ39B\r\nContent-Disposition: form-data; name="username"\r\n\r\nstre\r\n------WebKitFormBoundaryHBvB2tr9viCiZ39B--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000038_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000039_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '145',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryWka32EdXp8MeklbT',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundaryWka32EdXp8MeklbT\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress\r\n------WebKitFormBoundaryWka32EdXp8MeklbT--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000041_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000042_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '146',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryG988OVKVQ9kvr9Ei',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundaryG988OVKVQ9kvr9Ei\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.\r\n------WebKitFormBoundaryG988OVKVQ9kvr9Ei--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000044_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000045_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '150',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJB2a5b2s6Fwwce3S',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundaryJB2a5b2s6Fwwce3S\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.test\r\n------WebKitFormBoundaryJB2a5b2s6Fwwce3S--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000046_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000047_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '152',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryQh8k3BbBH6ItXb3J',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'------WebKitFormBoundaryQh8k3BbBH6ItXb3J\r\nContent-Disposition: form-data; name="username"\r\n\r\n{self.user_id}\r\n------WebKitFormBoundaryQh8k3BbBH6ItXb3J--\r\n'
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000050_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000052_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryE0ampKZTIitJ3TkJ',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'------WebKitFormBoundaryE0ampKZTIitJ3TkJ\r\nContent-Disposition: form-data; name="username"\r\n\r\n{self.user_id}\r\n------WebKitFormBoundaryE0ampKZTIitJ3TkJ--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000056_GET_dataserver2_logon_nti_password(self):
        url = '/dataserver2/logon.nti.password'
        sval = f"{self.user_id}:temp001"
        password = base64.b64encode(sval.encode('utf-8')).decode('utf-8')
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'Authorization': f'Basic {password}',
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-NTI-Client-Version': '2021.6.0',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'username': self.user_id,
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000058_GET_loginsuccess(self):
        url = f'/loginsuccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            '_u': '42',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000059_GET_app(self):
        url = f'/app'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000145_GET_app_js_version(self):
        url = f'/app/js/version'
        
        headers = {
            'Connection': 'keep-alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000150_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000155_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'username={self.user_id}'

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000157_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '88cc604a9e8b445e918463b71ee251d6-b04f89b49e300f10-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000159_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryTPvnQhh8WzRAEYo7',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '88cc604a9e8b445e918463b71ee251d6-b62e021384a31d57-0',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundaryTPvnQhh8WzRAEYo7\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester7\r\n------WebKitFormBoundaryTPvnQhh8WzRAEYo7--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000160_GET_dataserver2_service(self):
        url = f'/dataserver2/service'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '88cc604a9e8b445e918463b71ee251d6-948212d0221c7548-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000162_GET_dataserver2_users_stress_tester7(self):
        url = f'/dataserver2/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '88cc604a9e8b445e918463b71ee251d6-8ada55459ba8e809-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000165_GET_dataserver2_users_stress_tester7(self):
        url = f'/dataserver2/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000167_GET_dataserver2_users_stress_tester7_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000169_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = f'/dataserver2/analytics/sessions/%40%40analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000170_GET_dataserver2_users_stress_tester7_Groups(self):
        url = f'/dataserver2/users/{self.user_id}/Groups'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000171_GET_dataserver2_users_stress_tester7_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000172_GET_dataserver2_users_stress_tester7_FriendsLists(self):
        url = f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000180_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000181_GET_vendor_ext_4_2_resources_ext_theme_classic_images_form_exclamation_gif(self):
        url = f'/vendor/ext-4.2/resources/ext-theme-classic/images/form/exclamation.gif'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '/vendor/ext-4.2/resources/ext-theme-classic/ext-theme-classic-all.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000182_GET_dataserver2_users_stress_tester7_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

        values = self.response.json()
        if 'Items' in values:
            items = values["Items"]
            for item in items:
                if item["CatalogEntry"]["ProviderUniqueID"] == self.course_uid:
                    self.course_ntiid = item["CatalogEntry"]["NTIID"]
                    links = item["CatalogEntry"]["Links"]
                    for link in links:
                        if link['rel'] == "CourseInstance":
                            self.course_instance_link = link['href']
        print(self.course_instance_link, self.course_ntiid)

    @task()
    def task_000183_GET_dataserver2_users_stress_tester7_Calendars_40_40events(self):
        url = f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1618289999.189',
            'notBefore': '1618271090.189',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000184_GET_dataserver2_users_stress_tester7_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000185_GET_dataserver2_users_stress_tester7_Communities_Communities(self):
        url = f'/dataserver2/users/{self.user_id}/Communities/Communities'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000187_POST_dataserver2_users_stress_tester7_FriendsLists(self):
        url = f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '138',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.friendslist","tags":[],"Username":f"mycontacts-{self.user_id}","alias":"My Contacts","friends":[]}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000188_GET_dataserver2_users_stress_tester7_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000191_GET_dataserver2_users_stress_tester7_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '10',
            'batchStart': '0',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000192_GET_dataserver2_users_stress_tester7_FriendsLists(self):
        url = f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000200_GET_dataserver2_users_stress_tester7_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000201_GET_dataserver2_users_stress_tester7_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/{self.user_id}/Communities/AdministeredCommunities'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000229_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0xa88095_3A5573657273_3AucvfaTqmB9A(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': '3d9d76506a02403894f3e1e09101b4bd-9386efc04c3dc21d-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': '',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000231_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000233_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40AssignmentSummaryByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40AssignmentSummaryByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

        values = self.response.json()
        if 'Items' in values:
            items = values['Items'][self.course_ntiid]
            for item in items:
                title = item['title']
                if title == self.assignment_name:
                    self.assignment_target_ntiid = item['NTIID']
                    links = item['Links']
                    for link in links:
                        if link['rel'] == 'Commence':
                            self.commence_link = link['href']
                        elif link['rel'] == 'Savepoint':
                            self.savepoint_link = link['href']
                        elif link['rel'] == 'MetadataAttempts':
                            self.metadata_attempts_link = link['href']
                        elif link['rel'] == 'Submit':
                            self.submit_link = link['href']
        else:
            print(values)
        print(self.commence_link)
        print(self.savepoint_link)
        print(self.metadata_attempts_link)
        print(self.submit_link)

    @task()
    def task_000234_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000235_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3d9d76506a02403894f3e1e09101b4bd-bf0cf61285521646-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000238_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000240_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_ContentPackageBundle_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/ContentPackageBundle/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '10000',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000243_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000244_GET_dataserver2_users_stress_tester7_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139_AssignmentHistories_stress_tester7(self):
        url = f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139/AssignmentHistories/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000245_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_CourseTabPreferences(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/CourseTabPreferences'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3d9d76506a02403894f3e1e09101b4bd-974c1151a0c6e73d-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000246_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000248_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'true',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000249_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000250_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000251_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000253_GET_app_api_videos_youtube(self):
        url = f'/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'id': '-M1BVZ4zECA',
            'part': 'contentDetails,snippet,statistics',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000254_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000261_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000262_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e0a7c05862344409a1baf0f1779e2617-a76c6e211ab36bb1-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000263_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e0a7c05862344409a1baf0f1779e2617-8ce9df4c1da207ea-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000264_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e0a7c05862344409a1baf0f1779e2617-bde04d2b4fe28e7b-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000265_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e0a7c05862344409a1baf0f1779e2617-8e19374540b0f38e-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000270_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000271_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-8a9a0e6965fbab62-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'true',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000273_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-ab25b0f12ac466b2-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000274_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-84a0142adb26937a-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000275_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-b2f07774d5b93ba5-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000276_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-a96c04f267b07eaf-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000277_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-9db94b4011763353-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000278_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-809b85d35a93c938-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000279_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': '6eeac66ed1ec408aac29ea81e95b3d20-b0ac3de513819c2f-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

        values = self.response.json()
        if 'version' in values:
            self.version = values['version']
        else:
            print(values)

        if 'parts' in values and values['parts'] is not None and self.assignment_parts is None:
            self.assignment_parts = values['parts'][0]
        print(f'found assignment version: {self.version}')

    @task()
    def task_000282_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

        if self.version is None:
            values = self.response.json()
            if 'version' in values:
                self.version = values['version']
            else:
                print(values)

            if 'parts' in values and values['parts'] is not None and self.assignment_parts is None:
                self.assignment_parts = values['parts'][0]
        print(f'found assignment version: {self.version}')

    @task()
    def task_000284_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_40_40Commence(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/%40%40Commence'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {'version': self.version}
        print(f'commence call data: {self.user_id} {data}')
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )
        values = self.response.json()
        if 'parts' in values and self.assignment_parts is None:
            self.assignment_parts = values['parts'][0]


    @task()
    def task_000285_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000288_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentSavepoints_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentSavepoints/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/Savepoint'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000289_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000291_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_8060728956857908844_9D3722ACA2C4E554852D_eclipse_toc_xml(self):
        url = f'/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_8060728956857908844.9D3722ACA2C4E554852D/eclipse-toc.xml'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'dc': '1613229711',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000292_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_8060728956857908842_0CAD0F4A7574DA804B8A_eclipse_toc_xml(self):
        url = f'/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_8060728956857908842.0CAD0F4A7574DA804B8A/eclipse-toc.xml'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'dc': '1613229707',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000293_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000294_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentAttemptMetadataItem_40_40TimeRemaining(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40TimeRemaining'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000296_POST_dataserver2_analytics_batch_events(self):
        url = f'/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '863',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618271110.98,
                           "user":self.user_id,
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084",
                           "Duration":0.001,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084"}]}
        data_str=json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000297_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000298_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentSavepoints_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentSavepoints/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/Savepoint'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '20018',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        index = 0
        duration = randrange(3, 15)
        questions = []
        if self.assignment_parts is None:
            print(f'FAILED TO GET ASSIGNMENTINFO: {self.user_id}, {self.course_uid}')
        else:
            questions = self.assignment_parts['question_set']['questions']
        while index < len(questions):
            if index > 0:
                wait_time = randrange(3, 15)
                time.sleep(wait_time)
                duration += wait_time
            answers = {"MimeType": "application/vnd.nextthought.assessment.assignmentsubmission",
                       "tags": [],
                       "assignmentId": self.assignment_target_ntiid,
                       "CreatorRecordedEffortDuration": duration,
                       "version": self.version
                       }
            question_parts = []

            counter = 0
            for question in questions:
                question_submission = {
                    "MimeType": "application/vnd.nextthought.assessment.questionsubmission",
                    "NTIID": question["NTIID"],
                    "questionId": question["NTIID"],
                    "ContainerId": "",
                    "CreatorRecordedEffortDuration": None,
                    "tags": []}

                # generate random answers for questions
                selection_type = question['parts'][0]["Class"]
                selections = question['parts'][0]["choices"]
                upper_bound = len(selections)
                if selection_type == 'MultipleChoicePart' and counter <= index:
                    question_submission["parts"] = [randrange(upper_bound)]
                if selection_type == 'MultipleChoiceMultipleAnswerPart' and counter <= index:
                    question_submission["parts"] = [sorted(sample(range(0, upper_bound), randrange(1, upper_bound)))]
                if counter > index:
                    question_submission["parts"] = [None]

                question_submission["ContainerId"] = ""
                question_parts.append(question_submission)
                counter += 1

            parts = [{"MimeType": "application/vnd.nextthought.assessment.questionsetsubmission",
                      "NTIID": None,
                      "tags": [],
                      "questionSetId": self.assignment_parts['QuestionSetId'],
                      "questions": question_parts
                      }]
            answers["parts"] = parts
            answers_str = json.dumps(answers)
            self.response = self.client.request(
                method='POST',
                url=url,
                headers=headers,
                data=answers_str,
                name=url.replace(self.user_id, 'user')
            )
            index += 1
            if index == len(questions):
                self.final_answer = answers_str


    @task()
    def task_000303_POST_dataserver2_analytics_batch_events(self):
        url = f'/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '864',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A","timestamp":1618271110.98,
                           "user":self.user_id,
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084",
                           "Duration":10.003,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084"}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000304_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '25372',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=self.final_answer,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000305_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000306_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000307_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000309_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000310_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000311_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000312_GET_dataserver2_users_stress_tester7_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester7_OID_0x0148d3b9_3A5573657273_3AVr26HnyV3Gw(self):
        url = f'/dataserver2/users/{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3A{self.user_id}-OID-0x0148d3b9%3A5573657273%3AVr26HnyV3Gw'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000313_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000314_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000315_GET_dataserver2_users_stress_tester7_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester7_OID_0x0148d3b8_3A5573657273_3AVr26HnyV3Gx(self):
        url = f'/dataserver2/users/{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3A{self.user_id}-OID-0x0148d3b8%3A5573657273%3AVr26HnyV3Gx'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000316_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000322_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-8282f90276f16f36-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000324_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000325_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-99ea00eb98d3d398-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000326_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-8199b35825b28821-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000327_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-bad7db4d729fd498-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000328_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-a018af4e240677cb-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000329_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-aecba094a5a5f719-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000330_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-b98961d8539cc415-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

        values = self.response.json()
        if 'version' in values:
            self.version = values['version']
        else:
            print(values)

        print("B7EBF4310E05C7_0084" + self.version)

    @task()
    def task_000331_POST_dataserver2_analytics_batch_events(self):
        url = f'/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '864',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-98b4dd9496d186e0-0',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A","timestamp":1618271110.98,
                           "user":self.user_id,"ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084",
                           "Duration":19.902,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084"}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000332_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000333_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_40_40Commence(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/%40%40Commence'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000334_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentSavepoints_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentSavepoints/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/Savepoint'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000335_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000336_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'b4b3672db6494f7f9ae547a8497422fa-af5c5964b66b4522-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000337_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000338_POST_dataserver2_analytics_batch_events(self):
        url = f'/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '860',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618271131.908,
                           "user":self.user_id,
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084"}]}

        data_str=json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000339_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000342_POST_dataserver2_analytics_batch_events(self):
        url = f'/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '864',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618271131.908,
                           "user":self.user_id,
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084",
                           "Duration":9.096,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084"}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000343_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000345_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentSavepoints_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentSavepoints/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/Savepoint'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '44782',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":None,
                          "tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-27758084485CA5EB0E4B6E1696EAA2FD38E51D2A0649A88B35ED591768B39EB0_0084",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-805AFCE29113B27DCB03D0C4788361EF89482A3F313FC6BC7EE18CD49EE80666_0081",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-805AFCE29113B27DCB03D0C4788361EF89482A3F313FC6BC7EE18CD49EE80666_0081",
                                        "parts":[{"MimeType":"application/vnd.nextthought.assessment.uploadedfile",
                                                  "filename":"sample.doc",
                                                  "value":"data:application/msword;base64,0M8R4KGxGuEAAAAAAAAAAAAAAAAAAAAAPgADAP7/CQAGAAAAAAAAAAAAAAABAAAAFwAAAAAAAAAAEAAAGQAAAAEAAAD+////AAAAABYAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////spcEAWyAJBAAA+BK/AAAAAAAAEAAAAAAABAAAcAkAAA4AYmpiauIA4gAAAAAAAAAAAAAAAAAAAAAAAAAJBBYAIhoAAIBqAQCAagEAcAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//w8AAAAAAAAAAAD//w8AAAAAAAAAAAD//w8AAAAAAAAAAAAAAAAAAAAAAGwAAAAAANABAAAAAAAA0AEAANABAAAAAAAA0AEAAAAAAADQAQAAAAAAANABAAAAAAAA0AEAABQAAAAAAAAAAAAAAOQBAAAAAAAAzgYAAAAAAADOBgAAAAAAAM4GAAAAAAAAzgYAAAwAAADaBgAALAAAAOQBAAAAAAAAchYAADIBAAASBwAAFgAAACgHAAAAAAAAKAcAAAAAAAAoBwAAAAAAACgHAAAAAAAAKAcAAAAAAAAoBwAAAAAAACgHAAAAAAAA8RUAAAIAAADzFQAAAAAAAPMVAAAAAAAA8xUAAAAAAADzFQAAAAAAAPMVAAAAAAAA8xUAACQAAACkFwAAIAIAAMQZAABuAAAAFxYAABUAAAAAAAAAAAAAAAAAAAAAAAAA0AEAAAAAAAAoBwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoBwAAAAAAACgHAAAAAAAAKAcAAAAAAAAoBwAAAAAAABcWAAAAAAAApgcAAAAAAADQAQAAAAAAANABAAAAAAAAKAcAAAAAAAAAAAAAAAAAACgHAAAAAAAALBYAABYAAACmBwAAAAAAAKYHAAAAAAAApgcAAAAAAAAoBwAALgAAANABAAAAAAAAKAcAAAAAAADQAQAAAAAAACgHAAAAAAAA8RUAAAAAAAAAAAAAAAAAAKYHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAcAAAAAAADxFQAAAAAAAKYHAAA+AQAApgcAAAAAAADkCAAAbgEAAHETAAAIAQAA0AEAAAAAAADQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJRUAAAAAAAAoBwAAAAAAAAYHAAAMAAAA4N+7gEXRwgHkAQAA6gQAAM4GAAAAAAAAVgcAAC4AAAB5FAAAIAAAAAAAAAAAAAAAJRUAAMwAAABCFgAAMAAAAHIWAAAAAAAAmRQAAIwAAAAyGgAAAAAAAIQHAAAiAAAAMhoAAAAAAAAlFQAAAAAAAKYHAAAAAAAA5AEAAAAAAADkAQAAAAAAANABAAAAAAAA0AEAAAAAAADQAQAAAAAAANABAAAAAAAAAgDZAAAAVGhpcyBpcyBIZWFkaW5nMSBUZXh0DVRoaXMgaXMgYSByZWd1bGFyIHBhcmFncmFwaCB3aXRoIHRoZSBkZWZhdWx0IHN0eWxlIG9mIE5vcm1hbC4gVGhpcyBpcyBhIHJlZ3VsYXIgcGFyYWdyYXBoIHdpdGggdGhlIGRlZmF1bHQgc3R5bGUgb2YgTm9ybWFsLiBUaGlzIGlzIGEgcmVndWxhciBwYXJhZ3JhcGggd2l0aCB0aGUgZGVmYXVsdCBzdHlsZSBvZiBOb3JtYWwuIFRoaXMgaXMgYSByZWd1bGFyIHBhcmFncmFwaCB3aXRoIHRoZSBkZWZhdWx0IHN0eWxlIG9mIE5vcm1hbC4gVGhpcyBpcyBhIHJlZ3VsYXIgcGFyYWdyYXBoIHdpdGggdGhlIGRlZmF1bHQgc3R5bGUgb2YgTm9ybWFsLg1UaGlzIGlzIGEgRGVmaW5lZCBCbG9jayBTdHlsZSBDYWxsZWQgQmxvY2tTdHlsZVRlc3QNVGhpcyBpcyBtb3JlIE5vcm1hbCB0ZXh0Lg1UaGlzIGlzIEhlYWRpbmcgMiB0ZXh0DVRoaXMgaXMgbW9yZSBOb3JtYWwgdGV4dC4gVGhpcyBpcyBib2xkLCB0aGlzIGlzIGl0YWxpYywgYW5kIHRoaXMgaXMgYm9sZCBpdGFsaWMuIFRoaXMgaXMgbm9ybWFsLiBUaGlzIGlzIGluIGEgZGVmaW5lZCBpbmxpbmUgc3R5bGUgY2FsbGVkIElubGluZVN0eWxlLiBUaGlzIGlzIG5vcm1hbC4gVGhpcyBpcyByZWQgdGV4dC4gVGhpcyBpcyBub3JtYWwuIA1UaGlzIGJsb2NrIGlzIGNlbnRlcmVkLg1UaGlzIGlzIGxlZnQtYWxpZ25lZC4gDQ1GaXJzdCBpdGVtIG9mIGJ1bGxldGVkIGxpc3QuIA1TZWNvbmQgaXRlbSBvZiBidWxsZXRlZCBsaXN0Lg1TZWNvbmQgcGFyYWdyYXBoIG9mIHNlY29uZCBpdGVtIG9mIGJ1bGxldGVkIGxpc3QuIA1UaGlyZCBpdGVtIG9mIGJ1bGxldGVkIGxpc3QuDUZpcnN0IGl0ZW0gb2YgdGhpcmQgaXRlbZJzIG5lc3RlZCBsaXN0DVNlY29uZCBpdGVtIG9mIHRoaXJkIGl0ZW2ScyBuZXN0ZWQgbGlzdA1Gb3VydGggYW5kIGZpbmFsIGl0ZW0gb2YgbWFpbiBidWxsZXRlZCBsaXN0Lg0NVGhpcyBpcyBOb3JtYWwgdGV4dC4NDUZpcnN0IGl0ZW0gb2YgbnVtYmVyZWQgbGlzdC4gDVNlY29uZCBpdGVtIG9mIG51bWJlcmVkIGxpc3QuDVNlY29uZCBwYXJhZ3JhcGggb2Ygc2Vjb25kIGl0ZW0gb2YgbnVtYmVyZWQgbGlzdC4gDVRoaXJkIGl0ZW0gb2YgbnVtYmVyZWQgbGlzdC4NDUhlcmUgaXMgYSBCTVAgcGljdHVyZToNAQ1IZXJlIGlzIGEgdGFibGU6DQdOZXcgWW9yawdC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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAACAAAAAwAAAAQAAAAFAAAABgAAAAcAAAAIAAAACQAAAAoAAAALAAAADAAAAA0AAAD+////DwAAABAAAAARAAAAEgAAABMAAAAUAAAAFQAAAP7////9////GAAAACIAAAD+////GwAAABwAAAAdAAAAHgAAAB8AAAAgAAAAIQAAACMAAAAuAAAALQAAACUAAAAmAAAAJwAAACgAAAApAAAAKgAAACsAAAAsAAAA/v///y8AAAD+////MAAAAP7///8yAAAAMwAAADQAAAA1AAAANgAAADcAAAA4AAAAOQAAADoAAAA7AAAAPAAAAD0AAAA+AAAA/v//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////UgBvAG8AdAAgAEUAbgB0AHIAeQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYABQH//////////w0AAAAGCQIAAAAAAMAAAAAAAABGAAAAAAAAAAAAAAAAYGTagEXRwgEaAAAAwBYAAAAAAABEAGEAdABhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgACAf///////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AAAAAEAAAAAAAAFcAbwByAGQARABvAGMAdQBtAGUAbgB0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaAAIBDAAAAP//////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACIaAAAAAAAATwBiAGoAZQBjAHQAUABvAG8AbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYAAQEPAAAA/////wQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAID8pIBF0cIBYGTagEXRwgEAAAAAAAAAAAAAAABfADEAMQAwADYAMwA5ADYANAA3ADEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAABAf//////////BgAAACAIAgAAAAAAwAAAAAAAAEYAAAAAgPykgEXRwgHACaiARdHCAQAAAAAAAAAAAAAAAAEATwBsAGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAIB////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAwBQAFIASQBOAFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4AAgEFAAAACAAAAP////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAIg8AAAAAAAABAEMAbwBtAHAATwBiAGoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgACAf///////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4AAABmAAAAAAAAAP7///8CAAAAAwAAAAQAAAAFAAAABgAAAAcAAAAIAAAACQAAAAoAAAALAAAADAAAAA0AAAAOAAAADwAAABAAAAARAAAAEgAAABMAAAAUAAAAFQAAABYAAAAXAAAAGAAAABkAAAAaAAAAGwAAABwAAAAdAAAAHgAAAB8AAAAgAAAAIQAAACIAAAAjAAAAJAAAACUAAAAmAAAAJwAAACgAAAApAAAAKgAAACsAAAAsAAAALQAAAC4AAAAvAAAAMAAAADEAAAAyAAAAMwAAADQAAAA1AAAANgAAADcAAAA4AAAAOQAAADoAAAA7AAAAPAAAAD0AAAD+////PwAAAP7////+////QgAAAEMAAABEAAAA/v///0YAAABHAAAASAAAAEkAAAD+////SwAAAEwAAABNAAAATgAAAE8AAABQAAAA/v///1IAAABTAAAAVAAAAFUAAABWAAAAVwAAAFgAAAD+////WgAAAP7/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AQAAAggAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgA8SJ0DAAAAQAJAAADjQcAAAgAHAAAAAAABQAAAAkCAAAAAAUAAAABAv///wAFAAAABAENAAAABQAAAAIBAgAAAAUAAAAMAvECQQgDAAAAHgAEAAAAJwH//wMAAAAeAAQAAAAnAf//BQAAAAsCAAAAAAMAAAAeAAUAAAABAv///wAFAAAACQIAAAAABAAAACcB//8DAAAAHgAFAAAAAQL///8ABQAAAAkCAAAAAAcAAAAWBPACQAgAAAAABAAAACcB//8DAAAAHgAFAAAAAQL///8ABQAAAAkCAAAAAAcAAAAWBPACQAgAAAAAHAAAAPsCrf8AAAAAAAC8AgAAAAAAAAAgQXJpYWwA9XdAAAAASg0KDI9J9XeYSfV3AQAAAAAAMAAEAAAALQEAABwAAAD7Aq3/AAAAAAAAkAEBAAAAAAAAIEFyaWFsAPV3QAAAACINCgSPSfV3mEn1dwEAAAAAADAABAAAAC0BAQAcAAAA+wIQAAcAAAAAALwCAAAAAAECAiJTeXN0ZW0AAAAACgAAAAQAAAAAAP////8BAAAAAAAwAAQAAAAtAQIABAAAACcB//8DAAAAHgAEAAAALQEBAAUAAAABAv///wAFAAAACQIAAAAABwAAABYE5gBACIcACAAEAAAALQEBAAUAAAAEAQ0AAAAFAAAAAgEBAAAA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/wAAAAAAAAAAAAAAAIL///8AAAAAAAAAAAAAAACB////AAAAAAAAAAAAAAAAgP///wAAAAAAAAAAAAAAAIj///8AAAAAAAAAAAAAAAB/////AAAAAAAAAAAAAAAAfv///wAAAAAAAAAAAAAAAH3///8AAAAAAAAAAAAAAAB8////AAAAAAAAAAAAAAAAIDDxXQAAAAAAAAAAAAAAAAQKuyoAAAAAAAAAAAAAAAAQaVkXAAAAAAAAAAAAAAAA////////////////////////////////////////////////////////////////////////DQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASAAEACQQDAAkEBQAJBAEACQQDAAkEBQAJBAEACQQDAAkEBQAJBBIADwAJBBkACQQbAAkEDwAJBBkACQQbAAkEDwAJBBkACQQbAAkEEgAPAAkEDwAJBAUACQQBAAkEAwAJBAUACQQBAAkEAwAJBAUACQQAAAAAgQQAAIIEAACLBAAAkgQAAJoEAACbBAAApAQAAKkEAACxBAAAuQQAAMAEAADBBAAAyAQAANAEAADaBAAA4QQAAOsEAADsBAAA9QQAAPwEAAABBQAACgUAABAFAAARBQAAcgUAAAAAAAAIAAAAAgEAAAIBAAACAQAAAgEAAJ4BAAACAQAAAgEAAAIBAAACAQAAAgEAAJ4BAAACAQAAAgEAAAIBAAACAQAAAgEAAJ4BAAACAQAAAgEAAAIBAAACAQAAAgEAAJYBAAD/QAGAAQAAAAAAAAAAAKQ3VgUBAAAAAAAAAAAAAAAAAAAAAAAAAAIQAAAAAAAAAHAFAACgAAAIAEAAAP//AQAAAAcAVQBuAGsAbgBvAHcAbgD//wEACAAAAAAAAAAAAAAA//8BAAAAAAD//wAAAgD//wAAAAD//wAAAgD//wAAAAAFAAAARxaQAQAAAgIGAwUEBQIDBIc6ACAAAAAAAAAAAAAAAAD/AQAAAAAAAFQAaQBtAGUAcwAgAE4AZQB3ACAAUgBvAG0AYQBuAAAANRaQAQIABQUBAgEHBgIFBwAAAAAAAAAQAAAAAAAAAAAAAACAAAAAAFMAeQBtAGIAbwBsAAAAMyaQAQAAAgsGBAICAgICBIc6ACAAAAAAAAAAAAAAAAD/AQAAAAAAAEEAcgBpAGEAbAAAAD81kAEAAAIHAwkCAgUCBASHegAgAAAAgAgAAAAAAAAA/wEAAAAAAABDAG8AdQByAGkAZQByACAATgBlAHcAAAA7BpABAgAFAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAIAAAAAAVwBpAG4AZwBkAGkAbgBnAHMAAAAiAAQAcQiIGADw0AIAAGgBAAAAADRUWSbuU3ImAAAAAAcAKQAAAMkAAAB7BAAAAQACAAAABAADEAkAAAAAAAAAAAAAAAEAAQAAAAEAAAAAAAAAIQMA8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAegBbQAtACBgTIwAAAAAAAAAAAAAAAAAACABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgUAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAMMoNRAPAQAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8SAAAAAAAAAAAAAAAAAAAAEQBMAGUAeABpAHMAIABOAGUAeABpAHMAIABHAHIAbwB1AHAAEQBMAGUAeABpAHMAIABOAGUAeABpAHMAIABHAHIAbwB1AHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="}],"CreatorRecordedEffortDuration":None,"ContainerId":""}],"CreatorRecordedEffortDuration":14,"ContainerId":""}],
                "CreatorRecordedEffortDuration":14,"version":self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000347_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '1955',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":None,
                          "tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-27758084485CA5EB0E4B6E1696EAA2FD38E51D2A0649A88B35ED591768B39EB0_0084",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-805AFCE29113B27DCB03D0C4788361EF89482A3F313FC6BC7EE18CD49EE80666_0081",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-805AFCE29113B27DCB03D0C4788361EF89482A3F313FC6BC7EE18CD49EE80666_0081",
                                        "parts":[{"Class":"QUploadedFile","CreatedTime":1618271146.297744,
                                                  "FileMimeType":"application/msword","Last Modified":1618271146.297744,
                                                  "MimeType":"application/vnd.nextthought.assessment.uploadedfile",
                                                  "NTIID":"tag:nextthought.com,2011-10:system-OID-0x0148d350:5573657273",
                                                  "OID":"tag:nextthought.com,2011-10:system-OID-0x0148d350:5573657273",
                                                  "contentType":"application/msword",
                                                  "download_url":"/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asystem-OID-0x0148d350%3A5573657273/@@download/sample.doc",
                                                  "filename":"sample.doc","name":"sample.doc","size":32768,
                                                  "url":"/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asystem-OID-0x0148d350%3A5573657273/@@view/sample.doc",
                                                  "value":"/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asystem-OID-0x0148d350%3A5573657273/@@view/sample.doc"}],
                                        "CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084"}],
                          "CreatorRecordedEffortDuration":16,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084"}],
                "CreatorRecordedEffortDuration":16,"version":self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000348_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000349_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000350_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000351_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000352_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000353_GET_dataserver2_users_stress_tester7_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester7_OID_0x0148d476_3A5573657273_3AVr26HnyV3Gh(self):
        url = f'/dataserver2/users/{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3A{self.user_id}-OID-0x0148d476%3A5573657273%3AVr26HnyV3Gh'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000354_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000355_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentAttemptMetadata_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentAttemptMetadata/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000356_GET_dataserver2_users_stress_tester7_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester7_OID_0x0148d475_3A5573657273_3AVr26HnyV3Gj(self):
        url = f'/dataserver2/users/{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3A{self.user_id}-OID-0x0148d475%3A5573657273%3AVr26HnyV3Gj'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000357_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000358_POST_dataserver2_analytics_batch_events(self):
        url = f'/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '863',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618271131.908,"user":self.user_id,
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084",
                           "Duration":19.1,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084"}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000359_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/items/NTI-NTIAssignmentRef-27FEE99878A8AB4A627C56CAF72B9ACF240D7B9A8E9F74FCD1B1CA79034A6225_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000362_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-90b8da81d09fa8e2-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000364_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000365_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-a91b7d4b929cb652-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'true',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000366_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-825396c9a23e73fb-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000367_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-8e2e380d8fbaaee1-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000368_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-b70ab82aad0fa151-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000369_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-92ac1d09f7f250f9-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000370_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '37789778ca12432b9065a26058332a0d-b98951127d82dc02-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000373_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = f'/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000374_GET_app_course_admin_user_OID_0xa88095_3A5573657273_3AucvfaTqmB9A_lessons_NTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3(self):
        url = f'/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000375_GET_app_resources_strings_strings_js(self):
        url = f'/app/resources/strings/strings.js'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000378_GET_app_js_version(self):
        url = f'/app/js/version'
        
        headers = {
            'Connection': 'keep-alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000379_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000382_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'''username={self.user_id}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000384_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-91c609743d4f72d6-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000385_POST_dataserver2_logon_handshake(self):
        url = f'/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary5jdqWorssIElAWBP',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-bf5adfca88597f50-0',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'''------WebKitFormBoundary5jdqWorssIElAWBP\r\nContent-Disposition: form-data; name="username"\r\n\r\n{self.user_id}\r\n------WebKitFormBoundary5jdqWorssIElAWBP--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000387_GET_dataserver2_service(self):
        url = f'/dataserver2/service'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-9a61e2df727004bc-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000388_GET_favicon_ico(self):
        url = f'/favicon.ico'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000389_GET_dataserver2_users_stress_tester7(self):
        url = f'/dataserver2/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-9c7c78d95044b70d-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000391_GET_dataserver2_users_stress_tester7(self):
        url = f'/dataserver2/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000392_GET_dataserver2_users_stress_tester7_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000393_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = f'/dataserver2/analytics/sessions/%40%40analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-95919cf0d2d32aed-0',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000394_GET_dataserver2_users_stress_tester7_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000395_GET_dataserver2_users_stress_tester7_Groups(self):
        url = f'/dataserver2/users/{self.user_id}/Groups'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000396_GET_dataserver2_users_stress_tester7_FriendsLists(self):
        url = f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000397_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-b9567369c4b8abaf-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000398_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0xa88095_3A5573657273_3AucvfaTqmB9A(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': '78a3b2d4abac4d93a9839a29dc8fc754-8b1668c453b29c7a-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': '',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000399_GET_dataserver2_users_stress_tester7_Calendars_40_40events(self):
        url = f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1618289999.751',
            'notBefore': '1618271161.751',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )


    @task()
    def task_000401_GET_dataserver2_users_stress_tester7_FriendsLists(self):
        url = f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000402_GET_dataserver2_users_stress_tester7_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000403_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000404_GET_dataserver2_users_stress_tester7_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '10',
            'batchStart': '0',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000406_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000407_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40AssignmentSummaryByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40AssignmentSummaryByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000408_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000409_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000410_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_ContentPackageBundle_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/ContentPackageBundle/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '10000',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000411_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000412_GET_dataserver2_users_stress_tester7_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139_AssignmentHistories_stress_tester7(self):
        url = f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139/AssignmentHistories/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000413_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_CourseTabPreferences(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/CourseTabPreferences'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000414_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'true',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000415_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000416_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000417_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'accept': 'application/vnd.nextthought.note',
            'filter': 'TopLevel',
            'omit_unpublished': 'True',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000418_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000419_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000420_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000421_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000422_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester7(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000423_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_AssignmentHistories_stress_tester7_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/AssignmentHistories/{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000424_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139(self):
        url = f'/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000426_GET_dataserver2_users_stress_tester7_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000427_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = f'/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000428_GET_dataserver2_logon_logout(self):
        url = f'/dataserver2/logon.logout'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'success': '/login/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000429_GET_login(self):
        url = f'/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000431_GET_dataserver2_logon_ping(self):
        url = f'/dataserver2/logon.ping'
        
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
            name=url.replace(self.user_id, 'stress.tester')
        )

        time.sleep(7200)



class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
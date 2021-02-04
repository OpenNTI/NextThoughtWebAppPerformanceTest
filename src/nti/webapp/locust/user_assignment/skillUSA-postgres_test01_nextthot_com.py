# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import urllib.parse
from random import randrange
from random import sample
import time

USER_CREDENTIALS = list(range(1, 1101))
ASSIGNMENT_INFO = [
    # {
    #     "course_uid": "LongAssignCourse4",
    #     "assignment_name": "80 Questions multiple choice"
    # },
    {
        "course_uid": "MASTER-USR",
        "assignment_name": "Technical Assessment"
    },
    {
        "course_uid": "MASTER-WEB",
        "assignment_name": "Technical Assessment"
    },
    {
        "course_uid": "MASTER-MRT",
        "assignment_name": "Technical Assessment"
    },
    {
        "course_uid": "MASTER-DA",
        "assignment_name": "Technical Assessment"
    },
    {
        "course_uid": "120-MM",
        "assignment_name": "Technical Assessment"
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
    def task_000006_GET_dataserver2_logon_nti_password(self):
        url = '' + '/dataserver2/logon.nti.password'
        sval = f"{self.user_id}:temp001"
        password = base64.b64encode(sval.encode('utf-8')).decode('utf-8')

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-login',
            'Authorization': f"Basic {password}",
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.9.0',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/login/',
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
            name=url.replace(self.user_id, 'user')
        )

    ### Additional tasks can go here #    @task()
    def task_000007_GET_loginsuccess(self):
        url = '' + '/loginsuccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/login/',
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
        )

    @task()
    def task_000008_GET_app(self):
        url = '' + '/app'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000009_GET_vendor_ext_4_2_resources_css_ext_all_css(self):
        url = '' + '/vendor/ext-4.2/resources/css/ext-all.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000010_GET_vendor_mathquill_0_9_4_mathquill_css(self):
        url = '' + '/vendor/mathquill-0.9.4/mathquill.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000011_GET_app_resources_css_legacy_css(self):
        url = '' + '/app/resources/css/legacy.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000012_GET_site_assets_webapp_site_css(self):
        url = '' + '/site-assets/webapp/site.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000013_GET_app_resources_shared_index_aa90340f6e81eb0af7eb_css(self):
        url = '' + '/app/resources/shared~index-aa90340f6e81eb0af7eb.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000014_GET_app_resources_vendor_index_f89bf420673703bab244_css(self):
        url = '' + '/app/resources/vendor~index-f89bf420673703bab244.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000015_GET_app_resources_index_e0bf32e11613701ec7db_css(self):
        url = '' + '/app/resources/index-e0bf32e11613701ec7db.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000050_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000051_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'username={self.user_id}'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000052_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000053_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryqGcwEi0Xk2vGAkGT',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'------WebKitFormBoundaryqGcwEi0Xk2vGAkGT\r\nContent-Disposition: form-data; name="username"\r\n\r\n{self.user_id}\r\n------WebKitFormBoundaryqGcwEi0Xk2vGAkGT--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000054_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000055_GET_dataserver2_users_stress_tester1(self):
        url = '' + f'/dataserver2/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000056_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = '' + f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000058_GET_dataserver2_users_stress_tester1(self):
        url = '' + f'/dataserver2/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000059_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_WebApp(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000061_GET_site_assets_shared_strings_en_json(self):
        url = '' + '/site-assets/shared/strings.en.json'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000062_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000063_GET_dataserver2_users_stress_tester1_Groups(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Groups'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000064_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = '' + f'/dataserver2/users/{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000065_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000067_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000073_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1611295199.865',
            'notBefore': '1611292492.865',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000074_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Favorites(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
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
    def task_000075_GET_dataserver2_users_stress_tester1_Communities_Communities(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Communities/Communities'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000076_GET_dataserver2_users_stress_tester1_ContentBundles_VisibleContentBundles(self):
        url = '' + f'/dataserver2/users/{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000077_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1611295199.907',
            'notBefore': '1611292492.907',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000078_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000079_GET_site_assets_shared_brand_web_library_png(self):
        url = '' + '/site-assets/shared/brand_web_library.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000082_GET_dataserver2_users_stress_tester1_Courses_AdministeredCourses_40_40Favorites(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

        values = self.response.json()
        if 'Items' in values:
            items = values["Items"]
            for item in items:
                if item["CatalogEntry"]["NTIID"] == self.course_ntiid:
                    links = item["CatalogEntry"]["Links"]
                    for link in links:
                        if link['rel'] == "CourseInstance":
                            self.course_instance_link = link['href']
        print(self.course_instance_link)

    @task()
    def task_000083_GET_dataserver2_users_stress_tester1_Communities_AdministeredCommunities(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Communities/AdministeredCommunities'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000084_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '50',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000085_GET_app_resources_images_7f0d99a5b5c1fd285d7623ab678e12b5_png(self):
        url = '' + '/app/resources/images/7f0d99a5b5c1fd285d7623ab678e12b5.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/shared~index-aa90340f6e81eb0af7eb.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000087_GET_app_resources_fonts_e8b470ef2ea162353e3f5a60ecb96d12_ttf(self):
        url = '' + '/app/resources/fonts/e8b470ef2ea162353e3f5a60ecb96d12.ttf'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Origin': '' + '',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'font',
            'Referer': '' + '/app/resources/index-e0bf32e11613701ec7db.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000094_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0x2166c2_3A5573657273_3APc3MCYfnMkJ(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000096_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_40_40UserCoursePreferredAccess(self):
        url = f'{self.course_instance_link}/%40%40UserCoursePreferredAccess'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000098_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = '' + f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

        values = self.response.json()
        if 'contents' in values[0]:
            links = values[0]['contents'][0]['Links']
            for link in links:
                if link['rel'] == 'overview-content':
                    self.overview_content_link = link['href']
                elif link['rel'] == 'overview-summary':
                    self.overview_summary_link = link['href']
            print(self.overview_summary_link)
            print(self.overview_content_link)
        else:
            print(values)

    @task()
    def task_000099_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = f'{self.course_instance_link}/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000100_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_40_40AssignmentSummaryByOutlineNode(self):
        url = f'{self.course_instance_link}/@@AssignmentSummaryByOutlineNode'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
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
    def task_000101_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_40_40UserCoursePreferredAccess(self):
        url = f'{self.course_instance_link}/%40%40UserCoursePreferredAccess'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000105_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000108_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_CourseTabPreferences(self):
        url = f'{self.course_instance_link}/CourseTabPreferences'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000109_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000110_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_8201875887945803727_4744544919703575729_AssignmentHistories_stress_tester1(self):
        url = f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/{self.course_ntiid}/AssignmentHistories/{self.user_id}'
        url = urllib.parse.quote(url)
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000112_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000113_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000114_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_0_40_40overview_content(self):
        # url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/{self.course_identifier}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/%40%40overview-content'
        url = self.overview_content_link
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000115_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_0_40_40overview_summary(self):
        # url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/{self.course_identifier}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/%40%40overview-summary'
        url = self.overview_summary_link
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
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
        )

    @task()
    def task_000116_GET_app_resources_images_93a65098f08d99ae88aff545e381105c_png(self):
        url = '' + '/app/resources/images/93a65098f08d99ae88aff545e381105c.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/shared~index-aa90340f6e81eb0af7eb.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000119_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = '' + f'{self.course_instance_link}/Assessments/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

        values = self.response.json()
        if 'version' in values:
            self.version = values['version']
        else:
            print(values)

    @task()
    def task_000120_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Completion_CompletedItems_users_stress_tester1(self):
        url = '' + f'{self.course_instance_link}/Completion/CompletedItems/users/{self.user_id}'
        url = urllib.parse.quote(url)
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )


    @task()
    def task_000122_GET_app_resources_images_cea7d35e06a1a6ce53d32c1bf69ed73c_png(self):
        url = '' + '/app/resources/images/cea7d35e06a1a6ce53d32c1bf69ed73c.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/shared~index-aa90340f6e81eb0af7eb.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000123_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = '' + f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
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
        )

    @task()
    def task_000124_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = '' + f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
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
        )

    @task()
    def task_000126_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_0_40_40overview_content(self):
        # url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/{self.course_identifier}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/%40%40overview-content'
        url = self.overview_content_link
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
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
        )

    @task()
    def task_000127_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_0_40_40overview_summary(self):
        # url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/{self.course_identifier}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/%40%40overview-summary'
        url = self.overview_summary_link
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
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
        )

    @task()
    def task_000128_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Completion_CompletedItems_users_stress_tester1(self):
        url = '' + f'{self.course_instance_link}/Completion/CompletedItems/users/{self.user_id}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000129_GET_app_resources_images_cea7d35e06a1a6ce53d32c1bf69ed73c_png(self):
        url = '' + '/app/resources/images/cea7d35e06a1a6ce53d32c1bf69ed73c.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/shared~index-aa90340f6e81eb0af7eb.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000130_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = f'/dataserver2/Objects/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0x2166c2:5573657273:Pc3MCYfnMkJ',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000133_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = f'/dataserver2/Objects/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0x2166c2:5573657273:Pc3MCYfnMkJ',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )


    @task()
    def task_000134_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = f'/dataserver2/Objects/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0x2166c2:5573657273:Pc3MCYfnMkJ',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )
        values = self.response.json()
        if 'version' in values:
            self.version = values['version']
        else:
            print(values)

        if 'parts' in values and values['parts'] is not None and self.assignment_parts is None:
            self.assignment_parts = values['parts'][0]
        print(self.version)

    @task()
    def task_000135_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084_40_40Commence(self):
        url = f'{self.course_instance_link}/AssignmentAttemptMetadata/{self.user_id}/{self.assignment_target_ntiid}/@@Commence'
        url = self.commence_link if self.commence_link is not None else urllib.parse.quote(url)
        print(url)
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {'version': self.version}
        print(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            name=url.replace(self.user_id, 'user')
        )
        values = self.response.json()
        if 'parts' in values and self.assignment_parts is None:
            self.assignment_parts = values['parts'][0]
        print(self.version)

    @task()
    def task_000135_1_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_MASTER_WEB_AssignmentAttemptMetadata_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_CCEC304B1D5A53E0D47E7D0C6F54E2FFC6BDDA27762FA0DDD026BA1B6CF09CD9_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'{self.metadata_attempts_link}/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2021.0.0',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
            'Referer': '/app/course/site.admin.alpha-OID-0x27a5d6%3A5573657273%3AKS4zsTUN79t/lessons/NTI-NTICourseOutlineNode-9007678577205568157_4744547776816629863.0.0/items/NTI-NTIAssignmentRef-F896A60099C754C0D63F8D979BCD00B871343CAD9F5CD1166FC1DD6EB2F51D56_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )
        values = self.response.json()
        if 'parts' in values and self.assignment_parts is None:
            self.assignment_parts = values['parts'][0]

    @task()
    def task_000135_2_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_MASTER_WEB_AssignmentSavepoints_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_CCEC304B1D5A53E0D47E7D0C6F54E2FFC6BDDA27762FA0DDD026BA1B6CF09CD9_0084_Savepoint(
            self):
        url = f"{self.course_instance_link}/AssignmentSavepoints/{self.user_id}/{self.assignment_target_ntiid}/Savepoint"
        url = self.savepoint_link if self.savepoint_link is not None else url
        url = urllib.parse.quote(url)

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2021.0.0',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
            'Referer': '/app/course/site.admin.alpha-OID-0x27a5d6%3A5573657273%3AKS4zsTUN79t/lessons/NTI-NTICourseOutlineNode-9007678577205568157_4744547776816629863.0.0/items/NTI-NTIAssignmentRef-F896A60099C754C0D63F8D979BCD00B871343CAD9F5CD1166FC1DD6EB2F51D56_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000039_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_MASTER_WEB_AssignmentAttemptMetadata_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_CCEC304B1D5A53E0D47E7D0C6F54E2FFC6BDDA27762FA0DDD026BA1B6CF09CD9_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'{self.metadata_attempts_link}/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
            'Referer': '/app/course/site.admin.alpha-OID-0x27a5d6%3A5573657273%3AKS4zsTUN79t/lessons/NTI-NTICourseOutlineNode-9007678577205568157_4744547776816629863.0.0/items/NTI-NTIAssignmentRef-F896A60099C754C0D63F8D979BCD00B871343CAD9F5CD1166FC1DD6EB2F51D56_0088',
            'X-NTI-Client-Version': '2021.0.0',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )


    @task()
    def task_000043_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_MASTER_WEB_AssignmentAttemptMetadata_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_CCEC304B1D5A53E0D47E7D0C6F54E2FFC6BDDA27762FA0DDD026BA1B6CF09CD9_0084_UsersCourseAssignmentAttemptMetadataItem_40_40TimeRemaining(
            self):
        url = f'{self.metadata_attempts_link}/UsersCourseAssignmentAttemptMetadataItem/%40%40TimeRemaining'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2021.0.0',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
            'Referer': '/app/course/site.admin.alpha-OID-0x27a5d6%3A5573657273%3AKS4zsTUN79t/lessons/NTI-NTICourseOutlineNode-9007678577205568157_4744547776816629863.0.0/items/NTI-NTIAssignmentRef-F896A60099C754C0D63F8D979BCD00B871343CAD9F5CD1166FC1DD6EB2F51D56_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000137_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084_Savepoint(self):
        url = '' + f'{self.course_instance_link}/AssignmentSavepoints/{self.user_id}/{self.assignment_target_ntiid}/Savepoint'
        url = self.savepoint_link if self.savepoint_link is not None else urllib.parse.quote(url)
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )


    @task()
    def task_000140_GET_app_resources_css_legacy_css(self):
        url = '' + '/app/resources/css/legacy.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000143_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000146_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000147_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '864',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0x2166c2:5573657273:Pc3MCYfnMkJ",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0x2166c2:5573657273:Pc3MCYfnMkJ",
                           "timestamp":1611292506.733,
                           "user":self.user_id,
                           "ResourceId":self.assignment_target_ntiid,
                           "Duration":0.001,
                           "ContentId":self.assignment_target_ntiid}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000148_GET_app_resources_css_nti_override_css(self):
        url = '' + '/app/resources/css/nti-override.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000149_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_40_40UserCoursePreferredAccess(self):
        url = '' + f'{self.course_instance_link}/%40%40UserCoursePreferredAccess'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000153_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000156_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084_Savepoint(self):
        url = '' + f'{self.course_instance_link}/AssignmentSavepoints/{self.user_id}/{self.assignment_target_ntiid}/Savepoint'
        url = self.savepoint_link if self.savepoint_link is not None else urllib.parse.quote(url)
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '31688',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission","tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084","parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":null,"tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-2B79751248879E53E45CD1106CA4CFB48E02A3F05E2411B91892FBB04D90D193_0085","questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-47FC490CC43012E86F18DE556E22EC36421CA9012E4C6D5C0A59F4DAC6857837_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-47FC490CC43012E86F18DE556E22EC36421CA9012E4C6D5C0A59F4DAC6857837_0082","parts":[1],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-67CBF684D1A0BA710E1A4092FBEFF062642F806B6DA570EFE157575B2174453A_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-67CBF684D1A0BA710E1A4092FBEFF062642F806B6DA570EFE157575B2174453A_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-31A14FA9E8D7F38770D4F6D993DB9E0AD3BAA92349A432ADE7C40F8638D1E065_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-31A14FA9E8D7F38770D4F6D993DB9E0AD3BAA92349A432ADE7C40F8638D1E065_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-33B6A75D4745331E203373F7EA7E33F1AB4AB32C5EB5E46C6A88C4ABEF190117_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-33B6A75D4745331E203373F7EA7E33F1AB4AB32C5EB5E46C6A88C4ABEF190117_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-1120A062752B75E04C3A7B81840669B5E25DB3DBC45CFF8D0CC69346DAC4450F_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-1120A062752B75E04C3A7B81840669B5E25DB3DBC45CFF8D0CC69346DAC4450F_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C320703995656DFC7BDD9CC258F76CD533B100BB33E9DB41A6E349C45E44BAF5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C320703995656DFC7BDD9CC258F76CD533B100BB33E9DB41A6E349C45E44BAF5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-CFF9FBFD2D18CC4EB7024C7530A3C6BAC60AB87D92B86EDE0D38B1E0D7BB8245_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-CFF9FBFD2D18CC4EB7024C7530A3C6BAC60AB87D92B86EDE0D38B1E0D7BB8245_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9E35437BCBF93EE64152A5EF20C5B685711E7466B66CBD6097BA834A4720F4C5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9E35437BCBF93EE64152A5EF20C5B685711E7466B66CBD6097BA834A4720F4C5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9EFAC9A5C0BE1E8679B29DA5DF4B09B30852429110E80028E09292714964173A_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9EFAC9A5C0BE1E8679B29DA5DF4B09B30852429110E80028E09292714964173A_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-AC1AF9CEEE8706D3960A4A0EB988BF794CEF5CE3DF8082D7DC84120AE42BE3B7_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-AC1AF9CEEE8706D3960A4A0EB988BF794CEF5CE3DF8082D7DC84120AE42BE3B7_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-12AD84813BC42741940F003CBFDD2F54F33BCADA037D8DBADE228DE369663744_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-12AD84813BC42741940F003CBFDD2F54F33BCADA037D8DBADE228DE369663744_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-32E06EF214C421E040A794EADB4439AC44F82A5EE5F35635E65E73B8AECDD76C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-32E06EF214C421E040A794EADB4439AC44F82A5EE5F35635E65E73B8AECDD76C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9E3087EBEEF070FDB2711BDF59FC839E5D79F62DB38B96673D75716B33731E05_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9E3087EBEEF070FDB2711BDF59FC839E5D79F62DB38B96673D75716B33731E05_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F9E742E57EB574223686FFA0CE05911729E0E9BD97A00BF026EAC77ADD8695EC_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F9E742E57EB574223686FFA0CE05911729E0E9BD97A00BF026EAC77ADD8695EC_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-76BE227FEC733FD2561AD6D1DF08B96A0A18D6BFC25E5516315B0169AF7399B7_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-76BE227FEC733FD2561AD6D1DF08B96A0A18D6BFC25E5516315B0169AF7399B7_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9F748A4903FD2DF0CF4021752A17170097F60D1A5D9ADC19B54E0D9A2841B6F6_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9F748A4903FD2DF0CF4021752A17170097F60D1A5D9ADC19B54E0D9A2841B6F6_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-AD5B0F076C17F520AA82D4E0DCADB6F063135BC523A014914FED29B8A76A4BA5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-AD5B0F076C17F520AA82D4E0DCADB6F063135BC523A014914FED29B8A76A4BA5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-7310F7DA66670169F67E46DFAD96EA103623E937EFF78C8BD840CBCD4A466CCC_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-7310F7DA66670169F67E46DFAD96EA103623E937EFF78C8BD840CBCD4A466CCC_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-7FCF395FA88EFBC747EBA58AD11D5E942408CE42690A5E8248096A4793FA757B_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-7FCF395FA88EFBC747EBA58AD11D5E942408CE42690A5E8248096A4793FA757B_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-665A61C2E51A75FADFCB162AA43E247D5F4E6F15797408DEEC84CF63778DFAC8_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-665A61C2E51A75FADFCB162AA43E247D5F4E6F15797408DEEC84CF63778DFAC8_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F76686EE54C46FEC7E87704BEF31CEF69E5324B74CD6B420967B96A24D0E165C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F76686EE54C46FEC7E87704BEF31CEF69E5324B74CD6B420967B96A24D0E165C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-04F21669DC02D7032C4DC4F43B2ED4654D3D5459E5672A7EAB79558F08B17345_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-04F21669DC02D7032C4DC4F43B2ED4654D3D5459E5672A7EAB79558F08B17345_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-2741F1CD01FE27C5AA147CAD9F9F8990C8FD70D8592151E1CCA06EA52D331017_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-2741F1CD01FE27C5AA147CAD9F9F8990C8FD70D8592151E1CCA06EA52D331017_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-8ADC8B702335ABDB995CB11D1A14D4E841EADDEB01EB0C535CD95F92B59610D0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-8ADC8B702335ABDB995CB11D1A14D4E841EADDEB01EB0C535CD95F92B59610D0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F3DA0069EB120EA864F3BB5A35616A8189773AB6FBFB07387BFE7C8ABF5E60F0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F3DA0069EB120EA864F3BB5A35616A8189773AB6FBFB07387BFE7C8ABF5E60F0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D90B5E03DE89450F6EC849ED0266BF874E1FFF6B77E0DFCC02F2848180499AAA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D90B5E03DE89450F6EC849ED0266BF874E1FFF6B77E0DFCC02F2848180499AAA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D33AB01878B73D44498AEE05583FAF8D6F4190D4A6395F8A33B969215E3D4694_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D33AB01878B73D44498AEE05583FAF8D6F4190D4A6395F8A33B969215E3D4694_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-97F3D33F5AA44AAF0506FA087E05AD183F5CDAAA42852A255835C6E1A532DF86_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-97F3D33F5AA44AAF0506FA087E05AD183F5CDAAA42852A255835C6E1A532DF86_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-0831C3D61987911D1E3C86FEAAB6927CE11D587F61269799B4ED7A7111F0E6CA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-0831C3D61987911D1E3C86FEAAB6927CE11D587F61269799B4ED7A7111F0E6CA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-5294B2845CE2C64D201A97D03A28ECCB78970DBFCABCCFEE2EAE97C671C54FD0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-5294B2845CE2C64D201A97D03A28ECCB78970DBFCABCCFEE2EAE97C671C54FD0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-63C042A573339D645FFDA7B0C46033AC5F39439FAD865A7AB0C8FD7813B8E875_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-63C042A573339D645FFDA7B0C46033AC5F39439FAD865A7AB0C8FD7813B8E875_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-6857C918927ED7DF04BCA2B0A4F4865C32A3B0E52B82427959E27B4A1471827D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-6857C918927ED7DF04BCA2B0A4F4865C32A3B0E52B82427959E27B4A1471827D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-944A14FA11B9299C1F758DEF5183A262C791B0845FAB55853D134971D3BCEF59_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-944A14FA11B9299C1F758DEF5183A262C791B0845FAB55853D134971D3BCEF59_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-77643CE6192DEDED1663136CC5779D1B93AE7FD17A0C4F53857A3E1884A87746_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-77643CE6192DEDED1663136CC5779D1B93AE7FD17A0C4F53857A3E1884A87746_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-6BE0FD73331D868E4FF384BD4E0A59446A6298D2A1740B2E3977CBAFBF52BEBE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-6BE0FD73331D868E4FF384BD4E0A59446A6298D2A1740B2E3977CBAFBF52BEBE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-8D772027A43FD3B9F547E25372919AD6FB54AF557DC5FAEB9E81C3D262371525_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-8D772027A43FD3B9F547E25372919AD6FB54AF557DC5FAEB9E81C3D262371525_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-17F19E4CB2CCD8AA42A05803F1298AD92AFF967A2CE3D333079388B102B50BED_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-17F19E4CB2CCD8AA42A05803F1298AD92AFF967A2CE3D333079388B102B50BED_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-5FF85093516E3B91F9F97E8FAC89DCEE044952ACDFBA51B49D48B9CCB98119C8_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-5FF85093516E3B91F9F97E8FAC89DCEE044952ACDFBA51B49D48B9CCB98119C8_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-8A306D09AC48A5A073A8DC0A293B9FE36A3519FD0904ACCDC1D79685F88D9F32_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-8A306D09AC48A5A073A8DC0A293B9FE36A3519FD0904ACCDC1D79685F88D9F32_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-3DD278A5890198CFFC63754A27E0C0AABDC3F4A2888227CC8FEEA57B1938472A_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-3DD278A5890198CFFC63754A27E0C0AABDC3F4A2888227CC8FEEA57B1938472A_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-1E5916E168A5CB12430C74F0B52FC17910192388172D701F66160E2C72C8FED0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-1E5916E168A5CB12430C74F0B52FC17910192388172D701F66160E2C72C8FED0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-91E1F1A98D9D6B07BD2134CEB45F055CA77431BC8A4460C7C84DB2805B894D5E_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-91E1F1A98D9D6B07BD2134CEB45F055CA77431BC8A4460C7C84DB2805B894D5E_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-4F31FCEBBD58A35918A07AF1390C58F410690C4D6595536F884BE1E6C9EC2B2F_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-4F31FCEBBD58A35918A07AF1390C58F410690C4D6595536F884BE1E6C9EC2B2F_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-38F91830F6BFB462A5AE50D0667432CA8007132544A8C28B33D8EC1D3E5D599D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-38F91830F6BFB462A5AE50D0667432CA8007132544A8C28B33D8EC1D3E5D599D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E440B724343B3B70747E1E72A0F9ECE1D2E13255C152FED34ECF2C36BD18CE52_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E440B724343B3B70747E1E72A0F9ECE1D2E13255C152FED34ECF2C36BD18CE52_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-0EE021DD1BB7DA228010A03E1B0C9501FD8AC4B81330056D8016DA44EFF84F22_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-0EE021DD1BB7DA228010A03E1B0C9501FD8AC4B81330056D8016DA44EFF84F22_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-66A1CD8929948A204F0AD3C4BDDBB4852DEDF2DCB19E9D37BB27BBC8A739AD47_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-66A1CD8929948A204F0AD3C4BDDBB4852DEDF2DCB19E9D37BB27BBC8A739AD47_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-EEC338D91E90130BF4FDC9917B76D6D10A87F7D380780714012EFA6065CF105D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-EEC338D91E90130BF4FDC9917B76D6D10A87F7D380780714012EFA6065CF105D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D67A23AA966886E9BEF73EE1CB42144238D979E385F5B142FE2E965E98ECF6D5_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D67A23AA966886E9BEF73EE1CB42144238D979E385F5B142FE2E965E98ECF6D5_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-33DBA7D582311F664DED7F46F082436BBAD040209328C36A527A145C48DD6B91_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-33DBA7D582311F664DED7F46F082436BBAD040209328C36A527A145C48DD6B91_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-65A3F2938ED947D8D0B896AE71557215F56AA7CC61B4B2A50530E3C578BA68BA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-65A3F2938ED947D8D0B896AE71557215F56AA7CC61B4B2A50530E3C578BA68BA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E3AC94FA9F98010FF4C6A4E165B96DE68F8BFADFA8ABF7287DB507897AD1E764_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E3AC94FA9F98010FF4C6A4E165B96DE68F8BFADFA8ABF7287DB507897AD1E764_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-A537C9D01BEC535DA6278FCE49042D47C349261C496BFF4290942A129583503E_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-A537C9D01BEC535DA6278FCE49042D47C349261C496BFF4290942A129583503E_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B7EC1ED9266AD904CB95FC53CBF130A0216033DA53BD16F0C27A847A06D61742_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B7EC1ED9266AD904CB95FC53CBF130A0216033DA53BD16F0C27A847A06D61742_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B92D7506E2DDFA89652E168CDD5C48238B9672AD97FAE6C620FA5D1385F43A7D_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B92D7506E2DDFA89652E168CDD5C48238B9672AD97FAE6C620FA5D1385F43A7D_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-75F2A2552BD9946B20CC5C1FCCD2011B8C267323869CCAD06275A04E8999BE8F_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-75F2A2552BD9946B20CC5C1FCCD2011B8C267323869CCAD06275A04E8999BE8F_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E157999B6F47B57A5460959F855CDDBB43AC06BF696B4C7507AA55C1981D0542_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E157999B6F47B57A5460959F855CDDBB43AC06BF696B4C7507AA55C1981D0542_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-15CA749CF73071F2DFA3267DF184773B6EA85B7DF597C2EAC05C7F2AE12EEAB8_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-15CA749CF73071F2DFA3267DF184773B6EA85B7DF597C2EAC05C7F2AE12EEAB8_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-2F505A04BDCCA0E40F679B8AA636A5AF05C737DE63F29D6F0A3AECD105587A73_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-2F505A04BDCCA0E40F679B8AA636A5AF05C737DE63F29D6F0A3AECD105587A73_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E768FCCB0CE5D0A4713F0CF5BEE6F9A6E7FBD6A4FFBF9E499AAEE593D50BAAF6_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E768FCCB0CE5D0A4713F0CF5BEE6F9A6E7FBD6A4FFBF9E499AAEE593D50BAAF6_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FD1AC5BECFE4A738D49A5648D44BFDD7159E045B52506BC5980F47CA1C6CFCFE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FD1AC5BECFE4A738D49A5648D44BFDD7159E045B52506BC5980F47CA1C6CFCFE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F27BD48F0D6E1AEB4FE4C4E1F13227D3FA78E351A0879790E6263FA0F12F89A9_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F27BD48F0D6E1AEB4FE4C4E1F13227D3FA78E351A0879790E6263FA0F12F89A9_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D7C7312A31A064BD233B2A06DB364CAA58A4BEB70B3E48DE2BF76B2305F48D3A_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D7C7312A31A064BD233B2A06DB364CAA58A4BEB70B3E48DE2BF76B2305F48D3A_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-45083928B871F20C50AA1AAB4A36E302615BD31D794F415BA05C1071B51327F5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-45083928B871F20C50AA1AAB4A36E302615BD31D794F415BA05C1071B51327F5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-65EA27679D71424D96ECBD8618B4D0E1C387CE562C073EE47D38333BE684D989_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-65EA27679D71424D96ECBD8618B4D0E1C387CE562C073EE47D38333BE684D989_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-72FA2F0859B63E65A4E02BB07F702FC6DB6E6C6BEF76FA73F4F5DFE5C71EC6AC_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-72FA2F0859B63E65A4E02BB07F702FC6DB6E6C6BEF76FA73F4F5DFE5C71EC6AC_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-6C10F74177925ABE41DE8B65C6B452BE163E34148DE7D5C98FBC2DB4014BC0AE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-6C10F74177925ABE41DE8B65C6B452BE163E34148DE7D5C98FBC2DB4014BC0AE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-3E4FA50EB54C82EDAE78B5F54F7FD7AB6395046B6479BF61F44C1CBE1FD5E96C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-3E4FA50EB54C82EDAE78B5F54F7FD7AB6395046B6479BF61F44C1CBE1FD5E96C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B6DC6755792DE52FAC03D416C447315B31DEDEEEB0FED3ADC862600644545BBA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B6DC6755792DE52FAC03D416C447315B31DEDEEEB0FED3ADC862600644545BBA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-7FC3E2F42FFB9186451AFDF2E28633D0F9D57D794BC4F79A4D6487982BF10906_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-7FC3E2F42FFB9186451AFDF2E28633D0F9D57D794BC4F79A4D6487982BF10906_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E946E07A146CA2F70039FA85BD3EF2B4BEEAD5C1113F68AA7C75F043A675DEED_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E946E07A146CA2F70039FA85BD3EF2B4BEEAD5C1113F68AA7C75F043A675DEED_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FE223846AA74DAA1DCEA101CA065AC19B2A7A3B16CBEE1CFA297561D22AEB9CA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FE223846AA74DAA1DCEA101CA065AC19B2A7A3B16CBEE1CFA297561D22AEB9CA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-766188B47433A13777B6780E229D3E155060B9F3C243F3934AEBBA2B49D70C27_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-766188B47433A13777B6780E229D3E155060B9F3C243F3934AEBBA2B49D70C27_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-892C96EAA5908639C40408144D8C755E0975EAC8041A44F54A09663AA7367613_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-892C96EAA5908639C40408144D8C755E0975EAC8041A44F54A09663AA7367613_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B3F88ACECEBE3C4E8304D3E2DB5D660EFA46F36589167FE8D3886FD91FE52CAE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B3F88ACECEBE3C4E8304D3E2DB5D660EFA46F36589167FE8D3886FD91FE52CAE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-EA45F824ED1E6D8AE61447DE422E25CEC4A0ACCB200D096F1FAB43709AEEE0AB_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-EA45F824ED1E6D8AE61447DE422E25CEC4A0ACCB200D096F1FAB43709AEEE0AB_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-83629000C486D76F3ABD1B3A1C35CC90B79DD46EB79F01FFB922AA49337958E5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-83629000C486D76F3ABD1B3A1C35CC90B79DD46EB79F01FFB922AA49337958E5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B5FE93543251EF68F296A714B8592498175D7B5F1A5A5881C6C37341220E5559_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B5FE93543251EF68F296A714B8592498175D7B5F1A5A5881C6C37341220E5559_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-A780AAC65825FA29B87AA7C6AC4ED3DE0908F366220388676BA112A3309B211C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-A780AAC65825FA29B87AA7C6AC4ED3DE0908F366220388676BA112A3309B211C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C7615094945FE00FCE99941DDADC40EB24E8F08D317B4A4B1B1F3F9D7A7F428D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C7615094945FE00FCE99941DDADC40EB24E8F08D317B4A4B1B1F3F9D7A7F428D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":""}],"CreatorRecordedEffortDuration":5,"ContainerId":""}],"CreatorRecordedEffortDuration":5,"version":"2021-01-22T05:12:12"}'''

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
    def task_000157_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = '' + f'{self.course_instance_link}/Assessments/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '40193',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission","tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084","parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":null,"tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-2B79751248879E53E45CD1106CA4CFB48E02A3F05E2411B91892FBB04D90D193_0085","questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-47FC490CC43012E86F18DE556E22EC36421CA9012E4C6D5C0A59F4DAC6857837_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-47FC490CC43012E86F18DE556E22EC36421CA9012E4C6D5C0A59F4DAC6857837_0082","parts":[1],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-67CBF684D1A0BA710E1A4092FBEFF062642F806B6DA570EFE157575B2174453A_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-67CBF684D1A0BA710E1A4092FBEFF062642F806B6DA570EFE157575B2174453A_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-31A14FA9E8D7F38770D4F6D993DB9E0AD3BAA92349A432ADE7C40F8638D1E065_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-31A14FA9E8D7F38770D4F6D993DB9E0AD3BAA92349A432ADE7C40F8638D1E065_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-33B6A75D4745331E203373F7EA7E33F1AB4AB32C5EB5E46C6A88C4ABEF190117_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-33B6A75D4745331E203373F7EA7E33F1AB4AB32C5EB5E46C6A88C4ABEF190117_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-1120A062752B75E04C3A7B81840669B5E25DB3DBC45CFF8D0CC69346DAC4450F_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-1120A062752B75E04C3A7B81840669B5E25DB3DBC45CFF8D0CC69346DAC4450F_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C320703995656DFC7BDD9CC258F76CD533B100BB33E9DB41A6E349C45E44BAF5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C320703995656DFC7BDD9CC258F76CD533B100BB33E9DB41A6E349C45E44BAF5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-CFF9FBFD2D18CC4EB7024C7530A3C6BAC60AB87D92B86EDE0D38B1E0D7BB8245_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-CFF9FBFD2D18CC4EB7024C7530A3C6BAC60AB87D92B86EDE0D38B1E0D7BB8245_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9E35437BCBF93EE64152A5EF20C5B685711E7466B66CBD6097BA834A4720F4C5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9E35437BCBF93EE64152A5EF20C5B685711E7466B66CBD6097BA834A4720F4C5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9EFAC9A5C0BE1E8679B29DA5DF4B09B30852429110E80028E09292714964173A_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9EFAC9A5C0BE1E8679B29DA5DF4B09B30852429110E80028E09292714964173A_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-AC1AF9CEEE8706D3960A4A0EB988BF794CEF5CE3DF8082D7DC84120AE42BE3B7_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-AC1AF9CEEE8706D3960A4A0EB988BF794CEF5CE3DF8082D7DC84120AE42BE3B7_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-12AD84813BC42741940F003CBFDD2F54F33BCADA037D8DBADE228DE369663744_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-12AD84813BC42741940F003CBFDD2F54F33BCADA037D8DBADE228DE369663744_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-32E06EF214C421E040A794EADB4439AC44F82A5EE5F35635E65E73B8AECDD76C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-32E06EF214C421E040A794EADB4439AC44F82A5EE5F35635E65E73B8AECDD76C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9E3087EBEEF070FDB2711BDF59FC839E5D79F62DB38B96673D75716B33731E05_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9E3087EBEEF070FDB2711BDF59FC839E5D79F62DB38B96673D75716B33731E05_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F9E742E57EB574223686FFA0CE05911729E0E9BD97A00BF026EAC77ADD8695EC_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F9E742E57EB574223686FFA0CE05911729E0E9BD97A00BF026EAC77ADD8695EC_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-76BE227FEC733FD2561AD6D1DF08B96A0A18D6BFC25E5516315B0169AF7399B7_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-76BE227FEC733FD2561AD6D1DF08B96A0A18D6BFC25E5516315B0169AF7399B7_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-9F748A4903FD2DF0CF4021752A17170097F60D1A5D9ADC19B54E0D9A2841B6F6_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-9F748A4903FD2DF0CF4021752A17170097F60D1A5D9ADC19B54E0D9A2841B6F6_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-AD5B0F076C17F520AA82D4E0DCADB6F063135BC523A014914FED29B8A76A4BA5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-AD5B0F076C17F520AA82D4E0DCADB6F063135BC523A014914FED29B8A76A4BA5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-7310F7DA66670169F67E46DFAD96EA103623E937EFF78C8BD840CBCD4A466CCC_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-7310F7DA66670169F67E46DFAD96EA103623E937EFF78C8BD840CBCD4A466CCC_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-7FCF395FA88EFBC747EBA58AD11D5E942408CE42690A5E8248096A4793FA757B_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-7FCF395FA88EFBC747EBA58AD11D5E942408CE42690A5E8248096A4793FA757B_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-665A61C2E51A75FADFCB162AA43E247D5F4E6F15797408DEEC84CF63778DFAC8_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-665A61C2E51A75FADFCB162AA43E247D5F4E6F15797408DEEC84CF63778DFAC8_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F76686EE54C46FEC7E87704BEF31CEF69E5324B74CD6B420967B96A24D0E165C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F76686EE54C46FEC7E87704BEF31CEF69E5324B74CD6B420967B96A24D0E165C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-04F21669DC02D7032C4DC4F43B2ED4654D3D5459E5672A7EAB79558F08B17345_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-04F21669DC02D7032C4DC4F43B2ED4654D3D5459E5672A7EAB79558F08B17345_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-2741F1CD01FE27C5AA147CAD9F9F8990C8FD70D8592151E1CCA06EA52D331017_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-2741F1CD01FE27C5AA147CAD9F9F8990C8FD70D8592151E1CCA06EA52D331017_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-8ADC8B702335ABDB995CB11D1A14D4E841EADDEB01EB0C535CD95F92B59610D0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-8ADC8B702335ABDB995CB11D1A14D4E841EADDEB01EB0C535CD95F92B59610D0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F3DA0069EB120EA864F3BB5A35616A8189773AB6FBFB07387BFE7C8ABF5E60F0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F3DA0069EB120EA864F3BB5A35616A8189773AB6FBFB07387BFE7C8ABF5E60F0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D90B5E03DE89450F6EC849ED0266BF874E1FFF6B77E0DFCC02F2848180499AAA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D90B5E03DE89450F6EC849ED0266BF874E1FFF6B77E0DFCC02F2848180499AAA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D33AB01878B73D44498AEE05583FAF8D6F4190D4A6395F8A33B969215E3D4694_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D33AB01878B73D44498AEE05583FAF8D6F4190D4A6395F8A33B969215E3D4694_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-97F3D33F5AA44AAF0506FA087E05AD183F5CDAAA42852A255835C6E1A532DF86_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-97F3D33F5AA44AAF0506FA087E05AD183F5CDAAA42852A255835C6E1A532DF86_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-0831C3D61987911D1E3C86FEAAB6927CE11D587F61269799B4ED7A7111F0E6CA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-0831C3D61987911D1E3C86FEAAB6927CE11D587F61269799B4ED7A7111F0E6CA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-5294B2845CE2C64D201A97D03A28ECCB78970DBFCABCCFEE2EAE97C671C54FD0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-5294B2845CE2C64D201A97D03A28ECCB78970DBFCABCCFEE2EAE97C671C54FD0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-63C042A573339D645FFDA7B0C46033AC5F39439FAD865A7AB0C8FD7813B8E875_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-63C042A573339D645FFDA7B0C46033AC5F39439FAD865A7AB0C8FD7813B8E875_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-6857C918927ED7DF04BCA2B0A4F4865C32A3B0E52B82427959E27B4A1471827D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-6857C918927ED7DF04BCA2B0A4F4865C32A3B0E52B82427959E27B4A1471827D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-944A14FA11B9299C1F758DEF5183A262C791B0845FAB55853D134971D3BCEF59_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-944A14FA11B9299C1F758DEF5183A262C791B0845FAB55853D134971D3BCEF59_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-77643CE6192DEDED1663136CC5779D1B93AE7FD17A0C4F53857A3E1884A87746_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-77643CE6192DEDED1663136CC5779D1B93AE7FD17A0C4F53857A3E1884A87746_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-6BE0FD73331D868E4FF384BD4E0A59446A6298D2A1740B2E3977CBAFBF52BEBE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-6BE0FD73331D868E4FF384BD4E0A59446A6298D2A1740B2E3977CBAFBF52BEBE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-8D772027A43FD3B9F547E25372919AD6FB54AF557DC5FAEB9E81C3D262371525_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-8D772027A43FD3B9F547E25372919AD6FB54AF557DC5FAEB9E81C3D262371525_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-17F19E4CB2CCD8AA42A05803F1298AD92AFF967A2CE3D333079388B102B50BED_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-17F19E4CB2CCD8AA42A05803F1298AD92AFF967A2CE3D333079388B102B50BED_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-5FF85093516E3B91F9F97E8FAC89DCEE044952ACDFBA51B49D48B9CCB98119C8_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-5FF85093516E3B91F9F97E8FAC89DCEE044952ACDFBA51B49D48B9CCB98119C8_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-8A306D09AC48A5A073A8DC0A293B9FE36A3519FD0904ACCDC1D79685F88D9F32_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-8A306D09AC48A5A073A8DC0A293B9FE36A3519FD0904ACCDC1D79685F88D9F32_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-3DD278A5890198CFFC63754A27E0C0AABDC3F4A2888227CC8FEEA57B1938472A_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-3DD278A5890198CFFC63754A27E0C0AABDC3F4A2888227CC8FEEA57B1938472A_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-1E5916E168A5CB12430C74F0B52FC17910192388172D701F66160E2C72C8FED0_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-1E5916E168A5CB12430C74F0B52FC17910192388172D701F66160E2C72C8FED0_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-91E1F1A98D9D6B07BD2134CEB45F055CA77431BC8A4460C7C84DB2805B894D5E_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-91E1F1A98D9D6B07BD2134CEB45F055CA77431BC8A4460C7C84DB2805B894D5E_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-4F31FCEBBD58A35918A07AF1390C58F410690C4D6595536F884BE1E6C9EC2B2F_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-4F31FCEBBD58A35918A07AF1390C58F410690C4D6595536F884BE1E6C9EC2B2F_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-38F91830F6BFB462A5AE50D0667432CA8007132544A8C28B33D8EC1D3E5D599D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-38F91830F6BFB462A5AE50D0667432CA8007132544A8C28B33D8EC1D3E5D599D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E440B724343B3B70747E1E72A0F9ECE1D2E13255C152FED34ECF2C36BD18CE52_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E440B724343B3B70747E1E72A0F9ECE1D2E13255C152FED34ECF2C36BD18CE52_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-0EE021DD1BB7DA228010A03E1B0C9501FD8AC4B81330056D8016DA44EFF84F22_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-0EE021DD1BB7DA228010A03E1B0C9501FD8AC4B81330056D8016DA44EFF84F22_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-66A1CD8929948A204F0AD3C4BDDBB4852DEDF2DCB19E9D37BB27BBC8A739AD47_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-66A1CD8929948A204F0AD3C4BDDBB4852DEDF2DCB19E9D37BB27BBC8A739AD47_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-EEC338D91E90130BF4FDC9917B76D6D10A87F7D380780714012EFA6065CF105D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-EEC338D91E90130BF4FDC9917B76D6D10A87F7D380780714012EFA6065CF105D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D67A23AA966886E9BEF73EE1CB42144238D979E385F5B142FE2E965E98ECF6D5_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D67A23AA966886E9BEF73EE1CB42144238D979E385F5B142FE2E965E98ECF6D5_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-33DBA7D582311F664DED7F46F082436BBAD040209328C36A527A145C48DD6B91_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-33DBA7D582311F664DED7F46F082436BBAD040209328C36A527A145C48DD6B91_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-65A3F2938ED947D8D0B896AE71557215F56AA7CC61B4B2A50530E3C578BA68BA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-65A3F2938ED947D8D0B896AE71557215F56AA7CC61B4B2A50530E3C578BA68BA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E3AC94FA9F98010FF4C6A4E165B96DE68F8BFADFA8ABF7287DB507897AD1E764_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E3AC94FA9F98010FF4C6A4E165B96DE68F8BFADFA8ABF7287DB507897AD1E764_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-A537C9D01BEC535DA6278FCE49042D47C349261C496BFF4290942A129583503E_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-A537C9D01BEC535DA6278FCE49042D47C349261C496BFF4290942A129583503E_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B7EC1ED9266AD904CB95FC53CBF130A0216033DA53BD16F0C27A847A06D61742_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B7EC1ED9266AD904CB95FC53CBF130A0216033DA53BD16F0C27A847A06D61742_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B92D7506E2DDFA89652E168CDD5C48238B9672AD97FAE6C620FA5D1385F43A7D_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B92D7506E2DDFA89652E168CDD5C48238B9672AD97FAE6C620FA5D1385F43A7D_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-75F2A2552BD9946B20CC5C1FCCD2011B8C267323869CCAD06275A04E8999BE8F_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-75F2A2552BD9946B20CC5C1FCCD2011B8C267323869CCAD06275A04E8999BE8F_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E157999B6F47B57A5460959F855CDDBB43AC06BF696B4C7507AA55C1981D0542_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E157999B6F47B57A5460959F855CDDBB43AC06BF696B4C7507AA55C1981D0542_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-15CA749CF73071F2DFA3267DF184773B6EA85B7DF597C2EAC05C7F2AE12EEAB8_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-15CA749CF73071F2DFA3267DF184773B6EA85B7DF597C2EAC05C7F2AE12EEAB8_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-2F505A04BDCCA0E40F679B8AA636A5AF05C737DE63F29D6F0A3AECD105587A73_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-2F505A04BDCCA0E40F679B8AA636A5AF05C737DE63F29D6F0A3AECD105587A73_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E768FCCB0CE5D0A4713F0CF5BEE6F9A6E7FBD6A4FFBF9E499AAEE593D50BAAF6_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E768FCCB0CE5D0A4713F0CF5BEE6F9A6E7FBD6A4FFBF9E499AAEE593D50BAAF6_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FD1AC5BECFE4A738D49A5648D44BFDD7159E045B52506BC5980F47CA1C6CFCFE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FD1AC5BECFE4A738D49A5648D44BFDD7159E045B52506BC5980F47CA1C6CFCFE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-F27BD48F0D6E1AEB4FE4C4E1F13227D3FA78E351A0879790E6263FA0F12F89A9_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-F27BD48F0D6E1AEB4FE4C4E1F13227D3FA78E351A0879790E6263FA0F12F89A9_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-D7C7312A31A064BD233B2A06DB364CAA58A4BEB70B3E48DE2BF76B2305F48D3A_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-D7C7312A31A064BD233B2A06DB364CAA58A4BEB70B3E48DE2BF76B2305F48D3A_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-45083928B871F20C50AA1AAB4A36E302615BD31D794F415BA05C1071B51327F5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-45083928B871F20C50AA1AAB4A36E302615BD31D794F415BA05C1071B51327F5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-65EA27679D71424D96ECBD8618B4D0E1C387CE562C073EE47D38333BE684D989_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-65EA27679D71424D96ECBD8618B4D0E1C387CE562C073EE47D38333BE684D989_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-72FA2F0859B63E65A4E02BB07F702FC6DB6E6C6BEF76FA73F4F5DFE5C71EC6AC_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-72FA2F0859B63E65A4E02BB07F702FC6DB6E6C6BEF76FA73F4F5DFE5C71EC6AC_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-6C10F74177925ABE41DE8B65C6B452BE163E34148DE7D5C98FBC2DB4014BC0AE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-6C10F74177925ABE41DE8B65C6B452BE163E34148DE7D5C98FBC2DB4014BC0AE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-3E4FA50EB54C82EDAE78B5F54F7FD7AB6395046B6479BF61F44C1CBE1FD5E96C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-3E4FA50EB54C82EDAE78B5F54F7FD7AB6395046B6479BF61F44C1CBE1FD5E96C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B6DC6755792DE52FAC03D416C447315B31DEDEEEB0FED3ADC862600644545BBA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B6DC6755792DE52FAC03D416C447315B31DEDEEEB0FED3ADC862600644545BBA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-7FC3E2F42FFB9186451AFDF2E28633D0F9D57D794BC4F79A4D6487982BF10906_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-7FC3E2F42FFB9186451AFDF2E28633D0F9D57D794BC4F79A4D6487982BF10906_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-E946E07A146CA2F70039FA85BD3EF2B4BEEAD5C1113F68AA7C75F043A675DEED_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-E946E07A146CA2F70039FA85BD3EF2B4BEEAD5C1113F68AA7C75F043A675DEED_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FE223846AA74DAA1DCEA101CA065AC19B2A7A3B16CBEE1CFA297561D22AEB9CA_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FE223846AA74DAA1DCEA101CA065AC19B2A7A3B16CBEE1CFA297561D22AEB9CA_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-766188B47433A13777B6780E229D3E155060B9F3C243F3934AEBBA2B49D70C27_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-766188B47433A13777B6780E229D3E155060B9F3C243F3934AEBBA2B49D70C27_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-892C96EAA5908639C40408144D8C755E0975EAC8041A44F54A09663AA7367613_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-892C96EAA5908639C40408144D8C755E0975EAC8041A44F54A09663AA7367613_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B3F88ACECEBE3C4E8304D3E2DB5D660EFA46F36589167FE8D3886FD91FE52CAE_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B3F88ACECEBE3C4E8304D3E2DB5D660EFA46F36589167FE8D3886FD91FE52CAE_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-EA45F824ED1E6D8AE61447DE422E25CEC4A0ACCB200D096F1FAB43709AEEE0AB_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-EA45F824ED1E6D8AE61447DE422E25CEC4A0ACCB200D096F1FAB43709AEEE0AB_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-83629000C486D76F3ABD1B3A1C35CC90B79DD46EB79F01FFB922AA49337958E5_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-83629000C486D76F3ABD1B3A1C35CC90B79DD46EB79F01FFB922AA49337958E5_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-B5FE93543251EF68F296A714B8592498175D7B5F1A5A5881C6C37341220E5559_0081","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-B5FE93543251EF68F296A714B8592498175D7B5F1A5A5881C6C37341220E5559_0081","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-A780AAC65825FA29B87AA7C6AC4ED3DE0908F366220388676BA112A3309B211C_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-A780AAC65825FA29B87AA7C6AC4ED3DE0908F366220388676BA112A3309B211C_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"},{"MimeType":"application/vnd.nextthought.assessment.questionsubmission","NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C7615094945FE00FCE99941DDADC40EB24E8F08D317B4A4B1B1F3F9D7A7F428D_0082","tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C7615094945FE00FCE99941DDADC40EB24E8F08D317B4A4B1B1F3F9D7A7F428D_0082","parts":[null],"CreatorRecordedEffortDuration":null,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"}],"CreatorRecordedEffortDuration":8,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084"}],"CreatorRecordedEffortDuration":8,"version":"2021-01-22T05:12:12"}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=self.final_answer,
        )

    @task()
    def task_000158_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = f'{self.course_instance_link}/Assessments/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000159_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000160_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'{self.course_instance_link}/AssignmentHistories/{self.user_id}/{self.assignment_target_ntiid}/UsersCourseAssignmentHistoryItem'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000161_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084_UsersCourseAssignmentHistoryItem(self):
        url = f'{self.course_instance_link}/AssignmentHistories/{self.user_id}/{self.assignment_target_ntiid}/UsersCourseAssignmentHistoryItem'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000162_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = f'/dataserver2/Objects/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000163_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course(self):
        url = self.course_instance_link
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000164_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000165_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_CourseCatalogEntry(self):
        url = f'{self.course_instance_link}/CourseCatalogEntry'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000167_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = f'{self.course_instance_link}/AssignmentHistories/{self.user_id}/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000169_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'{self.course_instance_link}/AssignmentAttemptMetadata/{self.user_id}/{self.assignment_target_ntiid}/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000170_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_4A6B95A017CC122F411DEF2ED648F575A82431DA021DE5F652EFE62ED8DB92ED_0084(self):
        url = '' + f'{self.course_instance_link}/{self.assignment_target_ntiid}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000171_GET_app_resources_images_20fb7a0d2fe9625be2cbe04443284d1b_svg(self):
        url = '' + '/app/resources/images/20fb7a0d2fe9625be2cbe04443284d1b.svg'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/shared~index-aa90340f6e81eb0af7eb.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000172_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/items/NTI-NTIAssignmentRef-5EA88011AC6C086CEBC92D0B71CB808D5C0F7742E7F22BE595A62977D69D46FF_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000173_GET_vendor_ext_4_2_resources_ext_theme_classic_images_form_exclamation_gif(self):
        url = '' + '/vendor/ext-4.2/resources/ext-theme-classic/images/form/exclamation.gif'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/vendor/ext-4.2/resources/ext-theme-classic/ext-theme-classic-all.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000174_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000175_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000176_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Completion_CompletedItems_users_stress_tester1(self):
        url = f'{self.course_instance_link}/Completion/CompletedItems/users/{self.user_id}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000178_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
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
        )

    @task()
    def task_000179_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_contents(self):
        url = f'{self.course_instance_link}/Outline/contents'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
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
        )

    @task()
    def task_000180_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Completion_Progress_users_stress_tester1(self):
        url = f'{self.course_instance_link}/Completion/Progress/users/{self.user_id}'
        url = urllib.parse.quote(url)

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000181_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_0_40_40overview_content(self):
        # url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/{self.user_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/%40%40overview-content'
        url = self.overview_content_link
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
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
            name=url.replace(self.user_id, 'user')
        )

    @task()
    def task_000182_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_Long_Assign_Course_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8201875887945803727_4744544919703575729_0_0_40_40overview_summary(self):
        # url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/{self.course_identifier}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/%40%40overview-summary'
        url = self.overview_summary_link

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-app',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.12.6',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
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
        )

    @task()
    def task_000183_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20201210171430',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000184_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000185_GET_dataserver2_logon_logout(self):
        url = '' + '/dataserver2/logon.logout'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
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
        )

    @task()
    def task_000186_GET_login(self):
        url = '' + '/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'Referer': '' + '/app/course/admin.user-OID-0x2166c2%3A5573657273%3APc3MCYfnMkJ/lessons/NTI-NTICourseOutlineNode-8201875887945803727_4744544919703575729.0.0/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000187_GET_site_assets_login_site_css(self):
        url = '' + '/site-assets/login/site.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000188_GET_login_js_index_dda78eb3_js(self):
        url = '' + '/login/js/index-dda78eb3.js'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000189_GET_login_resources_shared_index_02ce0f2495818179ee55_css(self):
        url = '' + '/login/resources/shared~index-02ce0f2495818179ee55.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000190_GET_login_resources_vendor_index_5628ade7a41ba4376653_css(self):
        url = '' + '/login/resources/vendor~index-5628ade7a41ba4376653.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000191_GET_login_js_vendor_index_dda78eb3_js(self):
        url = '' + '/login/js/vendor~index-dda78eb3.js'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000192_GET_login_resources_index_dfd10284e4c6dafb5149_css(self):
        url = '' + '/login/resources/index-dfd10284e4c6dafb5149.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'text/css,*/*;q=0.1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'style',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000193_GET_login_js_shared_index_dda78eb3_js(self):
        url = '' + '/login/js/shared~index-dda78eb3.js'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000198_GET_site_assets_shared_strings_en_json(self):
        url = '' + '/site-assets/shared/strings.en.json'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000199_GET_login_resources_images_174187b7474fdbc7f04568bb767ae2bb_png(self):
        url = '' + '/login/resources/images/174187b7474fdbc7f04568bb767ae2bb.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000200_GET_login_resources_images_d40e8c56563e9a73e287cc9a93cb5da1_png(self):
        url = '' + '/login/resources/images/d40e8c56563e9a73e287cc9a93cb5da1.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000201_GET_login_resources_images_14c8cb6ee9d598f2510836b67c279f07_png(self):
        url = '' + '/login/resources/images/14c8cb6ee9d598f2510836b67c279f07.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000202_GET_login_resources_images_0bcdabaa0b82ea3349f95d9a90a66551_png(self):
        url = '' + '/login/resources/images/0bcdabaa0b82ea3349f95d9a90a66551.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000203_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'X-NTI-Client-TZOffset': '-360',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-App': '@nti/web-login',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.9.0',
            'sec-ch-ua-mobile': '?0',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000205_GET_login_js_shared_index_dda78eb3_js_map(self):
        url = '' + '/login/js/shared~index-dda78eb3.js.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000208_GET_login_js_vendor_index_dda78eb3_js_map(self):
        url = '' + '/login/js/vendor~index-dda78eb3.js.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000209_GET_login_resources_index_dfd10284e4c6dafb5149_css_map(self):
        url = '' + '/login/resources/index-dfd10284e4c6dafb5149.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000210_GET_login_resources_shared_index_02ce0f2495818179ee55_css_map(self):
        url = '' + '/login/resources/shared~index-02ce0f2495818179ee55.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000211_GET_login_js_index_dda78eb3_js_map(self):
        url = '' + '/login/js/index-dda78eb3.js.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000212_GET_login_resources_vendor_index_5628ade7a41ba4376653_css_map(self):
        url = '' + '/login/resources/vendor~index-5628ade7a41ba4376653.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

        time.sleep(3600)

##


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
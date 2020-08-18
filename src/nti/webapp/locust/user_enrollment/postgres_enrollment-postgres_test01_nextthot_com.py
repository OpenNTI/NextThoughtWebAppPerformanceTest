# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import time

USER_CREDENTIALS = list(range(1, 1000))
COURSE_NTIIDS = ["tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914049040_4744481198483187534",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895426_4744481198244697563",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895339_4744481197987404016",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914049011_4744481197536151624",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-381762027272797856_4744477175327467881",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895500_4744481198805620892",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635894588_4744481197214508490",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635894564_4744481197088118676",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635895588_4744481199178767181",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-7337604134509948579_4744475820139681474",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914048981_4744481196940283859",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914048953_4744481196655629595"
                 ]

class UserEnrollment(SequentialTaskSet):
    user_id = 0
    ntiid = "tag:nextthought.com,2011-10:NTI-CourseInfo-381762027272797856_4744477175327467881"
    site = "postgres01.nextthought.com"
    course_id = 'QAAUTO-1595107828927'

    def on_start(self):
        self.user_id = USER_CREDENTIALS.pop()
        print(f'starting {self.user_id}')


    @task()
    def task_000000_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.6.2',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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

    ### Additional tasks can go here ###
    @task()
    def task_000001_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.6.2',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000002_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '152',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryB4kEACjJkjUpCJKS',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.6.2',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundaryB4kEACjJkjUpCJKS\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester\r\n------WebKitFormBoundaryB4kEACjJkjUpCJKS--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000003_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarygGVjPlnkPCKrZ0oB',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.6.2',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'------WebKitFormBoundarygGVjPlnkPCKrZ0oB\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundarygGVjPlnkPCKrZ0oB--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000029_GET_dataserver2_logon_nti_password(self):
        url = '/dataserver2/logon.nti.password'
        sval = f"stress.tester{self.user_id}:temp001"
        password = base64.b64encode(sval.encode('utf-8')).decode('utf-8')

        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'Authorization': f"Basic {password}",
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'X-NTI-Client-Version': '2020.6.2',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'username': f'stress.tester{self.user_id}',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/logon.nti.password'
        )

    @task()
    def task_000038_GET_loginsuccess(self):
        url = '' + '/loginsuccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
    def task_000039_GET_app(self):
        url = '' + '/app'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
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
    def task_000040_GET_app_resources_strings_strings_js(self):
        url = '' + '/app/resources/strings/strings.js'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
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
    def task_000043_GET_app_js_version(self):
        url = '' + '/app/js/version'
        
        headers = {
            'Connection': 'keep-alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000044_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000045_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'username=stress.tester{self.user_id}'
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000046_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000048_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryowBGabOWu3d9SU7Z',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = f'------WebKitFormBoundaryowBGabOWu3d9SU7Z\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryowBGabOWu3d9SU7Z--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000050_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000051_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000052_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        )


    @task()
    def task_000054_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000056_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        )


    @task()
    def task_000058_GET_site_assets_shared_strings_en_json(self):
        url = '' + '/site-assets/shared/strings.en.json'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000059_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
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
            name='/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        )

    @task()
    def task_000060_GET_dataserver2_users_stress_tester1_Groups(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Groups'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Groups'
        )

    @task()
    def task_000061_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
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
    def task_000062_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        )

    @task()
    def task_000063_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1595912399.937',
            'notBefore': '1595893791.937',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000064_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000065_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        )

    @task()
    def task_000066_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1595912399.964',
            'notBefore': '1595893791.964',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000067_GET_dataserver2_users_stress_tester1_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        )

    @task()
    def task_000068_GET_dataserver2_users_stress_tester1_Communities_Communities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
        )

    @task()
    def task_000069_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        )

    @task()
    def task_000070_GET_dataserver2_users_stress_tester1_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        )

    @task()
    def task_000071_GET_dataserver2_users_stress_tester1_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        )

    @task()
    def task_000072_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        )

    @task()
    def task_000073_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'bucketSize': '4',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag'
        )

    @task()
    def task_000075_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40Featured(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40Featured'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40Featured'
        )

    @task()
    def task_000076_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_qaauto_1595107828927(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/qaauto-1595107828927'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '32',
            'batchStart': '0',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/qaauto-1595107828927'
        )

    @task()
    def task_000078_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseCatalogEntry(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        )

    @task()
    def task_000079_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_qaauto_1595107828927(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/qaauto-1595107828927'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '32',
            'batchStart': '0',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/qaauto-1595107828927'
        )

    @task()
    def task_000081_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        )

    @task()
    def task_000082_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asite_admin_alpha_OID_0x059616_3A5573657273_3AyV5mWSA22FK(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asite.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000083_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '430',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiid,
                           "timestamp":1595893802.196,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiid,
                           "Duration":0}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000084_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        )

    @task()
    def task_000085_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        )

    @task()
    def task_000086_POST_dataserver2_users_stress_tester1_Courses_EnrolledCourses(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '93',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"NTIID":self.ntiid}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        )

    @task()
    def task_000087_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Archived(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Archived'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Archived'
        )

    @task()
    def task_000088_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1595912399.563',
            'notBefore': '1595893804.563',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000089_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Current(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Current'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Current'
        )

    @task()
    def task_000090_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Upcoming(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Upcoming'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Upcoming'
        )

    @task()
    def task_000091_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseCatalogEntry(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        )

    @task()
    def task_000092_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1595912399.924',
            'notBefore': '1595893804.924',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000093_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseCatalogEntry(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        )

    @task()
    def task_000094_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/qaauto-1595107828927/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTUxMDc4Mjg5MjcvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        )

    @task()
    def task_000095_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asite_admin_alpha_OID_0x059616_3A5573657273_3AyV5mWSA22FK(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asite.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
    def task_000097_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000098_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_40_40AssignmentSummaryByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40AssignmentSummaryByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000099_HEAD_app_resources_images_default_course_vendoroverrideicon_png(self):
        url = '' + '/app/resources/images/default-course/vendoroverrideicon.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '0',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000100_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000101_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000102_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
    def task_000103_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000104_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
    def task_000105_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_381762027272797856_4744477175327467881_AssignmentHistories_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-381762027272797856_4744477175327467881/AssignmentHistories/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-381762027272797856_4744477175327467881/AssignmentHistories/stress.tester{self.user_id}'
        )

    @task()
    def task_000106_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_CourseTabPreferences(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseTabPreferences'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseTabPreferences'
        )

    @task()
    def task_000107_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        )

    @task()
    def task_000108_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        )

    @task()
    def task_000109_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_site_admin_alpha_4744477176277576681_0_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_site_admin_alpha_4744477176277576681_0/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_site_admin_alpha_4744477176277576681_0/%40%40overview-summary'
        )

    @task()
    def task_000110_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_site_admin_alpha_4744477176277576681_0_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_site_admin_alpha_4744477176277576681_0/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-381762027272797856_4744477175327467881_site_admin_alpha_4744477176251820496_0_site_admin_alpha_4744477176277576681_0/%40%40overview-content'
        )

    @task()
    def task_000111_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744477177929797563_2067396560(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744477177929797563_2067396560'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744477177929797563_2067396560'
        )

    @task()
    def task_000112_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Completion_CompletedItems_users_stress_tester1(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Completion/CompletedItems/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000113_GET_app_api_videos_youtube(self):
        url = '' + '/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'id': 'ryx1CKskau8',
            'part': 'contentDetails,snippet,statistics',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000114_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744477182576546856_2316555167(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744477182576546856_2316555167'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000115_GET_app_api_videos_youtube(self):
        url = '' + '/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'id': 'dt5g5_1cKVk',
            'part': 'contentDetails,snippet,statistics',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000120_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        )

    @task()
    def task_000123_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '434',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiid,"timestamp":1595893802.196,
                           "user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiid,"Duration":5.991}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000124_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
    def task_000125_GET_dataserver2_logon_logout(self):
        url = '' + '/dataserver2/logon.logout'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
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
    def task_000126_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1595107828927_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000127_GET_login(self):
        url = '' + '/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x059616%3A5573657273%3AyV5mWSA22FK/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000129_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.6.2',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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

        time.sleep(36000)



class WebsiteUser(HttpUser):
    tasks = [UserEnrollment]
    wait_time = between(1, 5)
# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64

USER_CREDENTIALS = list(range(1, 1000))

class UserEnrollment(SequentialTaskSet):
    user_id = 0
    ntiid = "tag:nextthought.com,2011-10:NTI-CourseInfo-8814601425988072132_4744471694987486254"
    site = "alpha.nextthought.com"
    course_id = "QAAUTO-1593801202849"


    def on_start(self):
        self.user_id = USER_CREDENTIALS.pop()
        print(f'starting {self.user_id}')

    @task()
    def task_000000_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '143',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary1LV10fRg8RjFhLAq',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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

        data = '''------WebKitFormBoundary1LV10fRg8RjFhLAq\r\nContent-Disposition: form-data; name="username"\r\n\r\nstre\r\n------WebKitFormBoundary1LV10fRg8RjFhLAq--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000003_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
    def task_000004_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '144',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7gCahoPomXWPBRH8',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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

        data = '''------WebKitFormBoundary7gCahoPomXWPBRH8\r\nContent-Disposition: form-data; name="username"\r\n\r\nstres\r\n------WebKitFormBoundary7gCahoPomXWPBRH8--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000005_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
    def task_000006_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '145',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryDp2P4lr0KL2UBdNU',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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

        data = '''------WebKitFormBoundaryDp2P4lr0KL2UBdNU\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress\r\n------WebKitFormBoundaryDp2P4lr0KL2UBdNU--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000007_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
    def task_000008_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '146',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryOe58u72vyzpwRK0F',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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

        data = '''------WebKitFormBoundaryOe58u72vyzpwRK0F\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.\r\n------WebKitFormBoundaryOe58u72vyzpwRK0F--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000009_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '152',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXL7YGCXvIm7eYUJk',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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

        data = '''------WebKitFormBoundaryXL7YGCXvIm7eYUJk\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester\r\n------WebKitFormBoundaryXL7YGCXvIm7eYUJk--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000010_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
    def task_000011_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3IIQRxtfPGVflVwz',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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

        data = f'------WebKitFormBoundary3IIQRxtfPGVflVwz\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundary3IIQRxtfPGVflVwz--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000012_GET_dataserver2_logon_nti_password(self):
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
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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
    def task_000014_GET_loginsuccess(self):
        url = '/loginsuccess'
        
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
    def task_000015_GET_app(self):
        url = '/app'
        
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
    def task_000016_GET_app_resources_strings_strings_js(self):
        url = '/app/resources/strings/strings.js'
        
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
    def task_000019_GET_app_js_version(self):
        url = '/app/js/version'
        
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
    def task_000020_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000021_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000022_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000024_POST_dataserver2_logon_handshake(self):
        url = '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryIzJkS4kKLUiQv5iJ',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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

        data = f'------WebKitFormBoundaryIzJkS4kKLUiQv5iJ\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryIzJkS4kKLUiQv5iJ--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000025_GET_dataserver2_service(self):
        url = '/dataserver2/service'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000026_GET_dataserver2_users_stress_tester0(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000027_GET_dataserver2_users_stress_tester0_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000028_GET_dataserver2_users_stress_tester0(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000030_GET_dataserver2_users_stress_tester0_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000032_GET_site_assets_shared_strings_en_json(self):
        url = '/site-assets/shared/strings.en.json'
        
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
    def task_000033_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '/dataserver2/analytics/sessions/%40%40analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000034_GET_dataserver2_users_stress_tester0_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000035_GET_dataserver2_users_stress_tester0_Groups(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Groups'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000036_GET_dataserver2_users_stress_tester0_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000037_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000038_GET_dataserver2_users_stress_tester0_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
            'notAfter': '1595912399.722',
            'notBefore': '1595861415.722',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000039_GET_dataserver2_users_stress_tester0_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000040_GET_dataserver2_users_stress_tester0_Communities_Communities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000041_GET_dataserver2_users_stress_tester0_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000042_GET_dataserver2_users_stress_tester0_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
            'notAfter': '1595912399.749',
            'notBefore': '1595861415.749',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000043_GET_dataserver2_users_stress_tester0_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000044_GET_dataserver2_users_stress_tester0_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000045_GET_dataserver2_users_stress_tester0_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000046_GET_dataserver2_users_stress_tester0_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000047_GET_content_sites_alpha_nextthought_com_ContentPackageBundles_Alpha_presentation_assets_webapp_contentpackage_landing_232x170_png(self):
        url = '/content/sites/alpha.nextthought.com/ContentPackageBundles/Alpha/presentation-assets/webapp/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '0',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000048_GET_content_sites_alpha_nextthought_com_ContentPackageBundles_NextThoughtFAQ_RPN_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '/content/sites/alpha.nextthought.com/ContentPackageBundles/NextThoughtFAQ-RPN/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1507568586',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000049_GET_content_sites_alpha_nextthought_com_Courses_DefaultAPICreated_QAAUTO_1521661598323_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = f'/content/sites/alpha.nextthought.com/Courses/DefaultAPICreated/{self.course_id}/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1522097161',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000050_GET_dataserver2_users_stress_tester0_Catalog_Courses_40_40ByTag(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000052_GET_dataserver2_users_stress_tester0_Catalog_Courses_40_40Featured(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40Featured'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
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
    def task_000061_GET_dataserver2_users_stress_tester0_Catalog_Courses_40_40ByTag(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000062_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseCatalogEntry(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        )

    @task()
    def task_000064_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000065_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asite_admin_alpha_OID_0x12c2f599_3A5573657273_3AMB0r6d4B3ab(self):
        url = '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asite.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000066_POST_dataserver2_analytics_batch_events(self):
        url = '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '432',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiid,
                           "timestamp":1595861429.241,"user":f"stress.tester{self.user_id}",
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
    def task_000067_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000068_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000069_GET_dataserver2_users_stress_tester0_Catalog_Courses_40_40Featured(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40Featured'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000070_GET_dataserver2_ResolveUser_inst1234(self):
        url = '/dataserver2/ResolveUser/inst1234'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000071_GET_dataserver2_ResolveUser_content_editor_alpha(self):
        url = '/dataserver2/ResolveUser/content.editor.alpha'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000072_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asystem_OID_0x4e90b7_3A5573657273_40_40avatar_view(self):
        url = '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asystem-OID-0x4e90b7%3A5573657273/%40%40avatar_view'
        
        headers = {
            'Connection': 'keep-alive',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000073_POST_dataserver2_users_stress_tester0_Courses_EnrolledCourses(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '94',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000074_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asystem_OID_0x4e90b7_3A5573657273_40_40avatar_view(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asystem-OID-0x4e90b7%3A5573657273/%40%40avatar_view'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000075_GET_dataserver2_users_stress_tester0_Courses_EnrolledCourses_40_40Current(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Current'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000076_GET_dataserver2_users_stress_tester0_Courses_EnrolledCourses_40_40Archived(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Archived'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000077_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseCatalogEntry(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        )

    @task()
    def task_000078_GET_dataserver2_users_stress_tester0_Courses_EnrolledCourses_40_40Upcoming(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Upcoming'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000079_GET_dataserver2_users_stress_tester0_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1595912399.838',
            'notBefore': '1595861431.838',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000080_GET_dataserver2_users_stress_tester0_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1595912399.32',
            'notBefore': '1595861432.32',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000081_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseCatalogEntry(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry'
        )

    @task()
    def task_000082_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvYWxwaGEubmV4dHRob3VnaHQuY29tLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUNyZWF0ZWQvUUFBVVRPLTE1OTM4MDEyMDI4NDkvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        )

    @task()
    def task_000083_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asite_admin_alpha_OID_0x12c2f599_3A5573657273_3AMB0r6d4B3ab(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asite.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000085_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000086_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000087_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_40_40AssignmentSummaryByOutlineNode(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40AssignmentSummaryByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000088_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000089_HEAD_app_resources_images_default_course_vendoroverrideicon_png(self):
        url = '' + '/app/resources/images/default-course/vendoroverrideicon.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000090_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000091_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000092_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000093_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_CourseTabPreferences(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/CourseTabPreferences'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000094_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000095_GET_dataserver2_users_stress_tester0_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_8814601425988072132_4744471694987486254_AssignmentHistories_stress_tester0(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-8814601425988072132_4744471694987486254/AssignmentHistories/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-8814601425988072132_4744471694987486254/AssignmentHistories/stress.tester{self.user_id}'
        )

    @task()
    def task_000097_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_site_admin_alpha_4744471695841646541_0_40_40overview_content(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_site_admin_alpha_4744471695841646541_0/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_site_admin_alpha_4744471695841646541_0/%40%40overview-content'
        )

    @task()
    def task_000098_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_contents(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/contents'
        )

    @task()
    def task_000099_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_site_admin_alpha_4744471695841646541_0_40_40overview_summary(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_site_admin_alpha_4744471695841646541_0/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-8814601425988072132_4744471694987486254_site_admin_alpha_4744471695793290629_0_site_admin_alpha_4744471695841646541_0/%40%40overview-summary'
        )

    @task()
    def task_000102_GET_app_api_videos_youtube(self):
        url = '' + '/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000103_GET_app_api_videos_youtube(self):
        url = '' + '/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000104_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744471699091768755_1446068238(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744471699091768755_1446068238'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744471699091768755_1446068238'
        )

    @task()
    def task_000105_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Completion_CompletedItems_users_stress_tester0(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Completion/CompletedItems/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000106_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744471706818391273_4170222605(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744471706818391273_4170222605'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744471706818391273_4170222605'
        )

    @task()
    def task_000112_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '436',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiid,"timestamp":1595861429.241,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiid,"Duration":7.267}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000113_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1593801202849_40_40UserCoursePreferredAccess(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/{self.course_id}/%40%40UserCoursePreferredAccess'
        )

    @task()
    def task_000114_GET_dataserver2_users_stress_tester0_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200724194746',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000116_GET_dataserver2_logon_logout(self):
        url = '/dataserver2/logon.logout'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000117_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
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
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
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
    def task_000118_GET_login(self):
        url = '/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x12c2f599%3A5573657273%3AMB0r6d4B3ab/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000120_GET_dataserver2_logon_ping(self):
        url = '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'accept': 'application/json',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200724162756',
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



class WebsiteUser(HttpUser):
    tasks = [UserEnrollment]
    wait_time = between(1, 5)

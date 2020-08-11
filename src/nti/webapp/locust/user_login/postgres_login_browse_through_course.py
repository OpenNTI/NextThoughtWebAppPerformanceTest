# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
USER_CREDENTIALS = list(range(1, 2000))

class UserBehavior(SequentialTaskSet):
    user_id=0
    #this gets called before each User is trigered
    def on_start(self):
        self.user_id = USER_CREDENTIALS.pop()
        print(f'starting {self.user_id}')

    @task()
    def task_000002_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    ### Additional tasks can go here ###
    @task()
    def task_000003_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary9UaRaKWA4iNYvWGc',
            'Origin': '' + '',
            'Content-Length': '143',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundary9UaRaKWA4iNYvWGc\r\nContent-Disposition: form-data; name="username"\r\n\r\nstre\r\n------WebKitFormBoundary9UaRaKWA4iNYvWGc--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000004_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000005_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryl0fJfCst7TrVMEZg',
            'Origin': '' + '',
            'Content-Length': '145',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryl0fJfCst7TrVMEZg\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress\r\n------WebKitFormBoundaryl0fJfCst7TrVMEZg--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000006_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000007_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryZKwCV12hBQ6MAdyX',
            'Origin': '' + '',
            'Content-Length': '146',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryZKwCV12hBQ6MAdyX\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.\r\n------WebKitFormBoundaryZKwCV12hBQ6MAdyX--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000008_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000009_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryH2TQtQwBMx55kATy',
            'Origin': '' + '',
            'Content-Length': '150',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryH2TQtQwBMx55kATy\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.test\r\n------WebKitFormBoundaryH2TQtQwBMx55kATy--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000010_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000011_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryym6sP1y2TkSARpOl',
            'Origin': '' + '',
            'Content-Length': '152',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryym6sP1y2TkSARpOl\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester\r\n------WebKitFormBoundaryym6sP1y2TkSARpOl--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000012_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000013_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary2klsnSmq2nSB59Ax',
            'Origin': '' + '',
            'Content-Length': '153',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = f'------WebKitFormBoundary2klsnSmq2nSB59Ax\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundary2klsnSmq2nSB59Ax--\r\n'

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000014_GET_dataserver2_logon_nti_password(self):
        url = '/dataserver2/logon.nti.password'
        sval = f"stress.tester{self.user_id}:temp001"
        password = base64.b64encode(sval.encode('utf-8')).decode('utf-8')

        headers = {
            'Authorization': f"Basic {password}",
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-App': '@nti/web-login',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        params = {
            'username': f'stress.tester{self.user_id}',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name = '/dataserver2/logon.nti.password'
        )

    @task()
    def task_000015_GET_loginsuccess(self):
        url = '' + '/loginsuccess'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
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
    def task_000016_GET_app(self):
        url = '' + '/app'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000017_GET_app_resources_css_legacy_css(self):
        url = '' + '/app/resources/css/legacy.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000018_GET_app_resources_strings_strings_js(self):
        url = '' + '/app/resources/strings/strings.js'

        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000019_GET_app_resources_vendor_index_9d65298d2bb7f17340e2_css(self):
        url = '' + '/app/resources/vendor~index-9d65298d2bb7f17340e2.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000020_GET_app_resources_locales_en_LC_MESSAGES_NextThoughtWebApp_js(self):
        url = '' + '/app/resources/locales/en/LC_MESSAGES/NextThoughtWebApp.js'

        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000024_GET_app_js_version(self):
        url = '' + '/app/js/version'

        headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Cache-Control': 'no-cache',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000025_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000026_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Content-Length': '23',
            'Connection': 'keep-alive',
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
    def task_000027_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000029_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryhmJN4AbpdsVWHkei',
            'Origin': '' + '',
            'Content-Length': '153',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Connection': 'keep-alive',
        }

        data = f'------WebKitFormBoundaryhmJN4AbpdsVWHkei\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryhmJN4AbpdsVWHkei--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000031_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000032_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000033_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        )

    # @task()
    # def task_000034_GET_socket_io_1(self):
    #     url = '' + '/socket.io/1'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         't': '1594846509146',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000035_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000036_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        )

    # @task()
    # def task_000037_GET_socket_io_1_websocket_0x64c4d636be071a9e(self):
    #     url = '' + '/socket.io/1/websocket/0x64c4d636be071a9e'
    #
    #     headers = {
    #         'Upgrade': 'websocket',
    #         'Connection': 'Upgrade',
    #         'Origin': '' + '',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'Sec-WebSocket-Key': 'sYaOCD5QcB7qGT5Ari7TUw==',
    #         'Sec-WebSocket-Version': '13',
    #         'Sec-WebSocket-Extensions': 'x-webkit-deflate-frame',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000038_GET_site_assets_shared_strings_en_json(self):
        url = '' + '/site-assets/shared/strings.en.json'

        headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000039_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'

        headers = {
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        )

    @task()
    def task_000040_GET_dataserver2_users_stress_tester1_Groups(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Groups'

        headers = {
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Content-Type': 'application/vnd.nextthought.friendslist+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Groups'
        )

    @task()
    def task_000041_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '2',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Connection': 'keep-alive',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000042_GET_app_resources_images_b01e099bd186dd076d5fd26ab9006b2e_svg(self):
        url = '' + '/app/resources/images/b01e099bd186dd076d5fd26ab9006b2e.svg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000043_GET_site_assets_shared_brand_web_library_png(self):
        url = '' + '/site-assets/shared/brand_web_library.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000044_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000045_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        )

    @task()
    def task_000046_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        )

    @task()
    def task_000047_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1594875599.902',
            'notBefore': '1594846509.902',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000048_GET_dataserver2_users_stress_tester1_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        )

    @task()
    def task_000049_GET_dataserver2_users_stress_tester1_Communities_Communities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
        )

    @task()
    def task_000050_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        )

    @task()
    def task_000051_GET_dataserver2_users_stress_tester1_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        )

    @task()
    def task_000052_GET_dataserver2_users_stress_tester1_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        )

    @task()
    def task_000053_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
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
    def task_000054_GET_app_resources_images_9f385584bc111c738a1a1f797918e606_svg(self):
        url = '/app/resources/images/9f385584bc111c738a1a1f797918e606.svg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000055_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        params = {
            't': '1594784789',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000056_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Ajulie_zhu_40nextthought_com_OID_0x071a_3A5573657273_3AU1j0YSfyWD7(
            self):
        url = '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Ajulie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000059_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40UserCoursePreferredAccess(
            self):
        url = '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40UserCoursePreferredAccess'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000061_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_background_png(
            self):
        url = '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/background.png'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
        }

        params = {
            't': '1594784789',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000062_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(
            self):
        url = '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000063_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40AssignmentSummaryByOutlineNode(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40AssignmentSummaryByOutlineNode'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000064_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000066_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_vendoroverrideicon_png(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/vendoroverrideicon.png'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
        }

        params = {
            't': '1594784789',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000067_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40UserCoursePreferredAccess(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40UserCoursePreferredAccess'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000068_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
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
    def task_000069_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_background_png(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/background.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        params = {
            't': '1594784789',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000070_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_7337604134509948579_4744475820139681474_AssignmentHistories_stress_tester1(
            self):
        url = f'/dataserver2/users/stress.tester1/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-7337604134509948579_4744475820139681474/AssignmentHistories/stress.tester{self.user_id}'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester1/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-7337604134509948579_4744475820139681474/AssignmentHistories/stress.tester{self.user_id}'
        )

    @task()
    def task_000071_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_CourseTabPreferences(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/CourseTabPreferences'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000072_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000073_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000074_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_0_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000075_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000076_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_0_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000077_GET_dataserver2_cf_io_eYpthwSua1V_Screen_Shot_2020_07_08_at_7_51_48_PM_png(self):
        url = '' + '/dataserver2/cf.io/eYpthwSua1V/Screen_Shot_2020-07-08_at_7.51.48_PM.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000078_GET_app_resources_images_038450b97daf7fc972276c3e04610153_png(self):
        url = '' + '/app/resources/images/038450b97daf7fc972276c3e04610153.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000079_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000088_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000090_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000091_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_0_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000092_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_0_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000093_GET_app_resources_images_047ac8735d1f282989602045506031f3_svg(self):
        url = '' + '/app/resources/images/047ac8735d1f282989602045506031f3.svg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000094_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000095_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40MediaByOutlineNode(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40MediaByOutlineNode'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000096_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIVideo_51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000097_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIVideo_51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080_29_RelevantContainedUserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080%29/RelevantContainedUserGeneratedData'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080%29/RelevantContainedUserGeneratedData'
        )

    @task()
    def task_000109_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '788',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-E30F50593E633F83810511F9612A37BE48B5FE3303CEE0718E2743B201F6B778_0144"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846519.409,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080",
                           "Duration":None,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":0,"MaxDuration":49.195,"PlaySpeed":1}]}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000126_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '731',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.skipvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-E30F50593E633F83810511F9612A37BE48B5FE3303CEE0718E2743B201F6B778_0144"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846528.221,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080",
                           "player_configuration":"media-modal","with_transcript":True,"Duration":None}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000129_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '790',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-E30F50593E633F83810511F9612A37BE48B5FE3303CEE0718E2743B201F6B778_0144"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846519.409,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080",
                           "Duration":23.402,"player_configuration":"media-modal","with_transcript":True,"video_start_time":0,"MaxDuration":49.195,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000140_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '731',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIVideoRef-system_20200715034634_764903_3237562182',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.skipvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-E30F50593E633F83810511F9612A37BE48B5FE3303CEE0718E2743B201F6B778_0144"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846533.186,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080",
                           "player_configuration":"media-modal","with_transcript":True,"Duration":None}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000173_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000176_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000177_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_1_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000178_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_1_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000179_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0x08c8_3A5573657273_3AeYpthwSua1U(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0x08c8%3A5573657273%3AeYpthwSua1U'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000180_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351286_C755F1DE0A3FD614E866_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351286.C755F1DE0A3FD614E866/eclipse-toc.xml'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'dc': '1594841289',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000181_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351284_00CA767CB76F5BEA2334_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351284.00CA767CB76F5BEA2334/eclipse-toc.xml'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'dc': '1594841288',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000182_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351280_74448240CA635EAFDDE6_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351280.74448240CA635EAFDDE6/eclipse-toc.xml'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'dc': '1594841288',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000183_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351268_9A832782BAAACFAADBCA_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351268.9A832782BAAACFAADBCA/eclipse-toc.xml'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'dc': '1594841274',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000184_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351274_DD67A9B0422FD43B99AA_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351274.DD67A9B0422FD43B99AA/eclipse-toc.xml'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'dc': '1594841278',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000185_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351272_032F35A4B5321914224B_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351272.032F35A4B5321914224B/eclipse-toc.xml'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'dc': '1594841277',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000186_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351278_F2EEB56BFC7BD87C00C8_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351278.F2EEB56BFC7BD87C00C8/eclipse-toc.xml'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'dc': '1594841279',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000187_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351270_139D34A1D85EF663F079_eclipse_toc_xml(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351270.139D34A1D85EF663F079/eclipse-toc.xml'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'dc': '1594841277',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000188_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089%29/UserGeneratedData'
        )

    @task()
    def task_000189_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '775',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846538.535,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089","Duration":0}]}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000190_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '814',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/items/NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-E30F50593E633F83810511F9612A37BE48B5FE3303CEE0718E2743B201F6B778_0144"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846519.409,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-51371409ED9C304531D434B2A3DBFC9AA9487536588A5EB682508E77B825ACE4_0080",
                           "Duration":47.604,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":0,"video_end_time":47.604,"MaxDuration":49.195,"PlaySpeed":1}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000192_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000194_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000195_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_2_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000196_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_1_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000197_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_2_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000198_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_1_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000199_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000200_GET_dataserver2_cf_io_eYpthwSua1T_Screen_Shot_2020_07_10_at_5_02_32_PM_png(self):
        url = '' + '/dataserver2/cf.io/eYpthwSua1T/Screen_Shot_2020-07-10_at_5.02.32_PM.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000201_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000202_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088%29/UserGeneratedData'
        )

    @task()
    def task_000203_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '778',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846546.77,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088",
                           "Duration":0.001}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000204_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '779',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846538.535,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-E04DB0B96DF41E1C1168735DA29EC256FEDD10DBAD7787C740AF6A2D1EFCD91D_0089",
                           "Duration":6.524}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000205_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Content-Length': '2',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000220_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '778',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846546.77,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088",
                           "Duration":4.241}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000221_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '2',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'Connection': 'keep-alive',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000222_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1/items/NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000234_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000235_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_5_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.5/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000236_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000237_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_5_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.5/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000238_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_2_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000239_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_2_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000242_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000243_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_6_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000244_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_6_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000247_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIVideo_E3FADBCEF62A9BA57524DAE46A466F071763FD374A80F7B00BCC4D779565E9C7_0080(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-E3FADBCEF62A9BA57524DAE46A466F071763FD374A80F7B00BCC4D779565E9C7_0080'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000248_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIVideo_E3FADBCEF62A9BA57524DAE46A466F071763FD374A80F7B00BCC4D779565E9C7_0080_29_RelevantContainedUserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-E3FADBCEF62A9BA57524DAE46A466F071763FD374A80F7B00BCC4D779565E9C7_0080%29/RelevantContainedUserGeneratedData'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.2/items/NTI-NTIVideoRef-system_20200715034634_861078_2092547791',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-E3FADBCEF62A9BA57524DAE46A466F071763FD374A80F7B00BCC4D779565E9C7_0080%29/RelevantContainedUserGeneratedData'
        )

    @task()
    def task_000260_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_0_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.0/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000261_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_6_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000262_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000263_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_6_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000264_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_0_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.0/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000265_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_1_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000266_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000267_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_1_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000268_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0x08d3_3A5573657273_3AeYpthwSua1M(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0x08d3%3A5573657273%3AeYpthwSua1M'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000269_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089%29/UserGeneratedData'
        )

    @task()
    def task_000270_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '1478',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846552.79,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088",
                           "Duration":0.002},{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                                              "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                                              "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6",
                                                              "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089"],
                                              "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                              "timestamp":1594846561.709,"user":f"stress.tester{self.user_id}",
                                              "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089",
                                              "Duration":0}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000271_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '778',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6/items/NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846552.79,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-452C04D1E22C282A90335D52CD89AC1F639AE9072839B354617B2CF15A23A80A_0088",
                           "Duration":1.586}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000272_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000274_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000275_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_1_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000276_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_1_1_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000277_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000278_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000279_GET_dataserver2_cf_io_eYpthwSua1D_CA93D633_6D4A_4CB8_8F26_54D5C5FCBFB4_4_5005_c_14_18_51_1_jpeg(
            self):
        url = '' + '/dataserver2/cf.io/eYpthwSua1D/CA93D633-6D4A-4CB8-8F26-54D5C5FCBFB4_4_5005_c.14.18.51.1.jpeg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000280_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000281_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000282_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000283_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000284_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000285_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000286_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000287_GET_dataserver2_NTIIDs_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056(
            self):
        url = '' + '/dataserver2/NTIIDs/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/vnd.nextthought.renderablecontentpackage',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000288_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000289_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000290_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351268_9A832782BAAACFAADBCA_real_pages_json(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351268.9A832782BAAACFAADBCA/real_pages.json'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000291_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_CourseCatalogEntry(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/CourseCatalogEntry'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000292_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351268_9A832782BAAACFAADBCA_index_html(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351268.9A832782BAAACFAADBCA/index.html'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000293_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_HTML_5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056%29/UserGeneratedData'
        )

    @task()
    def task_000295_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '762',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846567.013,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056","Duration":0}]}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000296_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000298_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000299_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000300_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000301_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000302_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000303_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000304_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_Savepoint(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        )

    @task()
    def task_000305_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000306_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentAttemptMetadataItem_40_40HistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40HistoryItem'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40HistoryItem'
        )

    @task()
    def task_000307_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x15cf_3A5573657273_3AU1j0YSfyWAX(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x15cf%3A5573657273%3AU1j0YSfyWAX'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x15cf%3A5573657273%3AU1j0YSfyWAX'
        )

    @task()
    def task_000308_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        )

    @task()
    def task_000310_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000312_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x15ce_3A5573657273_3AU1j0YSfyWAY(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x15ce%3A5573657273%3AU1j0YSfyWAY'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x15ce%3A5573657273%3AU1j0YSfyWAY'
        )

    @task()
    def task_000314_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '886',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846569.952,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                           "Duration":0,
                           "ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000318_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '1470',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.6",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846561.709,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-70493E058B576AF9CCE3295DC6900A2732FF7C049D6924AAF88FBBC10019196E_0089",
                           "Duration":2.149},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-8F6897458DA239E19FBD0482257927851C7C9BF3480768BC878EDBAD646F2582_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846567.013,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-5F2A1D5212AC75787DC40C3040CA812123810DC9D6A3B454C3C7E8F45C745419_0056",
                           "Duration":0.988}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000319_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000321_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000322_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000323_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000324_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000325_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000326_GET_dataserver2_NTIIDs_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056(
            self):
        url = '' + '/dataserver2/NTIIDs/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/vnd.nextthought.renderablecontentpackage',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000327_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000328_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351270_139D34A1D85EF663F079_real_pages_json(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351270.139D34A1D85EF663F079/real_pages.json'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000329_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351270_139D34A1D85EF663F079_index_html(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351270.139D34A1D85EF663F079/index.html'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000330_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351270_139D34A1D85EF663F079_styles_content_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351270.139D34A1D85EF663F079/styles/content.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000331_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351270_139D34A1D85EF663F079_styles_styles_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351270.139D34A1D85EF663F079/styles/styles.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000332_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_HTML_C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056%29/UserGeneratedData'
        )

    @task()
    def task_000333_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '762',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7","timestamp":1594846579.931,
                           "user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056","Duration":0}]}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000334_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000335_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000337_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000338_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000339_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000340_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000341_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000342_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_Savepoint(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/Savepoint'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/Savepoint'
        )

    @task()
    def task_000343_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000344_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentAttemptMetadataItem_40_40HistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40HistoryItem'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40HistoryItem'
        )

    @task()
    def task_000345_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x1480_3A5573657273_3AdpuaAE2Vc2W(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x1480%3A5573657273%3AdpuaAE2Vc2W'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x1480%3A5573657273%3AdpuaAE2Vc2W'
        )

    @task()
    def task_000346_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084'
        )

    @task()
    def task_000347_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000348_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x147f_3A5573657273_3AdpuaAE2Vc2X(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x147f%3A5573657273%3AdpuaAE2Vc2X'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x147f%3A5573657273%3AdpuaAE2Vc2X'
        )

    @task()
    def task_000349_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '886',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846582.449,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084"}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000350_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '1581',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-F52BA72EC2B7E1B3769FADAC081596DC8D24311B247A216F62BDABC042B944A2_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846569.952,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                           "Duration":7.583,
                           "ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-BF12846CBD02F854E26E114C0CB6E7A8B7DB653E645F01585BDFE2F656D2B65B_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846579.931,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-C17E39144F4B09E99B03251A07A2DB4E68CE3C94556122E93C882EE8BE1F98AC_0056",
                           "Duration":0.846}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000351_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000354_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000355_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000356_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000357_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000358_GET_dataserver2_NTIIDs_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056(
            self):
        url = '' + '/dataserver2/NTIIDs/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.renderablecontentpackage',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000359_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351272_032F35A4B5321914224B_real_pages_json(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351272.032F35A4B5321914224B/real_pages.json'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000360_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351272_032F35A4B5321914224B_index_html(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351272.032F35A4B5321914224B/index.html'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000361_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351272_032F35A4B5321914224B_styles_content_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351272.032F35A4B5321914224B/styles/content.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000362_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_HTML_086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056%29/UserGeneratedData'
        )

    @task()
    def task_000363_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '762',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846589.538,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056","Duration":0}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000364_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000366_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000367_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000368_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0x08df_3A5573657273_3AeYpthwSua1E(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0x08df%3A5573657273%3AeYpthwSua1E'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000369_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000370_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089%29/UserGeneratedData'
        )

    @task()
    def task_000371_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '2285',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-AF5406A05EE534A749406721965F58513918E316D486E0A545179659A7246695_0087"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846582.449,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084",
                           "Duration":4.839,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-8D63AAC81733C67FB4157BC3DB4A9B0DF4653A075EE52E295E137489CB3206DF_0084"},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-EF95C119040F18A32B42F46100BE8295A24D662A7416B53C77781499BDADB34C_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846589.538,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-086B07B16DADA90576FC6480D45B1F2054586F53431ACA75B7B70145F5B52F56_0056","Duration":1.959},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7","timestamp":1594846592.883,
                           "user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089",
                           "Duration":0.001}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000372_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000374_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000375_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000376_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000377_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000378_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000379_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000380_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_Savepoint(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/Savepoint'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/Savepoint'
        )

    @task()
    def task_000381_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentHistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000382_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentAttemptMetadataItem_40_40HistoryItem(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40HistoryItem'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40HistoryItem'
        )

    @task()
    def task_000383_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x151c_3A5573657273_3AU1j0YSfyWAq(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x151c%3A5573657273%3AU1j0YSfyWAq'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x151c%3A5573657273%3AU1j0YSfyWAq'
        )

    @task()
    def task_000384_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083'
        )

    @task()
    def task_000385_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000386_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x151b_3A5573657273_3AU1j0YSfyWAr(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x151b%3A5573657273%3AU1j0YSfyWAr'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x151b%3A5573657273%3AU1j0YSfyWAr'
        )

    @task()
    def task_000387_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '886',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088',
            'Connection': 'keep-alive',
        }

        data = '''{"MimeType":"application/vnd.nextthought.analytics.batchevents","events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent","context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7","tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1","tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088"],"RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7","timestamp":1594846597.091,"user":"stress.tester1","ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083","Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083"}]}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000388_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000390_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000391_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000392_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000393_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000394_GET_dataserver2_NTIIDs_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056(
            self):
        url = '' + '/dataserver2/NTIIDs/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/vnd.nextthought.renderablecontentpackage',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000395_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351284_00CA767CB76F5BEA2334_real_pages_json(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351284.00CA767CB76F5BEA2334/real_pages.json'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000396_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351284_00CA767CB76F5BEA2334_index_html(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351284.00CA767CB76F5BEA2334/index.html'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000397_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_HTML_4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056%29/UserGeneratedData'
        )

    @task()
    def task_000398_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '762',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846602.683,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056","Duration":0}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000399_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000401_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0x08df_3A5573657273_3AeYpthwSua1E(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0x08df%3A5573657273%3AeYpthwSua1E'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000402_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000403_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000404_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088%29/UserGeneratedData'
        )

    @task()
    def task_000405_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '2294',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846592.883,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-6790189423EB2FC71A7FD5FD805E39B3F0C617AB1E50DB7C28BB0FBD9C03F57C_0089","Duration":2.468},
                          {"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-F3D003EE79447ED6E9832A41FD8DF941424C1EFEDAEE6054EF71B0078E7A73AD_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7","timestamp":1594846597.091,
                           "user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083","Duration":3.358,
                           "ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-61CFF56ED77939B961BEA6E5B3A22095D98B00FB824C6898489D4F986CEFE196_0083"},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846605.585,"user":"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088","Duration":0}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000407_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000408_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000409_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_0_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000410_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_0_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000411_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000412_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000413_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000414_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000415_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083_Savepoint(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083/Savepoint'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083/Savepoint'
        )

    @task()
    def task_000416_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000417_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '886',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1/items/NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846608.097,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083"}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000418_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000421_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000422_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_0_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000423_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_0_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000424_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000425_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000426_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2D29F748E78F2CC80714194F7C5FB9612B0721C2C34A41FB205DE55B1C40C503_0084(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2D29F748E78F2CC80714194F7C5FB9612B0721C2C34A41FB205DE55B1C40C503_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000427_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000428_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000429_GET_dataserver2_cf_io_eYpthwSua19_DB3B744A_B299_45A8_8ED8_23D78D68A153_4_5005_c_14_31_31_1_jpeg(
            self):
        url = '' + '/dataserver2/cf.io/eYpthwSua19/DB3B744A-B299-45A8-8ED8-23D78D68A153_4_5005_c.14.31.31.1.jpeg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000430_GET_dataserver2_cf_io_eYpthwSua18_CA93D633_6D4A_4CB8_8F26_54D5C5FCBFB4_4_5005_c_14_34_49_1_jpeg(
            self):
        url = '' + '/dataserver2/cf.io/eYpthwSua18/CA93D633-6D4A-4CB8-8F26-54D5C5FCBFB4_4_5005_c.14.34.49.1.jpeg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000431_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000432_GET_dataserver2_cf_io_eYpthwSua1A_CA93D633_6D4A_4CB8_8F26_54D5C5FCBFB4_4_5005_c_14_30_24_1_jpeg(
            self):
        url = '' + '/dataserver2/cf.io/eYpthwSua1A/CA93D633-6D4A-4CB8-8F26-54D5C5FCBFB4_4_5005_c.14.30.24.1.jpeg'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000433_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000434_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000435_GET_dataserver2_NTIIDs_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056(
            self):
        url = '' + '/dataserver2/NTIIDs/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.renderablecontentpackage',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000436_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351274_DD67A9B0422FD43B99AA_real_pages_json(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351274.DD67A9B0422FD43B99AA/real_pages.json'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000437_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351274_DD67A9B0422FD43B99AA_index_html(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351274.DD67A9B0422FD43B99AA/index.html'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000438_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351274_DD67A9B0422FD43B99AA_styles_content_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351274.DD67A9B0422FD43B99AA/styles/content.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000439_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351274_DD67A9B0422FD43B99AA_styles_styles_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351274.DD67A9B0422FD43B99AA/styles/styles.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000440_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_HTML_FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056%29/UserGeneratedData'
        )

    @task()
    def task_000441_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '2284',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-0D881D7673701EC5A5869894330136627C9DC68A85943D5DFD5FB2D75643A81D_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846602.683,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-4B9E2AAD1038F26C8C40B8314D2B2A2C8B115A4FC8D770C7364C551C5FB1D327_0056",
                           "Duration":1.551},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846605.585,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-873D12CECA2934F7530BB677C8E0E698C7792DC99D4FA1FECB6B3127A299E0B5_0088",
                           "Duration":1.35},
                          {"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.1.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-2355AB7A3E78222612E60F9AF1A329EC9675B4421CB5AF270A1A5E2F9E9D7753_0087"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846608.097,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083",
                           "Duration":3.191,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-ABA5AEC8CC929755AA866851D6077066683D77C236069EFF92DBD003441F0530_0083"}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000442_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '762',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846614.325,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056","Duration":0}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000443_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000445_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000446_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000447_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000448_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        values = self.response.json()
        self.version = values['version']

    @task()
    def task_000449_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083_40_40Commence(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083/%40%40Commence'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'Origin': '' + '',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'Connection': 'keep-alive',
        }

        data = {'version': self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data = data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083/%40%40Commence'
        )

    @task()
    def task_000450_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000451_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083_Savepoint(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083/Savepoint'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083/Savepoint'
        )

    @task()
    def task_000452_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '886',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846618.115,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083"}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000453_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000455_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000456_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000457_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000458_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000459_GET_dataserver2_NTIIDs_tag_3Anextthought_com_2C2011_10_3ANTI_HTML_D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056(
            self):
        url = '' + '/dataserver2/NTIIDs/tag%3Anextthought.com%2C2011-10%3ANTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.renderablecontentpackage',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000460_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351278_F2EEB56BFC7BD87C00C8_real_pages_json(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351278.F2EEB56BFC7BD87C00C8/real_pages.json'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000461_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351278_F2EEB56BFC7BD87C00C8_index_html(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351278.F2EEB56BFC7BD87C00C8/index.html'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000462_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351278_F2EEB56BFC7BD87C00C8_styles_content_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351278.F2EEB56BFC7BD87C00C8/styles/content.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000463_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351278_F2EEB56BFC7BD87C00C8_styles_styles_css(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351278.F2EEB56BFC7BD87C00C8/styles/styles.css'

        headers = {
            'Accept': 'text/css,*/*;q=0.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000464_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_HTML_D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056%29/UserGeneratedData'
        )

    @task()
    def task_000465_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '1581',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-309840F694F23803D7D4830311F69439319CF5090CD68779CCBF6B797DE0DD55_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846614.325,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-FB8C304DCF84DB63A07A1C6766BA021CAA061EADC68AB7A73A21C4533EE8DD6F_0056",
                           "Duration":2.678},
                          {"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-ED5C17D4961F973D6E9185338EB7E2F76E36C6E07EE9A3DAF9CBDAE40AE5E8E9_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846618.115,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083",
                           "Duration":3.398,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-43416A0E1F791BE4C72973D33BAA7A6425D68841E1552E09BCC54C699367F363_0083"}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000466_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '762',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846623.768,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056","Duration":0}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000467_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000469_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000470_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000471_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0x08df_3A5573657273_3AeYpthwSua1E(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0x08df%3A5573657273%3AeYpthwSua1E'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000472_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089_29_UserGeneratedData(
            self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089%29/UserGeneratedData'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.collection+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'sortOn': 'lastModified',
            'sortOrder': 'descending',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089%29/UserGeneratedData'
        )

    @task()
    def task_000474_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '779',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846627.277,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089",
                           "Duration":0.001}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000475_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000477_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000478_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000479_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000480_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084(
            self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000482_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084_40_40Commence(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084/%40%40Commence'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'Origin': '' + '',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'X-NTI-Client-Version': '2020.7.1',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
        )

    @task()
    def task_000485_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000486_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084_Savepoint(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084/Savepoint'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084/Savepoint'
        )

    @task()
    def task_000488_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '886',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846631.667,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084"}]}


        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000497_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '1470',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/items/NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7CE2AA982B012AB9B069A0179587E7A339304FAB3865FEA930CC6E7D84257783_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846623.768,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-HTML-D22F27C969B3DCD309A589B344F972C2EE848227F34EDE9BB0249DB10AA13E64_0056","Duration":2.135},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846627.277,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-DD675D38CCB88B81664B523F4EBBD43315BBEEC1EE2D3BE39068F61E05F3DCBD_0089","Duration":3.368}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000498_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester1(
            self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    @task()
    def task_000500_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
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
    def task_000501_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000502_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '890',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0",
                                           "tag:nextthought.com,2011-10:NTI-NTIAssignmentRef-EF088A1314FAD70ED3BC5DDC80738873F613D980A392C9D4003483C828178EB4_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1594846631.667,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084",
                           "Duration":2.095,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-575519D9AE6463156900D97411EFC5EB52C072B18C1FB218F1B84191D3F711FD_0084"}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000503_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_0_40_40overview_summary(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/%40%40overview-summary'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000504_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_2_0_40_40overview_content(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/%40%40overview-content'

        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'X-NTI-Client-Version': '2020.7.1',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
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
    def task_000505_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.1',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000506_GET_dataserver2_logon_logout(self):
        url = '' + '/dataserver2/logon.logout'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        params = {
            'success': '/login/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        )

    @task()
    def task_000507_GET_login(self):
        url = '' + '/login'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000508_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/lessons/NTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.2.0/',
            'Content-Length': '2',
        }

        data = '''{}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000510_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 9)



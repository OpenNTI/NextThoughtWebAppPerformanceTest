# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import time

USER_CREDENTIALS = list(range(1, 1000))

class SurveySubmission(SequentialTaskSet):
    user_id = 0
    version = None

    def on_start(self):
        self.user_id = USER_CREDENTIALS.pop()
        print(f'starting {self.user_id}')

    @task()
    def task_000000_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000001_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryQGK3nWIKn5g3C1rx',
            'Origin': '' + '',
            'Content-Length': '143',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryQGK3nWIKn5g3C1rx\r\nContent-Disposition: form-data; name="username"\r\n\r\nstre\r\n------WebKitFormBoundaryQGK3nWIKn5g3C1rx--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000003_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryMIXQ6BzT1x7mv0Yx',
            'Origin': '' + '',
            'Content-Length': '144',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryMIXQ6BzT1x7mv0Yx\r\nContent-Disposition: form-data; name="username"\r\n\r\nstres\r\n------WebKitFormBoundaryMIXQ6BzT1x7mv0Yx--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000006_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryHep6Sx7dxqcVOBl7',
            'Origin': '' + '',
            'Content-Length': '145',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryHep6Sx7dxqcVOBl7\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress\r\n------WebKitFormBoundaryHep6Sx7dxqcVOBl7--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000007_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000008_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8D1PmZtzCffa7arX',
            'Origin': '' + '',
            'Content-Length': '146',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundary8D1PmZtzCffa7arX\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.\r\n------WebKitFormBoundary8D1PmZtzCffa7arX--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000009_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000010_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarybqbsmPg4qGaAKY4J',
            'Origin': '' + '',
            'Content-Length': '147',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundarybqbsmPg4qGaAKY4J\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.t\r\n------WebKitFormBoundarybqbsmPg4qGaAKY4J--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000011_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000012_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryD9ZGVAOdOWcBsXkM',
            'Origin': '' + '',
            'Content-Length': '149',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryD9ZGVAOdOWcBsXkM\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tes\r\n------WebKitFormBoundaryD9ZGVAOdOWcBsXkM--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000013_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000014_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary1zsRMj42q55oziXq',
            'Origin': '' + '',
            'Content-Length': '150',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundary1zsRMj42q55oziXq\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.test\r\n------WebKitFormBoundary1zsRMj42q55oziXq--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000015_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000016_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzcY93PsOEvEgTvab',
            'Origin': '' + '',
            'Content-Length': '152',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryzcY93PsOEvEgTvab\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester\r\n------WebKitFormBoundaryzcY93PsOEvEgTvab--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    # @task()
    # def task_000017_GET_dataserver2_logon_ping(self):
    #     url = '' + '/dataserver2/logon.ping'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-login',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/login/',
    #         'X-NTI-Client-Version': '2020.6.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000018_POST_dataserver2_logon_handshake(self):
    #     url = '' + '/dataserver2/logon.handshake'
    #
    #     headers = {
    #         'Accept': 'application/json',
    #         'X-NTI-Client-App': '@nti/web-login',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryJAwVLKh10JEi6EHZ',
    #         'Origin': '' + '',
    #         'Content-Length': '153',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'X-NTI-Client-Version': '2020.6.2',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/login/',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     data = '''------WebKitFormBoundaryJAwVLKh10JEi6EHZ\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester1\r\n------WebKitFormBoundaryJAwVLKh10JEi6EHZ--\r\n'''
    #
    #     self.response = self.client.request(
    #         method='POST',
    #         url=url,
    #         headers=headers,
    #         data=data,
    #     )

    @task()
    def task_000019_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000020_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryU7jGdYhpPNMHiRBl',
            'Origin': '' + '',
            'Content-Length': '154',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = f'------WebKitFormBoundaryU7jGdYhpPNMHiRBl\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryU7jGdYhpPNMHiRBl--\r\n'

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000021_GET_dataserver2_logon_nti_password(self):

        url = '' + '/dataserver2/logon.nti.password'
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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
            name='/dataserver2/logon.nti.password'
        )

    @task()
    def task_000022_GET_loginsuccess(self):
        url = '' + '/loginsuccess'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000023_GET_app(self):
        url = '' + '/app'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/login/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000024_GET_app_js_index_4d26438d_js(self):
    #     url = '' + '/app/js/index-4d26438d.js'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000025_GET_app_resources_strings_strings_js(self):
    #     url = '' + '/app/resources/strings/strings.js'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000026_GET_app_resources_vendor_index_9d65298d2bb7f17340e2_css(self):
    #     url = '' + '/app/resources/vendor~index-9d65298d2bb7f17340e2.css'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'text/css,*/*;q=0.1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000027_GET_app_resources_css_legacy_css(self):
    #     url = '' + '/app/resources/css/legacy.css'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'text/css,*/*;q=0.1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000028_GET_app_js_vendor_index_4d26438d_js(self):
    #     url = '' + '/app/js/vendor~index-4d26438d.js'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000029_GET_app_resources_lib_timeline_js_storyjs_embed_js(self):
    #     url = '' + '/app/resources/lib/timeline/js/storyjs-embed.js'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000030_GET_app_resources_shared_index_1de289914274f0a5f4f9_css(self):
    #     url = '' + '/app/resources/shared~index-1de289914274f0a5f4f9.css'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'text/css,*/*;q=0.1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000031_GET_app_resources_index_b310df32898df9f3e132_css(self):
    #     url = '' + '/app/resources/index-b310df32898df9f3e132.css'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'text/css,*/*;q=0.1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000032_GET_app_js_shared_index_4d26438d_js(self):
    #     url = '' + '/app/js/shared~index-4d26438d.js'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000034_GET_app_resources_locales_en_LC_MESSAGES_NextThoughtWebApp_js(self):
    #     url = '' + '/app/resources/locales/en/LC_MESSAGES/NextThoughtWebApp.js'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000035_GET_app_resources_css_nti_override_css(self):
    #     url = '' + '/app/resources/css/nti-override.css'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'text/css,*/*;q=0.1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000036_GET_app_resources_images_elements_folding_logo_gif(self):
    #     url = '' + '/app/resources/images/elements/folding_logo.gif'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000038_GET_app_resources_images_backdrops_whiteboard_error_loading_image_png(self):
    #     url = '' + '/app/resources/images/backdrops/whiteboard_error_loading_image.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000039_GET_app_resources_images_backdrops_whiteboard_error_unknown_png(self):
    #     url = '' + '/app/resources/images/backdrops/whiteboard_error_unknown.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000041_GET_app_js_version(self):
    #     url = '' + '/app/js/version'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Cache-Control': 'no-cache',
    #         'Accept-Language': 'en-us',
    #         'Pragma': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Connection': 'keep-alive',
    #         'Referer': '' + '/app/',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000042_GET_socket_io_static_socket_io_js(self):
    #     url = '' + '/socket.io/static/socket.io.js'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000043_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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
    def task_000044_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Content-Length': '24',
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
    def task_000045_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000047_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryoV8n44z45RUIR253',
            'Origin': '' + '',
            'Content-Length': '154',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Connection': 'keep-alive',
        }

        data = f'------WebKitFormBoundaryoV8n44z45RUIR253\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryoV8n44z45RUIR253--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000048_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000049_GET_dataserver2_users_stress_tester10(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}'
        )

    # @task()
    # def task_000050_GET_dataserver2_users_stress_tester10_FriendsLists(self):
    #     url = '' + '/dataserver2/users/stress.tester10/FriendsLists'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000051_POST_dataserver2_users_stress_tester10_FriendsLists(self):
    #     url = '' + '/dataserver2/users/stress.tester10/FriendsLists'
    #
    #     headers = {
    #         'Accept': 'application/json',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Content-Type': 'application/json',
    #         'Origin': '' + '',
    #         'Content-Length': '154',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     data = '''{"MimeType":"application/vnd.nextthought.friendslist","Username":"mycontacts-stress.tester10","alias":"My Contacts","friends":[],"IsDynamicSharing":false}'''
    #
    #     self.response = self.client.request(
    #         method='POST',
    #         url=url,
    #         headers=headers,
    #         data=data,
    #     )
    #
    # @task()
    # def task_000052_GET_socket_io_1(self):
    #     url = '' + '/socket.io/1'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         't': '1595302230523',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000053_GET_dataserver2_users_stress_tester10(self):
    #     url = '' + '/dataserver2/users/stress.tester10'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000054_GET_socket_io_1_websocket_0x730822d9e7373c7f(self):
    #     url = '' + '/socket.io/1/websocket/0x730822d9e7373c7f'
    #
    #     headers = {
    #         'Upgrade': 'websocket',
    #         'Connection': 'Upgrade',
    #         'Origin': '' + '',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'Sec-WebSocket-Key': 'lCVOIIGbYQTQcTZmZ5NFaA==',
    #         'Sec-WebSocket-Version': '13',
    #         'Sec-WebSocket-Extensions': 'x-webkit-deflate-frame',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000055_GET_dataserver2_users_stress_tester10_2B_2Bpreferences_2B_2B_WebApp(self):
    #     url = '' + '/dataserver2/users/stress.tester10/%2B%2Bpreferences%2B%2B/WebApp'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000058_GET_site_assets_shared_strings_en_json(self):
    #     url = '' + '/site-assets/shared/strings.en.json'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000059_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
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
            'X-NTI-Client-Version': '2020.7.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
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

    # @task()
    # def task_000060_GET_dataserver2_users_stress_tester10_Groups(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Groups'
    #
    #     headers = {
    #         'Accept': 'application/vnd.nextthought.collection+json',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Content-Type': 'application/vnd.nextthought.friendslist+json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Referer': '' + '/app/',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000061_GET_dataserver2_users_stress_tester10_FriendsLists(self):
    #     url = '' + '/dataserver2/users/stress.tester10/FriendsLists'
    #
    #     headers = {
    #         'Accept': 'application/vnd.nextthought.collection+json',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Content-Type': 'application/vnd.nextthought.friendslist+json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Referer': '' + '/app/',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000062_GET_dataserver2_users_stress_tester10_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
    #     url = '' + '/dataserver2/users/stress.tester10/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000063_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000064_GET_app_resources_images_sprite_png(self):
    #     url = '' + '/app/resources/images/sprite.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         't': '20200715192358',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000065_GET_dataserver2_users_stress_tester10_Calendars_40_40events(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Calendars/%40%40events'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'batchSize': '1',
    #         'notAfter': '1595307599.314',
    #         'notBefore': '1595302231.314',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000066_GET_dataserver2_users_stress_tester10_40_40NamedLinks_content_initial_tos_page(self):
    #     url = '' + '/dataserver2/users/stress.tester10/%40%40NamedLinks/content.initial_tos_page'
    #
    #     headers = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000067_GET_dataserver2_users_stress_tester10_Courses_EnrolledCourses_40_40Favorites(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Courses/EnrolledCourses/%40%40Favorites'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000068_GET_dataserver2_users_stress_tester10_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        )

    # @task()
    # def task_000069_GET_dataserver2_users_stress_tester10_Communities_Communities(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Communities/Communities'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000070_GET_app_resources_fonts_e8b470ef2ea162353e3f5a60ecb96d12_ttf(self):
    #     url = '' + '/app/resources/fonts/e8b470ef2ea162353e3f5a60ecb96d12.ttf'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000071_GET_app_resources_images_9f385584bc111c738a1a1f797918e606_svg(self):
    #     url = '' + '/app/resources/images/9f385584bc111c738a1a1f797918e606.svg'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000072_GET_dataserver2_users_stress_tester10_Calendars_40_40events(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Calendars/%40%40events'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'batchSize': '1',
    #         'notAfter': '1595307599.44',
    #         'notBefore': '1595302231.44',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000073_GET_dataserver2_users_stress_tester10_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000074_GET_dataserver2_users_stress_tester10_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        )

    @task()
    def task_000075_GET_dataserver2_users_stress_tester10_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        )

    # @task()
    # def task_000076_GET_app_resources_images_b01e099bd186dd076d5fd26ab9006b2e_svg(self):
    #     url = '' + '/app/resources/images/b01e099bd186dd076d5fd26ab9006b2e.svg'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000077_GET_vendor_ext_4_2_resources_ext_theme_classic_images_form_checkbox_gif(self):
    #     url = '' + '/vendor/ext-4.2/resources/ext-theme-classic/images/form/checkbox.gif'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000078_GET_dataserver2_users_stress_tester10_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'batchSize': '50',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000079_GET_app_resources_images_d892e3b9df35da881b61788e211f7530_png(self):
    #     url = '' + '/app/resources/images/d892e3b9df35da881b61788e211f7530.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000080_GET_app_resources_images_5e8ec3915fa05f4a981eb5e6eb60fc5f_png(self):
    #     url = '' + '/app/resources/images/5e8ec3915fa05f4a981eb5e6eb60fc5f.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000081_GET_app_resources_images_53605715bb0cda1017d5ea0f93f6698a_png(self):
    #     url = '' + '/app/resources/images/53605715bb0cda1017d5ea0f93f6698a.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000082_GET_app_resources_images_7f0d99a5b5c1fd285d7623ab678e12b5_png(self):
    #     url = '' + '/app/resources/images/7f0d99a5b5c1fd285d7623ab678e12b5.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000083_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         't': '1594784789',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000085_GET_app_resources_images_ee764b6ee333c4bfcadbc97eb818253c_png(self):
    #     url = '' + '/app/resources/images/ee764b6ee333c4bfcadbc97eb818253c.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000088_DELETE_dataserver2_users_stress_tester10_40_40NamedLinks_content_initial_tos_page(self):
    #     url = '' + '/dataserver2/users/stress.tester10/%40%40NamedLinks/content.initial_tos_page'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'Origin': '' + '',
    #         'Content-Length': '0',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Referer': '' + '/app/',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='DELETE',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000089_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Ajulie_zhu_40nextthought_com_OID_0x071a_3A5573657273_3AU1j0YSfyWD7(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Ajulie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
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

    # @task()
    # def task_000091_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40UserCoursePreferredAccess(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40UserCoursePreferredAccess'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000092_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000093_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_vendoroverrideicon_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/vendoroverrideicon.png'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'Content-Length': '0',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #     }
    #
    #     params = {
    #         't': '1594784789',
    #     }
    #
    #     self.response = self.client.request(
    #         method='HEAD',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000094_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000095_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_background_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/background.png'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'Content-Length': '0',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #     }
    #
    #     params = {
    #         't': '1594784789',
    #     }
    #
    #     self.response = self.client.request(
    #         method='HEAD',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000096_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40UserCoursePreferredAccess(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40UserCoursePreferredAccess'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000097_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40AssignmentSummaryByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40AssignmentSummaryByOutlineNode'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000098_GET_app_resources_images_elements_spinning_logo_png(self):
    #     url = '' + '/app/resources/images/elements/spinning_logo.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000099_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_background_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/background.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         't': '1594784789',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000100_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
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
    def task_000101_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_CourseTabPreferences(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/CourseTabPreferences'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000102_GET_dataserver2_users_stress_tester10_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_7337604134509948579_4744475820139681474_AssignmentHistories_stress_tester10(self):
    #     url = '' + '/dataserver2/users/stress.tester10/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-7337604134509948579_4744475820139681474/AssignmentHistories/stress.tester10'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000103_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'omit_unpublished': 'True',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000104_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     params = {
    #         'omit_unpublished': 'true',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000105_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'omit_unpublished': 'True',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000106_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_0_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/%40%40overview-content'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
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
    def task_000107_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_7337604134509948579_4744475820139681474_0_0_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-7337604134509948579_4744475820139681474.0.0/%40%40overview-summary'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
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

    # @task()
    # def task_000108_GET_app_resources_images_f41d087bc927db9186958dd8b6cbac66_png(self):
    #     url = '' + '/app/resources/images/f41d087bc927db9186958dd8b6cbac66.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000109_GET_app_resources_images_038450b97daf7fc972276c3e04610153_png(self):
    #     url = '' + '/app/resources/images/038450b97daf7fc972276c3e04610153.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000110_GET_app_resources_images_42ea90a441b4cdc8493a4ebd8593a56b_png(self):
    #     url = '' + '/app/resources/images/42ea90a441b4cdc8493a4ebd8593a56b.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000111_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Completion_CompletedItems_users_stress_tester10(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Completion/CompletedItems/users/stress.tester{self.user_id}'
        )

    # @task()
    # def task_000112_GET_dataserver2_cf_io_eYpthwSua1V_Screen_Shot_2020_07_08_at_7_51_48_PM_png(self):
    #     url = '' + '/dataserver2/cf.io/eYpthwSua1V/Screen_Shot_2020-07-08_at_7.51.48_PM.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000122_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_40_40AssignmentSummaryByOutlineNode(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/%40%40AssignmentSummaryByOutlineNode'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000123_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'omit_unpublished': 'True',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000124_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
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
        if 'version' in values:
            self.version = values['version']
        else:
            print(values)


    @task()
    def task_000126_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
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
    def task_000127_GET_dataserver2_users_stress_tester10_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_7337604134509948579_4744475820139681474_AssignmentHistories_stress_tester10(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-7337604134509948579_4744475820139681474/AssignmentHistories/stress.tester{self.user_id}'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-7337604134509948579_4744475820139681474/AssignmentHistories/stress.tester{self.user_id}'
        )

    @task()
    def task_000128_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
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
    def task_000129_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_40_40Commence(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/%40%40Commence'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'Origin': '' + '',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'X-NTI-Client-Version': '2020.7.2',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Connection': 'keep-alive',
        }

        data = {'version': self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/%40%40Commence'
        )

    @task()
    def task_000130_GET_app_resources_images_8982edf3b26c6e0e50972121db74da1a_png(self):
        url = '' + '/app/resources/images/8982edf3b26c6e0e50972121db74da1a.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000131_GET_app_resources_images_28c1ffce03b65d9f19f7a008e3628c5c_png(self):
        url = '' + '/app/resources/images/28c1ffce03b65d9f19f7a008e3628c5c.png'

        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000132_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
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
    def task_000133_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000135_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351278_F2EEB56BFC7BD87C00C8_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351278.F2EEB56BFC7BD87C00C8/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1594841279',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000136_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351270_139D34A1D85EF663F079_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351270.139D34A1D85EF663F079/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1594841277',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000137_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351274_DD67A9B0422FD43B99AA_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351274.DD67A9B0422FD43B99AA/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1594841278',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000138_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351284_00CA767CB76F5BEA2334_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351284.00CA767CB76F5BEA2334/eclipse-toc.xml'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'dc': '1594841288',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # # @task()
    # def task_000139_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351268_9A832782BAAACFAADBCA_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351268.9A832782BAAACFAADBCA/eclipse-toc.xml'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'dc': '1594841274',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000140_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351272_032F35A4B5321914224B_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351272.032F35A4B5321914224B/eclipse-toc.xml'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'dc': '1594841277',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000141_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351286_C755F1DE0A3FD614E866_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351286.C755F1DE0A3FD614E866/eclipse-toc.xml'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'dc': '1594841289',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    # @task()
    # def task_000142_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_authored_Sfdd0438bbad141b59137b0e12c47d7ed_nti_4670688607145351280_74448240CA635EAFDDE6_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/_authored_Sfdd0438bbad141b59137b0e12c47d7ed.nti_4670688607145351280.74448240CA635EAFDDE6/eclipse-toc.xml'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'dc': '1594841288',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000143_POST_dataserver2_analytics_batch_events(self):
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
            'Content-Length': '667',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7"],
                           "RootContextID":"tag:nextthought.com,2011-10:julie.zhu@nextthought.com-OID-0x071a:5573657273:U1j0YSfyWD7",
                           "timestamp":1595302245.722,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000144_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Content-Length': '2513',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission",
                          "NTIID":None,"tags":[],
                          "questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-B6A978B13988D712A78BAE28B51C488732638EC363A3F0DD4209B00DFF29B74F_0085",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":2,"ContainerId":""}],"CreatorRecordedEffortDuration":2,"version":self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        )

    @task()
    def task_000145_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Content-Length': '2510',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission",
                          "NTIID":None,"tags":[],
                          "questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-B6A978B13988D712A78BAE28B51C488732638EC363A3F0DD4209B00DFF29B74F_0085",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":4,"ContainerId":""}],"CreatorRecordedEffortDuration":4,"version":self.version}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        )

    @task()
    def task_000146_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentSavepoints_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Content-Length': '2690',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission",
                          "NTIID":None,"tags":[],
                          "questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-B6A978B13988D712A78BAE28B51C488732638EC363A3F0DD4209B00DFF29B74F_0085",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "parts":[{"MimeType":"application/vnd.nextthought.assessment.modeledcontentresponse","value":["test"]}],
                                        "CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "parts":[{"MimeType":"application/vnd.nextthought.assessment.modeledcontentresponse","value":["test"]}],
                                        "CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":11,"ContainerId":""}],"CreatorRecordedEffortDuration":11,"version":self.version}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/Savepoint'
        )

    @task()
    def task_000148_POST_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Content-Length': '3409',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission",
                          "NTIID":None,"tags":[],
                          "questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-B6A978B13988D712A78BAE28B51C488732638EC363A3F0DD4209B00DFF29B74F_0085",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-02F3C818C5CD196A8C3627DFB4698034E081C750B667CE237A4F3E7EB8965233_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-81F4CECB55227297A7AE6947E884D72AF2105DF3B04C04ED0077C7CEAA4045D7_0082",
                                        "parts":[0],"CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-C9BE79E7A739EE50EC6B0F0BB854D698996C8C6F8EC4DD285A37106C7C1BD521_0082",
                                        "parts":[{"MimeType":"application/vnd.nextthought.assessment.modeledcontentresponse","value":["test"]}],
                                        "CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-FCD92C62C7BF351FE1FA35E29E15C99674DC86BFB39E2B69115C226A0B718344_0082",
                                        "parts":[{"MimeType":"application/vnd.nextthought.assessment.modeledcontentresponse","value":["test"]}],
                                        "CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-92B0928836B8054E8BBC8ACA467EE49219DAFEFA7EA842959CC377DFE10E7818_0082",
                                        "parts":[{"MimeType":"application/vnd.nextthought.assessment.modeledcontentresponse","value":["test"]}],
                                        "CreatorRecordedEffortDuration":None,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"}],
                          "CreatorRecordedEffortDuration":14,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083"}],
                "CreatorRecordedEffortDuration":14,"version":self.version}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        )

    @task()
    def task_000149_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000150_GET_dataserver2_users_stress_tester10_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester10_OID_0x06ac9f_3A5573657273_3Ayk7ZtyetvF5(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x06ac9f%3A5573657273%3Ayk7ZtyetvF5'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x06ac9f%3A5573657273%3Ayk7ZtyetvF5'
        )

    @task()
    def task_000151_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentHistories_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        )

    @task()
    def task_000152_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000153_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_AssignmentAttemptMetadata_stress_tester10_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000154_GET_dataserver2_users_stress_tester10_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester10_OID_0x06ac9e_3A5573657273_3Ayk7ZtyetvF6(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x06ac9e%3A5573657273%3Ayk7ZtyetvF6'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x06ac9e%3A5573657273%3Ayk7ZtyetvF6'
        )

    @task()
    def task_000155_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000156_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000157_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_ctat_0000_20_281_29_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/ctat-0000%20%281%29/CourseCatalogEntry'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'X-NTI-Client-Version': '2020.7.2',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000158_GET_app_resources_images_20fb7a0d2fe9625be2cbe04443284d1b_svg(self):
        url = '' + '/app/resources/images/20fb7a0d2fe9625be2cbe04443284d1b.svg'
        
        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000159_GET_dataserver2_users_stress_tester10_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.7.2',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        )

    @task()
    def task_000163_GET_dataserver2_logon_logout(self):
        url = '/dataserver2/logon.logout'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
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
        )

    @task()
    def task_000164_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
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
    def task_000165_GET_login(self):
        url = '' + '/login'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/julie.zhu%40nextthought.com-OID-0x071a%3A5573657273%3AU1j0YSfyWD7/assignments/NTI-NAQ-2693BEA250B5854249BB137426CADB7EDF176C749E6A11B60BC1CBE821CD89BA_0083/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000166_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

        time.sleep(36000)

class WebsiteUser(HttpUser):
    tasks = [SurveySubmission]
    wait_time = between(5, 15)

# -*- coding: UTF-8 -*-

from locust import HttpUser, task, SequentialTaskSet, between
import json
import base64

USER_CREDENTIALS = list(range(1, 1000))

class AssignmentSubmission(SequentialTaskSet):
    user_id = 0
    version = None

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarygIFRFwOcXwvl3BAE',
            'Origin': '' + '',
            'Content-Length': '143',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundarygIFRFwOcXwvl3BAE\r\nContent-Disposition: form-data; name="username"\r\n\r\nstre\r\n------WebKitFormBoundarygIFRFwOcXwvl3BAE--\r\n'''

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryceVIlpY33s2NsFdm',
            'Origin': '' + '',
            'Content-Length': '144',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryceVIlpY33s2NsFdm\r\nContent-Disposition: form-data; name="username"\r\n\r\nstres\r\n------WebKitFormBoundaryceVIlpY33s2NsFdm--\r\n'''

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarylBKEzelXcFT0t2J1',
            'Origin': '' + '',
            'Content-Length': '145',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundarylBKEzelXcFT0t2J1\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress\r\n------WebKitFormBoundarylBKEzelXcFT0t2J1--\r\n'''

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXpAsAscFByUj5euc',
            'Origin': '' + '',
            'Content-Length': '146',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryXpAsAscFByUj5euc\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.\r\n------WebKitFormBoundaryXpAsAscFByUj5euc--\r\n'''

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySdlYwIBiLfiCPZaW',
            'Origin': '' + '',
            'Content-Length': '150',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundarySdlYwIBiLfiCPZaW\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.test\r\n------WebKitFormBoundarySdlYwIBiLfiCPZaW--\r\n'''

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryqYUZ45potp1dih7b',
            'Origin': '' + '',
            'Content-Length': '152',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = '''------WebKitFormBoundaryqYUZ45potp1dih7b\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester\r\n------WebKitFormBoundaryqYUZ45potp1dih7b--\r\n'''

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
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryqqiFbgRdmdlC3X0N',
            'Origin': '' + '',
            'Content-Length': '153',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/login/',
            'Connection': 'keep-alive',
        }

        data = f'------WebKitFormBoundaryqqiFbgRdmdlC3X0N\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryqqiFbgRdmdlC3X0N--\r\n'
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str
        )

    @task()
    def task_000017_GET_dataserver2_logon_nti_password(self):
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
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
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
            name=url
        )

    @task()
    def task_000020_GET_loginsuccess(self):
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
    def task_000021_GET_app(self):
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

    @task()
    def task_000024_GET_app_resources_strings_strings_js(self):
        url = '' + '/app/resources/strings/strings.js'
        
        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000025_GET_content_sites_alpha_nextthought_com_ContentPackageBundles_Alpha_presentation_assets_webapp_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/ContentPackageBundles/Alpha/presentation-assets/webapp/contentpackage-landing-232x170.png'
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
    #         't': '0',
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
    # def task_000027_GET_content_sites_alpha_nextthought_com_ContentPackageBundles_NextThoughtFAQ_RPN_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/ContentPackageBundles/NextThoughtFAQ-RPN/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
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
    #         't': '1507568586',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000030_GET_app_js_version(self):
        url = '' + '/app/js/version'
        
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Accept-Language': 'en-us',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000031_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    def task_000032_POST_dataserver2_logon_handshake(self):
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
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    def task_000033_GET_dataserver2_logon_ping(self):
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
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000035_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryUNcuJ1T8RI5AXS47',
            'Origin': '' + '',
            'Content-Length': '153',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Connection': 'keep-alive',
        }

        data = f'------WebKitFormBoundaryUNcuJ1T8RI5AXS47\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryUNcuJ1T8RI5AXS47--\r\n'
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000036_GET_dataserver2_service(self):
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
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000038_GET_dataserver2_users_stress_tester1(self):
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
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name = '/dataserver2/users/stress.tester{self.user_id}'
        )

    # @task()
    # def task_000039_GET_dataserver2_users_stress_tester1_FriendsLists(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
    #     )
    #
    # @task()
    # def task_000040_GET_socket_io_1(self):
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
    #         't': '1595266013214',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000041_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}'
        )

    # @task()
    # def task_000042_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_WebApp(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}%2B%2Bpreferences%2B%2B/WebApp'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    #         name='/dataserver2/users/stress.tester{self.user_id}%2B%2Bpreferences%2B%2B/WebApp'
    #     )
    #
    # @task()
    # def task_000043_GET_socket_io_1_websocket_0x469cfc32ad6e40a3(self):
    #     url = '' + '/socket.io/1/websocket/0x469cfc32ad6e40a3'
    #
    #     headers = {
    #         'Upgrade': 'websocket',
    #         'Connection': 'Upgrade',
    #         'Origin': '' + '',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'Sec-WebSocket-Key': 'yTkPpQ2V/+Hbo8YShFbNyQ==',
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
    # def task_000044_GET_site_assets_shared_strings_en_json(self):
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

    # @task()
    # def task_000045_GET_dataserver2_users_stress_tester1_FriendsLists(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Referer': '' + '/app/',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
    #     )

    # @task()
    # def task_000046_GET_dataserver2_users_stress_tester1_Groups(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Groups'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Referer': '' + '/app/',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/Groups'
    #     )

    @task()
    def task_000047_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
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
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000048_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Favorites(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
    #     )

    # @task()
    # def task_000049_GET_dataserver2_users_stress_tester1_ContentBundles_VisibleContentBundles(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
    #     )

    # @task()
    # def task_000050_GET_dataserver2_users_stress_tester1_Communities_Communities(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
    #     )

    # @task()
    # def task_000051_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'batchSize': '1',
    #         'notAfter': '1595307599.084',
    #         'notBefore': '1595266014.084',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #         name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
    #     )

    @task()
    def task_000052_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000053_GET_dataserver2_users_stress_tester1_Communities_AdministeredCommunities(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
    #     )
    #
    # @task()
    # def task_000054_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    #         name='/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
    #     )
    #
    # @task()
    # def task_000055_GET_dataserver2_users_stress_tester1_Courses_AdministeredCourses_40_40Favorites(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
    #     )
    #
    # @task()
    # def task_000056_GET_content_sites_alpha_nextthought_com_Courses_DefaultAPICreated_QAAUTO_1521661598323_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/Courses/DefaultAPICreated/QAAUTO-1521661598323/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
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
    #         't': '1522097161',
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
    # def task_000057_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    #         name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
    #     )
    #
    # @task()
    # def task_000058_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
    #     url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    #         name='/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
    #
    #     )
    #
    # @task()
    # def task_000060_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Asite_admin_alpha_OID_0x118f1cc7_3A5573657273_3Ayt1TD1Sqtmf(self):
    #     url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Asite.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'type': '',
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
    # def task_000063_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_40_40UserCoursePreferredAccess(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/%40%40UserCoursePreferredAccess'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
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
    # def task_000064_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/contents'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
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
    # def task_000065_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_40_40AssignmentSummaryByOutlineNode(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/%40%40AssignmentSummaryByOutlineNode'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000066_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
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
    # def task_000067_HEAD_content_sites_alpha_nextthought_com_Courses_DefaultAPICreated_QAAUTO_1589485885660_presentation_assets_webapp_v1_vendoroverrideicon_png(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/Courses/DefaultAPICreated/QAAUTO-1589485885660/presentation-assets/webapp/v1/vendoroverrideicon.png'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #     }
    #
    #     params = {
    #         't': '1592320897',
    #     }
    #
    #     self.response = self.client.request(
    #         method='HEAD',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    # @task()
    # def task_000068_HEAD_content_sites_alpha_nextthought_com_Courses_DefaultAPICreated_QAAUTO_1589485885660_presentation_assets_webapp_v1_background_png(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/Courses/DefaultAPICreated/QAAUTO-1589485885660/presentation-assets/webapp/v1/background.png'
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
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #     }
    #
    #     params = {
    #         't': '1592320897',
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
    # def task_000069_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000070_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_40_40UserCoursePreferredAccess(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/%40%40UserCoursePreferredAccess'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000071_GET_app_resources_images_elements_spinning_logo_png(self):
    #     url = '' + '/app/resources/images/elements/spinning_logo.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000072_GET_content_sites_alpha_nextthought_com_Courses_DefaultAPICreated_QAAUTO_1589485885660_presentation_assets_webapp_v1_background_png(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/Courses/DefaultAPICreated/QAAUTO-1589485885660/presentation-assets/webapp/v1/background.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         't': '1592320897',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000073_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_285410572809419328_4744453595198602974_AssignmentHistories_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-285410572809419328_4744453595198602974/AssignmentHistories/stress.tester{self.user_id}'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-285410572809419328_4744453595198602974/AssignmentHistories/stress.tester{self.user_id}'
        )

    # @task()
    # def task_000074_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000075_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_40_40CourseCatalogFamilies(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/%40%40CourseCatalogFamilies'
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
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000076_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_CourseTabPreferences(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/CourseTabPreferences'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000077_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000078_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0_site_admin_alpha_4744453596247220212_0_40_40overview_content(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0_site_admin_alpha_4744453596247220212_0/%40%40overview-content'
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
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000079_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000080_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0_site_admin_alpha_4744453596247220212_0_40_40overview_summary(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-285410572809419328_4744453595198602974_site_admin_alpha_4744453596212420051_0_site_admin_alpha_4744453596247220212_0/%40%40overview-summary'
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
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     params = {
    #         'accept': 'application/vnd.nextthought.note',
    #         'filter': 'TopLevel',
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
    # def task_000082_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aunknown_OID_0x1190a4c0_3A5573657273_3ANCH2fKzzbNn(self):
    #     url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aunknown-OID-0x1190a4c0%3A5573657273%3ANCH2fKzzbNn'
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
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    # def task_000083_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aunknown_OID_0x121a9832_3A5573657273_3Aj2MX84t5ut7(self):
    #     url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aunknown-OID-0x121a9832%3A5573657273%3Aj2MX84t5ut7'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000084_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aunknown_OID_0x12cc89af_3A5573657273_3Ar61xgMGRAmN(self):
    #     url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aunknown-OID-0x12cc89af%3A5573657273%3Ar61xgMGRAmN'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000086_GET_dataserver2_cf_io_vuczCBruEyq_blob_16_53_52_1(self):
    #     url = '' + '/dataserver2/cf.io/vuczCBruEyq/blob.16.53.52.1'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000087_GET_dataserver2_cf_io_y57dcJ1T0p6_blob(self):
    #     url = '' + '/dataserver2/cf.io/y57dcJ1T0p6/blob'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000088_GET_app_resources_images_f41d087bc927db9186958dd8b6cbac66_png(self):
    #     url = '' + '/app/resources/images/f41d087bc927db9186958dd8b6cbac66.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000089_GET_app_resources_images_038450b97daf7fc972276c3e04610153_png(self):
    #     url = '' + '/app/resources/images/038450b97daf7fc972276c3e04610153.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
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
    # def task_000090_GET_app_resources_images_b4d2739df987c59e9bda7e5cd517949b_png(self):
    #     url = '' + '/app/resources/images/b4d2739df987c59e9bda7e5cd517949b.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000092_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Completion_CompletedItems_users_stress_tester1(self):
    #     url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Completion/CompletedItems/users/stress.tester{self.user_id}'
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
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Completion/CompletedItems/users/stress.tester{self.user_id}'
    #     )

    @task()
    def task_000093_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744458708117747583_2340402359(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744458708117747583_2340402359'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000094_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000095_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453605595589116_2053085062(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453605595589116_2053085062'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000096_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_webinars_3100755134455669260(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/webinars/3100755134455669260'
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
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000097_GET_app_api_videos_youtube(self):
    #     url = '' + '/app/api/videos/youtube'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         'id': 'dt5g5_1cKVk',
    #         'part': 'contentDetails,snippet,statistics',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    # @task()
    # def task_000098_GET_app_api_videos_youtube(self):
    #     url = '' + '/app/api/videos/youtube'
    #
    #     headers = {
    #         'Accept': '*/*',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     params = {
    #         'id': 'ryx1CKskau8',
    #         'part': 'contentDetails,snippet,statistics',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    # @task()
    # def task_000099_GET_app_resources_images_42ea90a441b4cdc8493a4ebd8593a56b_png(self):
    #     url = '' + '/app/resources/images/42ea90a441b4cdc8493a4ebd8593a56b.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000100_GET_app_resources_images_900da250fbe95b256565a7ab472b6de6_png(self):
    #     url = '' + '/app/resources/images/900da250fbe95b256565a7ab472b6de6.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000101_GET_app_resources_images_93a65098f08d99ae88aff545e381105c_png(self):
    #     url = '' + '/app/resources/images/93a65098f08d99ae88aff545e381105c.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000104_GET_app_resources_images_23e86814c81448b7d2c36a160b7f25c7_svg(self):
    #     url = '' + '/app/resources/images/23e86814c81448b7d2c36a160b7f25c7.svg'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
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
    # def task_000106_GET_dataserver2_cf_io_arUfAzfczh9_osdebg_jpg(self):
    #     url = '' + '/dataserver2/cf.io/arUfAzfczh9/osdebg.jpg'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
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
    # def task_000108_GET_dataserver2_cf_io_m7fbX6PStwh_sample_jpg(self):
    #     url = '' + '/dataserver2/cf.io/m7fbX6PStwh/sample.jpg'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000110_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_webinars_3100755134455669260(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/webinars/3100755134455669260'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000111_GET_dataserver2_cf_io_arUfAzfczhF_test_png_png(self):
    #     url = '' + '/dataserver2/cf.io/arUfAzfczhF/test_png.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000112_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Outline_contents(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Outline/contents'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-us',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
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
    def task_000114_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_40_40AssignmentSummaryByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/%40%40AssignmentSummaryByOutlineNode'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000115_GET_dataserver2_cf_io_eZHypS4hYj4_sample_image_jpg(self):
    #     url = '' + '/dataserver2/cf.io/eZHypS4hYj4/sample_image.jpg'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    # @task()
    # def task_000116_GET_app_resources_images_cea7d35e06a1a6ce53d32c1bf69ed73c_png(self):
    #     url = '' + '/app/resources/images/cea7d35e06a1a6ce53d32c1bf69ed73c.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000119_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:site.admin.alpha-OID-0x118f1cc7:5573657273:yt1TD1Sqtmf',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000121_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_285410572809419328_4744453595198602974_AssignmentHistories_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-285410572809419328_4744453595198602974/AssignmentHistories/stress.tester{self.user_id}'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-285410572809419328_4744453595198602974/AssignmentHistories/stress.tester{self.user_id}'
        )

    @task()
    def task_000122_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/vnd.nextthought.pageinfo+json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:site.admin.alpha-OID-0x118f1cc7:5573657273:yt1TD1Sqtmf',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000123_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        params = {
            'type': '',
            'course': 'tag:nextthought.com,2011-10:site.admin.alpha-OID-0x118f1cc7:5573657273:yt1TD1Sqtmf',
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
    def task_000124_POST_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_40_40Commence(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/@@Commence'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'Origin': '' + '',
            'Content-Length': '0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Connection': 'keep-alive',
        }

        data = {'version': self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/%40%40Commence'
        )

    # @task()
    # def task_000125_GET_app_resources_images_8982edf3b26c6e0e50972121db74da1a_png(self):
    #     url = '' + '/app/resources/images/8982edf3b26c6e0e50972121db74da1a.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
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
    # def task_000126_GET_app_resources_images_28c1ffce03b65d9f19f7a008e3628c5c_png(self):
    #     url = '' + '/app/resources/images/28c1ffce03b65d9f19f7a008e3628c5c.png'
    #
    #     headers = {
    #         'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    #         'Connection': 'keep-alive',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Accept-Language': 'en-us',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000127_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        )

    @task()
    def task_000128_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000129_GET_content_sites_alpha_nextthought_com_authored_ds2_alpha_3362141176211398366_0AA76D41887901DC0FD7_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/_authored_ds2.alpha_3362141176211398366.0AA76D41887901DC0FD7/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1589490653',
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
    # def task_000130_GET_content_sites_alpha_nextthought_com_authored_ds1_alpha_3892070235549704722_84C6B30E7FC6D005B11E_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/_authored_ds1.alpha_3892070235549704722.84C6B30E7FC6D005B11E/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1591043040',
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
    # def task_000131_GET_content_sites_alpha_nextthought_com_authored_ds2_alpha_214204222507076197_1B6EF77135BED7094612_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/_authored_ds2.alpha_214204222507076197.1B6EF77135BED7094612/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1589491214',
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
    # def task_000132_GET_content_sites_alpha_nextthought_com_authored_ds1_alpha_4225957961008038870_98EE4E5A7218242FAE59_eclipse_toc_xml(self):
    #     url = '' + '/content/sites/alpha.nextthought.com/_authored_ds1.alpha_4225957961008038870.98EE4E5A7218242FAE59/eclipse-toc.xml'
    #
    #     headers = {
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'Connection': 'keep-alive',
    #         'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
    #         'Accept': 'application/json',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    #         'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
    #         'Accept-Language': 'en-us',
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }
    #
    #     params = {
    #         'dc': '1593716453',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )
    #
    @task()
    def task_000133_POST_dataserver2_analytics_batch_events(self):
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
            'Content-Length': '614',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.assignmentviewevent",
                           "context_path":["tag:nextthought.com,2011-10:site.admin.alpha-OID-0x118f1cc7:5573657273:yt1TD1Sqtmf"],
                           "RootContextID":"tag:nextthought.com,2011-10:site.admin.alpha-OID-0x118f1cc7:5573657273:yt1TD1Sqtmf",
                           "timestamp":1595266027.085,"user":f"stress.tester{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054",
                           "Duration":0,"ContentId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054"}]}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000135_POST_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Content-Length': '1897',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission",
                          "NTIID":None,"tags":[],
                          "questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-questionset_system_4744453599499416785_1789052273",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":2,"ContainerId":""}],"CreatorRecordedEffortDuration":2,"version":self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        )

    @task()
    def task_000137_POST_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Content-Length': '1894',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":None,
                          "tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-questionset_system_4744453599499416785_1789052273",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "parts":[1],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":4,"ContainerId":""}],"CreatorRecordedEffortDuration":4,"version":self.version}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        )

    @task()
    def task_000138_POST_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Content-Length': '1891',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":None,
                          "tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-questionset_system_4744453599499416785_1789052273",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "parts":[1],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "parts":[None],"CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":7,"ContainerId":""}],"CreatorRecordedEffortDuration":7,"version":self.version}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        )

    @task()
    def task_000139_POST_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentSavepoints_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_Savepoint(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Content-Length': '1888',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission",
                          "NTIID":None,"tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-questionset_system_4744453599499416785_1789052273",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "parts":[1],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,"ContainerId":""}],
                          "CreatorRecordedEffortDuration":9,"ContainerId":""}],"CreatorRecordedEffortDuration":9,"version":self.version}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentSavepoints/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/Savepoint'
        )

    @task()
    def task_000140_POST_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/vnd.nextthought.assessment.assignmentsubmission+json',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Content-Length': '2310',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.assessment.assignmentsubmission",
                "tags":[],"assignmentId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054",
                "parts":[{"MimeType":"application/vnd.nextthought.assessment.questionsetsubmission","NTIID":None,
                          "tags":[],"questionSetId":"tag:nextthought.com,2011-10:NTI-NAQ-questionset_system_4744453599499416785_1789052273",
                          "questions":[{"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599499303988_1789052273",
                                        "parts":[1],"CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599713389879_2364452265",
                                        "parts":[2],"CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453599925774510_2990125323",
                                        "parts":[1],"CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054"},
                                       {"MimeType":"application/vnd.nextthought.assessment.questionsubmission",
                                        "NTIID":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "tags":[],"questionId":"tag:nextthought.com,2011-10:NTI-NAQ-question_system_4744453600138204948_168356570",
                                        "parts":[1],"CreatorRecordedEffortDuration":None,
                                        "ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054"}],
                          "CreatorRecordedEffortDuration":10,"ContainerId":"tag:nextthought.com,2011-10:NTI-NAQ-assignment_system_4744453599329600317_2527767054"}],
                "CreatorRecordedEffortDuration":10,"version":self.version}

        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000141_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_UsersCourseAssignmentHistoryItem(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/UsersCourseAssignmentHistoryItem'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/UsersCourseAssignmentHistoryItem'
        )

    @task()
    def task_000142_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x1309cf15_3A5573657273_3AjfHHgPyN9yE(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x1309cf15%3A5573657273%3AjfHHgPyN9yE'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x1309cf15%3A5573657273%3AjfHHgPyN9yE'
        )

    @task()
    def task_000143_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentHistories_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentHistories/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        )

    @task()
    def task_000144_GET_dataserver2_users_stress_tester1_Objects_tag_3Anextthought_com_2C2011_10_3Astress_tester1_OID_0x1309cf14_3A5573657273_3AjfHHgPyN9yF(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x1309cf14%3A5573657273%3AjfHHgPyN9yF'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/users/stress.tester{self.user_id}/Objects/tag%3Anextthought.com%2C2011-10%3Astress.tester{self.user_id}-OID-0x1309cf14%3A5573657273%3AjfHHgPyN9yF'
        )

    @task()
    def task_000145_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-us',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000146_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_AssignmentAttemptMetadata_stress_tester1_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054_UsersCourseAssignmentAttemptMetadataItem_40_40Assignment(self):
        url = f'/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Language': 'en-us',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            name='/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/AssignmentAttemptMetadata/stress.tester{self.user_id}/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054/UsersCourseAssignmentAttemptMetadataItem/%40%40Assignment'
        )

    @task()
    def task_000147_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000148_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_assignment_system_4744453599329600317_2527767054(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-assignment_system_4744453599329600317_2527767054'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000149_GET_dataserver2_2B_2Betc_2B_2Bhostsites_alpha_nextthought_com_2B_2Betc_2B_2Bsite_Courses_DefaultAPICreated_QAAUTO_1589485885660_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/alpha.nextthought.com/%2B%2Betc%2B%2Bsite/Courses/DefaultAPICreated/QAAUTO-1589485885660/CourseCatalogEntry'
        
        headers = {
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-TZOffset': '-300',
            'Accept': 'application/json',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000150_GET_app_resources_images_20fb7a0d2fe9625be2cbe04443284d1b_svg(self):
        url = '' + '/app/resources/images/20fb7a0d2fe9625be2cbe04443284d1b.svg'
        
        headers = {
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000151_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'X-NTI-Client-App': '@nti/web-app',
            'Connection': 'keep-alive',
            'X-NTI-Client-Version': '2020.8.0-alpha.20200717170026',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
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
    def task_000152_GET_dataserver2_logon_logout(self):
        url = '' + '/dataserver2/logon.logout'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
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
    def task_000153_GET_login(self):
        url = '' + '/login'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000155_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': '' + '/app/course/site.admin.alpha-OID-0x118f1cc7%3A5573657273%3Ayt1TD1Sqtmf/assignments/NTI-NAQ-assignment_system_4744453599329600317_2527767054/',
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
    def task_000156_GET_dataserver2_logon_ping(self):
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
            'X-NTI-Client-Version': '2020.7.0-alpha.20200711004229',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


class WebsiteUser(HttpUser):
    tasks = [AssignmentSubmission]
    wait_time = between(2, 9)

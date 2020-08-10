# -*- coding: UTF-8 -*-
import json
from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import uuid

class UserCreation(SequentialTaskSet):
    ts = None

    def on_start(self):
        self.ts = str(uuid.uuid4())

    @task()
    def task_000004_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '57',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.locus15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = '''{"realname":"postgres","opt_in_email_communication":null}'''

        response = self.client.post(
            url=url,
            headers=headers,
            data=data,
        )
        if response.status_code == 422:
            print('failure found!')

    ### Additional tasks can go here ###
    @task()
    def task_000005_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'
        
        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '64',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres tester", "opt_in_email_communication":None}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000006_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '64',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres tester{self.ts}", "opt_in_email_communication":None}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000007_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '65',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres tester{self.ts}", "opt_in_email_communication":None}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000012_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '111',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres test{self.ts}",
                "email": f"julie.zhu+{self.ts}@nextthought.com",
                "opt_in_email_communication":None}
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000015_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '140',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres test{self.ts}",
                "email": f"julie.zhu+{self.ts}@nextthought.com",
                "Username": f"postgres.tester{self.ts}",
                "opt_in_email_communication":None
                }
        data_str = json.dumps(data)

        # data = '''{"realname":"postgres tester1","email":"julie.zhu+postgres1@nextthought.com","Username":"postgres.tester","opt_in_email_communication":null}'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000016_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '141',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres test{self.ts}",
                "email": f"julie.zhu+{self.ts}@nextthought.com",
                "Username": f"postgres.tester{self.ts}",
                "opt_in_email_communication":None
                }
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000017_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '162',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres test{self.ts}",
                "email": f"julie.zhu+{self.ts}@nextthought.com",
                "Username": f"postgres.tester{self.ts}",
                "opt_in_email_communication":None,
                "password": "temp001"
                }
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000018_POST_dataserver2_account_preflight_create(self):
        url = '' + '/dataserver2/account.preflight.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '162',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres test{self.ts}",
                "email": f"julie.zhu+{self.ts}@nextthought.com",
                "Username": f"postgres.tester{self.ts}",
                "opt_in_email_communication":None,
                "password": "temp001"
                }
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000020_POST_dataserver2_account_create(self):
        url = '' + '/dataserver2/account.create'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '162',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = {"realname":f"postgres test{self.ts}",
                "email": f"julie.zhu+{self.ts}@nextthought.com",
                "Username": f"postgres.tester{self.ts}",
                "opt_in_email_communication":None,
                "password": "temp001"
                }
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000023_GET_dataserver2_logon_ping(self):
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
            'Referer': '' + '/login/signup',
            'X-NTI-Client-Version': '2020.6.2',
            'Connection': 'keep-alive',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000024_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-login',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarytKfEZAZT3ts8migC',
            'Origin': '' + '',
            'Content-Length': '155',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.6.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/login/signup',
            'Connection': 'keep-alive',
        }

        data = '------WebKitFormBoundarytKfEZAZT3ts8migC\r\nContent-Disposition: form-data; name="username"\r\n\r\npostgres.tester%s\r\n------WebKitFormBoundarytKfEZAZT3ts8migC--\r\n' % self.ts
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    # @task()
    # def task_000025_DELETE_dataserver2_users_postgres_tester1_40_40NamedLinks_content_initial_tos_page(self):
    #     url = f'/dataserver2/users/postgres.tester{self.ts}/%40%40NamedLinks/content.initial_tos_page'
    #
    #     headers = {
    #         'X-NTI-Client-App': '@nti/web-login',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'Accept-Language': 'en-us',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'Accept': 'application/json',
    #         'Origin': '' + '',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    #         'X-NTI-Client-Version': '2020.6.2',
    #         'Referer': '' + '/login/signup',
    #         'Content-Length': '0',
    #         'Connection': 'keep-alive',
    #     }
    #
    #     self.response = self.client.request(
    #         method='DELETE',
    #         url=url,
    #         headers=headers,
    #     )

    @task()
    def task_000026_GET_loginsuccess(self):
        url = '' + '/loginsuccess'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/login/signup',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000027_GET_app(self):
        url = '' + '/app'

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Accept-Language': 'en-us',
            'Referer': '' + '/login/signup',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000028_GET_app_resources_strings_strings_js(self):
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
    def task_000032_GET_app_js_version(self):
        url = '' + '/app/js/version'

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache',
            'Accept-Language': 'en-us',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Connection': 'keep-alive',
            'Referer': '' + '/app/',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000033_GET_dataserver2_logon_ping(self):
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
    def task_000034_POST_dataserver2_logon_handshake(self):
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
            'Content-Length': '25',
            'Connection': 'keep-alive',
        }

        data = f'username=postgres.tester{self.ts}'
        data_str = json.dumps(data)

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000036_GET_dataserver2_logon_ping(self):
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
    def task_000037_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryiuGdOMUfgvsLcGtE',
            'Origin': '' + '',
            'Content-Length': '155',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Connection': 'keep-alive',
        }

        data = '------WebKitFormBoundaryiuGdOMUfgvsLcGtE\r\nContent-Disposition: form-data; name="username"\r\n\r\npostgres.tester%s\r\n------WebKitFormBoundaryiuGdOMUfgvsLcGtE--\r\n' % self.ts
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000038_GET_dataserver2_service(self):
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
    def task_000039_GET_dataserver2_users_postgres_tester1(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}'

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

        self.response = self.client.get(
          url, name="/dataserver2/users/postgres.tester{self.ts}"
        )

    @task()
    def task_000040_GET_dataserver2_users_postgres_tester1_FriendsLists(self):
        url =  f'/dataserver2/users/postgres.tester{self.ts}/FriendsLists'

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
            name="/dataserver2/users/postgres.tester{self.ts}/FriendsLists"
        )

    @task()
    def task_000041_POST_dataserver2_users_postgres_tester1_FriendsLists(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/FriendsLists'

        headers = {
            'Accept': 'application/json',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'X-NTI-Client-TZOffset': '-300',
            'Accept-Language': 'en-us',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'Origin': '' + '',
            'Content-Length': '155',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'X-NTI-Client-Version': '2020.7.1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': '' + '/app/',
            'Connection': 'keep-alive',
        }

        data = {"MimeType":"application/vnd.nextthought.friendslist","Username":f"mycontacts-postgres.tester{self.ts}","alias":"My Contacts","friends":[],"IsDynamicSharing":False}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name="/dataserver2/users/postgres.tester{self.ts}/FriendsLists"
        )

    # @task()
    # def task_000042_GET_socket_io_1(self):
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
    #         't': '1594918822385',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000043_GET_dataserver2_users_postgres_tester1(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}'

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
            name="/dataserver2/users/postgres.tester{self.ts}"
        )

    @task()
    def task_000044_GET_dataserver2_users_postgres_tester1_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/%2B%2Bpreferences%2B%2B/WebApp'

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
            name='/dataserver2/users/postgres.tester{self.ts}/%2B%2Bpreferences%2B%2B/WebApp'
        )

    # @task()
    # def task_000045_GET_socket_io_1_websocket_0x60071a6cfc791f6e(self):
    #     url = '' + '/socket.io/1/websocket/0x60071a6cfc791f6e'
    #
    #     headers = {
    #         'Upgrade': 'websocket',
    #         'Connection': 'Upgrade',
    #         'Origin': '' + '',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'Sec-WebSocket-Key': 'rrhGOOG3QSZ5r4xzRCAKew==',
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
    def task_000046_GET_site_assets_shared_strings_en_json(self):
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
    def task_000047_GET_dataserver2_users_postgres_tester1_Groups(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Groups'

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
            name='/dataserver2/users/postgres.tester{self.ts}/Groups'
        )

    @task()
    def task_000048_GET_dataserver2_users_postgres_tester1_FriendsLists(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/FriendsLists'

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
            name='/dataserver2/users/postgres.tester{self.ts}/FriendsLists'
        )

    @task()
    def task_000049_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
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
    def task_000050_GET_dataserver2_users_postgres_tester1_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'

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
            name='/dataserver2/users/postgres.tester{self.ts}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        )

    @task()
    def task_000051_GET_dataserver2_users_postgres_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'

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
            name='/dataserver2/users/postgres.tester{self.ts}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        )

    @task()
    def task_000052_GET_dataserver2_users_postgres_tester1_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Courses/EnrolledCourses/%40%40Favorites'

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
            name="/dataserver2/users/postgres.tester{self.ts}/Courses/EnrolledCourses/%40%40Favorites"
        )

    @task()
    def task_000053_GET_dataserver2_users_postgres_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Calendars/%40%40events'

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
            'notAfter': '1594961999.231',
            'notBefore': '1594918823.231',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/postgres.tester{self.ts}/Calendars/%40%40events'
        )

    @task()
    def task_000054_GET_dataserver2_users_postgres_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'

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
            name='/dataserver2/users/postgres.tester{self.ts}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        )

    @task()
    def task_000055_GET_dataserver2_users_postgres_tester1_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Courses/AdministeredCourses/%40%40Favorites'

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
            name='/dataserver2/users/postgres.tester{self.ts}/Courses/AdministeredCourses/%40%40Favorites'
        )

    @task()
    def task_000056_GET_dataserver2_users_postgres_tester1_Communities_Communities(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Communities/Communities'

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
            name='/dataserver2/users/postgres.tester{self.ts}/Communities/Communities'
        )

    @task()
    def task_000057_GET_dataserver2_users_postgres_tester1_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/ContentBundles/VisibleContentBundles'

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
            name='/dataserver2/users/postgres.tester{self.ts}/ContentBundles/VisibleContentBundles'
        )

    @task()
    def task_000058_GET_dataserver2_users_postgres_tester1_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/Communities/AdministeredCommunities'

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
            name='/dataserver2/users/postgres.tester{self.ts}/Communities/AdministeredCommunities'
        )

    @task()
    def task_000061_GET_dataserver2_users_postgres_tester1_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/postgres.tester{self.ts}/%2B%2Bpreferences%2B%2B/ChatPresence'

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
            name='/dataserver2/users/postgres.tester{self.ts}/%2B%2Bpreferences%2B%2B/ChatPresence'
        )


class WebsiteUser(HttpUser):
    tasks = [UserCreation]
    wait_time = between(5, 9)

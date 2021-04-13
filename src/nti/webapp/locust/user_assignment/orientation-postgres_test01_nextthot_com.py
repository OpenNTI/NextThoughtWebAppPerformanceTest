# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import urllib.parse
from random import randrange
from random import sample
import time

USER_CREDENTIALS = list(range(1, 1101))

class UserBehavior(SequentialTaskSet):
    user_id = 0

    def on_start(self):
        index_val = USER_CREDENTIALS.pop()
        self.user_id = f'stress.tester{index_val}'
        print(f'starting {self.user_id}')

    @task()
    def task_000001_GET_dataserver2_logon_nti_password(self):
        url = '' + '/dataserver2/logon.nti.password'
        sval = f"{self.user_id}:temp001"
        password = base64.b64encode(sval.encode('utf-8')).decode('utf-8')
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'Authorization': f"Basic {password}",
            'accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-NTI-Client-Version': '2021.6.0',
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
            'username': self.user_id,
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    ### Additional tasks can go here ###
    @task()
    def task_000002_GET_loginsuccess(self):
        url = '' + '/loginsuccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
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
    def task_000003_GET_app(self):
        url = '' + '/app'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
    def task_000004_GET_app_resources_strings_strings_js(self):
        url = '' + '/app/resources/strings/strings.js'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
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
    def task_000007_GET_app_resources_257_0b9aebba418f222d3aef_css_map(self):
        url = '' + '/app/resources/257-0b9aebba418f222d3aef.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000008_GET_app_resources_593_4898835c1c8213c0f26e_css_map(self):
        url = '' + '/app/resources/593-4898835c1c8213c0f26e.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000009_GET_app_resources_index_5616c68a_bab3deb0a81826b351c0_css_map(self):
        url = '' + '/app/resources/index-5616c68a-bab3deb0a81826b351c0.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000010_GET_app_resources_index_7cc21f2e_4db7bcbc4885170a5d9e_css_map(self):
        url = '' + '/app/resources/index-7cc21f2e-4db7bcbc4885170a5d9e.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000011_GET_app_resources_392_de5adb513927e9d73166_css_map(self):
        url = '' + '/app/resources/392-de5adb513927e9d73166.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000012_GET_app_resources_990_f6c2317677240019d538_css_map(self):
        url = '' + '/app/resources/990-f6c2317677240019d538.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000013_GET_app_resources_259_04dd2eb75858d10b9759_css_map(self):
        url = '' + '/app/resources/259-04dd2eb75858d10b9759.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000014_GET_app_resources_362_42c7ad94a64cc113907a_css_map(self):
        url = '' + '/app/resources/362-42c7ad94a64cc113907a.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000015_GET_app_resources_index_85d703ae_368561d071ecc39680ae_css_map(self):
        url = '' + '/app/resources/index-85d703ae-368561d071ecc39680ae.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000016_GET_app_resources_368_8cb546e317e247390cc4_css_map(self):
        url = '' + '/app/resources/368-8cb546e317e247390cc4.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000017_GET_app_resources_119_aaca253bf377b8189428_css_map(self):
        url = '' + '/app/resources/119-aaca253bf377b8189428.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000018_GET_app_resources_172_ea4022a11e6cdf02915e_css_map(self):
        url = '' + '/app/resources/172-ea4022a11e6cdf02915e.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000019_GET_app_resources_912_845a648f410d03e627ce_css_map(self):
        url = '' + '/app/resources/912-845a648f410d03e627ce.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000020_GET_app_resources_index_725566d1_5938ac3d7855ddd452fb_css_map(self):
        url = '' + '/app/resources/index-725566d1-5938ac3d7855ddd452fb.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000021_GET_app_resources_917_1dfa58688bb217505cc4_css_map(self):
        url = '' + '/app/resources/917-1dfa58688bb217505cc4.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000022_GET_app_resources_505_70aa56ff0f30495a1d8c_css_map(self):
        url = '' + '/app/resources/505-70aa56ff0f30495a1d8c.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000023_GET_app_resources_461_42a54af044e82aedb669_css_map(self):
        url = '' + '/app/resources/461-42a54af044e82aedb669.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000024_GET_app_resources_index_c0d25d36_33fe6c9d0871a62fd184_css_map(self):
        url = '' + '/app/resources/index-c0d25d36-33fe6c9d0871a62fd184.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000025_GET_app_resources_index_cb8cd673_11f289c080edc25e4b1d_css_map(self):
        url = '' + '/app/resources/index-cb8cd673-11f289c080edc25e4b1d.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000026_GET_app_resources_index_aec23333_655f19207cc10f8e9761_css_map(self):
        url = '' + '/app/resources/index-aec23333-655f19207cc10f8e9761.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000027_GET_app_resources_341_45982afdb45f7cfe648a_css_map(self):
        url = '' + '/app/resources/341-45982afdb45f7cfe648a.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000029_GET_app_resources_822_10349e7a4b7e3cec765b_css_map(self):
        url = '' + '/app/resources/822-10349e7a4b7e3cec765b.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000060_GET_app_js_version(self):
        url = '' + '/app/js/version'
        
        headers = {
            'Connection': 'keep-alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
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
    def task_000061_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
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
    def task_000067_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''username=stress.tester2'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000079_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e35f1e65aaa5472c9962e1e73990d3e1-a8b8eaf5f42b5f60-0',
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
    def task_000086_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarya4bFSg8B6E1SZ6aT',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
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

        data = '''------WebKitFormBoundarya4bFSg8B6E1SZ6aT\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester2\r\n------WebKitFormBoundarya4bFSg8B6E1SZ6aT--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000088_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'
        
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
    def task_000089_GET_dataserver2_users_stress_tester2(self):
        url = '' + '/dataserver2/users/stress.tester2'
        
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
    def task_000091_GET_socket_io_1(self):
        url = '' + '/socket.io/1'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1618248657923',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000092_GET_dataserver2_users_stress_tester2(self):
        url = '' + f'/dataserver2/users/{self.user_id}'
        
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
            'Referer': '' + '/app/',
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
    def task_000094_GET_socket_io_1_websocket_0x4baf4d257ff4e651(self):
        url = '' + '/socket.io/1/websocket/0x4baf4d257ff4e651'
        
        headers = {
            'Connection': 'Upgrade',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Upgrade': 'websocket',
            'Origin': '' + '',
            'Sec-WebSocket-Version': '13',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-WebSocket-Key': 'IdR+rLIJfRGZaIh8AUx77w==',
            'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000095_GET_dataserver2_users_stress_tester2_2B_2Bpreferences_2B_2B_WebApp(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
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
            'Referer': '' + '/app/',
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
    def task_000096_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
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
    def task_000097_GET_dataserver2_users_stress_tester2_FriendsLists(self):
        url = '' + f'/dataserver2/users/{self.user_id}/FriendsLists'
        
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
            'Referer': '' + '/app/',
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
    def task_000098_GET_dataserver2_users_stress_tester2_Groups(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Groups'
        
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
            'Referer': '' + '/app/',
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
    def task_000099_GET_dataserver2_users_stress_tester2_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
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
            'Referer': '' + '/app/',
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
    def task_000100_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
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
            'Referer': '' + '/app/',
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
        )

    @task()
    def task_000101_GET_dataserver2_users_stress_tester2_Calendars_40_40events(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
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
            'Referer': '' + '/app/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1618289999.71',
            'notBefore': '1618248658.71',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000102_GET_dataserver2_users_stress_tester2_Courses_EnrolledCourses_40_40Favorites(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
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
            'Referer': '' + '/app/',
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
    def task_000103_GET_dataserver2_users_stress_tester2_FriendsLists(self):
        url = '' + f'/dataserver2/users/{self.user_id}/FriendsLists'
        
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
            'Referer': '' + '/app/',
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
    def task_000104_GET_dataserver2_users_stress_tester2_ContentBundles_VisibleContentBundles(self):
        url = '' + f'/dataserver2/users/{self.user_id}/ContentBundles/VisibleContentBundles'
        
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
            'Referer': '' + '/app/',
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
    def task_000105_GET_dataserver2_users_stress_tester2_Communities_Communities(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Communities/Communities'
        
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
            'Referer': '' + '/app/',
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
    def task_000106_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
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
            'Referer': '' + '/app/',
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
    def task_000107_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
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
            'Referer': '' + '/app/',
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
    def task_000108_GET_dataserver2_users_stress_tester2_Communities_AdministeredCommunities(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Communities/AdministeredCommunities'
        
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
            'Referer': '' + '/app/',
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
    def task_000109_GET_dataserver2_users_stress_tester2_Courses_AdministeredCourses_40_40Favorites(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
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
            'Referer': '' + '/app/',
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
    def task_000119_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0xa88095_3A5573657273_3AucvfaTqmB9A(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': '65ecafde9b5a40c1ac43d442daeb4b5b-8146f54fd86f8a49-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000121_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000122_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40AssignmentSummaryByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40AssignmentSummaryByOutlineNode'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000123_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000124_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000125_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_ContentPackageBundle_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/ContentPackageBundle/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
        )

    @task()
    def task_000126_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_120_Orientation_presentation_assets_webapp_v1_vendoroverrideicon_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/120-Orientation/presentation-assets/webapp/v1/vendoroverrideicon.png'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1613229695',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000127_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '65ecafde9b5a40c1ac43d442daeb4b5b-bb763f6aee9ff5c6-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000128_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000129_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_CourseTabPreferences(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/CourseTabPreferences'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000130_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000131_GET_dataserver2_users_stress_tester2_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139_AssignmentHistories_stress_tester2(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139/AssignmentHistories/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000132_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000133_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-content'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000134_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000135_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-summary'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000136_GET_app_api_videos_youtube(self):
        url = '' + '/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
        )

    @task()
    def task_000137_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/',
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
    def task_000138_GET_app_resources_images_038450b97daf7fc972276c3e04610153_png(self):
        url = '' + '/app/resources/images/038450b97daf7fc972276c3e04610153.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/362-42c7ad94a64cc113907a.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000141_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000144_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-a9fc5931d310697e-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000145_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-84eefc3b433fad56-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000146_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-be4011dd75e5daf2-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000147_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-89cbbd83d11ba70b-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000148_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-828619ac64800c53-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000149_GET_app_resources_images_047ac8735d1f282989602045506031f3_svg(self):
        url = '' + '/app/resources/images/047ac8735d1f282989602045506031f3.svg'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/392-de5adb513927e9d73166.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000150_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40MediaByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40MediaByOutlineNode'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-bcb9bf3c1db07292-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000151_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIVideo_47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'f4280c6d7907458fb4415bbe5de6465d-8e28bcf903848c0a-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000152_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIVideo_47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079_29_RelevantContainedUserGeneratedData(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079%29/RelevantContainedUserGeneratedData'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
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
    def task_000153_GET_app_resources_images_4848550fb492cbd9ba46211316ee25e3_svg(self):
        url = '' + '/app/resources/images/4848550fb492cbd9ba46211316ee25e3.svg'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/368-8cb546e317e247390cc4.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000166_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '769',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248669.505,
                           "user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":
                               "media-modal","with_transcript":True,"video_start_time":0.01618,"MaxDuration":153.241,"PlaySpeed":1}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000172_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000185_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '773',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A","timestamp":1618248669.505,
                           "user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":9.885707,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":0.01618,"MaxDuration":153.241,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000186_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000190_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '780',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248681.596,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":"media-modal","with_transcript":True,
                           "video_start_time":29.981734143049948,"MaxDuration":153.241,"PlaySpeed":1}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000194_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000195_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '771',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248682.079,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":30.002051,"MaxDuration":153.241,"PlaySpeed":1}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000196_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000202_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '778',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248685.506,
                           "user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":49.4181686909582,"MaxDuration":153.241,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000206_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000208_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '771',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248686.153,
                           "user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":"media-modal","with_transcript":True,
                           "video_start_time":49.605134,"MaxDuration":153.241,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000210_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000214_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '3713',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248669.505,
                           "user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":11.88637,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":0.01618,"video_end_time":11.90255,
                           "MaxDuration":153.241,"PlaySpeed":1},
                          {"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248681.596,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":"media-modal","with_transcript":True,
                           "video_start_time":29.981734143049948,"video_end_time":29.981734143049948,
                           "MaxDuration":153.241,"PlaySpeed":1},
                          {"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248682.079,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":3.167131999999995,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":30.002051,"video_end_time":33.169183,
                           "MaxDuration":153.241,"PlaySpeed":1},
                          {"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248685.506,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":None,"player_configuration":"media-modal","with_transcript":True,
                           "video_start_time":49.4181686909582,"video_end_time":49.4181686909582,
                           "MaxDuration":153.241,"PlaySpeed":1},
                          {"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":
                              ["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                               "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248686.153,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":3.241315,"player_configuration":"media-modal","with_transcript":True,
                           "video_start_time":49.605134,"MaxDuration":153.241,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000216_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000224_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '785',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248686.153,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":13.240496999999998,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":49.605134,"MaxDuration":153.241,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000225_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/items/NTI-NTIVideoRef-system_20210213152141_726225_2441827711',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000234_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-98518693a9f87fce-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000237_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-afb01c6c50295a56-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000238_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-a44f0435e5d878a8-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000239_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000240_GET_app_resources_images_b4d2739df987c59e9bda7e5cd517949b_png(self):
        url = '' + '/app/resources/images/b4d2739df987c59e9bda7e5cd517949b.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/119-aaca253bf377b8189428.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000241_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-86ff77aa6b46c78c-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000242_GET_dataserver2_cf_io_R9h1WN6Rjk0_SpeedTest_08_png(self):
        url = '' + '/dataserver2/cf.io/R9h1WN6Rjk0/SpeedTest-08.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000243_GET_dataserver2_cf_io_R9h1WN6Rjk2_blob(self):
        url = '' + '/dataserver2/cf.io/R9h1WN6Rjk2/blob'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000244_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-9662b36ac3c6e760-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000245_GET_dataserver2_cf_io_R9h1WN6Rjjy_Youtube_09_09_png(self):
        url = '' + '/dataserver2/cf.io/R9h1WN6Rjjy/Youtube-09-09.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000246_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-966aa9f1b4c7023a-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000247_GET_app_resources_images_f41d087bc927db9186958dd8b6cbac66_png(self):
        url = '' + '/app/resources/images/f41d087bc927db9186958dd8b6cbac66.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/119-aaca253bf377b8189428.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000248_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '10ba873b53e14d1d9af18096c763e85e-80ffbba0f235af84-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
        )

    @task()
    def task_000249_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088_29_UserGeneratedData(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088%29/UserGeneratedData'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000251_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '812',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.watchvideoevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTILessonOverview-61553261D452D8DE1EA39345B91DE6B707736B56C512286F69ADF731361D8EE3_0179"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248686.153,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIVideo-47DFFBBB8349BE8D78F4ADC062B95E1401051C62BE9600E0CF1C030453707BA6_0079",
                           "Duration":21.490291000000006,"player_configuration":"media-modal",
                           "with_transcript":True,"video_start_time":49.605134,
                           "video_end_time":71.095425,"MaxDuration":153.241,"PlaySpeed":1}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000252_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000253_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '749',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248710.284,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088",
                           "Duration":0}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000254_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000256_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000287_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '753',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248710.284,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088",
                           "Duration":2.494}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000288_GET_app_js_version(self):
        url = '' + '/app/js/version'
        
        headers = {
            'Connection': 'keep-alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000289_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
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
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000290_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000291_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000292_GET_app_resources_images_da233d104d8e07b77f760acb36b3f068_png(self):
        url = '' + '/app/resources/images/da233d104d8e07b77f760acb36b3f068.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/119-aaca253bf377b8189428.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000293_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000294_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
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
    def task_000295_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '1431',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248718.853,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088",
                           "Duration":0.004},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248718.853,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088",
                           "Duration":0.838}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000298_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000302_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3d4f93ca36984d7290537de4242d8c9d-9ee8a78c8dcb1f89-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000304_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000305_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3d4f93ca36984d7290537de4242d8c9d-90efb12c50f5c0d0-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000306_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3d4f93ca36984d7290537de4242d8c9d-aeb98a451aac0761-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000307_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3d4f93ca36984d7290537de4242d8c9d-8936498af094f090-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
        )

    @task()
    def task_000308_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089_29_UserGeneratedData(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089%29/UserGeneratedData'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000309_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '747',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248724.5,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089",
                                        "Duration":0}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000310_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000312_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000374_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
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
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000375_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '1429',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248718.853,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-7925A1BEB1F66EA18D5C76EE7E4D14E78D8CEB39ECEA9D6ADA599FF89BBDCA0A_0088",
                           "Duration":4.092},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248724.5,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089",
                           "Duration":2.071}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000378_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000379_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000380_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089',
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
    def task_000381_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e3e9bfd2df5e4e408000970f7a6e551c-8ca383e3b6af0207-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
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
    def task_000383_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
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
    def task_000385_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e3e9bfd2df5e4e408000970f7a6e551c-a9d60373df3947eb-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
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
    def task_000388_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e3e9bfd2df5e4e408000970f7a6e551c-b139c13221f0f8f9-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
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
    def task_000389_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e3e9bfd2df5e4e408000970f7a6e551c-bd497d1aeddf42e4-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
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
    def task_000391_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0xa88434_3A5573657273_3AR9h1WN6Rjjz(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0xa88434%3A5573657273%3AR9h1WN6Rjjz'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/vnd.nextthought.pageinfo+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': 'e3e9bfd2df5e4e408000970f7a6e551c-9a70da1abd3c6555-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'course': 'tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A',
            'type': 'application/vnd.nextthought.pageinfo+json',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000392_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
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
        )

    @task()
    def task_000394_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ANTI_NTIRelatedWorkRef_9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088_29_UserGeneratedData(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ANTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088%29/UserGeneratedData'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/vnd.nextthought.collection+json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
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
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000395_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Azope_security_management_system_user_OID_0xa88434_3A5573657273_3AR9h1WN6Rjjz_40_40view_UnlistedYoutube_pdf(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Azope.security.management.system_user-OID-0xa88434%3A5573657273%3AR9h1WN6Rjjz/%40%40view/UnlistedYoutube.pdf'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'iframe',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000396_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '1427',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248734.677,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089","Duration":0.004},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248739.673,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088",
                           "Duration":0}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000397_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000399_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '1430',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248734.677,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-D8F4450505688C88DD74AFBA02BD75E3FBD0FFE6EDE1BC87770AC1F94101CAC8_0089","Duration":2.657},
                          {"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248739.673,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088","Duration":5.01}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000400_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/items/NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000403_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-97373f0f4203fb7d-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000405_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-82755d9ce957fc63-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000406_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-84692753d630cb65-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000407_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000408_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-84a18139fc4aecd2-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000409_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-b3343d4d33ace2e8-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000410_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-b6ae03ca1863098f-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000411_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-8c6839b908bee6d2-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000412_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '3a0327eec610490da603854959783115-94b77ca06ab34a4a-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
    def task_000413_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': '3a0327eec610490da603854959783115-938071ee46e198a0-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
        )

    @task()
    def task_000414_GET_app_resources_images_cea7d35e06a1a6ce53d32c1bf69ed73c_png(self):
        url = '' + '/app/resources/images/cea7d35e06a1a6ce53d32c1bf69ed73c.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/912-845a648f410d03e627ce.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000415_GET_app_resources_images_ce045f5eda80df1ac38bb2a062f21eb8_svg(self):
        url = '' + '/app/resources/images/ce045f5eda80df1ac38bb2a062f21eb8.svg'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/index-85d703ae-368561d071ecc39680ae.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000416_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
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
        )

    @task()
    def task_000419_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '753',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.resourceevent",
                           "context_path":["tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                                           "tag:nextthought.com,2011-10:NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1",
                                           "tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088"],
                           "RootContextID":"tag:nextthought.com,2011-10:admin.user-OID-0xa88095:5573657273:ucvfaTqmB9A",
                           "timestamp":1618248739.673,"user":f"{self.user_id}",
                           "ResourceId":"tag:nextthought.com,2011-10:NTI-NTIRelatedWorkRef-9127C860A4B27C7F5BF6450C1BD72A442D7D655B550FEA3F5CFA00B73B0EB1B6_0088",
                           "Duration":9.064}]}

        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000420_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/items/NTI-NTIAssignmentRef-9273988BA9829FA574D8D2CA31598196A6A9882879066574FFE7FEF0403A9190_0088',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000423_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000424_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-906d84951a8f5140-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000426_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-9d449ecf97b38fe3-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000427_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-80750aad6508bfe1-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000428_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-a7d3dd2f80173c0c-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000429_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-95ee14d194124e80-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000430_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-93556cbf0257283f-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000431_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_1_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.1/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '9e75b4c99ee44618ac92d125cabb4a5c-88d0296f223c2838-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000432_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000433_GET_app_course_admin_user_OID_0xa88095_3A5573657273_3AucvfaTqmB9A_lessons_NTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2(self):
        url = '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000434_GET_app_resources_strings_strings_js(self):
        url = '' + '/app/resources/strings/strings.js'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000477_GET_app_js_version(self):
        url = '' + '/app/js/version'
        
        headers = {
            'Connection': 'keep-alive',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000480_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000484_GET_app_resources_368_8cb546e317e247390cc4_css_map(self):
        url = '' + '/app/resources/368-8cb546e317e247390cc4.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000485_GET_app_resources_index_cb8cd673_11f289c080edc25e4b1d_css_map(self):
        url = '' + '/app/resources/index-cb8cd673-11f289c080edc25e4b1d.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000486_GET_app_resources_461_42a54af044e82aedb669_css_map(self):
        url = '' + '/app/resources/461-42a54af044e82aedb669.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000487_GET_app_resources_172_ea4022a11e6cdf02915e_css_map(self):
        url = '' + '/app/resources/172-ea4022a11e6cdf02915e.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000488_GET_app_resources_index_85d703ae_368561d071ecc39680ae_css_map(self):
        url = '' + '/app/resources/index-85d703ae-368561d071ecc39680ae.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000490_GET_app_resources_917_1dfa58688bb217505cc4_css_map(self):
        url = '' + '/app/resources/917-1dfa58688bb217505cc4.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000492_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''username=stress.tester2'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000493_GET_app_resources_257_0b9aebba418f222d3aef_css_map(self):
        url = '' + '/app/resources/257-0b9aebba418f222d3aef.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000494_GET_app_resources_index_5616c68a_bab3deb0a81826b351c0_css_map(self):
        url = '' + '/app/resources/index-5616c68a-bab3deb0a81826b351c0.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000495_GET_app_resources_505_70aa56ff0f30495a1d8c_css_map(self):
        url = '' + '/app/resources/505-70aa56ff0f30495a1d8c.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000496_GET_app_resources_822_10349e7a4b7e3cec765b_css_map(self):
        url = '' + '/app/resources/822-10349e7a4b7e3cec765b.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000497_GET_app_resources_392_de5adb513927e9d73166_css_map(self):
        url = '' + '/app/resources/392-de5adb513927e9d73166.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000498_GET_app_resources_912_845a648f410d03e627ce_css_map(self):
        url = '' + '/app/resources/912-845a648f410d03e627ce.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000499_GET_app_resources_341_45982afdb45f7cfe648a_css_map(self):
        url = '' + '/app/resources/341-45982afdb45f7cfe648a.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000500_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000501_GET_app_resources_362_42c7ad94a64cc113907a_css_map(self):
        url = '' + '/app/resources/362-42c7ad94a64cc113907a.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000502_GET_app_resources_index_7cc21f2e_4db7bcbc4885170a5d9e_css_map(self):
        url = '' + '/app/resources/index-7cc21f2e-4db7bcbc4885170a5d9e.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000503_GET_app_resources_index_725566d1_5938ac3d7855ddd452fb_css_map(self):
        url = '' + '/app/resources/index-725566d1-5938ac3d7855ddd452fb.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000504_GET_app_resources_259_04dd2eb75858d10b9759_css_map(self):
        url = '' + '/app/resources/259-04dd2eb75858d10b9759.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000505_GET_app_resources_119_aaca253bf377b8189428_css_map(self):
        url = '' + '/app/resources/119-aaca253bf377b8189428.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000506_GET_app_resources_index_c0d25d36_33fe6c9d0871a62fd184_css_map(self):
        url = '' + '/app/resources/index-c0d25d36-33fe6c9d0871a62fd184.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000507_GET_app_resources_index_aec23333_655f19207cc10f8e9761_css_map(self):
        url = '' + '/app/resources/index-aec23333-655f19207cc10f8e9761.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000508_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarywN1OJAjYHSSryPcQ',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '''------WebKitFormBoundarywN1OJAjYHSSryPcQ\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester2\r\n------WebKitFormBoundarywN1OJAjYHSSryPcQ--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000510_GET_app_resources_593_4898835c1c8213c0f26e_css_map(self):
        url = '' + '/app/resources/593-4898835c1c8213c0f26e.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000512_GET_app_resources_990_f6c2317677240019d538_css_map(self):
        url = '' + '/app/resources/990-f6c2317677240019d538.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000517_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000518_GET_favicon_ico(self):
        url = '' + '/favicon.ico'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000520_GET_dataserver2_users_stress_tester2(self):
        url = '' + f'/dataserver2/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000521_GET_socket_io_1(self):
        url = '' + '/socket.io/1'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1618248767086',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000522_GET_dataserver2_users_stress_tester2(self):
        url = '' + f'/dataserver2/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000524_GET_socket_io_1_websocket_0x6209aa66a1eb1b3e(self):
        url = '' + '/socket.io/1/websocket/0x6209aa66a1eb1b3e'
        
        headers = {
            'Connection': 'Upgrade',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Upgrade': 'websocket',
            'Origin': '' + '',
            'Sec-WebSocket-Version': '13',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-WebSocket-Key': 'w3PxEENwwaaIi4r6q/+VPA==',
            'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000525_GET_dataserver2_users_stress_tester2_2B_2Bpreferences_2B_2B_WebApp(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000526_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
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
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000527_GET_dataserver2_users_stress_tester2_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000528_GET_dataserver2_users_stress_tester2_FriendsLists(self):
        url = '' + f'/dataserver2/users/{self.user_id}/FriendsLists'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000529_GET_dataserver2_users_stress_tester2_Groups(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Groups'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000530_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0xa88095_3A5573657273_3AucvfaTqmB9A(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000531_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
        )

    @task()
    def task_000532_GET_dataserver2_users_stress_tester2_FriendsLists(self):
        url = '' + f'/dataserver2/users/{self.user_id}/FriendsLists'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000533_GET_dataserver2_users_stress_tester2_Calendars_40_40events(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1618289999.227',
            'notBefore': '1618248768.227',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name=url.replace(self.user_id, 'stress.tester')
        )

    @task()
    def task_000534_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000535_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000536_GET_dataserver2_users_stress_tester2_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000537_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40NonAssignmentAssessmentSummaryItemsByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40NonAssignmentAssessmentSummaryItemsByOutlineNode'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000538_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40AssignmentSummaryByOutlineNode(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40AssignmentSummaryByOutlineNode'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000539_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000540_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/%40%40UserCoursePreferredAccess'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000542_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_120_Orientation_presentation_assets_webapp_v1_vendoroverrideicon_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/120-Orientation/presentation-assets/webapp/v1/vendoroverrideicon.png'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1613229695',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000543_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000544_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_ContentPackageBundle_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/ContentPackageBundle/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
        )

    @task()
    def task_000545_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_CourseTabPreferences(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/CourseTabPreferences'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000546_GET_dataserver2_users_stress_tester2_Courses_EnrolledCourses_tag_3Anextthought_com_2C2011_10_3ANTI_CourseInfo_1358944583079762845_4744553183735993139_AssignmentHistories_stress_tester2(self):
        url = '' + f'/dataserver2/users/{self.user_id}/Courses/EnrolledCourses/tag%3Anextthought.com%2C2011-10%3ANTI-CourseInfo-1358944583079762845_4744553183735993139/AssignmentHistories/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000547_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000549_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000550_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-summary'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000551_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_2_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/%40%40overview-content'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000552_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
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
    def task_000553_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-80D83ED6F2F135F490BED679E6C6F9B0E5521025F82FC1755111DBAFC9CA33F0_0084'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.2/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000557_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '09fac170cb2c41d4a0b2a9ccde7eb5bb-97bd2a7316122dc0-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
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
    def task_000558_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_3_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '09fac170cb2c41d4a0b2a9ccde7eb5bb-9f7783d140abde35-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
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
    def task_000559_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
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
    def task_000562_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Assessments_tag_3Anextthought_com_2C2011_10_3ANTI_NAQ_8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Assessments/tag%3Anextthought.com%2C2011-10%3ANTI-NAQ-8BFD14ED014634B732EA7E27EB1FEF211AE3FC741268530C3AB7EBF4310E05C7_0084'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '09fac170cb2c41d4a0b2a9ccde7eb5bb-97b3ffd3aae7becf-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000563_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '09fac170cb2c41d4a0b2a9ccde7eb5bb-8bb84e640f91a531-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.3/',
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
    def task_000571_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_summary(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-summary'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '1116dcc1fbdc4bfb8ad778903d39f4ac-ae9c498d17bd6e9a-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000572_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_contents(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/contents'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000573_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Outline_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_tag_3Anextthought_com_2C2011_10_3ANTI_NTICourseOutlineNode_1358944583079762845_4744553183735993139_0_0_40_40overview_content(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Outline/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0/tag%3Anextthought.com%2C2011-10%3ANTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/%40%40overview-content'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '1116dcc1fbdc4bfb8ad778903d39f4ac-9421692aee3e9469-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000574_GET_app_api_videos_youtube(self):
        url = '' + '/app/api/videos/youtube'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'sentry-trace': '1116dcc1fbdc4bfb8ad778903d39f4ac-98fd06a3ab03a33a-0',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
        )

    @task()
    def task_000575_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_CompletedItems_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/CompletedItems/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '1116dcc1fbdc4bfb8ad778903d39f4ac-9b295059a5b1ccb5-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000576_GET_app_resources_images_9f48c6ca72a668827d03ef667daf96a1_png(self):
        url = '' + '/app/resources/images/9f48c6ca72a668827d03ef667daf96a1.png'
        
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/912-845a648f410d03e627ce.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000577_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_120_Orientation_Completion_Progress_users_stress_tester2(self):
        url = '' + f'/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/120-Orientation/Completion/Progress/users/{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'accept': 'application/json',
            'X-NTI-Client-Version': '2021.6.12',
            'X-NTI-Client-App': '@nti/web-app',
            'x-requested-with': 'XMLHttpRequest',
            'sentry-trace': '1116dcc1fbdc4bfb8ad778903d39f4ac-af70c42c30766cd3-0',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000578_GET_dataserver2_users_stress_tester2_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = '' + f'/dataserver2/users/{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
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
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000580_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000581_GET_dataserver2_logon_logout(self):
        url = '' + '/dataserver2/logon.logout'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
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
    def task_000582_GET_login(self):
        url = '' + '/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/course/admin.user-OID-0xa88095%3A5573657273%3AucvfaTqmB9A/lessons/NTI-NTICourseOutlineNode-1358944583079762845_4744553183735993139.0.0/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000587_GET_login_resources_index_bd9d172d9d33af4d7042_css_map(self):
        url = '' + '/login/resources/index-bd9d172d9d33af4d7042.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000590_GET_login_resources_255_a03653a05e52665938dd_css_map(self):
        url = '' + '/login/resources/255-a03653a05e52665938dd.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000591_GET_login_resources_507_ca6b2886d16685d1fd68_css_map(self):
        url = '' + '/login/resources/507-ca6b2886d16685d1fd68.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )


    @task()
    def task_000596_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
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
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
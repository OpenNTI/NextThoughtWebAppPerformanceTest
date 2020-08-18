# -*- coding: UTF-8 -*-

from locust import HttpUser, TaskSet, task, SequentialTaskSet, between
import json
import base64
import random
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
                 #"tag:nextthought.com,2011-10:NTI-CourseInfo-7337604134509948579_4744475820139681474",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914048981_4744481196940283859",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-5954844452914048953_4744481196655629595",
                 "tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635897999_4744481499102048854"
                 ]

class LoadImages(TaskSet):
    @task()
    def task_000155_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry/%40%40UserCoursePreferredAccess'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000156_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066960',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000157_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066747',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000158_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
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
    def task_000159_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066846',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000160_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066703',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000161_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067083',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000162_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066640',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000163_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067150',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000164_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_40_40UserCoursePreferredAccess(
            self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/%40%40UserCoursePreferredAccess'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000165_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_background_png(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/background.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066747',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000166_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(
            self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067025',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )


class UserEnrollment(SequentialTaskSet):
    user_id = 0
    ntiid = "tag:nextthought.com,2011-10:NTI-CourseInfo-381762027272797856_4744477175327467881"
    site = "postgres01.nextthought.com"
    course_id = 'QAAUTO-1595107828927'

    def on_start(self):
        self.user_id = USER_CREDENTIALS.pop()
        self.ntiids = random.sample(COURSE_NTIIDS, 3)
        print(f'starting stress.tester{self.user_id}')
        print(self.ntiids)

    @task()
    def task_000001_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000002_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '142',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryVe6dv7D6GeMGofOR',
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

        data = '''------WebKitFormBoundaryVe6dv7D6GeMGofOR\r\nContent-Disposition: form-data; name="username"\r\n\r\nsgr\r\n------WebKitFormBoundaryVe6dv7D6GeMGofOR--\r\n'''

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
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000004_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '143',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySo4EejNShAyXnsAm',
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

        data = '''------WebKitFormBoundarySo4EejNShAyXnsAm\r\nContent-Disposition: form-data; name="username"\r\n\r\nsgre\r\n------WebKitFormBoundarySo4EejNShAyXnsAm--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000005_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000006_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '142',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryoPeQJBxZ2qlS6byA',
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

        data = '''------WebKitFormBoundaryoPeQJBxZ2qlS6byA\r\nContent-Disposition: form-data; name="username"\r\n\r\nsgr\r\n------WebKitFormBoundaryoPeQJBxZ2qlS6byA--\r\n'''

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
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000010_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '142',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryibw7z3THc90mq78l',
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

        data = '''------WebKitFormBoundaryibw7z3THc90mq78l\r\nContent-Disposition: form-data; name="username"\r\n\r\nstr\r\n------WebKitFormBoundaryibw7z3THc90mq78l--\r\n'''

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
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000012_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '143',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryFfT3ByffzwB3Pxhd',
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

        data = '''------WebKitFormBoundaryFfT3ByffzwB3Pxhd\r\nContent-Disposition: form-data; name="username"\r\n\r\nstre\r\n------WebKitFormBoundaryFfT3ByffzwB3Pxhd--\r\n'''

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
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000014_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '145',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryk8EKWxM0m1J9GJgm',
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

        data = '''------WebKitFormBoundaryk8EKWxM0m1J9GJgm\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress\r\n------WebKitFormBoundaryk8EKWxM0m1J9GJgm--\r\n'''

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
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000016_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '146',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8LSt92HlCC6A1CuX',
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

        data = '''------WebKitFormBoundary8LSt92HlCC6A1CuX\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.\r\n------WebKitFormBoundary8LSt92HlCC6A1CuX--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000017_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000018_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '152',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryG6kodv2lCrLqBSev',
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

        data = '''------WebKitFormBoundaryG6kodv2lCrLqBSev\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester\r\n------WebKitFormBoundaryG6kodv2lCrLqBSev--\r\n'''

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000019_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000020_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryAxjVybfHAUzwydXr',
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

        data = f'------WebKitFormBoundaryAxjVybfHAUzwydXr\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryAxjVybfHAUzwydXr--\r\n'

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000023_GET_dataserver2_logon_nti_password(self):
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
    def task_000025_GET_loginsuccess(self):
        url = '' + '/loginsuccess'

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000026_GET_app(self):
        url = '' + '/app'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000069_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000071_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '23',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000072_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000075_POST_dataserver2_logon_handshake(self):
        url = '' + '/dataserver2/logon.handshake'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'X-NTI-Client-TZOffset': '-300',
            'X-NTI-Client-Timezone': 'America/Chicago',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryPETbBrdXfBQnoehC',
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

        data = f'------WebKitFormBoundaryPETbBrdXfBQnoehC\r\nContent-Disposition: form-data; name="username"\r\n\r\nstress.tester{self.user_id}\r\n------WebKitFormBoundaryPETbBrdXfBQnoehC--\r\n'

        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

    @task()
    def task_000077_GET_dataserver2_service(self):
        url = '' + '/dataserver2/service'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000078_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000079_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000081_GET_dataserver2_users_stress_tester1(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000082_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_WebApp(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/WebApp'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000085_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3ARoot(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000086_POST_dataserver2_analytics_sessions_40_40analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000087_GET_dataserver2_users_stress_tester1_Groups(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Groups'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000088_GET_dataserver2_users_stress_tester1_FriendsLists(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/FriendsLists'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000089_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence_Active(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence/Active'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000096_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000099_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'notAfter': '1596085199.076',
            'notBefore': '1596074720.075',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000100_GET_dataserver2_users_stress_tester1_Communities_Communities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000101_GET_dataserver2_users_stress_tester1_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000102_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'notAfter': '1596085199.134',
            'notBefore': '1596074720.134',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000103_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn_lastViewed(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn/lastViewed'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000104_GET_dataserver2_users_stress_tester1_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000108_GET_dataserver2_users_stress_tester1_Pages_28tag_3Anextthought_com_2C2011_10_3ARoot_29_RUGDByOthersThatIMightBeInterestedIn(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000122_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000125_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40Featured(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40Featured'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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

    # @task()
    # def task_000128_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000129_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000130_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066960',
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
    # def task_000131_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000133_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    # @task()
    # def task_000135_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000136_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000137_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000139_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000140_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066960',
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
    # def task_000142_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
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
    # def task_000143_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
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
    # def task_000144_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067025',
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
    # def task_000145_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000146_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    @task()
    def task_000147_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry(self):
        url = '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000149_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20200715192358',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000150_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_background_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/background.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066747',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000151_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '436',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],"RootContextID":self.ntiids[0],
                           "timestamp":1596074735.034,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiids[0],"Duration":0.001}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000154_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0x0ada13_3A5573657273_3APNrw8x8JDDN(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0x0ada13%3A5573657273%3APNrw8x8JDDN'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    # @task()
    # def task_000155_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'accept': 'application/json',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'cors',
    #         'Sec-Fetch-Dest': 'empty',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000156_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066960',
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
    # def task_000157_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000158_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000159_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
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
    # def task_000160_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000161_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
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
    # def task_000162_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
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
    # def task_000163_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000164_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_40_40UserCoursePreferredAccess(self):
    #     url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/%40%40UserCoursePreferredAccess'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'accept': 'application/json',
    #         'X-NTI-Client-TZOffset': '-300',
    #         'X-NTI-Client-Version': '2020.7.2',
    #         'X-NTI-Client-App': '@nti/web-app',
    #         'x-requested-with': 'XMLHttpRequest',
    #         'X-NTI-Client-Timezone': 'America/Chicago',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'cors',
    #         'Sec-Fetch-Dest': 'empty',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #     )
    #
    # @task()
    # def task_000165_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_background_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/background.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000166_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067025',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    #tasks = [LoadImages]

    @task()
    def task_000167_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000169_POST_dataserver2_users_stress_tester1_Courses_EnrolledCourses(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '94',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        # data = {"NTIID":"tag:nextthought.com,2011-10:NTI-CourseInfo-8258097998635894564_4744481197088118676"}
        data = {"NTIID": self.ntiids[0]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        )

    @task()
    def task_000170_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Archived(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Archived'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000171_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000172_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1596085199.479',
            'notBefore': '1596074738.479',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000173_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Upcoming(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Upcoming'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000174_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Current(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Current'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000175_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1596085199.836',
            'notBefore': '1596074738.836',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000176_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000177_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L102_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L102/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDIvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000178_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20200715192358',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000181_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    @task()
    def task_000183_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066960',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    # @task()
    # def task_000184_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
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
    # def task_000185_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000186_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000187_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000188_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000189_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
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
    # def task_000190_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
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
    # def task_000191_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067025',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000192_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '436',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],"RootContextID":self.ntiids[0],
                           "timestamp":1596074735.034,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiids[0],"Duration":6.038}]}
        data_str=json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000195_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000196_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    @task()
    def task_000198_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_background_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/background.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067150',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000199_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000200_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '432',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiids[1],
                           "timestamp":1596074745.844,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiids[1],"Duration":0}]}
        data_str=json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000201_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0x0b0590_3A5573657273_3APNrw8x8JCwM(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0x0b0590%3A5573657273%3APNrw8x8JCwM'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000202_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066960',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    # @task()
    # def task_000203_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000204_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_background_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/background.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000205_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000206_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
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
    # def task_000207_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000208_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
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
    # def task_000209_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000210_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067150',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000211_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000212_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067025',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000213_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000214_POST_dataserver2_users_stress_tester1_Courses_EnrolledCourses(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '94',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"NTIID":self.ntiids[1]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        )

    @task()
    def task_000215_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000216_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Upcoming(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Upcoming'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000217_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Current(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Current'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000218_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1596085199.397',
            'notBefore': '1596074748.397',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000219_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Archived(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Archived'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
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
    def task_000220_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1596085199.823',
            'notBefore': '1596074748.823',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000221_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000222_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_L101_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/L101/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0wxMDEvQ291cnNlQ2F0YWxvZ0VudHJ5/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000225_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    @task()
    def task_000227_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
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

    # @task()
    # def task_000228_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000229_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
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
    # def task_000230_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066960',
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
    # def task_000231_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000232_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000233_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
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
    # def task_000234_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
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
    # def task_000235_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067025',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000236_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '436',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiids[1],
                           "timestamp":1596074745.844,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiids[1],"Duration":5.235}]}
        data_str= json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000237_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000241_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    @task()
    def task_000242_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000243_GET_dataserver2_Objects_tag_3Anextthought_com_2C2011_10_3Aadmin_user_OID_0x0b0301_3A5573657273_3AZUyjj6na7EF(self):
        url = '' + '/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3Aadmin.user-OID-0x0b0301%3A5573657273%3AZUyjj6na7EF'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000244_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '432',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiids[2],
                           "timestamp":1596074755.531,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiids[2],
                           "Duration":0}]}
        data_str=json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000245_HEAD_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_background_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/background.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067083',
        }

        self.response = self.client.request(
            method='HEAD',
            url=url,
            headers=headers,
            params=params,
        )

    # @task()
    # def task_000246_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066747',
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
    # def task_000247_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000248_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000249_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
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
    # def task_000250_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000251_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066960',
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
    # def task_000252_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
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
    # def task_000253_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000254_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_background_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/background.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067083',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000255_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000256_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067025',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000257_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000258_POST_dataserver2_users_stress_tester1_Courses_EnrolledCourses(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '94',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"NTIID":self.ntiids[2]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
            name='/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses'
        )

    @task()
    def task_000259_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Current(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Current'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
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
    def task_000260_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000261_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Archived(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Archived'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
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
    def task_000262_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Upcoming(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Upcoming'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
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
    def task_000263_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1596085199.429',
            'notBefore': '1596074758.429',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000264_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_CourseCatalogEntry(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/CourseCatalogEntry'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000265_GET_dataserver2_users_stress_tester1_Calendars_40_40events(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            'batchSize': '1',
            'notAfter': '1596085199.765',
            'notBefore': '1596074758.765',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            name='/dataserver2/users/stress.tester{self.user_id}/Calendars/%40%40events'
        )

    @task()
    def task_000266_GET_dataserver2_2B_2Betc_2B_2Bhostsites_sfdd0438bbad141b59137b0e12c47d7ed_2B_2Betc_2B_2Bsite_Courses_DefaultAPIImported_CTAT_104_CourseCatalogEntry_40_40UserCoursePreferredAccess(self):
        url = '' + '/dataserver2/%2B%2Betc%2B%2Bhostsites/sfdd0438bbad141b59137b0e12c47d7ed/%2B%2Betc%2B%2Bsite/Courses/DefaultAPIImported/CTAT-104/CourseCatalogEntry/%40%40UserCoursePreferredAccess'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/nti-course-catalog-entry/tag:nextthought.com,2011-10:__nti_object_href-L2RhdGFzZXJ2ZXIyLysrZXRjKytob3N0c2l0ZXMvc2ZkZDA0MzhiYmFkMTQxYjU5MTM3YjBlMTJjNDdkN2VkLysrZXRjKytzaXRlL0NvdXJzZXMvRGVmYXVsdEFQSUltcG9ydGVkL0NUQVQtMTA0L0NvdXJzZUNhdGFsb2dFbnRyeQ%3D%3D/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000269_GET_dataserver2_users_stress_tester1_Catalog_Courses_40_40ByTag_nti_other(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/catalog/.nti_other/',
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
            name='/dataserver2/users/stress.tester{self.user_id}/Catalog/Courses/%40%40ByTag/.nti_other'
        )

    @task()
    def task_000271_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L102_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L102/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596066747',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    # @task()
    # def task_000272_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_ctat_0000_20_281_29_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/ctat-0000%20%281%29/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
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
    # def task_000273_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_103_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT_-103/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066960',
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
    # def task_000274_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_TEA001_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-TEA001/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066703',
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
    # def task_000275_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_L101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/L101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067150',
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
    # def task_000276_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_104_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-104/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596067083',
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
    # def task_000277_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT006_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT006/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066640',
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
    # def task_000278_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_CTAT_101_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
    #     url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/CTAT-101/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Pragma': 'no-cache',
    #         'Cache-Control': 'no-cache',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'no-cors',
    #         'Sec-Fetch-Dest': 'image',
    #         'Referer': '' + '/app/catalog/.nti_other/',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #     }
    #
    #     params = {
    #         't': '1596066846',
    #     }
    #
    #     self.response = self.client.request(
    #         method='GET',
    #         url=url,
    #         headers=headers,
    #         params=params,
    #     )

    @task()
    def task_000279_GET_content_sites_sfdd0438bbad141b59137b0e12c47d7ed_Courses_DefaultAPIImported_12345_presentation_assets_webapp_v1_contentpackage_landing_232x170_png(self):
        url = '' + '/content/sites/sfdd0438bbad141b59137b0e12c47d7ed/Courses/DefaultAPIImported/12345/presentation-assets/webapp/v1/contentpackage-landing-232x170.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/catalog/.nti_other/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '1596067025',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000281_GET_site_assets_shared_brand_web_library_png(self):
        url = '' + '/site-assets/shared/brand_web_library.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/library/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000283_GET_dataserver2_users_stress_tester1_ContentBundles_VisibleContentBundles(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/ContentBundles/VisibleContentBundles'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/library/',
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
    def task_000284_GET_dataserver2_users_stress_tester1_Courses_EnrolledCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/EnrolledCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/library/',
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
    def task_000285_GET_dataserver2_users_stress_tester1_Communities_Communities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/Communities'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/library/',
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
    def task_000286_GET_site_assets_shared_brand_web_library_png(self):
        url = '' + '/site-assets/shared/brand_web_library.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/library/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000287_GET_dataserver2_users_stress_tester1_Communities_AdministeredCommunities(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Communities/AdministeredCommunities'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/library/',
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
    def task_000288_GET_dataserver2_users_stress_tester1_Courses_AdministeredCourses_40_40Favorites(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/Courses/AdministeredCourses/%40%40Favorites'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/library/',
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
    def task_000295_POST_dataserver2_analytics_batch_events(self):
        url = '' + '/dataserver2/analytics/batch_events'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '436',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
            'Referer': '' + '/app/library/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"MimeType":"application/vnd.nextthought.analytics.batchevents",
                "events":[{"MimeType":"application/vnd.nextthought.analytics.coursecatalogviewevent",
                           "context_path":[],
                           "RootContextID":self.ntiids[2],
                           "timestamp":1596074755.531,"user":f"stress.tester{self.user_id}",
                           "ResourceId":self.ntiids[2],
                           "Duration":5.539}]}
        data_str = json.dumps(data)
        self.response = self.client.request(
            method='POST',
            url=url,
            headers=headers,
            data=data_str,
        )

    @task()
    def task_000297_GET_app_resources_images_ee764b6ee333c4bfcadbc97eb818253c_png(self):
        url = '' + '/app/resources/images/ee764b6ee333c4bfcadbc97eb818253c.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/library/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000298_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20200715192358',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000299_GET_dataserver2_users_stress_tester1_2B_2Bpreferences_2B_2B_ChatPresence(self):
        url = f'/dataserver2/users/stress.tester{self.user_id}/%2B%2Bpreferences%2B%2B/ChatPresence'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'X-NTI-Client-Version': '2020.7.2',
            'X-NTI-Client-App': '@nti/web-app',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/library/',
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
    def task_000300_GET_app_resources_images_sprite_png(self):
        url = '' + '/app/resources/images/sprite.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'image',
            'Referer': '' + '/app/resources/css/legacy.css',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = {
            't': '20200715192358',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

    @task()
    def task_000301_GET_vendor_ext_4_2_resources_ext_theme_classic_images_form_exclamation_gif(self):
        url = '' + '/vendor/ext-4.2/resources/ext-theme-classic/images/form/exclamation.gif'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
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
    def task_000305_POST_dataserver2_analytics_sessions_40_40end_analytics_session(self):
        url = '' + '/dataserver2/analytics/sessions/%40%40end_analytics_session'
        
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Origin': '' + '',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '' + '/app/library/',
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
    def task_000306_GET_dataserver2_logon_logout(self):
        url = '' + '/dataserver2/logon.logout'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/library/',
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
    def task_000307_GET_login(self):
        url = '' + '/login'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': '' + '/app/library/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000308_GET_login_resources_shared_index_13abd1e41dd3e9cfc85d_css(self):
        url = '' + '/login/resources/shared~index-13abd1e41dd3e9cfc85d.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000309_GET_login_js_index_0f99ea1a_js(self):
        url = '' + '/login/js/index-0f99ea1a.js'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000310_GET_login_resources_vendor_index_bb59309bd49fe3f4c852_css(self):
        url = '' + '/login/resources/vendor~index-bb59309bd49fe3f4c852.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000311_GET_login_resources_index_0e19a878f457cb866b13_css(self):
        url = '' + '/login/resources/index-0e19a878f457cb866b13.css'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000312_GET_login_js_vendor_index_0f99ea1a_js(self):
        url = '' + '/login/js/vendor~index-0f99ea1a.js'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000313_GET_login_js_shared_index_0f99ea1a_js(self):
        url = '' + '/login/js/shared~index-0f99ea1a.js'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
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
    def task_000318_GET_login_resources_images_d40e8c56563e9a73e287cc9a93cb5da1_png(self):
        url = '' + '/login/resources/images/d40e8c56563e9a73e287cc9a93cb5da1.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
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
    def task_000319_GET_login_js_vendor_index_0f99ea1a_js_map(self):
        url = '' + '/login/js/vendor~index-0f99ea1a.js.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000320_GET_login_js_shared_index_0f99ea1a_js_map(self):
        url = '' + '/login/js/shared~index-0f99ea1a.js.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000321_GET_login_js_index_0f99ea1a_js_map(self):
        url = '' + '/login/js/index-0f99ea1a.js.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000322_GET_login_resources_images_174187b7474fdbc7f04568bb767ae2bb_png(self):
        url = '' + '/login/resources/images/174187b7474fdbc7f04568bb767ae2bb.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
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
    def task_000325_GET_dataserver2_logon_ping(self):
        url = '' + '/dataserver2/logon.ping'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
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
    def task_000327_GET_login_resources_images_14c8cb6ee9d598f2510836b67c279f07_png(self):
        url = '' + '/login/resources/images/14c8cb6ee9d598f2510836b67c279f07.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
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
    def task_000328_GET_login_resources_images_0bcdabaa0b82ea3349f95d9a90a66551_png(self):
        url = '' + '/login/resources/images/0bcdabaa0b82ea3349f95d9a90a66551.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Origin': '' + '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
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
    def task_000329_GET_login_resources_vendor_index_bb59309bd49fe3f4c852_css_map(self):
        url = '' + '/login/resources/vendor~index-bb59309bd49fe3f4c852.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000330_GET_login_resources_shared_index_13abd1e41dd3e9cfc85d_css_map(self):
        url = '' + '/login/resources/shared~index-13abd1e41dd3e9cfc85d.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000333_GET_login_resources_index_0e19a878f457cb866b13_css_map(self):
        url = '' + '/login/resources/index-0e19a878f457cb866b13.css.map'
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        self.response = self.client.request(
            method='GET',
            url=url,
            headers=headers,
        )

    @task()
    def task_000334_GET_login_resources_images_d40e8c56563e9a73e287cc9a93cb5da1_png(self):
        url = '' + '/login/resources/images/d40e8c56563e9a73e287cc9a93cb5da1.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
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
    def task_000335_GET_login_resources_images_0bcdabaa0b82ea3349f95d9a90a66551_png(self):
        url = '' + '/login/resources/images/0bcdabaa0b82ea3349f95d9a90a66551.png'
        
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
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
        time.sleep(36000)


class WebsiteUser(HttpUser):
    tasks = [UserEnrollment]
    wait_time = between(5, 15)
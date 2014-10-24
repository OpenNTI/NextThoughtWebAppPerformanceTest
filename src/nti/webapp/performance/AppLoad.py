'''
Created on Oct 9, 2014

@author: yunzhu
'''
# This locust test script example will simulate a user 
# browsing the Locust documentation on http://docs.locust.io

import random
from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery
from requests.auth import HTTPBasicAuth
import base64
import string
import json
import time
import random
import urllib
import os

class loadApp(TaskSet):

    config = open("/Users/yunzhu/workspace/NextThoughtWebAppPerformanceTest/src/nti/webapp/performance/config/perftestconfig.txt")
    lower =int(config.readline())
    upper =int(config.readline())
    config.close()
    print ("lower: %s upper: %s" % (lower, upper))
    USER_NAME=["LRPerf%s" % (x+1) for x in range(lower,upper)]
    random.shuffle(USER_NAME)
    username=None
    tkt=None
    cookie=None
    def on_start(self):
        print self.host        
        self.username = (self.USER_NAME).pop()

        self.cookie = self.logon_or_create()
        r = self.client.get("/dataserver2/logon.ping",
                            headers={"Cookie": self.cookie,
                                     })
        print "handshake after authenticating: %s" % (r.status_code)
        


    @task(1)
    def enroll_drop_random_courses(self):
        nttid_list = ["tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CHEM_4970_SubInstances_100",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CHEM_4970_200_SubInstances_200",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_UCOL_1002",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_BIOL_2124",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CS_1323",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_SOC_1113",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CLC_3403",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_PHIL_1203",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_IAS_2003"                     
                       ]
        size = len(nttid_list)
        index = random.randint(0, size-1)
        nttid = nttid_list[index]
        courseurl = urllib.quote_plus(nttid)
        nttidurl = "/dataserver2/users/%s/Courses/EnrolledCourses/%s" % (self.username, courseurl)
       
        
        r = self.client.post("/dataserver2/users/%s/Courses/EnrolledCourses" % self.username,
                             headers={"Accept": "application/json",
                                     "Accept-Encoding":"gzip,deflate",
                                     "Accept-Language":"en-US,en;q=0.8",
                                     "Connection":"keep-alive",
                                     "Content-Type":"application/json",
                                     "Cache-Control":"no-cache",
                                     "Cookie": self.cookie,
                                     "Pragma": "no-cache",
                                     "Referer":"https://ou-alpha.nextthought.com/app/",
                                     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                     },
                             data = json.dumps({"NTIID":nttid }) 
                             ) 
        print "open enrolled in course nttid:%s  STATUS: %s " %(nttid, r.status_code)
        
        time.sleep(random.randint(10, 30))
        
        r = self.client.delete (nttidurl,
                                headers={"Accept": "application/json",
                                         "Accept-Encoding":"gzip,deflate,sdch",
                                         "Accept-Language":"en-US,en;q=0.8",
                                         "Connection":"keep-alive",
                                         "Cache-Control":"no-cache",
                                         "Cookie": self.cookie,
                                         "Host": "ou-alpha.nextthought.com",
                                         "Pragma": "no-cache",
                                         "Referer":"https://ou-alpha.nextthought.com/app/",
                                         "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                         },                                                              
                                )
        print "drop course nttid: %s % response: %s " %(nttid, nttidurl,  r.status_code)
         
    #@task(1)
    def cob_admissions_preflightcheck(self):
        r = self.client.get("/dataserver2/janux/fmaep_admission_preflight",
                           headers = {"Content-Type":"application/json",
                                      "Cookie": self.cookie                                    
                                      },
                           data = json.dumps({"attended_other_institution": "Y",
                                             "bachelors_or_higher": "Y",
                                             "city": "norman",
                                             "country_of_citizenship": "United States",
                                             "date_of_birth": "19850303",
                                             "email": "julie.zhu@nextthought.com",
                                             "first_name": "mytest",
                                             "gender": "F",
                                             "good_academic_standing": "Y",
                                             "has_mailing_address": 'false',
                                             "high_school_graduate": "Y",
                                             "is_currently_attending_highschool": "N",
                                             "is_currently_attending_ou": "N",
                                             "last_name": "Zhu",
                                             "nation_code": "United States",
                                             "postal_code": "73072",
                                             "state": "Oklahoma",
                                             "still_attending": "Y",
                                             "street_line1": "address",
                                             "telephone_number": "789456123",
                                             "years_of_oklahoma_residency": "0",
                                              }))
        print "admissions_preflightcheck response: %s %s" % (r.status_code, r.content)
    
    @task(1)   
    def phantomjs_execution (self):
        print "executing phantomjs................"
        os.system('phantomjs loadtest.js')
        
                                 
    #@task(1)
    def view_cob_course_detail(self):
        r = self.client.get("/dataserver2/janux/fmaep_course_details?CRN=34847&Term=201410",
                            headers={"Accept": "application/json",
                                     "Accept-Encoding":"gzip,deflate,sdch",
                                     "Accept-Language":"en-US,en;q=0.8",
                                     "Connection":"keep-alive",
                                     "Cache-Control":"no-cache",
                                     "Cookie": self.cookie,
                                     "Host": "ou-alpha.nextthought.com",
                                     "Pragma": "no-cache",
                                     "Referer":"https://ou-alpha.nextthought.com/app/",
                                     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                    },
                            params={"CRN": "34847", "Term": "201410"}
                            )
    
        print "view course detail response: %s %s" %(r.status_code, r.content)
    

    #try logging in, if getting 401, means account not created, and go ahead and create.
    def logon_or_create(self):
        print "looking at logon for user: %s" % self.username
        base64string = base64.encodestring('%s:%s' % (self.username, 'test1234'))[:-1]
        with self.client.get("/dataserver2/logon.nti.password?username=%s" % self.username, 
                             headers={"Authorization": "Basic %s" % base64string}, 
                             catch_response=True) as response:
            if response.status_code == 401:
                print "%s has not been created, go ahead and create the account" % self.username
                self.create_account()
                response.success()
            elif response.status_code == 204:
                print "%s Authentication successful" % self.username
                header = response.headers
                set_cookie = header['set-cookie']
                #print "cookies: %s " % cookie
                key = set_cookie.split(";")
                self.tkt = key[0]
                self.cookie = '%s; %s; username=%s' % (self.tkt, self.tkt, self.user)
                print "Authentication successful for $: %s %s" % (self.username, response.status_code, self.cookie)
            else :
                response.failure("FALURE!!!! %s %s %s" % (self.username, response.status_code, response.content))
    
    def create_account(self):
        chars = string.ascii_letters
        user = ''.join(random.choice(chars) for _ in range(15))       
        random_user = "LR%s" % user

        r = self.client.post("/dataserver2/account.create", 
                                    headers= {"Content-Type": "application/json; charset=UTF-8"},
                                    data=json.dumps({"Username": self.username,
                                                     "email": "julie.zhu@nextthought.com",
                                                     "opt_in_email_communication": "false",
                                                     "password": "test1234",
                                                     "realname": "%s %s" %(random_user, random_user) }))        
         
        #print "account creation FINAL header: %s" %r.headers 
        header = r.headers
        cookie = header['set-cookie']
        #print "cookies: %s " % cookie
        keys = cookie.split(":")
        key = keys[0]
        tkts = key.split(";")
        self.tkt = keys[0]
        self.cookie = '%s; %s; username=%s' % (self.tkt, self.tkt, self.username)
        #print "cookie created: %s; %s; username=%s" % (keys, keys, self.random_user)
        print "account creation FINAL response: %s %s \n cookie %s:" % (self.username, r.status_code, self.cookie)  

    
    def log_out(self):
        pass
        


    
class AppLoadUser(HttpLocust):
    task_set = loadApp
    #host = "https://ou-alpha.nextthought.com"
    host = "https://ou-alpha.nextthought.com"
    loadApp.host = host
    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 20 and 600 seconds), since there's a bunch of text 
    # on each page
    min_wait = 2  * 1000
    max_wait = 6 * 1000
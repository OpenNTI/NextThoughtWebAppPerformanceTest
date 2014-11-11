'''
Created on Oct 15, 2014

@author: yunzhu
'''


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
import socket
from posix import getuid

class course_work(TaskSet):
    username=None
    cookie = None

    def on_start(self):
        #print course_work.cookie
        #print self.username
        pass
       
        
    #@task(1)
    def enroll_drop_random_courses(self):
        nttid_list = ["tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CHEM_4970_SubInstances_100",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_UCOL_1002",
                              "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CHEM_1315",
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
                                     "Cookie": course_work.cookie,
                                     "Pragma": "no-cache",
                                     "Referer":"https://ou-alpha.nextthought.com/app/",
                                     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                     },
                             data = json.dumps({"NTIID":nttid }) 
                             ) 
        print "open enrolled in course nttid:%s  STATUS: %s %s %s" %(nttid, r.status_code, self.username, course_work.cookie)
        

    @task(1)
    def stop(self):
        self.interrupt()  

 


class loadApp(TaskSet):
    config = open("/Users/yunzhu/workspace/NextThoughtWebAppPerformanceTest/src/nti/webapp/performance/config/loginConfig.txt")
    lower =int(config.readline())
    upper =int(config.readline())
    config.close()
    # print ("lower: %s upper: %s" % (lower, upper))
    USER_NAME=["perfConcurrent%s" % (x+1) for x in range(lower,upper)]
    username=None
    tkt=None
    cookie=None
    def on_start(self):
        print self.host        
        #self.username = (self.USER_NAME).pop()
        self.username=self.guid()
        self.cookie = self.logon_or_create()
        r = self.client.get("/dataserver2/logon.ping",
                            headers={"Cookie": self.cookie,
                                     })
        #print "handshake after authenticating: %s Logged in as: %s" % (r.status_code, self.username)
        course_work.cookie = self.cookie
        course_work.username = self.username
    
    
    #try logging in, if getting 401, means account not created, and go ahead and create.
    def logon_or_create(self):
        #print "looking at logon for user: %s" % self.username
        base64string = base64.encodestring('%s:%s' % (self.username, 'test1234'))[:-1]
        with self.client.get("/dataserver2/logon.nti.password?username=%s" % self.username, 
                             headers={"Authorization": "Basic %s" % base64string}, 
                             catch_response=True) as response:
            if response.status_code == 401:
                print "%s has not been created, go ahead and create the account" % self.username
                self.create_account()
                response.success()
            elif response.status_code == 204:
                #print "%s Authentication successful" % self.username
                header = response.headers
                #print "header: %s" % header
                set_cookie = header['set-cookie']
                #print "cookies: %s " % set_cookie
                key = set_cookie.split(";")
                self.tkt = key[0]
                self.cookie = '%s; %s; username=%s' % (self.tkt, self.tkt, self.username)
                print "Authentication successful for %s: %s %s" % (self.username, response.status_code, self.cookie)
            else :
                response.failure("FALURE!!!! %s %s %s" % (self.username, response.status_code, response.content))
        time.sleep(1)
        
        '''
        nttid = "tag:nextthought.com,2011-10:NTI-CourseInfo-Fall2014_CHEM_4970_200_SubInstances_200"
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
                                     "Referer":"https://performance.nextthought.com/app/",
                                     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                     },
                             data = json.dumps({"NTIID":nttid }) 
                             ) 
        print "open enrolled in course nttid:%s  STATUS: %s %s %s" %(nttid, r.status_code, self.username, self.cookie)
        '''


    
    def create_account(self):
        chars = string.ascii_letters
        user = ''.join(random.choice(chars) for _ in range(15))       
        random_user = "%sLR" % user
       

        r = self.client.post("/dataserver2/account.create", 
                                    headers= {"Content-Type": "application/json; charset=UTF-8"},
                                    data=json.dumps({"Username": self.username,
                                                     "email": "julie.zhu@nextthought.com",
                                                     "opt_in_email_communication": "false",
                                                     "password": "test1234",
                                                     "realname": "%s %s" %(random_user, random_user) }))        
         
        #print "account creation FINAL header: %s \n %s" % (r.headers, r.content) 
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


    #@task(1)
    def view_cob_course_detail(self):
        queryid = self.getuid()
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
                            params={"CRN": "34847", "Term": "201410",
                                    "queryID": queryid}
                            )
    
        print "view course detail response: %s %s %s" %(r.status_code, r.content, queryid)
    
    @task(20)
    def dosomething(self):
        time.sleep(60000)
    
    
    def guid(self):
        chars = string.ascii_letters
        hostname = socket.gethostname()
        mname = hostname.replace('.local', '')
        user = ''.join(random.choice(chars) for _ in range(15))
        t = str( long( time.time() * 1000 ))
        name = "%s%s%s" % (user, mname, t)       
        return name        


    
class AppLoadUser(HttpLocust):
    task_set = loadApp
    #host = "https://ou-alpha.nextthought.com"
    host = "https://performance.nextthought.com"
    loadApp.host = host
    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 20 and 600 seconds), since there's a bunch of text 
    # on each page
    min_wait = 3  * 1000
    max_wait = 10  * 1000

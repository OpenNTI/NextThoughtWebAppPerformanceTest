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
        
        time.sleep(random.randint(10, 30))
        
        r = self.client.delete (nttidurl,
                                headers={"Accept": "application/json",
                                         "Accept-Encoding":"gzip,deflate,sdch",
                                         "Accept-Language":"en-US,en;q=0.8",
                                         "Connection":"keep-alive",
                                         "Cache-Control":"no-cache",
                                         "Cookie": course_work.cookie,
                                         "Host": "ou-alpha.nextthought.com",
                                         "Pragma": "no-cache",
                                         "Referer":"https://ou-alpha.nextthought.com/app/",
                                         "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                         },                                                              
                                )
        print "drop course nttid: %s response: %s " %(nttid, r.status_code)

    @task(1)
    def view_cob_course_detail(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r = self.client.get("/dataserver2/janux/fmaep_course_details?CRN=34847&Term=201410",
                            headers={"Accept": "application/json",
                                     "Accept-Encoding":"gzip,deflate,sdch",
                                     "Accept-Language":"en-US,en;q=0.8",
                                     "Connection":"keep-alive",
                                     "Cache-Control":"no-cache",
                                     "Cookie": course_work.cookie,
                                     "Host": "ou-alpha.nextthought.com",
                                     "Pragma": "no-cache",
                                     "Referer":"https://ou-alpha.nextthought.com/app/",
                                     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                    },
                            params={"CRN": "34847", "Term": "201410"}
                            )
        end = long(time.time()*1000)
        print "|view course detail response|  %s  | TIME | %d | ms" %(r.status_code, end-start)
    
    #@task(1)
    def cob_admissions_preflightcheck(self):
        r = self.client.get("/dataserver2/janux/fmaep_admission_preflight",
                           headers = {"Content-Type":"application/json",
                                      "Cookie": course_work.cookie                                    
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
    def stop(self):
        self.interrupt()  

 


class loadApp(TaskSet):
    config = open("/home/ltuser/VirtualEnvs/loadtest/workspace/NextThoughtWebAppPerformanceTest/src/nti/webapp/performance/config/loginConfig.txt")
    lower =int(config.readline())
    upper =int(config.readline())
    config.close()
    # print ("lower: %s upper: %s" % (lower, upper))
    USER_NAME=["performance%s" % (x+1) for x in range(lower,upper)]
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
        #print "handshake after authenticating: %s Logged in as: %s" % (r.status_code, self.username)
        course_work.cookie = self.cookie
        course_work.username = self.username
    


    @task(1)
    def login_load_javascript (self):
        queryid = self.guid()
        start=long(time.time()*1000)
        r = self.client.get("/app/javascript/app.min.js?dc=20141015140235",
                            headers ={"cookie": self.cookie},
                            params = {"dc":"20141015140235"}
                                     # "queryID": queryid}
                            )
        end=long(time.time()*1000)
        print "|login_load_javascript| %s |  TIME | %d | ms" % (r.status_code, end-start)
    
    @task(1)
    def login_load_png(self):
        queryid = self.guid()
        start=long(time.time()*1000)
        r=self.client.get("/content/sites/platform.ou.edu/Courses/Fall2014/CHEM%204970-200/presentation-assets/webapp/v1/contentpackage-landing-232x170.png",
                          headers ={"cookie": self.cookie},
                          #params = {"queryID": queryid}
                          )
        end=long(time.time()*1000)
        print "|login_load_png|  %s  | TIME | %d | ms" % (r.status_code,  end-start)
    
    @task(3)
    def login_root(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3ARoot",
                          headers ={"cookie": self.cookie},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|login_root| %s | TIME | %d | ms" % (r.status_code,  end-start) 
        
    @task(3)
    def login_beer_quiz(self):
	queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3AOU-NAQ-CHEM4970_200_F_2014_Chemistry_of_Beer.naq.asg.assignment%3Ajanux_features_verification_quiz",
                          headers ={"cookie": self.cookie},
                          #params = {"queryID": queryid}
                          )
        end = long(time.time()*1000)
        print "|login_beer_quiz| %s | TIME | %d | ms" % (r.status_code,  end-start)

    @task(3)
    def login_beer_healthimpact (self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/Objects/tag%3Anextthought.com%2C2011-10%3AOU-HTML-CHEM4970_200_F_2014_Chemistry_of_Beer.reading%3AHealthImpacts",
                          headers ={"cookie": self.cookie},
                          #params = {"queryID": queryid}
                          )
        end = long(time.time()*1000)
        print "|login_beer_healthimpact| %s | TIME | %d | ms" % (r.status_code,  end-start)

 
    @task(1)    
    def login_all_courses(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/users/%s/Courses/AllCourses" % self.username,
                          headers ={"cookie": self.cookie},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|login_all_courses| %s | TIME | %d | ms" % (r.status_code,  end-start)                              

    @task(1)    
    def login_enrolled_courses(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/users/%s/Courses/EnrolledCourses" % self.username,
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/vnd.nextthought.collection+json"},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|login_enrolled_courses| %s | TIME | %d | ms " % (r.status_code, end-start)                              
   
    @task(1)
    def login_library_main (self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/users/%s/Library/Main" % self.username,
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/vnd.nextthought.collection+json"},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|login_library_main| %s | TIME | %d | ms" % (r.status_code,  end-start)                              

    @task(1)
    def login_users(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/users/%s/FriendsLists" % self.username,
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/vnd.nextthought.collection+json"},
                          #params = {"queryID": queryid}                                                   
                          ) 
        end = long(time.time()*1000)
        print "|login_users| %s | TIME | %d | ms " % (r.status_code,  end-start)                              
        
    @task(10)
    def login_resolve_users(self):
        queryid = self.guid()
        index = random.randint(1, 3)
        user = 'performance%s' % index
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/ResolveUser/%s" % user,
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/json"},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|login_resolve_users| %s | TIME: | %d | ms " % (r.status_code, end-start)                              
   
    @task(1)
    def lognin_outline_content(self):  
        queryid = self.guid()      
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/%2B%2Betc%2B%2Bhostsites/platform.ou.edu/%2B%2Betc%2B%2Bsite/Courses/Fall2014/CHEM%204970-200/Outline/contents",
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/json"},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|lognin_outline_content| %s | TIME | %d | ms" % (r.status_code, end-start)                              
    
    @task(1)
    def login_AssignmentsByOutlineNode(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/dataserver2/%2B%2Betc%2B%2Bhostsites/platform.ou.edu/%2B%2Betc%2B%2Bsite/Courses/Fall2014/CHEM%204970-200/SubInstances/200/AssignmentsByOutlineNode",
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/json"},
                          #params = {"queryID": queryid}
                          )  
        end = long(time.time()*1000)
        print "|login_AssignmentsByOutlineNode| %s | TIME | %d | ms " % (r.status_code, end-start)  
    
    @task(1)
    def login_NonAssignmentAssessmentItemsByOutlineNode(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r = self.client.get("/dataserver2/%2B%2Betc%2B%2Bhostsites/platform.ou.edu/%2B%2Betc%2B%2Bsite/Courses/Fall2014/CHEM%204970-200/SubInstances/200/NonAssignmentAssessmentItemsByOutlineNode",
                             headers ={"cookie": self.cookie,
                                      "Accept":"application/json"}
                          )  
        end = long(time.time()*1000)
        print "|login_NonAssignmentAssessmentItemsByOutlineNode:| %s | TIME: | %d | ms" % (r.status_code, end-start)                      
    
    @task(1)
    def login_eclipse_toc(self):
        queryid = self.guid()
        start = long(time.time()*1000)
        r=self.client.get("/content/sites/platform.ou.edu/CHEM4970_200_F_2014_Chemistry_of_Beer/eclipse-toc.xml?dc=1412271537", 
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/json"},
                          params = {"dc":"1412271537"}
					#, "queryID": queryid}                         
                          )
        end = long(time.time()*1000)
        print "|login_eclipse_toc| %s | TIME | %d | ms " % (r.status_code,  end-start)                              

    #@task(1)    
    def login_recursive_generate_data(self):
        queryid = self.guid()
        start=long(time.time()*1000)
        urlstring = "Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RecursiveUserGeneratedData?sortOn=createdTime&sortOrder=descending&accept=application%2Fvnd.nextthought.transcriptsummary%2Capplication%2Fvnd.nextthought.transcript&batchStart=0&batchSize=100"
        r=self.client.get("/dataserver2/users/%s/%s" % (self.username, urlstring), 
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/vnd.nextthought.collection+json"},
                          params = {"sortOn":"createdTime",
                                    "sortOrder":"descending",
                                    "accept":"application/vnd.nextthought.transcriptsummary,application/vnd.nextthought.transcript",
                                    "batchStart":"0",
                                    "batchSize":"100"}
                                   # "queryID": queryid}                         
                          )
        end = long(time.time()*1000)
        print "|login_recursive_generate_data| %s | TIME | %d | ms " % (r.status_code,  end-start)                              


    #@task(1)
    def login_othersMightbeInterested(self):
        queryid = self.guid()
        start=long(time.time()*1000)
        url = "Pages%28tag%3Anextthought.com%2C2011-10%3ARoot%29/RUGDByOthersThatIMightBeInterestedIn?batchBefore=&batchSize=50"
        r=self.client.get("/dataserver2/users/%s/%s" % (self.username, url),
                          headers ={"cookie": self.cookie,
                                    "Accept":"application/vnd.nextthought.collection+json"},
                          params = {"batchBefore":"",
                                    "batchSize":"50"}
                                    #"queryID": queryid}                         
                          )
        end = long(time.time()*1000)
        print "|login_othersMightbeInterested| %s | TIME| %d |ms " % (r.status_code, end-start)                              
                          
                          
    
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
                                     "Cookie": self.cookie,
                                     "Pragma": "no-cache",
                                     "Referer":"https://ou-alpha.nextthought.com/app/",
                                     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
                                     },
                             data = json.dumps({"NTIID":nttid }) 
                             ) 
        print "open enrolled in course nttid:%s  STATUS: %s %s %s" %(nttid, r.status_code, self.username, self.cookie)
        
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
        print "drop course nttid: %s response: %s " %(nttid, r.status_code)

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
        
    def log_out(self):
        pass
    
    
    def guid(self):
        chars = string.ascii_letters
        hostname = socket.gethostname()
        mname = hostname.replace('.local', '')
        user = ''.join(random.choice(chars) for _ in range(15))
        t = str( long( time.time() * 1000 ))
        name = "%s%s%s" % (mname, user, t)       
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

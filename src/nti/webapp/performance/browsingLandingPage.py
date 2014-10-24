# This locust test script example will simulate a user 
# browsing the Locust documentation on http://docs.locust.io

import random
from locust import HttpLocust, TaskSet, task, Locust
from pyquery import PyQuery
from requests.auth import HTTPBasicAuth
import base64
import string
import json
import uuid
import time
import random
import socket
import hashlib
import os


class account_creation(TaskSet):
    random_user=None
    random_pass = None
    random_user_name = None
    host=None

    def on_start(self):
        chars = string.ascii_letters
        user = ''.join(random.choice(chars) for _ in range(15))       
        self.random_user = "LR%s" % user
        t = str(long(time.time())*1000)
        self.random_user_name=self.guid()
        self.random_pass = 'test1234'    

        
    @task(20)
    def preflight_check(self):
        username = self.guid()
        #print "PREFLIGHT CHECK WITH username: %s" % username
        response = self.client.post("/dataserver2/account.preflight.create", 
                                    headers= {"Content-Type": "application/json"},
                                    data=json.dumps({"Username": username,
                                                     "email": self.guidName()+"Julie.zhu@nextthought.com",
                                                     "opt_in_email_communication": "true",
                                                     "realname": "%s %s" % (self.guidName(), self.guidName()) }))
        if (response.status_code!=200):
            print "account creation PREFLIGHT check response: %s %s " % (username, response.status_code)
     
    @task(2)
    def account_create(self):
        rand_user=self.guid()
        start = long( time.time() * 1000 )
        r = self.client.post("/dataserver2/account.create", 
                                    headers= {"Content-Type": "application/json; charset=UTF-8"},
                                    data=json.dumps({"Username": rand_user,
                                                     "email": self.guidName() +"Julie.zhu@nextthought.com",
                                                     "opt_in_email_communication": "false",
                                                     "password": "test1234",
                                                     "realname": "%s %s" %(self.guidName(), self.guidName()) }))        
        end = long( time.time() * 1000 )
        print "account creation FINAL response: %s %s TIME:%dms" % (rand_user, r.status_code, end-start)   
        #print "account creation FINAL header: %s" %r.headers 
        header = r.headers
        cookie = header['set-cookie']
        #print "cookies: %s " % cookie
        keys = cookie.split(":")
        key = keys[0]
        tkts = key.split(";")
        tkt = keys[0]
        
        #print "cookie created: %s; %s; username=%s" % (keys, keys, self.random_user)
        time.sleep(random.randrange(3, 30))
        
        
        
        #log out 
        request_string = None
        if self.host == "https://performance.nextthought.com":
            request_string = "/dataserver2/logon.logout"
            #request_string = "/dataserver2/logon.logout?success=https%3A%2F%2Fperformance.nextthought.com%2Fapp%2F"
            #r = self.client.get("/dataserver2/logon.logout?success=https%3A%2F%2Fperformance.nextthought.com%2Fapp%2F",
            #                            headers={"Cookie": '%s; %s; username=%s' % (keys, keys, rand_user)})
        elif self.host == "https://ou-alpha.nextthought.com":
            request_string = "/dataserver2/logon.logout?success=https%3A%2F%2Fou-alpha.nextthought.com%2Fapp%2F"
            #r = self.client.get("/dataserver2/logon.logout?success=https%3A%2F%2Fou-alpha.nextthought.com%2Fapp%2F",
            #                        headers={"Cookie": '%s; %s; username=%s' % (keys, keys, rand_user)})
        #print "account creation LOGOUT response: %s %s " % (rand_user, r.status_code)
        index = 3

        while (index>0):
            index = index-1
            start = long( time.time() * 1000 )
            with self.client.get(request_string,
                                headers={"Cookie": '%s; %s; username=%s' % (keys, keys, rand_user)},
                                catch_response=True) as response:
                end =long( time.time() * 1000 )
                if response.status_code == 200 or response.status_code==204:
                    print "account creation LOGOUT response: %s %s TIME:%dms" % (rand_user, response.status_code, end-start)
                    break
                elif index>=1:
                    print "LOGOUT for %s failed!!!!, retry %s after 10 seconds. ERROR: %s %s TIME: %dms" % (rand_user, index, response.status_code, response.content, end-start)
                    time.sleep(10)
                else:
                    print "exhausted retry for %s, killing this locust session and pawn off a new one..." % rand_user 
        
        self.interrupt() 
        
    @task(1)
    def stop(self):
        self.interrupt()  
        
                
    def guid(self):
        chars = string.ascii_letters
        hostname = socket.gethostname()
        mname = hostname.replace('.local', '')
        user = ''.join(random.choice(chars) for _ in range(15))
        t = str( long( time.time() * 1000 ))
        name = "%s%s%sLR" % (user, mname, t)       
        return name    
     
    def guidName(self):
        chars = string.ascii_letters
        hostname = socket.gethostname()
        mname = hostname.replace('.local', '')
        user = ''.join(random.choice(chars) for _ in range(15))
        name = "%s%s" % (user, mname)       
        return name   
    
               
class BrowseDocumentation(TaskSet):
    host = None
    def on_start(self):
        print "using host %s" % self.host 

        # assume all users arrive at the index page
        #self.index_page()
        #self.urls_on_current_page = self.toc_urls

    tasks = {account_creation:30}
       
    #@task(100)
    def index_page(self):
        start = long(time.time()*1000)
        with self.client.get("/landing/index.html", catch_response=True) as response:
            end = long(time.time()*1000)
            if response.status_code==403:
                response.success()
            elif response.status_code ==200:
                pg= PyQuery(response.content)
                print "landing page title captured: %s on HOST: %s TIME: %dms" % (pg("title").text(), self.host, end-start)
            else:
                print "landing page FAILURE!!!!! %s %s TIME:%dms" % (response.status_code, response.content, end-start)
  

    #@task(3)   
    def phantomjs_execution (self):
        index = random.randint(1, 30)
        username = "performance%d" % index
        print "executing phantomjs................"
        start = long(time.time()*1000)
        os.system('phantomjs loadwaitingtest.js '+ self.host +'/login '+username)    
        end = long(time.time()*1000)
        print "executing phantomjs complete TIME: %dms" % (end-start)

        
    def login (self):
        r = self.client.get("/login/", )
        pg = PyQuery(r.content)
        element = pg('body')
        print "Login page captured: %s %s" % (self.host, element.text())
        print r.status_code
        username = 'alpha_fivems_tester_2'
        #creating basic authentication string using username and password
        base64string = base64.encodestring('%s:%s' % (username, 'test1234'))[:-1]
        print base64string
        r = self.client.get("/dataserver2/logon.nti.password?username=%s" % username, 
                            headers={"Authorization": "Basic %s" % base64string})
        print "authentication response: %s " % (r.status_code)
        header = r.headers
        cookie = header['set-cookie']
        #print "cookies: %s " % cookie
        keys = cookie.split(";")
        tkt = keys[0]
        print "got tkt: %s" % tkt
        r = self.client.get("/dataserver2/logon.ping",
                            headers={"Cookie": '%s; %s; username=%s' % (keys, keys, username),
                                     })
        print "handshake after authenticating: %s" % (r.status_code)
        #print "handshake header after authenticating %s" % (r.headers)
        #print "handshake content after authenticating %s" % (r.content)
     
    #@task(1000)
    def static_ping (self):
        start = long(time.time())
        response = self.client.get("/login/resources/css/site.css?v=20141014105701") 
        end = long(time.time())
        if (response.status_code!=200):
            print "%s %s %d" %(response.status_code, response.content, end-start)
      
    @task(20)
    def ping (self):
        start = long(time.time())
        response = self.client.get("/dataserver2/logon.ping")
        end = long(time.time())
        if (response.status_code !=200):
            print "ping response: %s TIME: %dms" % (response.status_code, (end-start))
        
    @task(10)
    def handshake (self):       
        chars = string.ascii_uppercase+string.lowercase+string.digits
        username = ''.join(random.choice(chars) for _ in range(10))
        response = self.client.post("/dataserver2/logon.handshake", {"username": username, "password":"", "remember": "false"})
        #print "handshake username: %s %s" % (username, response.status_code)



class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation
    #host = "https://ou-alpha.nextthought.com"
    host = "https://performance.nextthought.com"   
    BrowseDocumentation.host = host
    account_creation.host=host
    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 20 and 600 seconds), since there's a bunch of text 
    # on each page
    min_wait = 3*1000
    max_wait = 10*1000 

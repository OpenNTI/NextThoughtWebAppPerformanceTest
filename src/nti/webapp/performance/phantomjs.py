# This locust test script example will simulate a user 
# browsing the Locust documentation on http://docs.locust.io

import random
from locust import HttpLocust, TaskSet, task
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



        
class BrowseDocumentation(TaskSet):
    host = None
    def on_start(self):
        pass

    
    @task(100)   
    def phantomjs_execution (self):
        index = random.randint(1, 30)
        username = "performance%d" % index
        print "executing phantomjs................"
        start = long(time.time()*1000)
        os.system('phantomjs loadwaitingtest.js '+ self.host +'/login '+username)    
        end = long(time.time()*1000)
        print "executing phantomjs complete TIME: %dms" % (end-start)
        
 
class PhantomUser(HttpLocust):
    task_set = BrowseDocumentation
    #host = "https://ou-alpha.nextthought.com"
    host = "https://performance.nextthought.com"   
    BrowseDocumentation.host = host
    
    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 20 and 600 seconds), since there's a bunch of text 
    # on each page
    min_wait = 3  * 1000
    max_wait = 6 * 1000


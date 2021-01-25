# Locust Performance Testing NT

## Introduction
This package contains various locust scripts for performance testing purpose.
In order for scripts to work, you must have locust installed:
[Instructions to install Locust](https://docs.locust.io/en/stable/installation.html)

## How to run the scripts

### To start the locust server: locust -f path_to_file
```bash
yunzhu@Yuns-MacBook-Pro workspace % locust -f NextThoughtWebAppPerformanceTest/src/nti/webapp/locust/user_login/locust_stress.py
[2020-08-10 15:38:01,702] Yuns-MacBook-Pro.local/INFO/locust.main: Starting web interface at http://:8089
[2020-08-10 15:38:01,712] Yuns-MacBook-Pro.local/INFO/locust.main: Starting Locust 1.1.1

### --step-load flag Allows more control on how many user can be spawn in how long of interval
yunzhu@Yuns-MacBook-Pro locust % locust -f user_assignment/skillUSA-postgres_test01_nextthot_com.py --step-load
[2021-01-24 22:45:41,164] Yuns-MacBook-Pro.local/INFO/locust.main: Starting web interface at http://:8089
[2021-01-24 22:45:41,172] Yuns-MacBook-Pro.local/INFO/locust.main: Starting Locust 1.1.1
```

## To kick off a run
go to: [http://localhost:8089](http://localhost:8089) and specify follow:
1. total number of users to spawn
2. how many user to spawn every second
3. target URL for the test to run on

if you are using --step-load flag when starting locust server, you'd need to specify 2 additional params:
1. step-users: number of users to spawn during each step
2. step-time: amount of time (s) to wait before going to next step

## What tests are available?
There are 4 types of tests you can run and separated by self explaining folder names
```bash
drwxr-xr-x  5 yunzhu  staff   160B Aug 10 13:30 user_assignment/
drwxr-xr-x  3 yunzhu  staff    96B Aug 10 13:30 user_creation/
drwxr-xr-x  7 yunzhu  staff   224B Aug 10 13:39 user_enrollment/
drwxr-xr-x  5 yunzhu  staff   160B Aug 10 16:25 user_login/
```
Most of the file names are straight-forward except for user_enrollment:
```bash
drwxr-xr-x  7 yunzhu  staff   224B Aug 10 13:39 ./
drwxr-xr-x  8 yunzhu  staff   256B Aug 10 13:30 ../
-rw-r--r--  1 yunzhu  staff   122K Jul 27 19:44 enrollment-alpha_nextthought_com.py
-rw-r--r--  1 yunzhu  staff   106K Jul 29 19:44 postgres_enrollment-postgres_test01_3_per_user_nextthot_com.py
-rw-r--r--  1 yunzhu  staff   106K Jul 29 19:31 postgres_enrollment-postgres_test01_nextthot_com.py
-rw-r--r--  1 yunzhu  staff   297K Jul 30 20:13 postgres_multienrollment-postgres_test01_nextthot_com.py
```
`postgres_enrollment-postgres_test01_3_per_user_nextthot_com.py` allows each user to randomly select 3 courses from the
site and enroll.

> Due to the nature of these calls, course, assignments are very specific to environment. So please pay attention to the
environment defined in the file name.

## Convenience scripts
under scripts folder we have also added helper scripts to aid performance testing:
```bash
-rw-r--r--   1 yunzhu  staff     0B Aug 10 13:16 __init__.py
drwxr-xr-x   8 yunzhu  staff   256B Aug 10 13:30 locust/
drwxr-xr-x  10 yunzhu  staff   320B Aug 10 13:16 performance/
drwxr-xr-x   3 yunzhu  staff    96B Aug 10 16:34 scripts/
yunzhu@Yuns-MacBook-Pro webapp % ll scripts
total 8
drwxr-xr-x  3 yunzhu  staff    96B Aug 10 16:34 ./
drwxr-xr-x  6 yunzhu  staff   192B Aug 10 16:32 ../
-rwxr--r--  1 yunzhu  staff   1.4K Jul 30 15:02 dropAllStudenthttp.sh*
```
`dropAllStudenthttp.sh` drops all students from list of courses defined in the script given correct connection token.


## Tools to collect http calls
[locust.replay](https://github.com/zlorb/locust.replay) is a good tool to use for collecting needed locust steps from certain UI action sequence
In order for this tool to work, we need to setup [mitmproxy](https://docs.mitmproxy.org/stable/overview-getting-started/)
Here are some basic steps we need to follow for things to work:


#### Step 1. install mitmproxy

```bash
pip3 installl mitmproxy
```

#### Step 2. install mitmproxy certificate

see [instruction](https://docs.mitmproxy.org/stable/concepts-certificates/)

`Note: I had this done a while back, so the instructions have changed slightly. But if installed successfully, you should
 see mitmproxy certificate in your keychains app.`


#### Step 3. Configure proxy

- Go to System Preferences > Network > Advanced... > Proxies
- Select 'Secure Web Proxy (HTTPS)'
- Enter 127.0.0.1:8080 as Secure Web Proxy Server setup
- Once you apply that change, all network traffic will route to 127.0.0.1:8080


#### Step 4. Start mitmproxy server

To test if it is working you can start up mitmproxy server
```bash
mitmproxy --anticache
```
go to any URL from browser and you should see network traffic flowing in the terminal window. now quit the server and
issue following command:
```bash
 mitmdump --anticache -s <path>/locust_extractor.py --set filename_prefix=<prefix>
```
This will dump all netwwork traffic and add each network call as task in a locust readable file. That file with some
manipulation can be used to replay in locust as is.








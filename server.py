#!/usr/bin/python
#-*- coding: utf-8 -*-
# NASA Space Apps
# server for BlueMix  
# author:  Claude Falbriard 
# date:    Apr. 12 2015
# version: 1.5 
# purpose:  mini-web app 
# desined for Internet domain: spaceappsalgae.mybluemix.net
# hosted by IBM Bluemix
from bottle import static_file, route, run, request, response 
import requests
from requests.exceptions import ConnectionError
from requests.auth import HTTPBasicAuth
import urllib
import json
import os
# HTTPS authentication 
#from http.client import HTTPSConnection for Python 3
from httplib import HTTPSConnection # for Python 2.7
from base64 import b64encode
# reset page counters
global frontpage_count
frontpage_count = 0
global staticpage_count
staticpage_count = 0
#
code = '' 
# access with http://localhost:8080/static/index.html
global mypath
mypath = os.path.dirname(os.path.realpath(__file__))
print "Server variable - mypath : " + str(mypath)
# load Bluemix variables
PORT = int(os.getenv('VCAP_APP_PORT', '8000'))
HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
#
print "Bluemix server URI used by route: " + str(HOST)
print "Bluemix dynamic port URI used by route: " + str(PORT)
#
@route('/')
def root():
    global frontpage_count	
    frontpage_count += 1	
    return static_file('/index.html', root=mypath)
#@route('/index.html')
#def frontpage():
#    return static_file('/index.html', root=mypath)  
@route('/static/<filename>')
def server_static(filename):
    global staticpage_count	
    staticpage_count += 1	
    global mypath	
    return static_file(filename, root=mypath)
@route('/images/<filename>')
def images_static(filename):
    global mypath	
    return static_file(filename, root=mypath + "/images")
@route('/statistics')
def statistics():
    global frontpage_count
    global staticpage_count    
    statpage = """
<HTML>
<HEAD>
<style> 
@font-face {
    font-family:"Jalane";
    src: url("/static/jalane_light.ttf") /* TTF file for CSS3 browsers */
}
p {
font-family:'Jalane', sans-serif;
font-size: 18px;
font-weight:bold;
color:white;
margin-left:20px;
margin-bottom:30px;
text-decoration: none;
a:link {color:white;};      /* unvisited link */
a:visited {color:white !important;};  /* visited link */
a:hover {color:white !important;};  /* mouse over link */
a:active {color:white;};
}
</style>
</HEAD>
<BODY bgcolor="1a1a1a" vlink="#c0c0c0" alink="#c0c0c0" link="#c0c0c0" text="#c0c0c0">
<style type="text/css">
    a:link { text-decoration:none; color: white;}
    a:hover { color: white;}
    a:visited { color: white; }
</style>
<text> 
<br><br>
Traffic Statistics for Space Apps Algae Web Site<br><br>

Front Page Access Count: """ + str(frontpage_count)  + "<br><br>" \
    "Static Page Access Count:  " + str(staticpage_count) + "<br><br>" + \
    "or contact Web Page Admin at e-mail: falbriard@aol.com<br><br>" + \
    "</text></BODY></HTML>"
    return statpage    
# To execute under the Bluemix, use      
run(host=HOST, port=PORT)
# to execute under localhost
#run(host='localhost', port=8080)
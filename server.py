#!/usr/bin/python
#-*- coding: utf-8 -*-
# NASA Space Apps
# server for BlueMix  
# author:  Claude Falbriard 
# date:    Apr. 11 2015
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
    return static_file('/index.html', root=mypath)
#@route('/index.html')
#def frontpage():
#    return static_file('/index.html', root=mypath)  
@route('/static/<filename>')
def server_static(filename):
    global mypath	
    return static_file(filename, root=mypath)
@route('/images/<filename>')
def images_static(filename):
    global mypath	
    return static_file(filename, root=mypath + "/images")
# URI to test    
#https://oauthaqua1.mybluemix.net/resources/oauth2Callback?code=x...x  
#http://localhost:8080/resources/oauth2Callback?code=x...x
# test it with initial Web request: 
# https://idaas.ng.bluemix.net/sps/oauth20sp/oauth20/authorize?client_id=BukWRqSkD0qbO5ooesHU&response_type=code&scope=profile&redirect_uri=https://oauthaqua1.mybluemix.net/resources/oauth2Callback&requestedAuthnPolicy=http://www.ibm.com/idaas/authnpolicy/basic
# To execute under the Bluemix, use      
run(host=HOST, port=PORT)
# to execute under localhost
#run(host='localhost', port=8080)
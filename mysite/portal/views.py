from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.views import logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
#from django.contrib.auth import logout
import google_auth_oauthlib.flow
import googleapiclient.discovery
from oauth2client import file, client, tools
from oauth2client.file import Storage
from google_auth_oauthlib.flow import Flow
import google.oauth2.credentials
import httplib2
import os
import requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPILCATION_NAME = 'Google Calendar'
CREDENTIAL=""


def set_credentials():
    try:
        import argparse
        flags = tools.argparser.parse_args([])
    except ImportError:
        flags = None
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if True or ( not credentials or credentials.invalid):
        flow = OAuth2WebServerFlow(client_id='1065322067496-bqpqmcirs9u93qt5tl5n5ef4aehne2rp.apps.googleusercontent.com',
                                   client_secret='Kilf5fDJud2oElH3Dgs1PzA6',
                                   scope=SCOPES,
                                   redirect_uri='http://localhost:8000/')
#        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE,
#                                       scope=SCOPES,
#                                       redirect_uri='http://localhost:8000')
        flow.user_agent = APPILCATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
        print(credentials)
    global CREDENTIAL
    CREDENTIAL = credentials


# Create your views here.
def first_page(request):
    return render(request, 'portal/firstPage.html')

def home(request):
    return render(request, 'portal/home.html')

def login(request):
    set_credentials()
    credentials = CREDENTIAL
    http = credentials.authorize(httplib2.Http())
    print('login')
    return render(request, 'portal/home.html')

def logout(request):
    global CREDENTIAL
    credentials = CREDENTIAL
    h = httplib2.Http()
    credentials.revoke(h)
    CREDENTIAL = ""
    print(credentials)
    return render(request,'portal/firstPage.html')

#what is login page

def calendar(request):
    return render(request, 'googlecalendar/calendar.html')
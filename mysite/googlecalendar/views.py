from __future__ import print_function
from django.shortcuts import render
import httplib2
import os
import sys
import datetime
from googleapiclient import sample_tools
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import discovery
from apiclient.discovery import build
from .models import Calendar
from oauth2client.file import Storage
from django.http import HttpResponse

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPILCATION_NAME = 'Google Calendar'

def get_credentials():
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
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPILCATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def calendar(request):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    now = '2016-01-01T01:01:01.000001Z'
    print(now)
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=100, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    cal_list = []
    count = 1
    if not events:
        print('No upcoming events found.')
    for event in events:
        #print(count)
        name=event['summary']
        print('title : ', name)
        #loc=event['location']
        #print('location : ', loc)
        dat=event['start'].get('dateTime')
        print('date : ',dat[0:10])
        #calendar = Calendar(title = name, date=dat[0:10], location=loc)
        calendar = Calendar(title=name, date=dat[0:10])
        cal_list.append(calendar)
        count+=1
    context = {'Calendar_list':cal_list}
    return render(request, 'googlecalendar/calendar.html', context)
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
import flask
import requests
from oauth2client.client import flow_from_clientsecrets

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPILCATION_NAME = 'Google Calendar'
CREDE=""


def get_credentials():
    try:
        import argparse
        flags = tools.argparser.parse_args([])
    except ImportError:
        flags = None
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPILCATION_NAME = 'Google Calendar'
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if True or ( not credentials or credentials.invalid):
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES,redirect_uri='http://localhost:8000/')
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE,
                                       scope=SCOPES,
                                       redirect_uri='http://localhost:8000/')
        flow.user_agent = APPILCATION_NAME
        print('1000000000000')
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
        print(credentials)
    print('2000000000000')
    print(type(credentials))
    return credentials


# Create your views here.
def first_page(request):
    return render(request, 'portal/firstPage.html')

def home(request):
    return render(request, 'portal/home.html')

def login(request):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    print('login')
    return render(request, 'portal/home.html')

def logout(request):
    """
    app = flask.Flask(__name__)
    app.run('localhost', 8080, debug=True)
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE, scopes=SCOPES,state = state)
    flow.redirect_uri = 'https://www.example.com/oauth2callback'
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scope=['https://www.googleapis.com/auth/youtube.force-ssl'],
        state=state
    )
    authorization_response = flask.url_for('oauth2callback', _external = True)
    flow.fetch_token(authorization_response=authorization_response)

    credentials=flow.credentials
    flask.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}
    """

    credentials = get_credentials()
    h = httplib2.Http()
    credentials = credentials.get_access_token(h)

    if 'credentials' not in flask.session:
        return ('You need to <a href="/authorize">authorize</a> before ' +
        'testing the code to revoke credentials.')

    print(credentials)
    revoke=requests.post('https://accounts.google.com/o/oauth2/revoke',
                  params={'token': credentials.token},
                  headers = {'content-type': 'application/x-www-form-urlencoded'})
    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        return('Credentials successfully revoked.')
    else:
        return('An error occurred.')
    #logout(request) #Recursive Error

#    print('logout')
#    return render(request, 'portal/firstpage.html')
#    return redirect('/')

#auth_logout(request)
#   return render_to_response('portal/home.html', {}, RequestContext(request))

def calendar(request):
    return render(request, 'googlecalendar/calendar.html')
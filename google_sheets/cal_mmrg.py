from __future__ import print_function

import datetime
import os.path
import pickle

import yaml
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def get_books():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_cal.pickle'):
        with open('token_cal.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials_cal.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_cal.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime(2000, 1, 1).isoformat() + 'Z'  # 'Z' indicates UTC time
    print(now)

    events_result = service.events().list(calendarId="ualberta.ca_iuhi2j1tjpviabe54hjqaetcac@group.calendar.google.com",
                                          timeMin=now,
                                          maxResults=1000, singleEvents=True,
                                          orderBy='startTime').execute()

    events = events_result.get('items', [])
    parser = HTMLParser()
    cal_events = {}
    keys = ["htmlLink", "start", "description"]
    for event in events:
        # print(event)
        data_event = yaml.safe_load(strip_tags(event["description"].replace("<br>", "\n")))

        # print(yaml.safe_load(event["description"]))
        event_keys = event.keys()
        active_keys = []
        for key in keys:
            if key in event.keys():
                active_keys.append(key)
            else:
                continue
        # print(active_keys, keys)
        data_event["htmlLink"] = event["htmlLink"]
        cal_events[event["summary"]] = list(data_event.values())
        # if len(active_keys) == len(keys):
        #     for k in active_keys:
        #         if k == "description":
        #             cal_events[event["summary"]] = data_event
        #         else:
        #             cal_events[event["summary"]] = event[k]
    # print(cal_events)
    return cal_events


if __name__ == "__main__":
    get_books()

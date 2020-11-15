import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def auth_flow():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def get_spreadsheet_values(spreadsheetId, spread_range):
    creds = auth_flow()
    service = build('sheets', 'v4', credentials=creds)
    ss_values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=spread_range).execute()
    return ss_values


def write_spreadsheet_values(spreadsheetId, spread_range, values):
    creds = auth_flow()
    service = build('sheets', 'v4', credentials=creds)
    body = {'values': values}
    response = service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId, range=spread_range, valueInputOption='RAW', body=body).execute()
    print('{0} cells updated.'.format(response.get('updatedCells')))

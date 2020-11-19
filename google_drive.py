import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']


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


def get_drive_files(product_name):
    file_ids = []
    links = []
    creds = auth_flow()
    service = build('drive', 'v3', credentials=creds)
    results = service.files().list(
        q=f"name contains '{product_name}' and trashed = false", fields="nextPageToken, files(id, name, webViewLink)").execute()
    for file in results['files']:
        file_ids.append(file['id'])
        links.append(file['webViewLink'])
    return (file_ids, links)


def create_permissions(file_id):
    creds = auth_flow()
    service = build('drive', 'v3', credentials=creds)
    user_permission = {
        'type': 'anyone',
        'role': 'reader'
    }
    results = service.permissions().create(
        fileId=file_id, body=user_permission, fields='id').execute()
    if results != {'id': 'anyoneWithLink'}:
        print('Permissions change was unsuccessful')
        return
    return True


def google_processing(listing_title):
    file_ids_links = get_drive_files(listing_title)
    for file in file_ids_links[0]:
        create_permissions(file)
    return file_ids_links[1]

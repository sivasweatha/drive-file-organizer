from Google import Create_Service
import os

path = r"C:\Users\hp\Pictures\Camera"

SCOPE = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'

service = Create_Service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPE)
folder_id = '1kyHyQZnS-vHeSVHRVxIpO77k82Lluyjo'

query = f"parents  = '{folder_id}'"

response = service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query, pageToken=nextPageToken).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')
i = 0
for file in files:
    print(f"Found file {i}: {file['name']}")
    i += 1

l = os.listdir(path)
print(l)
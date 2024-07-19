from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd

CLIENT_SECRETS_PATH = 'C:\\Users\\tmana\\OneDrive\\Desktop\\analytics\\working\\client_secret_446483660750-02367vkpk841cf8cn4br0l31hke34trv.apps.googleusercontent.com.json' # your google cient key from cloud
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def authenticate_google_account():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_PATH, SCOPES)
    credentials = flow.run_local_server(port=8080)
    site_url = 'https://techieresearch.blogspot.com/'
    service = build('webmasters', 'v3', credentials=credentials)
    return service, site_url

def get_search_console_data(service, site_url):
    request = {
        'startDate': '2024-05-01',
        'endDate': '2024-05-07',
        'dimensions': ['query'],
        'rowLimit': 1000
    }
    response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
    if 'rows' not in response:
        print('No data available for the given date range.')
        return pd.DataFrame()
    rows = response['rows']
    data = []
    for row in rows:
        data.append([row['keys'][0], row['clicks'], row['impressions'], row['ctr'], row['position']])
    df = pd.DataFrame(data, columns=['Top queries', 'Clicks', 'Impressions', 'CTR', 'Position'])
    return df

def main():
    service, site_url = authenticate_google_account()
    data = get_search_console_data(service, site_url)
    return data

if __name__ == '__main__':
    data = main()
    print(data)

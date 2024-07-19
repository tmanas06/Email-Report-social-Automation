import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.oauth2 import service_account

# Set up global variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\tmana\\OneDrive\\Desktop\\analytics\\wh-work-424210-5530b9fc03be.json' # your google service account key
property_id = '445428510'

# Load the credentials from the service account key file
try:
    credentials = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
    print("Service account authenticated successfully.")
except Exception as e:
    print("Failed to authenticate service account:", e)

# Instantiate the client using the authenticated session
try:
    client = BetaAnalyticsDataClient(credentials=credentials)
    print("Client instantiated successfully.")
except Exception as e:
    print("Failed to instantiate client:", e)

# Format Report - run_report method
def format_report(request):
    try:
        response = client.run_report(request)
        for row in response.rows:
            print(row.dimension_values[0].value, row.metric_values[0].value)
        print("Report ran successfully.")
    except Exception as e:
        print("Failed to run report:", e)

# Prepare the request
request = RunReportRequest(
    property=f"properties/{property_id}",
    date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
    dimensions=[Dimension(name="city")],
    metrics=[Metric(name="activeUsers")]
)

# Call the function with the request
try:
    format_report(request)
except Exception as e:
    print("Failed to call format_report:", e)
import os
import numpy as np
import pandas as pd
from datetime import date, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest, OrderBy

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\tmana\\OneDrive\\Desktop\\analytics\\working\\wh-work-424210-5530b9fc03be.json' # your google service account key
property_id = '445428510'
client = BetaAnalyticsDataClient()

def format_report(request):
    response = client.run_report(request)
    
    row_index_names = [header.name for header in response.dimension_headers]
    row_header = []
    for i in range(len(row_index_names)):
        row_header.append([row.dimension_values[i].value for row in response.rows])
    
    row_index_named = pd.MultiIndex.from_arrays(np.array(row_header), names=np.array(row_index_names))
    
    metric_names = [header.name for header in response.metric_headers]
    data_values = []
    for i in range(len(metric_names)):
        data_values.append([row.metric_values[i].value for row in response.rows])
    
    output = pd.DataFrame(data=np.transpose(np.array(data_values, dtype='f')),
                          index=row_index_named, columns=metric_names)
    return output

def main():
    request = RunReportRequest(
        property='properties/' + property_id,
        dimensions=[Dimension(name="month"), Dimension(name="sessionMedium")],
        metrics=[Metric(name="averageSessionDuration"), Metric(name="activeUsers")],
        order_bys=[OrderBy(dimension={'dimension_name': 'month'}), OrderBy(dimension={'dimension_name': 'sessionMedium'})],
        date_ranges=[DateRange(start_date="2024-06-01", end_date="today")],
    )
    output_df = format_report(request)
    return output_df

if __name__ == '__main__':
    data = main()
    print(data)
import boto3
from datetime import datetime, timedelta

def get_cost_and_usage():
    client = boto3.client('ce', region_name='us-east-1')  # Make sure to replace with your region

    # Define time range for the query (current month)
    start_date = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    end_date = start_date.replace(month=start_date.month + 1)

    # Format dates for API request
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Get cost and usage data
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date_str,
            'End': end_date_str
        },
        Granularity='MONTHLY',
        Metrics=['BlendedCost']
    )

    # Print the result
    print(f"Cost for the current month: {response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']} {response['ResultsByTime'][0]['Total']['BlendedCost']['Unit']}")

if __name__ == "__main__":
    get_cost_and_usage()
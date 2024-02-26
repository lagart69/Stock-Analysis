import requests
from datetime import datetime

# Load API key from .env file
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('B2ZQjbMYXTC_CvPPg71s')

# Define the API endpoint and parameters
url = f'https://data.nasdaq.com/api/v3/datasets/FSE/AFX_X.json'
params = {
    'api_key': API_KEY,
    'start_date': '2017-01-01',
    'end_date': '2017-12-31'
}

# Make the API request
response = requests.get(url, params=params)
data = response.json()

# Extract relevant data
daily_data = data['dataset']['data']
opening_prices = [day[1] for day in daily_data if day[1] is not None]

# Calculate highest and lowest opening prices
highest_opening = max(opening_prices)
lowest_opening = min(opening_prices)

print(f"Highest Opening Price: {highest_opening}")
print(f"Lowest Opening Price: {lowest_opening}")

# Calculate largest change in one day (based on High and Low price)
daily_changes = [day[2] - day[3] for day in daily_data if day[2] is not None and day[3] is not None]
largest_change_one_day = max(daily_changes)

print(f"Largest Change in One Day: {largest_change_one_day}")

# Calculate largest change between any two days (based on Closing Price)
closing_prices = [day[4] for day in daily_data if day[4] is not None]
change_between_days = [abs(closing_prices[i] - closing_prices[i - 1]) for i in range(1, len(closing_prices))]
largest_change_two_days = max(change_between_days)

print(f"Largest Change Between Any Two Days: {largest_change_two_days}")

# Calculate average daily trading volume
trading_volumes = [day[6] for day in daily_data if day[6] is not None]
average_trading_volume = sum(trading_volumes) / len(trading_volumes)

print(f"Average Daily Trading Volume: {average_trading_volume}")

# Calculate median trading volume
sorted_trading_volumes = sorted(trading_volumes)
n = len(sorted_trading_volumes)

if n % 2 == 0:
    median_trading_volume = (sorted_trading_volumes[n // 2 - 1] + sorted_trading_volumes[n // 2]) / 2
else:
    median_trading_volume = sorted_trading_volumes[n // 2]

print(f"Median Trading Volume: {median_trading_volume}")
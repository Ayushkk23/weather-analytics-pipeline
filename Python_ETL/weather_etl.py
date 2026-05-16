import requests
import snowflake.connector

# Weather API
API_KEY = "YOUR_API_KEY"
CITY = "Hyderabad"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=yes"

response = requests.get(url)
data = response.json()

# Extract Data
location = data['location']
current = data['current']

# Snowflake Connection
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT_IDENTIFIER',
    warehouse='COMPUTE_WH',
    database='WEATHER_DB',
    schema='WEATHER_SCHEMA'
)

cur = conn.cursor()

# Insert Query
insert_query = f"""
INSERT INTO CURRENT_DATA VALUES (
'{location['name']}',
'{location['region']}',
'{location['country']}',
{current['temp_c']},
{current['feelslike_c']},
{current['humidity']},
{current['wind_kph']},
{current['pressure_mb']},
{current['precip_mm']},
{current['vis_km']},
{current['uv']},
{current['air_quality']['co']},
{current['air_quality']['no2']},
{current['air_quality']['o3']},
{current['air_quality']['so2']},
{current['air_quality']['pm2_5']},
{current['air_quality']['pm10']},
CURRENT_TIMESTAMP
)
"""

cur.execute(insert_query)

conn.commit()

print("Weather data inserted successfully!")

conn.close()
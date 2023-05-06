import requests
import datetime

# Define the OpenSky Network API endpoint and parameters
opensky_url = 'https://opensky-network.org/api/states/all'
icao_code = 'KJFK' # JFK International Airport
opensky_params = {
    'icao24': '',
    'time': ''
}

# Define the Google Maps API endpoint and parameters
google_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
origin = 'New York JFK International Airport'
destination = 'Times Square, New York'
google_params = {
    'origins': origin,
    'destinations': destination,
    'key': 'your_google_maps_api_key'
}

# Make the requests to the APIs and retrieve the data
opensky_response = requests.get(opensky_url, params=opensky_params).json()
google_response = requests.get(google_url, params=google_params).json()

# Extract the relevant data from the API responses
air_traffic = opensky_response['states']
road_traffic = google_response['rows'][0]['elements'][0]['duration']['text']

# Determine the peak times for air and road traffic
peak_air_traffic = max(air_traffic, key=lambda x: x[8]) # 8th index corresponds to the last contact time
peak_road_traffic = datetime.datetime.now().strftime('%H:%M:%S') # Current time

# Print the peak times for air and road traffic
print(f"Peak air traffic at {peak_air_traffic[8]}")
print(f"Peak road traffic at {peak_road_traffic} from {origin} to {destination} ({road_traffic})")


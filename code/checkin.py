#logic file for checkin
import requests
import json


def get_current_location(): #returns the lat and lng of the user's location 
    # Set up the request parameters
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCHFCLcZvBCRrkFPKDLtMUq_ijnTQ1aRXE"
    headers = {'content-type': 'application/json'}
    data = {}

    # Make the request to the API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the status code of the response
    if response.status_code != 200:
        return "Error: Request failed with status code " + str(response.status_code)

    # Parse the JSON response
    location = json.loads(response.content.decode('utf-8'))

    # Return the current location as a tuple of latitude and longitude
    return (location["location"]["lat"], location["location"]["lng"])

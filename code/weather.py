import requests

#find the region a location belongs in
def getRegion(lat, lng):
    if lat>1.472 or lat<1.158 or lng<103.600 or lng>104.090: #outside bounds of Singapore
        region='Not in Singapore'
        return region
    else:
        if lng>=103.897:
            region='East' #Use tampines forecast, ignoring pulau ubin as not connected to mainland
        elif lng<=103.762:
            if lat<=1.366:
                region='West' #Use jurong west forecast
            else: #lat>1.366:
                region='UluWest' #Use tengah forecast
        elif lng>103.762 and lng<103.897:
            if lat>=1.393:
                region='North' #Use Mandai
            elif lat<=1.260:
                region='Sentosa' #Use Sentosa
            elif lat>1.260 and lat<=1.338:
                region='South' #Use Tanglin
            else: #lat>1.338 and lat<1.393
                region='Central' #Use Bishan
        else:
            print(lat,lng)
            region='Error'
    return region

#air temperature
def getTemperature():
    url = 'https://api.data.gov.sg/v1/environment/air-temperature'
    response = requests.get(url)
    temperature=-69.6

    if response.status_code == 200:
        data = response.json()
        #print(data['metadata']['stations'])
        for aItem in data['metadata']['stations']: # 1 station at woodlands 1 at pulau ubin, ignore pulau ubin
            if aItem['id']=='S104':
                aSid=aItem['id']
                break
        #print(data['items'][0]['readings'])
        for aItem2 in data['items'][0]['readings']: #each item has station_id(same as id above), temperature in deg celcius(value), e.g {'station_id': 'S104', 'value': 29}
            if aItem2['station_id']==aSid:
                temperature=aItem2['value']
    else:
        print("Error retrieving data")
    if temperature==-69.6:
        print("Something went wrong with the API")
    return temperature

#rainfall, not used
def getRainfall(region):
     url = "https://api.data.gov.sg/v1/environment/rainfall"
     response = requests.get(url)

     if response.status_code == 200:
         data = response.json()
         print(data)
         for rItem in data['metadata']['stations']: #each item has id, device_id, name(e.g Alexandra Road), location{lat. , long.}, 
             # e.g {'id': 'S77', 'device_id': 'S77', 'name': 'Alexandra Road', 'location': {'latitude': 1.2937, 'longitude': 103.8125}}
             if rItem['id']=='S77':
                 print(rItem['id'])
                 break
         rSid=rItem['id']
         #print(rItem)
         for rItem in data['items'][0]['readings']: #each item has station_id(same as id above), rainfall(value) e.g {'station_id': 'S117', 'value': 0}
             if rItem['station_id']==rSid:
                 print("Rainfall =", rItem['value'])
                 #break
             if rItem['value']>0:
                 print("Station ID =", rItem['station_id'], "Rainfall =", rItem['value'])
     else:
         print("Error retrieving data")

#forecast
def getForecast(region):
    url = 'https://api.data.gov.sg/v1/environment/2-hour-weather-forecast'
    response = requests.get(url)

    location=''
    weather='Error'
    if region=='Error' or region=='Not in Singapore':
        print("Invalid region")
        return weather
    if response.status_code == 200:
        print(response.status_code)
        data = response.json()
        if 'forecasts' in data['items'][0]:
            if region=='North':
                location='Mandai'
            elif region=='UluWest':
                location='Tengah'
            elif region=='West':
                location='Jurong West'
            elif region=='Central':
                location='Bishan'
            elif region=='South':
                location='Tanglin'
            elif region=='East':
                location='Tampines'
            elif region=='Sentosa':
                location='Sentosa'
            #print(data['items'][0]['forecasts'])
            for fItem in data['items'][0]['forecasts']:
                if fItem['area']==location:
                    weather=fItem['forecast']
                    break
            if weather=='Error':
                print("Weather not found despite valid location, something went wrong with the API")
        else:
           # 'forecasts' key does not exist in the response dictionary
            print("No forecasts found in response")
            return "Error with API"
    else:
        print("Error retrieving data")
    return weather

#print(getForecast(getRegion(1.362582, 103.671071)))
#print(getTemperature())

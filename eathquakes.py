import requests
import csv

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
PARAMS = {
    "format": "geojson",
    "starttime": "2000-01-01",
    "endtime": "2023-12-31",
    "minmagnitude": 2,  
    "limit": 20000  
}

try:

    response = requests.get(URL, params=PARAMS)
    response.raise_for_status()
    data = response.json()


    earthquakes = data['features']
    
    
    with open('earthquakes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(['Time', 'Latitude', 'Longitude', 'Magnitude', 'Depth (km)', 'Place'])
        
        
        for earthquake in earthquakes:
            props = earthquake['properties']
            coords = earthquake['geometry']['coordinates']
            
            writer.writerow([
                props['time'],  
                coords[1],      
                coords[0],      
                props['mag'],   
                coords[2],      
                props['place']  
            ])

    print(f"Success! Saved {len(earthquakes)} earthquakes to earthquakes.csv")

except Exception as e:
    print(f"Error: {e}")

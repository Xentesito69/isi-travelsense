import sqlite3
import urllib.request
import json
import time

def fetch_coords():
    conn = sqlite3.connect('travelsense.db')
    c = conn.cursor()
    c.execute("SELECT id, nombre, pais FROM Destinos")
    dests = c.fetchall()
    
    city_coords = {}
    print("Fetching coordinates for", len(dests), "cities...")
    
    for row in dests:
        city_id, nombre, pais = row
        # Use Open-Meteo geocoding API which is fast and free without key
        query = urllib.parse.quote(nombre)
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={query}&count=1&language=es"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'TravelSense/1.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                if 'results' in data and len(data['results']) > 0:
                    lat = data['results'][0]['latitude']
                    lon = data['results'][0]['longitude']
                    city_coords[nombre] = [lat, lon]
                else:
                    print(f"No result found for {nombre}")
        except Exception as e:
            print(f"Error fetching {nombre}: {e}")
        
        # Small sleep to avoid overwhelming
        time.sleep(0.1)
        
    # Write the dictionary to a JS format file
    js_output = "const NEW_COORDS = {\n"
    for name, coords in city_coords.items():
        js_output += f'    "{name}": {coords},\n'
    js_output += "};\n"
    
    with open('coords.js', 'w', encoding='utf-8') as f:
        f.write(js_output)
    
    print("Done! Saved to coords.js")

if __name__ == "__main__":
    fetch_coords()

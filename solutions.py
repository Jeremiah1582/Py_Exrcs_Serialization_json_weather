import json
from datetime import datetime

# Assuming the JSON string is saved in weather_data.py as a variable named weather_data_str
from weather_data import data as weather_data_str

# 1) Reading and Deserializing Data:
data = json.loads(weather_data_str)

# 2) Data Extraction:
location = f"{data['coord']['lon']}°E, {data['coord']['lat']}°N"
weather_description = data['weather'][0]['description'].capitalize()
current_temp_kelvin = data['main']['temp']
wind_speed = data['wind']['speed']
sunrise = datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M %p')
sunset = datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M %p')

# 3) Data Transformation:
current_temp_celsius = current_temp_kelvin - 273.15
duration_of_daylight = datetime.utcfromtimestamp(data['sys']['sunset']) - datetime.utcfromtimestamp(data['sys']['sunrise'])
hours, remainder = divmod(duration_of_daylight.seconds, 3600)
minutes, _ = divmod(remainder, 60)

# 4) Serialization:
processed_data = {
    "Location": location,
    "Weather Description": weather_description,
    "Temperature": f"{current_temp_celsius:.2f}°C",
    "Wind Speed": f"{wind_speed} m/s",
    "Sunrise": sunrise,
    "Sunset": sunset,
    "Duration of Daylight": f"{hours} hours {minutes} minutes"
}

with open('processed_weather_data.json', 'w') as outfile:
    json.dump(processed_data, outfile, indent=4)

# 5) Display Information:
print("Location:", location)
print("Weather Description:", weather_description)
print(f"Current Temperature: {current_temp_celsius:.2f}°C")
print(f"Wind Speed: {wind_speed} m/s")
print("Sunrise:", sunrise)
print("Sunset:", sunset)
print("Duration of Daylight:", f"{hours} hours {minutes} minutes")

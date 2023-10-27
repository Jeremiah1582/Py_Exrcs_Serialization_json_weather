# Backstory:
You've just landed a job at WeatherVision, a startup that provides innovative weather solutions to various clients. Your company receives datasets like the one provided below from various weather APIs. Your manager just came in and gave you a task to extract, process, and transform the raw weather data to make it more understandable for your clients.

# Objective:
Write a Python program that serializes and deserializes the provided JSON data, and then performs various data processing tasks.

# Task:
1) Reading and Deserializing Data:
- Read the provided JSON data.
- Deserialize the data to a Python object using the json library.

2) Data Extraction:
- Extract the following data points:
    > Location (Latitude and Longitude)
    > Weather Description
    > Current Temperature
    > Wind Speed
    > Sunrise and Sunset time (Convert this from UNIX timestamp to readable format)

3) Data Transformation:
- Convert the temperature from Kelvin to Celsius.
- Calculate the duration of daylight (i.e., the difference between sunset and sunrise) and present it in hours and minutes.

4) Serialization:
-  Create a new dictionary with the processed data.
- Serialize the dictionary back to a JSON string.
- Save this JSON string to a new file named processed_weather_data.json.

5) Display Information:
- Once you have completed all the steps, display the extracted and processed information neatly for the user to read on the console.

# Tips:
- you will find the json string in the weather_data.py file
- Remember to import the json module.
- The formula to convert Kelvin to Celsius is: *C=K−273.15*
- For timestamp conversion, you may find Python's datetime module helpful.
- Always handle potential exceptions, especially when working with files and data conversions.

**Expected Output in terminal**

Location: 10.99°E, 44.34°N
Weather Description: Moderate rain
Current Temperature: 25.33°C
Wind Speed: 0.62 m/s
Sunrise: 04:36 AM
Sunset: 17:57 PM
Duration of Daylight: 13 hours 21 minutes


*for additional Reading on the pros and Cons of Serial/Deserialization*
https://www.baeldung.com/cs/serialization-deserialization
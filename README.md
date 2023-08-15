# python_project1

# Phone Number Location Finder

This script allows you to retrieve the geographical location and service provider information for a given phone number using various libraries and APIs. It uses the `phonenumbers` library to extract information from the phone number, the `opencage` library to obtain geolocation data, and `folium` to visualize the location on a map.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed
- Required Python libraries: `phonenumbers`, `opencage`, `folium`
  You can install them using this in terminal:
  pip install phonenumbers 
  pip install  opencage 
  pip install  folium




  
- An API key from [OpenCage](https://opencagedata.com/) to access their geocoding service.

## Usage

1. Define your phone number as a string variable `number`:

 ```python
 number = "+1234567890"  # Replace with your phone number



1>  Replace # Enter your opencage data API key with your actual OpenCage API key in the script.

2>  The script will output the following information:

Location description (country, region, etc.)
Service provider name
Latitude and longitude

3>  The script will also generate an HTML file named find_location.html that displays a map with a marker at the obtained latitude and longitude




import csv
import os
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
import os
import random
import requests

# possible countries to label
country_labels = ["Canada", "United States", "Japan", "Sweden", "France"]

# Base url for google maps api
base_url = "https://maps.googleapis.com/maps/api/streetview?"

# base directory
base_dir = os.path.dirname(os.path.dirname(__name__))

# map api key
maps_api_key = open("api_key.txt", "r").read()

# countries csv file
# countries_csv = pd.read_csv("countries.csv")

def generate_images():
    with open('countries.csv') as countries_csv:
        heading = next(countries_csv)
        countries_csv_reader = csv.reader(countries_csv)
        for row in countries_csv_reader:
            country_name = str(row[0])
            country_capital_lat = float(row[1])
            country_capital_lng = float(row[2])
            for i in range(0, 5):
                get_image(i, country_name, country_capital_lat, country_capital_lng)

# takes the latitude and longitude of a country's capital city and returns a streetview image from
# a radius around the capital
import csv
import os
import requests
import pandas as pd
from PIL import Image
from io import BytesIO
import os
import random
import requests

# possible countries to label
country_labels = ["Canada", "United States", "Japan", "Sweden", "France"]

# Base url for google maps api
base_url = "https://maps.googleapis.com/maps/api/streetview?"

# base directory
base_dir = os.path.dirname(os.path.dirname(__name__))

# map api key
maps_api_key = open("api_key.txt", "r").read()

def generate_images():
    with open('countries.csv') as countries_csv:
        heading = next(countries_csv)
        countries_csv_reader = csv.reader(countries_csv)
        for row in countries_csv_reader:
            country_name = str(row[0])
            country_capital_lat = float(row[1])
            country_capital_lng = float(row[2])
            for i in range(0, 10):
                get_image(i, country_name, country_capital_lat, country_capital_lng)

# takes the latitude and longitude of a country's capital city and returns a streetview image from
# a radius around the capital
def get_image(id: int, country_name: str, capital_latitude: float, capital_longitude: float):
    for _ in range(5): # try 5 different locations
        random_lat_around_capital = random.random() * ((capital_latitude - 0.1) - (capital_latitude + 0.1)) + (
                    capital_latitude - 0.1)
        random_lng_around_capital = random.random() * ((capital_longitude - 0.1) - (capital_longitude + 0.1)) + (
                    capital_longitude - 0.1)

        # check the metadata first
        metadata_url = "https://maps.googleapis.com/maps/api/streetview/metadata?"
        metadata_params = {
            "location": f"{random_lat_around_capital},{random_lng_around_capital}",
            "key": maps_api_key,
        }
        metadata_response = requests.get(metadata_url, params=metadata_params)
        metadata = metadata_response.json()

        # if status ok get the image
        if metadata['status'] == 'OK':
            image_params = {
                "size": "224x224",
                "location": f"{random_lat_around_capital},{random_lng_around_capital}",
                "key": maps_api_key,
            }
            image_response = requests.get(base_url, params=image_params)
            image_name = country_name + "_" + str(id) + ".jpg"
            with open(image_name, "wb") as file:
                file.write(image_response.content)
            image_response.close()
            # if image is retrieved break the loop
            break

generate_images()






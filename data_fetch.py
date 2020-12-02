import requests
import json
import pprint

class Data_Fetch:

    # constructor of Python class
    def __init__(self):
        # initialization of SCOUT API from NASA
        url = 'https://ssd-api.jpl.nasa.gov/scout.api'
        self.url = url

    # pulling data from apu
    def access_api(self):
        url = self.url
        response = requests.get(url)

        json_data = response.json() # converting to json
        
        # encoding data into a json string
        json_string = json.dumps(json_data)
        json_string = json_string + '\n'
        json_entry = json_string.encode('utf-8')

        return json_entry

    def check_response(self):
        url = self.url
        response = requests.get(url)

        print('status code: {}'.format(response.status_code))
        print('headers: {}'.format(response.headers))
        print()
        print('***** Data: ')
        pprint.pprint(response.json())
        print('*****')
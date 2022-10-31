from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)

        my_dictionary= dict(query_string_list) # from list to dictionary
        # name = my_dictionary.get('name',False) # to git data from my_dictionary and in our cass its "name"
        if 'country' in my_dictionary:
            word=my_dictionary['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + word)
            data=r.json()
            country=data[0]['name']['common']
            capital=data[0]['capital'][0]
            message=f'The capital of {country} is {capital}.'
                #The capital of Chile is Santiago.

        elif 'capital' in my_dictionary:
            word=my_dictionary['capital']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + word)
            data=r.json()
            country=data[0]['name']['common']
            capital=data[0]['capital'][0]
            message=f'{capital} is the capital of {country}.'
            #Santiago is the capital of Chile.
        else:
            message='please provide me with a country or capital'


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return
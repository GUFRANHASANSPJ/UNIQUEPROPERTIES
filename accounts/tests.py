from django.test import TestCase

# Create your tests here.
import requests

url = "https://country-state-city-search-rest-api.p.rapidapi.com/cities-by-countrycode"

querystring = {"countrycode":"cr"}

headers = {
	"x-rapidapi-key": "579bb90280mshd97d7764cae77c7p1937fajsn6726ac6004ae",
	"x-rapidapi-host": "country-state-city-search-rest-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
import IP2Location
import re
from urllib2 import urlopen
import time
from pprint import pprint
import requests
import json
import geocoder
from flask import Flask, render_template
app = Flask(__name__)


GOOGLE_MAPS_GEOCODING_API_KEY = 'AIzaSyBoym47nwLUALcQyKiGJHJR0jYW1DpB-y8'


@app.route("/")
def information():
	current_time = format = time.strftime("%a %b %d, %Y  %I:%M:%S %p",time.localtime(time.time()))
	
	weather = get_weather("West Covina")
	ontario_weather = get_weather("Ontario")
	temperature_k = return_json_value(weather, "main")
	ontario_temp_k = return_json_value(ontario_weather, "main")	
	temperature_f = convert_kelvin_to_farenheit(temperature_k)
	ontario_temp_f = convert_kelvin_to_farenheit(ontario_temp_k)	
	print(temperature_f)
#	current_location = get_location()
#	current_military_time = time.asctime( time.localtime(time.time()) )
#	ip_address = get_ip_address()
#	ip_address_to_zip_code(ip_address)
	return render_template('index.html', clock_time=current_time, temp=temperature_f)


@app.route("/simple")
def simpleWeather():
	return render_template('simpleWeather.html')


def get_weather(location):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={West Covina}&&APPID=03f33649dab326cef9dc1f961f944a5f')
#	pprint(r.json())
	return(r.json())

def get_weather_by_zip(zip_code):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&&APPID=03f33649dab326cef9dc1f961f944a5f')
	pprint(r.json())
	

def return_json_value(json_data, item):
	for key,value in json_data.items():
		print(key,value)
		if(item == key):
			print("Found a match")
			return(value['temp'])


def convert_kelvin_to_farenheit(kelvin):
	# http://www.metric-conversions.org/temperature/kelvin-to-fahrenheit.htm
	farenheit = (kelvin - 273.15) * 1.8 + 32.00
	return farenheit

def get_location():
	g = geocoder.freegeoip('47.34.206.172')
	return(g.json)


def get_city_town(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    return town, country


def get_ip_address():
	data = str(urlopen('http://checkip.dyndns.com/').read())
	IP = re.compile(r'(\d+.\d+.\d+.\d+)').search(data).group(1)
	url = 'http://ipinfo.io/' + IP + '/json'
	response = urlopen(url)
	data = json.load(response)

	org=data['org']
	city = data['city']	
	country=data['country']
	region=data['region']

	print 'Your IP detail\n '	
	print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)
	return(IP)

def ip_address_to_zip_code(IP):
	IP2LocObj = IP2Location.IP2Location();
	IP2LocObj.open("data/IP-COUNTRY-SAMPLE.BIN");
	rec = IP2LocObj.get_all(IP);

	print rec.zipcode
	return rec.zipcode

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

import time
from pprint import pprint
import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def information():
	current_time = format = time.strftime("%a %b %d, %Y  %I:%M:%S %p",time.localtime(time.time()))
	
	get_weather("West Covina")
	current_military_time = time.asctime( time.localtime(time.time()) )
	return render_template('index.html', clock_time=current_time)


def get_weather(location):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={West Covina}&&APPID=03f33649dab326cef9dc1f961f944a5f')
	pprint(r.json())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

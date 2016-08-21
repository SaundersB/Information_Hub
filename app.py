import time
from datetime import datetime

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def information():
	current_time = format = time.strftime("%a %b %d, %Y  %I:%M:%S %p",time.localtime(time.time()))
	

	current_military_time = time.asctime( time.localtime(time.time()) )
	return render_template('index.html', clock_time=current_time)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

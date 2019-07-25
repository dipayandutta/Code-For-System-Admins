import subprocess
from gevent import sleep
from gevent.wsgi import WSGIServer
import flask

app = flask.Flask(__name__)
@app.route('/')

def call():
		def inner():
				proc = subprocess.Popen(['sh system.sh'],shell=True,stdout=subprocess.PIPE)
				for result in iter(proc.stdout.readline,''):
						sleep(0.1)
						yield "<th>"
						yield "<b>---------------------------------------------------</b>"
						yield "<br>"
						yield result +'<br>\n'

		return flask.Response(inner(),mimetype='text/html')


http_server = WSGIServer(('',5000),app)
http_server.serve_forever()

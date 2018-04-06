from flask import Flask
import transmission
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/transmit")
def transmit():
	transmission.write_packets("HelloWorld")


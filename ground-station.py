from flask import Flask, request
from commands import Command
import transmission

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/transmit")
# def transmit():
# 	transmission.write_packets("HelloWorld")

@app.route('/transmit', methods=['POST'])
def transmit():
    print("Transmitting...")
    request_json = request.get_json()
    print(request_json)
    for k, v in request_json.items():

    	if k not in Command.__members__:
    		print("ERROR: {} is not a valid command.".format(k))
    		continue

    	if v is None or len(v) < 1:
    		print("ERROR: Command {} has no value.".format(k))
    		continue

    	command_line = str(Command.ENDSTOP.value + Command[k].value 
    	+ str(v))

    	print(command_line)

    	transmission.write_packets(command_line)

    return "Done"
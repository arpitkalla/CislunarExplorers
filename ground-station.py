from flask import Flask, request, render_template
from commands import Command
import transmission

app = Flask(__name__)

@app.route("/")
def hello():
    return "HelloWorld"

@app.route('/index', methods=['GET', 'POST'])
def index():   
    return render_template("index.html")


@app.route('/commands', methods=['GET'])
def get_commands():
    return jsonify("Command" = Command.__members__)
# @app.route("/transmit")
# def transmit():
# 	transmission.write_packets("HelloWorld")

@app.route('/transmit', methods=['POST'])
def transmit():

    if request.method == 'POST':
        result = request.form
        print(result)

    print("Transmitting...")
    request_json = request.form
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



if __name__ == '__main__':
    app.run(debug=True) 
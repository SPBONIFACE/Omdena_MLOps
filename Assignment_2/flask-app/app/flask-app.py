from calculate_area import calculate_area
from flask import Flask, jsonify, request

#instantiate flask object
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_input():
    """ A function to get request using flask, evaluate and return results
    """
    packet = request.get_json(force=True)
    length = packet['length']
    width = packet['width']

    acres = calculate_area(length, width)

    return jsonify(packet, acres)

# driver function 
if __name__ == '__main__':
    app.run(debug=True)

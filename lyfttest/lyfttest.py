# Imports
import os
from flask import Flask, request, json, abort

# Flask app initialization
app = Flask(__name__) # create application instance

# Routes
@app.route('/test', methods=['POST'])
def read_json():
    try:
        string_to_cut = request.json['string_to_cut']
    except:
        print('BAD REQUEST')
        abort(400)
    result_string = string_cut(string_to_cut)
    return_json = {
        "return_string": result_string,
    }
    return json.dumps(return_json)

def string_cut(string):
    string = string.replace(" ", "")
    new_string=''
    count_no=1
    for c in string:
        if count_no%3==0:
            new_string+=c
        count_no+=1

    return new_string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
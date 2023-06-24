from flask import Flask, redirect, request
import random, string
import json

host = 'localhost'
port = 5000
keys_file = 'redirects.json'

data = open(keys_file)
codes = json.load(data)

app = Flask(__name__)
app.secret_key = ''.join((random.choice((list(string.ascii_letters)+list(string.digits)))) for _ in range(100))

@app.route("/<key>", methods=["GET",])
def logger(key):
    if key in list(codes['data'].keys()):
        print(request.remote_addr)
        print(request.headers)
        return redirect(codes['data'][key]['url'], code=codes['data'][key]['status_code'])
    else:
        return 'Not Found', 404

#Run app, the following block of code must be the last thing in the file
if __name__ == "__main__":
    app.run(debug=False, host=host, port=port) #debug ONLY for testing

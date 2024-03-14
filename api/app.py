from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return json.dumps({"name": "bob", "number": 3})
if __name__ == '__main__':
    app.run(debug=True)
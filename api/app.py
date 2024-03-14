from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def main():
    return json.dumps({"name": "bob", "number": 3})

def solve(chars):
    

if __name__ == '__main__':
    app.run(debug=True)
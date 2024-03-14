from flask import Flask
import json

with open("dictionary.json") as json_file:
    dictionary = json.load(json_file)
 
app = Flask(__name__)

@app.route('/')
def main():
    return json.dumps(dictionary)

# def solve(chars):
    

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, abort,request
import json
from flask_limiter import Limiter,util
from itertools import permutations,combinations
from flask_cors import CORS

with open("dictionary.json") as json_file:
    dictionary = json.load(json_file)

app = Flask(__name__)
CORS(app)



@app.route('/', methods=["GET"])
def main():
    string = request.args.get("string")
    if string == None:
        abort(400, description="No string given")

    if len(string) != 6:
        abort(400, description="Improper string length")

    if not string.isalpha():
        abort(400, description="Improper character in string")

    answer = {}
    for item in solve(string)[::-1]:
        l = len(item)
        if l == 6:
            answer[item] = 2000
        elif l == 5:
            answer[item] = 1200
        elif l == 4:
            answer[item] = 400
        elif l == 3:
            answer[item] = 100
    return json.dumps(answer)
    
    


def solve(chars):
    chars = list(chars)
    solutions = []

    # For all words from 2 letters to max letters
    for i in range(3, len(chars)+1):
        # Generate all combinations of those letters 
        for current_set in combinations(chars, i):
            # Generate all orders of those combinations 
            for current in permutations(current_set):
                current_word = ''.join(current)
                if check(current_word) and current_word not in solutions:
                    solutions.append(current_word)
    return solutions

def check(word: str) -> bool:
    word = word.upper()
    if word[0:2] in dictionary:
        wordList = dictionary[word[0:2]]
        for item in wordList:
            if word == item:
                return True
    return False
    

if __name__ == '__main__':
    app.run(debug=False)

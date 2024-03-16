from flask import Flask
import json
import itertools

 
app = Flask(__name__)

@app.route('/')
def main():
    return solve("gainly")

def solve(chars):
    from itertools import permutations,combinations
    import enchant

    dictionary = enchant.Dict("en_US")
    chars = list(chars)
    solutions = []

    # For all words from 2 letters to max letters
    for i in range(2, len(chars)+1):
        # Generate all combinations of those letters 
        for current_set in combinations(chars, i):
            # Generate all orders of those combinations 
            for current in permutations(current_set):
                current_word = ''.join(current)
                if dictionary.check(current_word)and current_word not in solutions:
                    solutions.append(current_word)
    return solutions

    

if __name__ == '__main__':
    app.run(debug=True)
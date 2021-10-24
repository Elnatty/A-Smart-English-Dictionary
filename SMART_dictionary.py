import json       # the json file contains the list of words and their meaning
from difflib import get_close_matches       #
# loading the json file data to python
data = json.load(open('data.json'))

# a function 'translate'
def translate(w):
    '''
    This function contains the app makeup...
    '''
    w = w.lower()
    if w in data:
        return data.get(w)
    # this condition seeks to get a ratio of words the user inputs, with the closest match
    # suggested as an answer.
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input('Did you mean {} instead? Enter y or n: '.format(get_close_matches(w, data.keys())[0]))
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return 'Unrecognized query ! !'
    else:
        return "The word doesn't exist. please double check it."

word = input('Input words: ')
output = translate(word)

# iterating through the output to give a nice touch of output, when result is a list.
if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
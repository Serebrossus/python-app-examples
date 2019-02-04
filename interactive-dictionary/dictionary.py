import json
import difflib
from difflib import get_close_matches

#loading json data.
data = json.load(open('dictionary.json'))

#function for retriving definition
def retrive_definition(word):
    #converting all lettersto lower because out data is in that format
    word = word.lower()
    #check for non existing word
    #1st elif : to make sure the program return the definition of words that start with a capital letter
    #2nd elif : to make sure the program return the definition of acronyms
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input('Did you mean %s instead? [y or n]' % get_close_matches(word, data.keys())[0])
        #if answer is yes, retrive deffinition of suggested word
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif action == "n":
            return ("The word doesn't exist")
        else:
            return ("We don't understand your entry")

#input for user
word_user = input('Enter a word: ')

#retriving definition using function and print result
output = retrive_definition(word_user)
if type(output) == list:
    for item in output:
        print("-", item)
else:
    print("-", output)
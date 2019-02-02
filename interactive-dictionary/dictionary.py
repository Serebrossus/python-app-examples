import json

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
    else:
        return 'the word does not exit, please double check it.'

#input for user
word_user = input('Enter a word: ')


#retriving definition using function and print result
print(retrive_definition(word_user))
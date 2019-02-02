import json

#loading json data.
data = json.load(open('dictionary.json'))

#function for retriving definition
def retrive_definition(word):
    return data[word]

#input for user
word_user = input('Enter a word: ')


#retriving definition using function and print result
print(retrive_definition(word_user))
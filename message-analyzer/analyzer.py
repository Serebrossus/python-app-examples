from textblob import TextBlob

# pip install -U textblob

user_message = input('Enter text: ')
try:
    analysis = TextBlob(user_message)

    for sentence in analysis.sentences:
        print(sentence)
        print("\n")


    # words
    print(analysis.words)

    # tags
    print(analysis.tags)

    # noun phrases
    print(analysis.noun_phrases)

except Exception as err:
    print(err)

# polarity - determines how emotional a text color is
# asubjectivity - determines how much the author’s personal opinion is expressed in the text
print(analysis.sentiment)
print("\n")

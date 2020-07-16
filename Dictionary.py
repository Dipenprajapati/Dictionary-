import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  # it gives a output of title(first letter capital) otherwise go to else statement
        return data[word.title()]
    elif word.upper() in data:  # it gives a output of upper case otherwise go to else statement
        return data[word.upper()]
    elif word.lower() in data:  # it gives a output of lower case otherwise go to else statement
        return data[word.lower()]
    # it gives close matches from dictionary if user input is wrong spelling for example superman from supermann
    elif len(get_close_matches(word, data.keys())) > 0:
        print(" Did you mean %s insted " % get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or no for n -->")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ("wrong input")
        else:
            return ("pls enter y or n ")

    else:
        print(" You entered wrong word.....")
word = input(" Enter word for search ---> ")
output = translate(word)
if type(output) == list:   # shows output of word in list manner
    for item in output:
        print(item)
else:
    print(output)


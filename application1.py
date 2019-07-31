import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower() #Since all the dictionary words are in lower case, we must first take the user input and convert it into all lower case letters
    if w in data:
        return data[w]
    elif w.title() in data: #w.title() converts the first letter to uppercase and rest to lower
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn =="N":
            return "The word is not found. Please check it"
        else:
            return "Only enter Y for YES or N for NO"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
#to display each definition in a different line instead of a list we do the following:
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) #if it's a string, like a message from the programmer, it should be displayed in 1 line and not divide each letter in different lines.

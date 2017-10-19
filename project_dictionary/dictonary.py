#---------------------------
#      19/10/2017
# created by Wojciech Kuczer 
#---------------------------
#import librarys
import json
from difflib import get_close_matches

#open dictonary file
data = json.load(open("data.json"))

#function to search dictonary
def find_definition(word):
    if word in data:
        return data[word]
    word = word.lower()
    checked_word = get_close_matches(word, data.keys())
    if len(checked_word) <= 0:
        return "No definition for Your query"
    if word in data:
        return data[word]
    else:
        answer = input("Did you mean '{}': (Y/N)".format(checked_word[0]))
        answer = answer.lower()
        if answer == "y":
            return data[checked_word[0]]
        else:
            return "No definition for Your query"

word = input("Enter definition: ")

#outputing resuts of search
output = find_definition(word)
counter = 0
if type(output) == list:
    for data in output:
        counter += 1
        print("{} - {}".format(counter, data))
else:
    print(output)


#project not totaly finished as has to implement method to check keys starting with capital letter
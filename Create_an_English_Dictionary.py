import json

file = open('data.json')
data = json.load(file)

def define(word):
  word = word.lower()
  if word in data:
    return data[word]

word = input('Please enter a word: ')
definition = define(word)
if definition:
  for item in definition:
    print(item)
else:
  print("Word was not found!")
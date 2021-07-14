import json
#A dictionary which needs to be converted into JSON
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON=json.dumps(person, indent=4, separators=('; ','= '), sort_keys=True) 
#This dumps it into JSON, changes indentation, uses separators and arranges keys alphabetically.
#Indent changes the indentation
#Separators denote the different custom separators to use
print(personJSON) #Note in the o/p that 'false' is in lower format

#Creating a JSON file with the given python dictionary
with open('person.json', 'w') as file:
  json.dump(person, file) 
  #Can also use indentation,sort etc. 

#Decoding the JSON file back to Python dictionary
person = json.loads(personJSON)
print(person)
#NOTE: Get rid of an custom delimiters if you've craeted while craeting JSOn, otherwise error will be thrown as it can't convert that to a dictionary.personJSON

#Decoding through the JSON file
with open('person.json','r') as file:
  person = json.load(file)
  print(person)
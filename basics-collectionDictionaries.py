#Dictionaries

"Dictionary is a collection which is ordered and changeable. No duplicate members."

#in python 3.6 and earlier dictionaries are unordered I AM ON PYTHON 3.10 SO ORDERED

firstDict = {
    "player":"Saka",
    "nationality": "English",
    "Foot":"Left"
} #LOOKS LIKE JSON FORMAT - CANT HAVE DUPES MEANING SAME KEY 

print(firstDict)
#dict are keys and values maening we can refer to the dict through the key
print(firstDict["player"]) # outputs saka

#get length
print(len(firstDict)) #3

#can be any data type - bool, str and int and list types

#can create a dict through the constructor
dictConstructor = dict(name = "Declan Rice", country = "English", club = ["West Ham", "Arsenal"]) # remember can use lists
print(dictConstructor)

print("---------------------------------")
print("ACCESSING DICT")
#using the key name
accessOne = dictConstructor["name"]
#can do it through the get method too
accessTwo = dictConstructor.get("country")  

#the keys method will return a list of all keys in the dictionary
ListOfKeys = dictConstructor.keys()
print(ListOfKeys) # returns name, country and club

#get a list of the values
ListOfValues = dictConstructor.values()
print(ListOfValues) # rice, english and the teams he plays for

#items method will return each item as a tuples list
tuplesListFromDict = dictConstructor.items()
print(tuplesListFromDict)

#check if key exists
if "name" in dictConstructor:
    print("YES") # returns yes as it is a key within the dict
    
    
print("---------------------------------")
print("CHANGE DICT")
#can change item by referring to the key
dictConstructor["country"] = "British"
print(dictConstructor) # changed country from english to british

#can do update like this
dictConstructor.update({"club" : "Gunners"})
print(dictConstructor) # changed the club to gunners

print("----------------------------------") 
print("ADDING DICT")    
dictConstructor["position"] = "CDM" 
print(dictConstructor) # added position to the dictionary

#you can use update to update a keys value and if it doesn't exist it will get added in 

print("---------------------------------------")    
print("REMOVING DICT")
dictConstructor.pop("position")
print(dictConstructor) # got rid of the position key
#if we did popitem() it will get rid of the last current key

del dictConstructor["country"] # this deletes the key name - it can also be used to delete the dict entirely
#clear clears the dict

print("--------------------------")
print("LOOPING DICT")
for x in dictConstructor:
    print(x) # this will print all key names

#this can also loop through the keys
for x in dictConstructor.keys():
    print(x)

#to loop through the values 
for x in dictConstructor:
    print(dictConstructor[x])  #prints out values
    

#can also loop values like this
for x in dictConstructor.values():
    print(x)
    
#loop through keys and values
for x,y in dictConstructor.items():
    print(x,y)

print("---------------------------------")  
print("COPYING DICT")
copyOfDictConstructor = dictConstructor.copy()
print(copyOfDictConstructor)# copies the keys and values into this new variable

#can also copy dict through dict function
copyThroughDictFunct = dict(dictConstructor)
print(copyThroughDictFunct) # same values as dict Constructor in this new value

print("-------------------------")
print("Nested Dict")
ArsenalPlayersDict = {
    "player 1" : {
        "name" : "Saka",
        "position" : "RW"   
    },
    "player 2" : {
        "name" : "Declan Rice", 
        "position" : "CDM"
    },
    "player 3": {
        "name" : "Trossard",
        "position": ["LW", "CF", "LCM"]
    }
}# SO SIMILAR TO JSON FORMAT = THIS IS A NESTED DICTIONARY

#Can also do it this way too 
p1 = {
        "name" : "Saka",
        "position" : "RW"   
}
p2 = {
        "name" : "Declan Rice", 
        "position" : "CDM"
}
p3 = {
        "name" : "Trossard",
        "position": ["LW", "CF", "LCM"]
}
GunnersPlayersDict = {
    "player 1" : p1,
    "player 2" : p2,
    "player 3" : p3
}

#accessing items within a nested dict
print(ArsenalPlayersDict["player 1"]["name"]) #returns saka











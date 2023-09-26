#imports
import random # this input is used for random number since python itself doesn't have the function bulit in

#Numbers
#standard types int,float - like in other languages

#float numbers can use the letter 'e' to illustrate the power 10
floatPowerOfTen = 25e3
print(floatPowerOfTen) #25000.0

#type conversion - chaning an int to a float example
convertInt = 1
convertedIntToFloat = float(convertInt) # changed it from 1 to 1.0
print(convertedIntToFloat)

print(type(convertedIntToFloat))#double checking the type has changed to float

#Random number - look at imports
print(random.randrange(1,10)) # random number between the range given

print("---------------------------------------------")
#casting
#we can force a data type on an variable we want 
forceItToBeAFloat = float(1) # outputs 1.0 instead of 1 - we force it to be 1.0 
forceItToBeAStr = str(2) # outputs '2' - so it is a string of 2 rather than a number of 2 like if it was an int or float
print(forceItToBeAFloat, forceItToBeAStr)

print("---------------------------------------------------")
#Strings
#we know how to assign a variable a string already - or straight up print a string

#multi-line strings
multiString = """This is random
multi line strings
aaaaaaaaaaaaaaaaaaaaaa"""
print(multiString) # the breaks in the line are translated over to the log version to - REMEMBER    

#Strings are arrays so to get a specfic character for example we can do this
stringArray = "This is an array"
print(stringArray[2]) #outputs i from 'this' remember arrays start from 0 
#can also loop through it since it's an array
print("--------------------------------------------")
for stringLoop in "This is looped":
    print(stringLoop)
    
#to get length of a string
print(len(stringArray)) # outputs 16 remember it counts spaces within the string

#to check whether something IS within the string 
print("arr" in stringArray) # output is true because in the string array variable arr is part of the word array within the string
#can use that in an if statement
if "arr" in stringArray:
    print("Yes, arr is part of the string!") # it outputs

#to check if a word is NOT part of the string 
print("looped" not in stringArray) # outputs true because the word looped is not part of the string array variable but part of the stringloop variable
#can be used in an if statement similar to the if statement above.

print("----------------------------------")
#Slicing strings
print(stringArray[2:6]) # gives the output of the elements of the string that fit within this range of the array so outputs 'is i' -end of this and start if is in the string 
#To slice from the start
print(stringArray[:6])# leave the start range blank 
#To slice from the end
print(stringArray[2:]) # starts from 2nd element and goes to the end of the string

#To start the slice from the end make the numbers negative
print(stringArray[-6:-2]) # this starts from the 6th element if the end of the string was -0 so outputs from -6 to -2 position which is the space between an and array as the -6 too 'arr' for -2

print("----------------------------------------------------------")
#Make the strings upper case
print(stringArray.upper())
#Make the strings lower case
print(stringArray.lower())
#if there was white space at the end or start of the string we can get rid of it with
print(stringArray.strip())
#To replace a string
print(stringArray.replace("This", "Replaced")) # this has changed to replaced in the string so it reads replaced is an array
#We can split the string at specific point
print(stringArray.split("an")) # this splits the array into 2 'This is ' and ' array'

print("------------------------------------------------------") 
#To combine two strings together
combineTheTwoStringsTogether = stringArray + " " + stringLoop
print(combineTheTwoStringsTogether) # outputs This is an array d  - combines the two strings together see how looped variable doesn't have the word an but when combined it has added it in.

print("-------------------------------")
#normally can't combine a string with an int - learnt in variables
#can though with the format method
albumNumber = 12
albumStr = "The album has {} songs!"
print(albumStr.format(albumNumber)) # outputs The album has 12 songs the {} tells python where we want the formatted variable inputted. 
albumNumberOnes = 2
albumNumberOnesStr = "The album has {} songs and has {} number ones!"
print(albumNumberOnesStr.format(albumNumber, albumNumberOnes)) # can do multiple placeholders and fill em in respectively. 

#can tell the order to ensure it goes in correctly
orderChangedString = "The album has {1} number ones, from a {0} song album"
print(orderChangedString.format(albumNumber, albumNumberOnes)) # outputs The album has 2 number ones, from a 12 song album as we told it which number element goes where.

print("----------------------------------------------------------")
#Escape
"""We normally would not be able
    to use quote marks within a string as it would mess with the quote marks of the string itself
    with escape character though we can    
"""
escapeCharacterString = "Harvin \"Developer\" Johal"
print(escapeCharacterString) # we can now use the quotes within quotes outputs Harvin "Developer" Johal

"""Different escape characters other than "" is 
    \n of course for a new line
    \\ backslash
    \t tab
    \b backspace
    \' single quote
"""

"""There is multiple methods that can come off a string
    did some such as split, replace, upper, lower but there are loads more so use the ide etc. to make sure you know what most do
"""
    

 
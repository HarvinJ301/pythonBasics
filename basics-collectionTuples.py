#Tuples Lists

"Tuple is a collection which is ordered and unchangeable. Allows duplicate members."

#REMEMBER UNLIKE LISTS THESE ARE UNCHANGEABLE
#ROUND BRACKETS INSTEAD OF []

firstTuple = ("saka", "foden", "rashford")
print(firstTuple)

#since they are indexed like lists they can have dupes

dupeTuple = ("saka", "foden", "rashford", "saka", "saka")
#get the length
print(len(dupeTuple)) #length 5

#to create a tuple with one item a comma has to come after the first one for it to recongise it as a tuple
oneItemTuple = ("saka",) # comma important
print(type(oneItemTuple)) # sees it as a tuple

# can be all data types strings, numbers and booleans and can be all in one tuple

#can create a tuple using its constructor
tupleConstructor = tuple(("saka", "foden", "pickford")) 
print(tupleConstructor)

print("------------------------------")
print("ACCESSING TUPLES")
print(tupleConstructor[1]) # outputs foden - index starts at 0      

#Negative index
print(tupleConstructor[-1]) # outputs pickford - negative index starts at -1

#range
print(tupleConstructor[1:3]) # foden and pickford - rememeber first number is included second number is not included just says when to stop

#leaving start empty will start the range and the start end will make it go all the way to the end - similar to lists

#check if item is in the tuple
if "saka" in tupleConstructor:
    print("Yes") # prints out because he is part of the tuple
    
print("------------------------------------------")
print("Update Tuples")
#tuples are unchangeable/immutable - there is a work around 
changingTupleData = ("g" , "s" , "h")
changingItToList = list(changingTupleData) # we change the tuple to a list
changingItToList[1] = "felix" # change element 1 to felix
changingTupleData = tuple(changingItToList) # change it back to a tuple
print(changingTupleData) # output with the new change "s" is now "felix"

#can add an item to the tuple the same way as above instead of changing an element use the append feature within lists

#we can add a tuple to another tuple to add items also
tupleToBeAddedWithChangingTupleData = ("t",)
changingTupleData += tupleToBeAddedWithChangingTupleData
print(changingTupleData) # added the two tuples together and now t is added to the end of the original tuple

#Removing items is the exact same where we change it to a list temporarily use the remove func within lists and change it back to a tuple

#can use the del keyword to delete the tuple entirely
del tupleToBeAddedWithChangingTupleData #deletes the tuple 

print("---------------------------------------")
print("UNPACKING TUPLES")
#when creating tuples we pack the tuple 
# we can unpack these elements into seperate variables to be used in different areas of code
unpackTuple = ("green", "red", "blue")
#we then unpack them
(colour1, colour2, colour3) = unpackTuple # we assign each variable to the corresponding element within the tuple
print(colour2) # prints out red which it got from the tuple 

#we can use asterisk to assign multiple elements within a single variable
unpackTupleMultiple = ("green", "red", "blue" ,"pink", "black")
(colourGreen, *multipleColours, colourBlack) = unpackTupleMultiple # when we use asterisk it creates a list up until the variables match the remaining elements left again
#if there is more elements than variables this is useful
print(colourGreen)
print(multipleColours) # this is the list containing red blue and pink as the asterisks keeps going until the variables match the number of elements again
print(colourBlack)  

print("----------------------------------------")   
print("LOOPING TUPLES")
#Loop through tuple
loopTuple = ("df " ,"fdg", "trtr")
for x in loopTuple:
    print(x)
    
# can also loop through referring to their index numbers
for i in range(len(loopTuple)):
    print(loopTuple[i])
    
#can loop through using a while loop too
j = 0
while j < len(loopTuple):
    print(loopTuple[j])
    j += 1
    
print("----------------------------------------")
print("JOINING TUPLES")
addTuple1 = ("j", "k", "l")
addTuple2 = (5, 3, 1)   
tuple3 = addTuple1 + addTuple2
print(tuple3) # adds tuple 2 to the end of tuple 1

#can also multiply the content of the tuple basically duplicating the tuple again
multiTuples = tuple3 * 2
print(multiTuples) # basically dupes the data again within the tuple

print("-------------------------------------")
print("METHODS")
print(tuple3.count("j")) # this outputs the amount of times a value is present within the tuple so in this one it outputs 1
print(tuple3.index(5)) #' this outputs where in the tuple is the element within the index so it outputs 3 because "5" is the 4th element within the tuple



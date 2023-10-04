#Sets

"Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members."

#sets use curly brackets
firstSet = {"first", "second", "third"}
print(firstSet) # sets are unordered so the order it is outputted is random i.e. first is not guarnteed to be outputted first all the time. 
# no dupe values either

dupeSet = {"first", "second", "third", True, 1} #true and 1 are seen as the same value within sets so its a dupe so 1 doesn't get outputted ever.
print(dupeSet)

#length of the set
print(len(firstSet)) # outputs 3

#all data types can be inputted - strings, ints and booleans

#Create a set using the constructor
setConstructor = set(("first","second", "third")) # cause of constructor use double brackets
print(setConstructor)

print("------------------------------------------")
print("Accesing Sets")

#loop through set
for x in firstSet:
    print(x)
    
#check if something is within the set
print("first" in firstSet) # returns true because it is present within the set

print("-------------------------------------")
print("Adding Items")
#you can't change items within a set but can add to the set
firstSet.add("fourth")
print(firstSet) # fourth is now part of the set

#to add elements from one set to another set use update()   
numSet = {1,2,3}    
firstSet.update(numSet)
print(firstSet) # added the numbers to the first set
#the update doesn't have to be another set it can be any collection type - list, tuple,set and dictoionary

print("----------------------------------")
print("Remove Items")
#use remove method
firstSet.remove(3)  #if item does not exist it will cause an error

#can use the discard method to remove and it will not cause an error if the item does not exist
firstSet.discard(1) 

#can use pop() method however can't decide what gets popped it's random as sets are not indexed 
findOutWhatGotPopped = firstSet.pop() #  this is so we can find out what we lost
print(findOutWhatGotPopped) # we lost number 2  
print(firstSet)

#clear will empty the set
dupeSet.clear() 
print(dupeSet) # returns set()  as there is no values

# can use del keyword to delete the set entirely. 

print("------------------------------")
print("Loop Items")
#use a for loop
for x in firstSet:
    print(x)    
    
print("---------------------------------------")
print("Join Sets")
# can use the update() method we used earlier or union() to create a new set made up of the 2 sets we join together
joinedSet = firstSet.union(numSet)
print(joinedSet) # joins the two together - both union and update will not push together dupes

#we can join two sets together where it only gets the dupes between the two sets
duplicateSet1 = {"fps", "action", "adventure"}
duplicateSet2 = {"fps", "camera", "action", "producer"}
duplicateSet1.intersection_update(duplicateSet2)
print(duplicateSet1) # this prints out fps and action because these are the words that are dupes across the two sets

#intersection() itself creates a new set with the duplicate values instead of overlaying a current set
duplicateSet3 = duplicateSet1.intersection(duplicateSet2)
print(duplicateSet3) # same print as the one above but now its own variable

# to do the opposite where we get the values that are not dupes only we can do this
notDupValues = duplicateSet1.symmetric_difference(duplicateSet2)
print(notDupValues) # this prints out camera and producer as they are the only values not duplicates across the two sets. 






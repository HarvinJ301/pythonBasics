#Normal lists

"""List is a collection which is ordered and changeable. Allows duplicate members.
"""
normList = ["saka", "jude", "jack"]
print(normList)

#normal lists are ordered starting at element 0 - anything added goes to the end

#Lists allow duplicates due to them being indexed/placed in order
dupList = ["saka", "jude", "jack", "saka", "saka"]

#can use len to find out length of list
print(len(dupList)) # returns 5

#lists can be any data type e.g. string, numbers, booleans and they can be part of the same list

#lists are defined as class type list

#can use the list constructor to create lists
constructorList = list(("saka", "jude", "jack")) # double brackets - one for the data and one for the list constructor
print(constructorList)

#accessing items within a list
print(constructorList[1]) #' returns jude remember it starts at 0 - so that would be saka if we wanted him

#can negative index to
print(constructorList[-1]) # unlike start to end - going from the back starts at -1 not 0 because again u can't do -0 - outputs jack

#can specify a range 
print(dupList[2:4]) # outputs jack and saka - starts at element 2 which is jack and ends at element 4 but not outputting element 4 so really outputs 2 and 3

"""can do the same things with the range as we doid within datatypes file to slice strings e.g. leaving start or end of range for different results
as well as negative ranges
"""
#check if something is in the list
if "saka" in constructorList:
    print("yes saka is part of this list") # prints out
print("---------------------------------------------------------------------")

#CHANGING items within a list
constructorList[2] = "foden"
print(constructorList) # we have specified which element we want to change which is jack and changed it to foden - remember earlier outputs before this still output jack until it gets here where we change it to foden

#can change a range
dupList [3:5] = ["kane", "ramsdale"]
print(dupList) # changed the duplicates of saka to kane and ramsdale    

#if we add more than we replace the new items will go where I specify and the others will move across
dupList[3:4] = ["colwill", "eze"]
print(dupList) # we made a range for only 1 item but put 2 items in the array - so kane was element 3 so he got replaced with the first item colwill, eze moved in after colwill at element 4 and pushed ramsdale to the end as element 5
#if we have a large range but don't input enough items to fit all the range - the value will input where we wanted with the first number but the numbers after this will be deleted
dupList[1:4] = ["emile smith rowe"] # so emile goes in at element 1 so after saka and elements 2 and 3 are deleted from the list. - so at this point that is jack and colwill
print(dupList)

print("--------------------------------------------------------------")
#ADDING
# to add an item to the list without losing anything in a specfic place we can do this
dupList.insert(2, "pickford")
print(dupList) # we have inserted pickford as element 2 within the list so after emile smith rowe

#to add an item to the end of a list
dupList.append("rashford")
print(dupList) # added rashford to the end of the list

# to append elements from one list to another list - it can be used to append other types of collections to the end of a list (tuples, sets, dictionaries etc)
dupList.extend(constructorList)
print(dupList) # now the constructor list has been added to the end of the dup list adding saka jude and foden to the end

print("------------------------------------------------------")
#REMOVING
dupList.remove("jude") #removes the first jude if there was more than one the others would not be removed
print(dupList) # removes jude from the list

dupList.pop(2) # removes a specific element - in this case it was pickford
print(dupList) # pickford gone

dupList.pop() # because it is not specified it removes the last item in the list - at the moment that is foden
print(dupList) # foden gone

del dupList[2] # does the same as pop

del normList # it can also be used to delete entire lists - the normal list has been deleted now

#clear can clear a list so the list still exists but there is no content

constructorList.clear()
print(constructorList) # it is now an empty list

print("-----------------------------------------------------------")
#LOOPING THROUGH LISTS
for x in dupList:
    print(x) #' loops through the list gives each item on a seperate line in the console

print("RANGE LOOP")
#can also loop through the list by referring to their index number too
for i in range(len(dupList)):
    print(dupList[i])
    
print("WHILE LOOP")
whileLoopNum = 0
while whileLoopNum < len(dupList): # while the loop number is less than the length of the dupList keep looping through 
    print(dupList[whileLoopNum])
    whileLoopNum += 1 #basically whileLoopNum = whileLoopNum + 1    
    
print("LIST COMPREHENSION")
#shorter way of looping through lists
[print(a) for a in dupList] # one line to do a for loop

#using List comprehension we can create new lists with certain values from another lists data within one line
newListFromDupList = [x for x in dupList if "o" in x] # this new list looks through duplist and gets the values that contain the letter "o" in them me
print(newListFromDupList) # this new list outputs rashford and emile smith rowe as they are the only values with o in their name

#the if line within the example above is the condition and can be removed if there is no condition needed
newListBasicallySameAsDupList = [x for x in dupList]
print(newListBasicallySameAsDupList) # basically the dupList again because there is no if condition to change it

#say we wanted the new list to remove any mention of ramsdale we can use the if conditon to do that
newListWithoutRamsdale = [x for x in dupList if x != "ramsdale"] # like other languages != means not equal to so as long as it doesnt equal ramsdale it will be part of the new list created
print(newListWithoutRamsdale) # this new list is the same as the duplist but without ramsdale now

# you can create a list or any collection with range too
listCreatedWithRangeComprehension = [x for x in range(10)] # Created a list from 0-9
print(listCreatedWithRangeComprehension)

#can also add conditions to the creatd list
sameRangeListWithConditions = [x for x in range(10) if x < 5] #creates a list up to 4 
print(sameRangeListWithConditions)

#the expression within the comprehension listed created can be manipulated too
useListCreatedByRangeToCreateListAllWithMyName = ['Harvin' for x in listCreatedWithRangeComprehension]
print(useListCreatedByRangeToCreateListAllWithMyName) # it prints out a list with the name harvin 10 times because remember the range of this list was 10 items 0-9

#can manipulate the list to change certain words by adding conditions to the expression at the start too
changeHarvinToBob = [x if x != "Harvin" else "Bob" for x in useListCreatedByRangeToCreateListAllWithMyName] #looks through loop to see if anything equals harvin change to bob
print(changeHarvinToBob) # the list created before with my name 10 times has been changed to bob 10 times

print("-------------------------------------------")
print("Sort Lists")
sortListWords = ["Steel", "Metal", "Titanium", "Wood"]
sortListWords.sort()
print(sortListWords) # sorts the list in aplhanumerical ascending order same if we did it with number list - lowest number first highest last

sortListWords.sort(reverse=True) # does the sort in reverse 
print(sortListWords) # now outputs Wood first and metal last 


#using functions to create a unique sort 
def sortByClosestToTen(x):
    return abs(x - 10) # abs returns absolute value of an arguement
    
sortListNumbers = [23, 10, 54, 100, 45, 32]
sortListNumbers.sort(key = sortByClosestToTen) # key allows us to call upon our function
print(sortListNumbers) # sorts by choosing the closest to the number 10 which of course in this list is 10 and then going 23,32,45,54,100 respectively 

#the default sort func if there are some words that are captial letters they will go first then the lowercase ones in alphanumeric order
#to stop this we can force all to be lower case 
sortMakeAllLowerCase = ["banana", "Apple", "Pear", "grapes"]    
sortMakeAllLowerCase.sort(key= str.lower) # using the key to make all strings  lower

print(sortMakeAllLowerCase) # without the str.lower it would output apple first then pear , with the str.lower it now outputs apple first and pear goes to the back due to the alphabet

#can get the order in reverse
sortListNumbers.reverse()
print(sortListNumbers) # reverses the sort so highest number came out first so 100 first then 10 last

print("----------------------------------------")
print("Copying Lists")

#one way to copy is use the copy method
copyOfNumberList = sortListNumbers.copy()
#copyOfNumberList = list(sortListNumbers) - another way of copying the list
print(copyOfNumberList) # outputs the same list of the most recent number list created earlier 

print("-----------------------------------------")
print("Join lists")

addListOne = [54, 32, 12]   
addListTwo = ["fd", "gf", "jy"]

twoListsAddedTogether = addListOne + addListTwo
print(twoListsAddedTogether) #outputs list one the numbers than list 2 the letters all in one list together

#Another way of joining lists
appendListOne = ["append 1", "append 2", "append 3"]
appendListTwo  =[21, 32, 54]    

for x in appendListTwo:
    appendListOne.append(x)

print(appendListOne) # appends the numbers to the end of the letters list similar to previous join

#can also join them through extend
extendListOne = ["extend1", "extend2", "extend3"]
extendListTwo = [54,13,65,6]

extendListOne.extend(extendListTwo)
print(extendListOne) # again adds in extend list two to the end of extend list one.


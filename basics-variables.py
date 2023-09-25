#Print to console
print("Hello World!")

#Here is a simple if statement - the indent line after is important it tells python the block of code to run.
#if you have multiple blocks of code after make sure they are the same indentation otherwise can cause error.
if 5 > 2:
    print("Five is greater than two!")
    
#Creating variables
x = 3
y= "Hello!"

print(x)

"""
multi line comment
"""

#Can change variable type on the fly such as from int to string

a= 3
a = "Harvin"
#now prints harvin
print(a)

#can hard code the type you want though
b= int(3)   # output 3
c= float(3) #output 3.0 

print(b,c)
print(type(b)) #this outputs the type it is which in this case outputs int

#VARIABLES ARE CASE SENSITIVE
do= 3
Do = 4
print(do,Do) #These are two different variables

#can declare variables on single line
fruit, veg, drink = "orange", "brocolli", "water"
print(fruit, veg, drink)

#declare same value to multiple variables together
gh = fd = jk = "banana"
print (gh, fd, jk) # they all have banana assigned so prints it out 3 times. 

#unpacking a collection of values
fruits = ["apple", "pear", "banana"]
yt, fr,de = fruits #assigns the values of the collection to the variables in the collection
print(yt,fr,de)

#you can use the '+' operator to add outputs together
i = "I "
am= "am "
learning = "learning "
py = "Python"
print(i + am + learning + py) # I am learning python- if it was numbers it would add them together instead - can't combine str and int together with +

#seperate the console out a bit
print("------------------------------------------------")
#GLOBAL VARIABLES
#global variables are assigned outside of a function such as the variables made above - so they can be used everywhere inside and outside of the functions
globalVariable = "global"

#function
def testingGlobalVariableScope():
    print("This is " + globalVariable)
    
testingGlobalVariableScope()

#if we create a variable inside the function with the same name - the one in the function stays local where as the one outside is global- the global
#variable will stay the same name with the original value

scopeTesting = "global scope"

def scopeTestingFunction():
    scopeTesting= "local scope"
    print("This is " + scopeTesting)
    
scopeTestingFunction()#even though its the same name as the global scope when the function is called the local scope version is printed
print("This is " + scopeTesting)#when outside of the function and not called by the function the global version is printed.

#You can make a variable inside of a function global with the keyword
def globalKeyword():
    global thisIsNowGlobalScope
    thisIsNowGlobalScope = "we made it global!"
    
globalKeyword()
print(thisIsNowGlobalScope)#We printed the variable created within the function out of the scope due to the global keyword. 

#With lines 73-80 we where able to create two seperate values for the same variable name due to scopes.
#if we wanted to change the global variable inside the function so the change doesn't stay local use the same keyword

thisWasMadeGlobal= "this was made outside of a function."

def changingGlobalVariablesInsideFunc():
    global thisWasMadeGlobal
    thisWasMadeGlobal = "this variable changed on a global scope within this function(not just a local change now)"
    
changingGlobalVariablesInsideFunc()

print(thisWasMadeGlobal) # through this function we have changed the variable name on a global scope now as well. 
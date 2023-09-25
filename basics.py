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

#Can change variable type on the fly such as from int to strring

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
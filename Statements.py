# For loop when same thing needs to be printed for no of times
# use underscore instead of assigning a variable

for _ in 'Hello World!':
    print('Hello Folks')

# We can iterate List , string, tuples, dictionaries

#TUPLE UNPACKING: duplicate the structure of the item in the list(in for loop) and unpack them

my_list = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in my_list:
    print(a)
    print(b)
#OR
for a,b in my_list:
    print(a + b)

#---------------------------------------------------------------------------------------------------------------------/

#----------WHILE LOOP----------

#syn
count = 9
while count > 0:
    print('do something')
    count = count -1
else:
    print('do something else')
#Note - Else is optional

#----------------------------------------------------------------------------------------------

# BREAK ---> Breaks out of the current closest enclosing loop
# CONTINUE --->Goes to the top of the closest enclosing loop i.e starts next iteration
# PASS ---> Does nothing at all

#---------------------------------------------------------------------------------------------

# ENUMERATE FUNCTION
word = 'asdfghbhu'
for index,letter in enumerate(word):
    print(index ,letter)

# ZIP FUNCTION

my_list = [1,3,5,7,5,7]

for item in zip(my_list,word): #will combine each element of a list in a tuple
    print(item)

# IN OPERATOR---checks if item is present in the list
print('x' in ['a','b','g'])
print('mykey' in {'mykey':456})

#----------------------------------------------------------------------------------------------------------------------
# MATHS FUNCTIONS

# min function ----> gives minimum value ---> min(mylist)
# max function ----> gives maximum value ---> max(mylist)

# RANDOM LIBRARY

from random import shuffle
my_list = [1,2,3,4,5,6,7,8]
shuffle(my_list) #will shuffle the list; doesn't return anything
print(my_list)

from random import randint
# syntax : randint(lower_range,upper_range) ----> grabs a random integer within the range

print(randint(0,100))

#-----------------------------------------------------------------------------------------------------------------------

# USER INPUT

# result = input('what is your name?') #Note: Always accepts result as a STRING!
# print(result)

#-----------------------------------------------------------------------------------------------------------------------

# LIST COMPREHENSIONS!
# if you find yourself using a for() loop with a append statement to create a list,
# List Comprehensions are a good alternative
#won't save computation time

# 1. Simple
my_list = [ele for ele in range(0,9)]
print(my_list)

# 2. Operations on element
my_list = [ele+'a' for ele in 'acfgbh']
print(my_list)

# 3.including 'IF' statement
my_list = [ele for ele in range(0,11) if ele%2==0]
print(my_list)

# 4. Cel to Fah
cel = [0,9,10,20,40.5]
fah = [((9/5)*temp + 32) for temp in cel]
print(fah)

# 5. If and Else statement
my_list = [x if x%2==0 else 'ODD' for x in range(0,10)]
print(my_list)

# 6. NESTED LOOPS
my_list = [x*y for x in range(2,7,2) for y in [1,100,1000]]
print(my_list)

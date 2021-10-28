#--------NUMBERS--------
print(0.1+0.2-0.3)
#to get square root
print(100 ** 0.5)
#to get square
print(100 ** 2)
#--------ASSIGNING VARIABLES------
A=3.01
print((type(A)))
#----------------------------------------------------------------------------------------------------------------------/

#--------|STRINGS|----------
print("I Don't Mind")
print("Meetali \nMude") #ESCAPE SEQUENCE-->NEW LINE
print("Meetali \tMude")#ESCAPE SEQENCE--->4 SPACES
print(len("I am hungry")) #Gives length of a string--->spaces included

#INDEXING-->Grabbing a single character of a string
myString = "Covid Sucks!!!"
print(myString[-1])
#or
print(myString[0])
#Both are same---Forward starts with "0" and Reverse starts with "-1"

#SLICING--->Grabbing a sub-section of a string
#Syntax------->string_name[start:stop:step]
myString1 = "LetsDoThis,ShallWe!"
print(myString1[4:]) #Start from the index,till the end of the string
print(myString1[:10]) #go upto that index, but don't inclue that index
print(myString1[11:16])
print(myString1[::]) #go from begining till the end--->not used
print(myString1[::2])
print(myString1[::-1]) #TO REVERSE A STRING!!----->TRICK:p

#STRING PROPERTIES AND STRING METHODS

#***Strings are 'IMMUTABLE' ---> does not support item assignment
name = 'Meetali Mude'
last_name = name[7:]
print(name[:7] + "Prashant" +last_name) #String Concatenation

letter = 'z'
print(letter*10) #multiplication

x = name.upper() #does not change the original string-->you need to assign it to another variable
print(x)
y="Lets see the split function!"
print(y.split()) #splits into a list based on whitespace
print(y.split('e')) #splits based on 'e'

#-----PRINT FORMATING------

#1. Formatting with the.format() method
print('I want coffee {}'.format('CAPPUCCINO!'))
print('My {} dog {} are {} {}'.format('golden retriever','favourite','breeds','husky'))
#this is going to insert the strings in the same order as supplied
print('My {1} dog {2} are {0} {3}'.format('golden retriever','favourite','breeds','husky'))
#this will display according to the index position
print('My {1} dog {2} are {2} {2}'.format('golden retriever','favourite','breeds','husky'))
# can be repeated
print('My {f} dog {b} are {h} {g}'.format(g='golden retriever',f='favourite',b='breeds',h='husky'))
# with keywords----->Preferable!

#2.Float Formatting with .format() method
#Synatx--->"{value:width.precision f}"
num1 = 100/898
print('The result is {n:8.4f}'.format(n=num1))

#3. f string or formatted string literals---->came in Python 3.6 (new*)
print(f'Hello! I am {name}') #Does the same thing but with a simpler synatx

#----------------------------------------------------------------------------------------------------------------------/

#-----------------\LIST\------------------
#lists are ordered sequences that can hold a variety of object types
my_list = [1,'One',100.00,]
print(len(my_list)) #prints length of the string
print(my_list[1])
another_list = [2,'Two',2000.25]
new_list = my_list + another_list #list concatenation
print(new_list)
print(new_list[2:]) #List Slicing

#***Lists are 'MUTABLE' unlike strings!!!----->supports item assignment
new_list[2] = 100.12345
print(new_list)
#List Methods
new_list.append('NEW!') #will add new element at the end
new_list.append('VIRUS')
print(new_list)
caught = new_list.pop() #will remove-->if no index provided, it will remove the last element of the list
new_list.remove(2) #Will remove first occurance of the element provided
print(new_list,caught)
#new_list.sort() #Observe the Error
alphabet_list = ['m','e','t','a','l','i']
alphabet_list.sort() #can sort alphabets and numbers, doesn't return anything,-->method
sorted(alphabet_list) #built in function, will return sorted list
print(alphabet_list)
new_list.reverse() #reverses the List
print(new_list)
#NOTE: There is a Special object in Python called 'None'---->used to indicate no value
new_list.remove
#list Searching:
biscuits = "HideNSeek"
fav_biscuits = ["HideNSeek","Oreo","ParleG"]
if biscuits in fav_biscuits:
    print("Available")
else:
    print("Out of Stock")

#List of list
Brand_details = [['HM',1],['ZARA',3],['MNS',4]]

help(my_list.extend)
#----------------------------------------------------------------------------------------------------------------------/

#--------------TUPLES-------------------
#They are similar to list except one key difference - 'IMMUTABILITY!'
#why use tuples --> provided data integrity
#Tuples use parenthesis --> (1,2,3) or set of values separated by comma

s_t = 4,5,6
t=(1,2,3,2)
#we can perform indexing and slicing on tuples

#Built-in functions:
print(t.count(2),type(s_t))
print(t.index(2))

single_ele_t = ('A')
print(single_ele_t)

t = t + ('d',0.58,1)
print(t)

#to convert a list into tuple
l_t = ([1,2,3,4])

#----------------------------------------------------------------------------------------------------------------------/

#-----------------DICTIONARIES-----------------------
#They are unordered mappings for storing objects. They use key-value pairing.
#Synatx --> {"key1":"value1","key2":"value2"}
#when do you use a dictionary ---> when you want to quickly retrieve a value without knowing its index
#Dictionaries are "MUTABLE"
# When two sets of data are needed and independently they do not make any sense

my_groceries = {'milk':24, 'bread':30, 'chocolate':35}
print(my_groceries['bread'])

d = {'k1':1213, 'k2':[1,3,5,7] ,'k3':{"insidekey": 100}}
print(d['k2'][2] ,  d['k3']['insidekey'])

print(my_groceries.keys()) #displays all the keys
print(my_groceries.values()) #displays all values
print(my_groceries.items()) #displays both keys and values

#Iterating through the dictionary:

for key,value in my_groceries.items():
    print(key,"-->",value)
for keys in my_groceries.keys():
    print(keys)
#Simailarly for values!

#----------------------------------------------------------------------------------------------------------------------/

#--------------SETS------------------
#Sets are 'unordered' collection of unique elements.

my_set = {1,2,3,4,5}
my_set.add(6)
print(my_set)
my_set.add(2) #won't be adding '2' as 2 is already present

#Eliminating duplicates from a list
exx_list = [1,1,3,5,3,6,3,64,6,7,4,7,6]
print(set(exx_list)) #will display unique values, also unordered values

#Common elements between 2 sets
my_set_A = {5,4,6,7,8,9}
print(my_set&my_set_A) #remember--> no spaces

#Merging elements of 2 sets
print(my_set|my_set_A)
whole_set = my_set|my_set_A
#Extracting elements of a set-->setA-setB---->gives the elements that are only in setA
print(whole_set-my_set)

#----------------------------------------------------------------------------------------------------------------------/

#------------BOOLEANS--------------
#Booleans are operators that allows you to convey True or False Statements

bool = True
print(type(bool))





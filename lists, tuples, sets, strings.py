#creating a square of a given list
list1=[1, 2, 3, 4, 5]
new_list=[i*i for i in list1]

print(list1)
print(new_list)

#separating comopnents of tuple
tuple1=(0, 1, 2, 3, 4, 5)
i1, *i2, i3 =tuple1

print(i1)  #prints 1st element
print(i2)  #prints all elements between first and last
print(i3)  #prints last element

# Point to note: Creating a list takes more time as well as memory than a tuple. So, working with tuples can be MORE efficient.

# Frozen Sets
setA=frozenset(["a",1,"MadMax"])
print(type(setA))
setA.add(1)  #throws an error as FrozenSets are immutable, unlike normal Sets
print(setA)

#Splitting strings into lists
string1='this:is:a:demo:program'
list2=string1.split(':') #mention the kind of delimiter in the split argument
print(list2) 
print(' '.join(list2)) #mention the kind of delimiter before the join function     

#Point to note: In order to create a string by joining elements of a list, prefer the 'join' function to looping through the list and storing it in a blank string. It saves time.

#Formatting in strings

#Using format()
var1=3.1234567
var2=5
string1="This is a new string with {} and {}".format(var1,var2)  #You can give arguments in the curly braces to mention the no. of decimal points e.g. {:.2f}->2 decimals
print(string1)

#Using f-strings
var1=3.1234567
var2=5
string1=f"This is a new string with {var1*2} and {var2}"  #This statemnets executes at runtime, so arithmetic operations can be included in the curly braces.
print(string1)
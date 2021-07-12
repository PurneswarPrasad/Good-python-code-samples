#Collections is a module that gives container functionality. We'll discuss their libraries below.

#Counter
from collections import Counter
#Counter is a container that stores the elemnts as dictionary keys and their counts as dictionary values
a="aaaaaabbbbcc"
my_counter=Counter(a)  #makes a dictionary of a
print(my_counter.keys())  #prints the keys
print(my_counter.values()) #prints the values
print(my_counter.most_common(1)) #prints the most common key-value pair. Putting 2 will print the 2 most common key-value pairs, etc.
# most_common() returns a list with tuples in it.
print(my_counter.most_common(1)[0][0])  #this prints the element with the highest occurence.
print(list(my_counter.elements())) #iterates over the whole Counter and returns a list of elements

#NamedTuple
from collections import namedtuple
Point=namedtuple('Point', 'x,y')
pt=Point(1,-4)   #returns point with x and y values
print(pt)

#OrderedDict library is used to create dictionaries whose order can be maintained. Python 3.7 and higher already has this built-in function while creating dictionaries.

#defaultDict
from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=2
d['c']=1   
print(d['d']) #Giving a key-value that is not there in the dictionary will give a default value of the kind of datatype mentioned in the defaultdict() function.

#Deque (Double ended queue)-(Insert and remove from both ends)
from collections import deque
dq=deque()

dq.append(1)
print(dq)
dq.append(2) #appends 2 to the right of 1
print(dq)
dq.appendleft(3) #append 3 to the left of 1
print(dq)
dq.pop() #removoes an element from the right side
print(dq)
dq.popleft() #removes an element from the left 
print(dq)
dq.clear() #Clears the entire deque
dq.extend(3,1,2,4,5,6) #appends multiple elements to the right
print(dq)
dq.extendleft(3,1,2,4,5,6) #appends multiple elements to the left
print(dq)
dq.rotate(1) #Shifts elements to the right side by 1 place
print(dq)
dq.rotate(-1) #Shifts elements to theleft by 1 place
print(dq)
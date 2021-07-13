# Iterators is a module which is a collection of tools for handling operators

# 1) product : makes the cartesian product of 2 lists given as input
# 2) permutations : takes the list and the length (if specified, otherwise the length of list) and gives all possible permutations
# 3) combinations : takes the list and the length (if specified, otherwise the length of list) and gives  all combinations, except duplicates.

# 4) accumulate
from itertools import accumulate
import operator  #mentions the desired operator 
a=[1,2,3,4]
b=[1,2,3,5,4]
acc=accumulate(a, func=operator.mul)  #for multiplication
acc1=accumulate(b, func=max) #moves through the list and looks for the highest and puts that in the new list 
print(a)
print(list(acc))
print(list(acc1))

# 5) groupby
from itertools import groupby

# def smaller_than_3(x):
#    return x<3

a=[1,2,3,4]
group_obj=groupby(a, key=lambda x: x<3)  # use lambda function instead of calling the function
for key, value in group_obj:
    print(key,list(value))   #returns in True and False along with the list that contains the values
    
# -----------------------------------------------------------------------------------------------------------------------------
# Some use cases of lambda fucntion

points2d=[(1,2),(15,1),(5,-1),(10,4)]

points2d_sorted=sorted(points2d) #this will sort by the x-values only
points2d_sorted_y=sorted(points2d, key=lambda x:x[1]) #sorting by the y-values
points2d_sorted_sum=sorted(points2d, key=lambda x:x[0]+x[1]) #sorting by the sum of x and y values
print(points2d_sorted)
print(points2d_sorted_y)
print(points2d_sorted_sum)

#map function: map(func, sequence)
x=[1,2,3,4,5]
print(list(map(lambda i: i*2, a)))  # This can also be done using list comprehension mentioned earlier

#filter function: filter(func, sequence)

#reduce function: reduce(func, sequence)
from functools import reduce  #Note this function is from the functools module

a=[1,2,3,4,5,6,7]
product_a=reduce(lambda i,j:i*j, a)  #multiplies the elements of the list with each other
print(product_a)
# ------------------------------------------------------------------------------------------------------------------------------

# 6) Infinite iterators
# a-> count() : takes a number as argument and adds 1 with it infinitely. Can set the limit where to stop.
# b-> cycle() : takes a list as argument and displays it infinitely
# c-> repeat() : takes a number and displays it infinitely. Can set the limit where to stop.



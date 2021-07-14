import random

#Seeding will keep on generating the same random numbers. If the seed value is changed, the value of the random number changes
random.seed(1)
print(random.random()) #random float between 0 and 1
print(random.uniform(1,10)) #random float between given range
print(random.randint(1,10)) #random integer between given range
print(random.randrange(1,10)) #random integer between given range excluding last one

random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10))
print(random.randrange(1,10))

#The upper two sets will produce the same results, but the lower one will be different

random.seed(2)
print(random.random())
print(random.uniform(1,10))
print(random.randint(1,10))
print(random.randrange(1,10))

#TO AVOID THIS seeding, we use the 'secrets' module

#List operations
mylist=list("ACDEFG")
print(mylist)
print(random.choice(mylist))  #random value from list
print(random.sample(mylist, 3)) #any given number random values from the list, without repetitions 
print(random.choices(mylist, k=3)) #any given number random values from the list, with repetitions
print(random.shuffle(mylist))

--------------------------------------------------------
#in Numpy :
#np.random.rand() - generates random array with numbers between 0 and 1, single or multi depending on argument
#np.random.randint() - generates random array with numbers between given range, single or multi depending on argument
#np.random.shuffle() - shuffle the array
---------------------------------------------------------
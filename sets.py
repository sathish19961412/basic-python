#sets integers
my_set={1,2,3}
print(my_set)

#set of mixed datatypes
my_set1={1,"sathish",(1,2,3)}
print(my_set1)

#Add Sets
my_set.add(4)
print(my_set)

#Add values 2 my_set
my_set.add(2)
print(my_set)

#update values
my_set.update([3,4,5])
print(my_set)

#remove values
my_set.remove(4)
print(my_set)


#Create Two Sets
my_set2={1,2,3}
my_set3={2,3,4,5}

#Equivalent to my_set2.union(my_set3)
print(my_set2|my_set3)

#Equivalent to my_set2.intersection(my_set3)
print(my_set2&my_set3)

#sets Difference

print(my_set2-my_set3)

print(my_set2^my_set3)
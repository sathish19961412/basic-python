#create range() function in access variables
numbers=range(1,6)
print(list(numbers))
print(tuple(numbers))
print(set(numbers))
print(dict.fromkeys(numbers,99)) 

#create range(start,end,step) function in access variables
numbers1=range(1,6,1)
print(list(numbers1))

numbers2=range(1,6,2)
print(tuple(numbers2))

numbers3=range(6,0,-2)
print(list(numbers3))


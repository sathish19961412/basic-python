#Show The Firuts List 
firuts=['apple','banana','cherry','apple','banana']
list=('a','3','5')
print(firuts)
print(len(firuts))
print(type(list))
print(type(firuts))

#Access The List

print(firuts[1])
print(firuts[-1])
print(firuts[0:3])
print(firuts[:2])
print(firuts[5:])

if "apple" in firuts:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is in the fruits list")

#Change Item Value

firuts[0]="blackcurrant"
firuts[1:3]=["blackcurrant","watermelon"]
firuts.insert(0,"sathish")
print(firuts)

#Add List Items

firuts.append('sathish')
print(firuts)

firuts.extend(list)
print(firuts)

#Remove list items

firuts.remove("sathish")
print(firuts)
firuts.pop(8)
print(firuts)
del firuts[0]
print(firuts)

#Loop Through a List
#for in
for x in firuts:
    print(x)

#for in range()
for y in range(len(firuts)):
    print(firuts[y])

#while loop
i=0
while i<len(firuts):
    print(firuts[i])
    i=i + 1

#List Comperhension

[print (x) for x in firuts]

#Without list comprehension

newlist=[]

for x in firuts:
    if 'apple' in x:
        newlist.append(x)
print(newlist)

#List Comprehension

list=[x for x in firuts if 'apple' in x]
print(list)

#sort

firuts.sort()
print(firuts)

listarry=[1,100,2,3,60,50,7]
listarry.sort(reverse=False)
print(listarry)

#function use sort

def myfunc(n):
    return abs(n-30)

list1=[100,50,60,70,23]
list1.sort(key=myfunc)
print(list1)



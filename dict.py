#Create Empty Dictionary
my_dict={}

#create dictionary with integer {keys:values}
my_dict1={
    1:'apple',
    2:'ball'
}

#create mixed datatypes in dictionary

my_dict2={
    'name':'sathish',
     1:[2,4,5]
}

print(my_dict)
print(my_dict1)
print(my_dict2)

#create dictionary to access the key:values

my_dict3={
    'name':'sathish',
    'age':26,
    'salary':3567.50
}

#Access to the Dictionary keys
print(my_dict3['age'])

#chanage to the age key=>values
my_dict3['age']=36
print(my_dict3)

#adding to the dictionary {key:values}
my_dict3['city']='coimbatore'
print(my_dict3)

#delete my_dict3 to city
del my_dict3['city']
print(my_dict3)

#delete dictionary
# del my_dict3
# print(my_dict3)

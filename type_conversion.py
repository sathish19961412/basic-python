#Type Conversion
num_int=123 #integer Type
num_flo=1.23 #float Type
num_str='456' #Str Type
num_new=num_int+num_flo

print('Value of num_new',num_new)
print('datatype of num_new',type(num_new))

#int and string
str_add=num_int+num_str
print(str_add)

#Explicity converted to int type
num_str=int(num_str)
print(num_int+num_str)



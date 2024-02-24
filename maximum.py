#maximum & minimum

def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
    
print("Search for the Maximum Number")
a=int(input('Enter the values a:'))
b=int(input('Enter the values b:'))
print(maximum(a,b))

##############################################################################

def minmum(c,d):
    if c<=d:
        return c
    else:
        return d
    
print("Search for the Minmum Number")
c=int(input('Enter the values c:'))
d=int(input('Enter the values d:'))
print(minmum(c,d))
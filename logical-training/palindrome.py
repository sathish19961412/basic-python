str=input('Enter the string to check palindrome')
str=str.casefold() # for caseless compare

if(str==str[::-1]):
    print("It is a palindrome")
else:
    print("It is a Not Palindrome")
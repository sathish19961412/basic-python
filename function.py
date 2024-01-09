#ex:1
#def function
def print_lines():
    print("I am lines1.")
    print("I am lines2.")
#function call
print_lines()

#ex:2
def add_numbers(a,b):
    sum=a+b
    print(sum)
add_numbers(5,8)

#ex:3
def add_numbers1(a,b):
    sum=a+b
    return sum
result=add_numbers(7,8)
print(result)
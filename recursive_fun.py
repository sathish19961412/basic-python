#Recursive Function To Find the factorial of numbers

def calc_factorial(x):
    if x==1:
        return 1
    else:
        return (x*calc_factorial(x-1))
num=int(input("Enter the number:"))
print("The factorial of",num,"is",calc_factorial(num))
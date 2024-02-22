def fact(n):
    if n<=1:
        return 1
    else:
        n=n*fact(n-1)
        return n
n=int(input("Enter The fact of Numbers"))
print("Factorial number",n,"is",fact(n))
y=int(input("Enter year to be Checked:"))

#leap year logical

if y % 4==0 and y % 100 !=0 or y % 400 ==0:
    print("yes,leap year")
else:
    print("Not a leap year")
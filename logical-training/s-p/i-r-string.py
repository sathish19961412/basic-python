str="SATHISH"
strlen=len(str)

for x in range(0,strlen):
  for y in range(strlen-1,x,-1):
    print("",end="") #2ws
  for z in range(0,x+1):
    print(str[z]+"",end="")
  print()
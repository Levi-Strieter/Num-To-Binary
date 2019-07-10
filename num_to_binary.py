arr = []

number = int(input("number- "))
x=0
while number-(2**x) > 0:
    x+=1
for y in range(x,0,-1):
    if number-(2**y)>=0:
        arr.append(1)
        number = number-(2**y)
        print(number)
    else:
        arr.append(0)
        print(number)

    
print(arr)


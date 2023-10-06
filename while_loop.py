num = int(input("Enter Number: "))
print(num)
cr = 0
while(num%10!=0):
    x = num%10
    cr = cr*10+x
    num = num//10
print(cr)

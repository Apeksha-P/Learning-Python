height = int(input("Enter your height in feet: "))
if height>=3:
    print("You can ride!")
    age = int(input("Enter your age: "))
    if age<=18:
        print("Pay Rs: 250")
    else:
        print("Pay Rs: 500")
else:
    print("You can not ride ! sorry!")
print("Good Bye!")

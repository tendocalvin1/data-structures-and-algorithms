while True:
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if (x == y):
            print("The two numbers are equal.")
        elif (x > y):
            print("The larger integer is:", x)
        else:
            print("The larger integer is:", y)
        break
    else:
        print("Invalid input. Please enter valid numbers.")
        
#script 
x =input("Enter my age:")
if x.isdigit():
    x = int(x)
if (x < 18):
    print("You're a child!")
elif(x > 18):
    print("You're an adult mate!")
elif(x > 12 & x < 20):
    print("You're a teenager mate!")
else:
     print("Invalid input. Please enter valid numbers.")
    
    
    
# script 2
age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    if age <= 1:
        print("You're an infant!")
    elif age > 1 and age < 13:
        print("You're a child!")
    elif age >= 13 and age < 20:
        print("You're a teenager!")
    elif age >= 20:
        print("You're an adult!")
    else:
        print("Invalid input. Please enter valid numbers.")

    


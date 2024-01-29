# odd or even
number =2
if (number % 2== 0):
    print("number is even")
else:
     print("number is odd")
     
     
while True:
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
        break
    else:
        print("Invalid input. Please enter a valid number.")
        
# grades
grade = input("Enter a number:")
if grade.isdigit():
    grade = int(grade)
if grade >= 60:
    print("Pass")
else:
    print("Fail")
    
# comparison
x = 45
y = 65
if (x == y):
    print("x is equal to y")
elif (x > y):
    print("The larger integer is:", x)
else:
    print("The larger integer is:", y)
    
    


    
    


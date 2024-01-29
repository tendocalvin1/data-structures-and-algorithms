#concatenation
string1 = "Hello"
string2 = "Jacinta!"
result = string1 + string2
print(result)

#string length
text= "I am going to become very wealthy in my family!"
length = len(text)
print("length of the string:", length)

# string formatting
name= "Eng Dave"
age = 25
formatted_string = f"Hello, my name is {name} and I am {age} years old."
print(formatted_string)

str="Beau"
print("beau".upper())
print("BEAU".lower())
print("tendo calvin".title())
print("tendo calvin".endswith("n"))
print("tendo calvin".__add__(" is a programmer, data scientist, cybersecurity analyst and a real estate developer"))

# escaping strings
str = "ca\"lvin"
print(str)
str ="Elon Musk is great"
print(str[3])
print(str[-1])
print(str[2:10])
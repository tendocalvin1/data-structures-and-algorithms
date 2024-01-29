# reverse
def reversed_string(str):
    reversed_string=str[::-1]
    return reversed_string

str = "Hello Family"
output_str = reversed_string(str)
print("Original_string:", str)
print("Reversed_string:", output_str)

#count
def count_vowels(input_string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
print("The number of vowels in the string is:", count_vowels(input_string))

# counting characters including space
str = "My name is Tendo Calvin"
count = len(str)
print("The number of characters in the string are:", count)
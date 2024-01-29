# lists (list of random numbers between 1 and 100.)
from random import randint

random_numbers = [randint(1,100) for number in range(10)]
print("generated random numbers:", random_numbers)
print("largest_number:",max(random_numbers))
print("smallest_number:",min(random_numbers))

# list (ascending order)
my_list =["dave","collins", "arnold","richard","calvin"]
my_list.sort()
my_list.append("Mercy")
print("Sorted list:",my_list)

# list (descending order)
my_list =["dave","collins", "arnold","richard","calvin"]
my_list.sort(reverse=True)
my_list.append("Mercy")
print("Sorted descending list:",my_list)
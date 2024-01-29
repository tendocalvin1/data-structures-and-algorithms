my_list = ["2","4",{"apple","banana","pineapple","watermelon"},{"calvin","melissa"}]
for my_list in my_list:
    print(my_list)

matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(j + 1 + i * 3)
    matrix.append(row)

print(matrix)
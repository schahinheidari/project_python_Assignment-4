#Assignment 5

n = int(input("Please enter a number for the shape of a triangle: "))
list= [[1 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(1, i):
        list[i][j] = list[i-1][j] + list[i-1][j-1]

for i in range(n):
    for j in range(i + 1):
        print(list[i][j], end=" ")
    print()
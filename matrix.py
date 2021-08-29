from array import *
matrix = []
for i in range(0,2):
    a = [];
    for j in range(0,2):
        a.append(int(input()));
    matrix.append(a);

#printing matrix
for i in range(0,2):
    for j in range(0,2):
        print(matrix[i][j], end=" ");
    print("\n");

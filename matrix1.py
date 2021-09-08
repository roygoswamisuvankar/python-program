c,r = input().split(" ");
col = int(c);
row = int(r);
#matrix function to printing matrix
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ");
        print();

#matrix initialization
m = [[0 for i in range(0, row)] for j in range(0, row)]
for i in range(0, row):
    for j in range(0, col):
        m[i][j] = int(input());

#printing matrix using matrix function pass the parameter
print(m);


#matrix print function
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end= " ");
    print("\n");

matrix_a = [[0 for i in range(0,2)] for j in range(0,2)];
matrix_b = [[0 for i in range(0,2)] for j in range(0,2)];
sum = [[0 for i in range(0,2)] for j in range(0,2)];

print("Enter Matrix A elements : ");
for i in range(0,2):
    for j in range(0,2):
        matrix_a[i][j] = int(input());

print("Enter Matrix B elements : ");
for i in range(0,2):
    for j in range(0,2):
        matrix_b[i][j] = int(input());

for i in range(0,2):
    for j in range(0,2):
        sum[i][j] = matrix_a[i][j] + matrix_b[i][j];


print("The sum of two Matrix : ");
matrix_print(sum);
        





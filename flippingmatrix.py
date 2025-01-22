import numpy as np  
matrix = np.array([    [16, 18, 15, 11, 15, 17, 15,  7,  7, 12, 12,  2],
    [ 9,  2, 10,  8,  2, 13,  2, 10,  8,  7, 17, 11],
    [13, 17,  3,  1, 11,  9, 20,  3,  3, 20,  6, 20],
    [ 3, 16, 13,  4,  6,  5, 16, 19, 15, 14, 16,  8],
    [ 6, 18, 18,  2, 126, 188, 105, 139, 11, 17, 17,  8],
    [10,  9, 14,  7, 159, 198, 200, 198, 14,  1,  5, 16],
    [ 6,  1,  4, 19, 130, 184, 178, 120, 12, 18, 10, 18],
    [19, 11, 11,  3, 200, 167, 171, 163,  4, 17,  9, 11],
    [ 8,  3, 18, 19,  18,  14,   1,   6, 14,  2,  4, 17],
    [ 6, 20, 18,  7,   4,   8,  13,   2,  6,  5, 20,  7],
    [ 8,  5, 12,  7,  15,  18,   5,   6,  7,  2, 14, 19],
    [19, 17, 14, 16,   4,  13,   6,   4, 11, 12,  9,  5]
])
n = len(matrix) // 2  #len of matrix
maxSum = 0
if n == 1:
    maxSum = matrix[0,0]   
for j in range(len(matrix[0])): # trough each column
    for i in range(n):  # looking for the max in the nxn
        if matrix[i][j] < matrix[-i-1][j]:
            matrix[i][j], matrix[-i-1][j] = matrix[-i-1][j], matrix[i][j]

# Order rows
for i in range(len(matrix)):  # for each row
    for j in range(n):  # for each mirror row
        if matrix[i][j] < matrix[i][-j-1]:
            # change only if the element coul'd be in submatrix
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

# sum NxN 
maxSum = 0
for i in range(n):
    for j in range(n):
        maxSum += matrix[i][j]

matrixN = matrix[0:n,0:n]
print (matrixN)
matriks = [[0 for j in range(4)] for i in range(3)]
print(matriks)

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
x = int(input())
y = int(input())


print(var_mat[x][y])

var = [[5, 0],
      [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var)):
  for j in range(len(var[0])):
    def_mat[i][j] = var[i][j]*2

print(def_mat)
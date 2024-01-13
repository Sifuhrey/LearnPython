var = [1,7,2,89,3]
leftpointer = var[0]

for i in range(1, len(var)):
    rightpointer = var[i]
    if rightpointer > leftpointer:
        leftpointer = rightpointer
print(leftpointer)
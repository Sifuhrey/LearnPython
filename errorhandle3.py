x = int(input())
if x < 0:
    raise ValueError
else:
    for i in range(x):
        print(i+1)
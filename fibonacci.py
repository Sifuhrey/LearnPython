
def fib(n):
   
    if n <=2:
        result = 1
    else:
        result = fib(n-1)+fib(n-2)
    return result
num = int(input())
print(fib(num))
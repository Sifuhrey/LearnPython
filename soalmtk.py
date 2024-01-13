def f(x, n):
    if n==0: return x
    else:
        x = (x**2)-(3*x)
        return f(x,n-1)
a = 2
hasil = f(a, 3) // f(a, 2) - f(a, 1)
print(hasil)
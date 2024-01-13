daftar = [1,2,3,4]
for i in daftar:
    print(id(i))
print(daftar)

nol = [0 for i in range(10)]
print(nol)

var = [1,2,3,4,5]
for i in range(len(var)):
    now = var[i]
    nextin = i+1
    if nextin < len(var):
        nextelemen = var[nextin]
    else:
        nextelemen = None
    print(f"sekarang: {now}, next: {nextelemen}")
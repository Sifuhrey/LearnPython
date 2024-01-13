print("for loop")
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in num:
    print(i)
print("while loop: ")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

print("break")
str = input()
for i in str:
    if i == " ":
        continue
    print(format(i))

print("else setelah for")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")
print("list comprehension")
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

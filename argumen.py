# keyword argument
def rectangle(panjang, lebar):
    luas = panjang*lebar
    return luas


persegipanjang = rectangle(lebar=10, panjang=5)
print(persegipanjang)


# positional argument
def persegipanjang(panjang, lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang


persegipanjang2 = persegipanjang(6, 7)
print(persegipanjang2)

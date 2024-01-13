#positional or keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

#positional only
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))

#keyword only
def sapa(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(sapa(pesan="Selamat sore!",nama="Dicoding"))

#var-positional (jumlah argumen fleksibel/dinamis)
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

#var-keyword(jumlah keyword argumen fleksibel/dinamis)
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

#lambda expression
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))
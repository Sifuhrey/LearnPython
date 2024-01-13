kata = "         sifuhrey           "
kata = kata.upper()
print(kata)
kata = kata.lower()
print(kata)
print(kata.rstrip())
print(kata.lstrip())
kata2 = '     wwkwkkw      '
print(kata2.strip())
katakata ='Fakhri Abdillah'
print(katakata.strip("Fakhri "))
print(katakata.startswith('Fakhri'))
print(katakata.endswith("fakhri"))
print(' '.join(["Fakhri","abdillah"]))
print('1111'.join(["Fakhri","abdillah"]))
print('kanjut badag hideung'.split())
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))
hurup= "ayam bebek sapi"
print(hurup.replace("ayam","domba"))
print(hurup.isupper())
print(hurup.islower())
print(hurup.isalpha())
print(hurup.isalnum())
print("123".isdecimal())
print("    ".isspace())
print("Mobil".istitle())
word = "roti"
print(word.zfill(5))
print(word.rjust(5,"5"))
print(word.ljust(5,"5"))
print(word.center(6,"5"))
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")
print(r'fakhri\tabdillah')
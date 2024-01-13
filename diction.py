x={'nama':'fakhri',"asal":"bandung","umur":20}
print(type(x))
print(x['asal'])
x["status"]='mahasiswa'
print(x)
del x['umur']
print(x)
x["asal"]='medan'
print(x)
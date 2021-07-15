# Menghitung Luas Segitiga
alas = 10
tinggi = 4
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}')


# Menggunakan fungsi def()
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


print(hitung_luas_segitiga(10, 6))

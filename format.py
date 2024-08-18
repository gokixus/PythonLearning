ad = 'Gokdeniz'
soyad = 'Yilmaz'
yas = 21

mesaj = "Merhaba benim adim {}, soyadim {} ve {} yasindayim".format(ad, soyad, yas)
print(mesaj)

mesaj = "Merhaba benim adim {2}, soyadim {0} ve {1} yasindayim".format(ad, soyad, yas)
print(mesaj)

mesaj = "Merhaba benim adim {a}, soyadim {s} ve {y} yasindayim".format(a=ad, s=soyad, y=yas)
print(mesaj)

mesaj = "Merhaba, benim adim {ad} ve {yas} yasindayim"
print(mesaj)

mesaj = f"Merhaba, benim adim {ad} ve {yas} yasindayim"
print(mesaj)
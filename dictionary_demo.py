#ogrenciler = {
#   "120": {
#        "ad":"Ali"
#        "soyad":"Yilmaz"
#        "telefon":"5320000001"
#    },
#    "125": {
#        "ad":"Can"
#        "soyad":"Korkmaz"
#        "telefon":"5320000002"
#    },
#    "128": {
#        "ad":"Volkan"
#        "soyad":"Yükselen"
#        "telefon":"5320000003"
#    },
#}

#1- Bilgileri verilen öğrencilerin kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
#2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrenciler1 = {}
number1 = input("Öğrenci No: ")
name1 = input("Öğrenci Adi: ")
surname1 = input("Öğrenci Soyadi: ")
phone1 = input("Öğrenci Telefon Numarası: ")

ogrenciler1[number1] = {
    "ad": name1,
    "soyad": surname1,
    "telefon": phone1,
}

print(ogrenciler1)

ogrenciler2 = {}
number2 = input("Öğrenci No: ")
name2 = input("Öğrenci Adi: ")
surname2 = input("Öğrenci Soyadi: ")
phone2 = input("Öğrenci Telefon Numarası: ")


ogrenciler2.update({
    number2: {
        "Ad": name2,
        "Soyad": surname2,
        "Telefon": phone2
    }
})

print(ogrenciler2)
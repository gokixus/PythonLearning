sayilar = [1,3,5,7,9,12,19,21]

#1- Sayilar listesindeki 3'ün katı olanları yazdır.
#2- Sayilar listesindeki tek sayi olanları karesini alıp yazdır.
#3- Sayılar listesindeki sayıları topla.

for sayi1 in sayilar:
    if(sayi1 % 3 == 0):
        print(sayi1)
print(" ")
for sayi2 in sayilar:
    if(sayi2 % 2 != 0):
        print(sayi2**2)
print(" ")

toplam = 0
for sayi3 in sayilar:
    toplam += sayi3
print(toplam)

print(" ")
#4- Şehirlerden hangileri en fazla 5 karakterlidir?
sehirler = ["Kocaeli", "İzmir", "Kayseri", "Ankara", "Van", "Rize", "Artvin", "Muş"]

for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)
        
print(" ")
#5- Ürünlerin fiyatları toplamı nedir ?
#6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz.

urunler = [{"name": "Samsung S6", "fiyat": "3000"},
           {"name": "Samsung S7", "fiyat": "4000"},
           {"name": "Samsung S8", "fiyat": "6000"},
           {"name": "Samsung S9", "fiyat": "7000"},
           {"name": "Samsung S10", "fiyat": "8000"}]

toplamFiyat = 0
for urun1 in urunler:
    toplamFiyat += int(urun1["fiyat"])
print(toplamFiyat)

print(" ")
for urun2 in urunler:
    if(int(urun2["fiyat"]) <= 5000):
        print(urun2["name"])
    

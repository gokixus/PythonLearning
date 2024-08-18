sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesini while ile ekrana yazdırın.

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# bas = int(input("Başlangıç değeri: "))
# son = int(input("Bitiş değeri: "))

# i = bas
# while (i < son):
#     i += 1
#     if(i % 2 != 0):
#         print(i)

# 3- 1-100 arasındaki sayıları azalan şeklinde yazdırın.

# i = 100
# while (i > 0):
#     print(i)
#     i -= 1
    
# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.

# numbers = []
# i = 0
# while (i < 5):
#     sayi = int(input(f"{i+1}. sayi giriniz: "))
#     numbers.append(sayi) 
#     i += 1
# numbers.sort()
# print(numbers)

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
#   *ürün sayısını kullanıcıya sorun.
#   **dictionary listesi yapısı (name, price) şeklinde olsun.
#   ***ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []
urunSayisi = int(input("Kaç adet ürün eklemek istiyorsunuz ? : "))
i = 0

while(i < urunSayisi):
    name = input("Ürün ismi: ")
    price = int(input("Ürün fiyatı: "))
    urunler.append({
        "Name": name,
        "Price": price
    })
    i += 1
    
for urun in urunler:
    print(f"Ürün adı {urun["Name"]} ve fiyatı {urun["Price"]}")
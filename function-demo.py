# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def kelimeYaz(kelime, adet):
#     for adet in kelime:
#         print(kelime)
# kelime = input("Bir kelime giriniz: ")
# adet = int(input("Kaç kez yazılacak ? : "))
# kelimeYaz(kelime, adet-1)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

# def listeyeCevir(*parametreler):
#     liste = []
#     for parametre in parametreler:
#         liste.append(parametre)
#     return liste

# print(listeyeCevir(10, 20, 30, "Merhaba"))

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asallariBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
                    
# sayi1 = int(input("1. Sayi : "))
# sayi2 = int(input("2. Sayi : "))
# asallariBul(sayi1, sayi2)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenleriBul(sayi):
    tamBolenler = []
    
    for i in range(1, sayi):
        if(sayi % i == 0):
            tamBolenler.append(i )
    return tamBolenler

print(tamBolenleriBul(20))
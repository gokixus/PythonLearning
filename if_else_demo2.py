# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = int(input("Sayi giriniz: "))

if (sayi > 0) and (sayi <= 100):
    print("Girilen sayi 0-100 arasindadir")
else:
    print("Girilen sayi 0-100 arasinda değildir.")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi2 = int(input("Sayı giriniz:"))

if (sayi2 > 0):
    if(sayi2 % 2 == 0):
        print("Girilen sayı hem pozitif hem de çift sayıdır")
    else:
        print("Girilen sayi pozitif ancak çift sayı değildir.")
else:
    if(sayi2 % 2 == 0):
        print("Girilen sayi çift sayı ancak negatiftir.")
    else:
        print("Girilen sayi hem pozitif hem de çift sayı değildir.")

# 3- Email ve parola bilgileriyle giriş kontrolü yapınız.

email = input("Email: ")
sifre = input("Şifre: ")

realEmail = "gokdeniizyilmaz@outlook.com"
realSifre = "123456789"

if (email == realEmail) and (realSifre == sifre):
    print("Giriş bilgileri doğru.")
else:
    print("Giriş bilgileri yanlış")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input("a. Sayi: "))
b = int(input("b. Sayi: "))
c = int(input("c. Sayi: "))

if (a > b > c):
    print("a > b > c")
elif (a > c > b):
    print("a > c > b")
elif (b > a > c):
    print("b > a > c")
elif (b > c > a):
    print("b > c > a")
elif (c > a > b):
    print("c > a > b")
else:
    print("c > b > a")
    
# 5- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti,
#değilse kaldı yazdırınız. Koşullar: Ortalama 50 olsa bile final notu en az 50 olmalıdır. Ayrıca finalden 70 alındığında
#ortalamanın önemi olmasın.

vize1 = int(input("1. Vize: "))
vize2 = int(input("2. Vize: "))
final = int(input("Final: "))
ortalama = vize1*0.3 + vize2*0.3 + final*0.4

if (ortalama >= 50):
    if(final >= 50):
        print("Geçtiniz")
    else:
        print("Final notunuz 50 altında olduğundan geçemedimiz")
else:
    if(final >= 70):
        print("Ortalamanız 50 altında ancak final 70 ve üstü aldığınız için geçtiniz")
    else:
        print("Geçemediniz")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız.
#   Formül : (kilo/boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#       0-18.4 -> Zayıf
#       18.5-24.9 -> Normal
#       25.0-29.9 -> Fazla Kilolu
#       30.0-34.9 -> Şişman(Obez)

boy = float(input("Boyunuzu giriniz(metre cinsinden): "))
kilo = int(input("Kilonuzu giriniz: "))
kilo_indeksi = kilo/(boy**2)

if (0 <= kilo_indeksi) and (kilo_indeksi <= 18.4):
    print(f"Kilo indeksiniz {kilo_indeksi} ve zayıfsıınız.")
elif (18 <= kilo_indeksi) and (kilo_indeksi <= 24.9):
    print(f"Kilo indeksiniz {kilo_indeksi} ve normalsınız.")
elif (25.0 <= kilo_indeksi) and (kilo_indeksi <= 29.9):
    print(f"Kilo indeksiniz {kilo_indeksi} ve fazla kilolusunuz.")
elif (30.0 <= kilo_indeksi) and (kilo_indeksi <= 34.9):
    print(f"Kilo indeksiniz {kilo_indeksi} ve şişmansınız.")
else:
    print(print(f"Kilo indeksiniz {kilo_indeksi} ve aşırı şişmansınız."))


#1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 yaş ve 
#   eğitim durumu lise ya da üniversite olmalıdır.

isim = input("İsim: ")
yas = int(input("Yaş: "))
egitim = input("Eğitim durumunuz: ")

if (yas >= 18) and (egitim == "Lise" or egitim == "Üniversite"):
    print(f"{isim} adlı kişisi ehliyet alabilir")
else:
    print(f"{isim} adlı kişisi ehliyet alamaz")
    
#2- Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#   0-24    => 0
#   25-44   => 1
#   45-54   => 2
#   55-69   => 3
#   70-84   => 4
#   85-100  => 5

sinav1 = int(input("1. Yazili Notu: "))
sinav2 = int(input("2. Yazili Notu: "))
sinav3 = int(input("Sözlü Notu: "))
ortalama = sinav1*0.3 + sinav2*0.3 + sinav3*0.4
print(ortalama)
if (0 <= ortalama <= 24):
    print("Notu => 0")
elif (25 <= ortalama <= 44):
    print("Notu => 1")
elif (45 <= ortalama <= 54):
    print("Notu => 2")
elif (55 <= ortalama <= 69):
    print("Notu => 3")
elif (70 <= ortalama <= 84):
    print("Notu => 4")
else:
    print("Notu => 5")
    
#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#   1. Bakım => 1.Yıl
#   2. Bakım => 2.Yıl
#   3. Bakım => 3.Yıl
#   **Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.

days = int(input("Araçınız kaç gündür trafikte ? : "))

if (0 <= days <= 365):
    print("1. Bakım aralığı")
elif(365 < days <= 365*2):
    print("2. Bakım aralığı")
elif(365*2 < days <= 365*3):
    print("3. Bakım aralığı")
else:
    print("Yetersiz süre")


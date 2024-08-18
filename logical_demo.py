#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi1 = int(input("Bir sayi giriniz: "))
message1 = (sayi1 >= 0 and sayi1 <= 100)
print(message1)

#2- Girilen bir sayının pozitif çift olup olmadığını kontrol ediniz.
message2 = (sayi1 >= 0 and (sayi1 % 2) == 0)
print(message2)

#3- Email ve parola bilgileriyle giriş kontrolü yapınız.
email = "gokdenizyilmaz@outlook.com"
sifre = "1234567"
emailGir = input("Email: ")
sifreGir = input("Şifre: ")
isHesap = (email == emailGir) and (sifre == sifreGir)

print(f"Hesaba Giris Durumu : {isHesap}")

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input("1. Sayi: "))
b = int(input("2. Sayi: "))
c = int(input("3. Sayi: "))

karsilastir1 = (a > b) and (a > c)
karsilastir2 = (b > a) and (b > c)
karsilastir3 = (c > a) and (c > b)
print(f"1. Sayi en büyük sayıdır : {karsilastir1}") 
print(f"2. Sayi en büyük sayıdır : {karsilastir2}") 
print(f"3. Sayi en büyük sayıdır : {karsilastir3}") 


#5- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti,
#değilse kaldı yazdırınız. Koşullar: Ortalama 50 olsa bile final notu en az 50 olmalıdır. Ayrıca finalden 70 alındığında
#ortalamanın önemi olmasın.
vize1 = int(input("1. Vize: "))
vize2 = int(input("2. Vize: "))
final = int(input("Final: "))
ortalama = (vize1*0.3+ vize2*0.3 + final*0.4)
message5 = ((ortalama >= 50 and final >= 50) or final >= 70)
print(message5)

#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indeksini hesaplayınız.
#   Formül : (kilo/boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#       0-18.4 -> Zayıf
#       18.5-24.9 -> Normal
#       25.0-29.9 -> Fazla Kilolu
#       30.0-34.9 -> Şişman(Obez)

ad = input("Adi: ")
kilo = float(input("Kilo: "))
boy = float(input("Boy: "))
hesapla = (kilo/(boy**2))
zayif = (hesapla >= 0 and hesapla <= 18.4)
normal = (hesapla >= 18.5 and hesapla <= 24.9)
kilolu = (hesapla >= 25.0 and hesapla <= 29.9)
obez = (hesapla >= 30.0 and hesapla <= 34.9)

print(f"{ad} kisinin kilo endeksi {hesapla} ve grup degelendirmen {zayif}: ")
print(f"{ad} kisinin kilo endeksi {hesapla} ve grup degelendirmen {normal}: ")
print(f"{ad} kisinin kilo endeksi {hesapla} ve grup degelendirmen {kilolu}: ")
print(f"{ad} kisinin kilo endeksi {hesapla} ve grup degelendirmen {obez}: ")
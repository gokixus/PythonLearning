#1- Girilen 2 sayidan hangisi büyüktür ?
sayi1 = int(input("1. Sayi giriniz: "))
sayi2 = int(input("2. Sayi giriniz: "))
karsilastir = (sayi1 > sayi2)
print(f"a: {sayi1} b: {sayi2}'den büyüktür: {karsilastir}")

#2- Kullanıcıdan 2 vize(%60) ve final notunu(%40) alıp ortalama hesaplayınız.
vize1 = int(input("1. Vize Notu: "))
vize2 = int(input("2. Vize Notu: "))
final = int(input("Final Notu: "))
ortalama = (vize1*0.3 + vize2*0.3 + final*0.4)
print(ortalama)

#3- Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
print(f"Ortalamanız {ortalama} ve geçme durumunuz: {ortalama >= 50}")

#4- Girilen bir sayının negatif pozitif durumunu yazdırınız.
sayi3 = int(input("Bir sayi giriniz(negatif veya pozitif): "))
print(f"Girilen sayi pozitif mi ? = {sayi3 >= 0}")
print(f"Girilen sayi negatif mi ? = {sayi3 < 0}")

#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
email = "gokdeniizyilmaz@outlook.com"
password = "12345678"

girilenEmail = input("Email giriniz: ")
girilenPassword = input("Şifre giriniz: ")

isEmail = (email == girilenEmail)
isPassword = (password == girilenPassword)

print(f"Email Bilgisi Doğru mu ? {isEmail}, Password Bilgisi Doğru mu ? {isPassword}")


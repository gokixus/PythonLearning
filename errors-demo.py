liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

#1- liste elemanları içindeki sayısal değerleri bulunuz.
#2- kullanıcı q değerini girmedikçe aldığınız her inputun sayısal olduğundan emin olunuz aksi halde hata mesajı yazdırın.
#3- girilen parola içinde türkçe karakter hatası veriniz.
#4- faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

#1-
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
    
#2-

while True:
    sayi = input("Sayi: ")
    if sayi == "q":
        break
    try:
        result = float(sayi)
        print("Girdiğiniz sayı: ", result)
    except ValueError:
        print("Geçersiz sayı")
        continue
    
#3-

turkceKarakterler = "şçğüöıİ"
password = input("Parolanız: ")

for i in password:
    if i in turkceKarakterler:
        raise TypeError("Parola türkçe karakterler içeremez!")
    else:
        pass
print("Geçerli parola")

#4-

def faktoriyel(x):
    x = int(x)
    
    if x < 0:
        raise ValueError("Negatif değer!")
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
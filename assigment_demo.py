x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
sayi1 = int(input("1. Sayi giriniz: "))
sayi2 = int(input("2. Sayi giriniz: "))
islem = sayi1*sayi2 - (x+y+z)
print(islem)

#2- y'nin x'e kalansız bölümünü hesaplayınız.
y1 = y//x
print(y1)

#3- (x,y,z) toplamının mod 3'ü nedir?
toplam = (x + y + z) % 3
print(toplam)

#4- y'nin x. kuvvetini hesaplayınız.
y2 = y**x
print(y2)

#5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır ?
x, *y, z = numbers
print(z**3)

#6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
print(y[0] + y[1] + y[2])
names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

#2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")
print(names)

#3- "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)

#4- "Deniz" isminin indeksi nedir?
if "Deniz" in names:
    indeks = names.index("Deniz")
    print(indeks)
else:
    print("Deniz ismi listede bulunmuyor.")

#5- "Ali" listenin bir elemanı mıdır ?
message1 = "Ali" in names
print(message1)

#6- Liste elemanlarını ters çevirin.
names.reverse()
print(names)

#7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

#8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
years.reverse()
print(years)

#9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = "Cehvrolet, Dacia"
result = str.split(", ")
print(result)

#10- years dizisinin en büyük ve en küçük elemanı nedir?
message2 = min(years)
message3 = max(years)
print(message2, message3)

#11- years dizisinde kaç tane 1998 değeri vardır?
message4 = years.count(1998)
print(message4)

#12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

#13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka = input("Marka: ")
markalar.append(marka)
marka = input("Marka: ")
markalar.append(marka)
marka = input("Marka: ")
markalar.append(marka)
print(markalar)
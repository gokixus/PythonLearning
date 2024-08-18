website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(50 Saat)"

#1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
mesaj1 = " Hello World "
message1 = mesaj1.strip()
print(message1)

#2- websitedeki sadikturan bilgisi haricindeki her karakteri silin
message2 = website.lstrip("/:pth")
message3 = message2.strip("w.moc")
print(message3)

#3- course karakter dizisinin tüm karakterlerini küçük harf yapın
message4 = course.lower()
print(message4)

#4- website içinde kaç tane a karakterleri vardir ?
message5 = website.count("a")
print(message5)

#5- website www ile başlayıp com ile bitiyor mu ?
message6 = website.startswith("www")
message7 = website.endswith("com")
print(message6, message7)

#6- website içinde .com ifadesi varmı ?
message8 = website.find(".com")
print(message8)

#7- course içindeki karakterlerin hepsi alfabetik mi ?
message9 = course.isalpha()
print(message9)

#8- contents ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
message10 = "Contents".center(50, "*")
print(message10)

#9- course karakter dizisini tüm boşluk karakterlerini - ile değiştir.
message11 = course.replace(" ", "-")
print(message11)

#10- Hello World karakter dizisinin World ifadesini There olarak değiştiriniz.
message12 = "Hello World".replace("Hello", "There")
print(message12)

#11- course karakter dizisini boşluk karakterlerinden ayırın
message13 = course.split()
print(message13)
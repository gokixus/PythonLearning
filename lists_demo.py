#1- "Bmw, Mercedes, Opet ve Mazda" elemalarına sahip bir liste oluşturunuz.
arabalar = ["BMW", "Mercedes", "Opet", "Mazda"]

#2- "Üstteki liste kaç elemanlıdır ?"
message1 = len(arabalar)
print(message1)

#3- Listenin ilk ve son elemanı nedir ?
message2 = arabalar[0]
message3 = arabalar[-1]
print(message2, message3)

#4- Mazda değerini Toyota ile değiştirin.
arabalar[-1] = "Toyota"
print(arabalar)

#5- Mercedes listenin bir elemanı mıdır ?
message4 = "Mercedes" in arabalar
print(message4)

#6- Listenin -2 indeksindeki değer nedir ?
message5 = arabalar[-2]
print(message5)

#7- Listenin ilk 3 elemanını alın.
message6 = arabalar[0:3]
print(message6)

#8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin
arabalar[-2:] = ["Totoya", "Renault"]
print(arabalar)

#9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
arabalar = arabalar + ["Audi", "Nissan"]
print(arabalar) 

#10- Listenin son elemanını silin.
del arabalar[-1]
print(arabalar)

#11- Liste elemanlarını tersten yazdırınız.
print(arabalar[::-1])

#12- Aşağıdaki verileri bir liste içinde saklayınız.
#studentA : Yiğit Bilgi 2010, (70, 60, 60)
#studentB : Sena Turan 1999, (80, 80, 70)
#studentC : Ahmet Turan 1998, (80, 70, 90)

studentA = ["Yigit", "Bilgi", 2010, [70, 60, 60]]
studentB = ["Sena", "Turan", 1999, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

#13- Liste elemanlarını ekrana yazdırınız.
students = [studentA, studentB, studentC]
print(students)
print(students[0][2])
print(students[2])
print(students[1][3])
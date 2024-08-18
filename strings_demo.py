website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(50 Saat)"

#1- 'course' ve 'website' karakter dizisinde kaç karakter bulunmaktadir?
result1 = len(course)
print(result1)
result2 = len(website)
print(result2)

#2- 'website' içinden www karakterlerini aliniz.
result = website[7:10]
print(result)

#3- 'website' içinden com karakterlerini aliniz.
result = website[22:25]
print(result)

#4- 'course' içinden ilk 15 ve son 15 karakterlerini alin
result3 = course[:15]
result4 = course[-15:]
print(result3, result4)


#5- 'course' ifadesinedki karakterleri tersten yazdiriniz
result5 = course[::-1]
print(result5)


name, surname, age, job = 'Bora', 'Yilmaz', 32, 'mühendis'
#6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırınız.
#'Benim adim Bora Yilmaz, Yasim 32 ve meslegim mühendis.'
result6 = f"Benim adim {name} {surname}, Yasim {age} ve meslegim {job}"
print(result6)

#7- 'Hello World ifadesindeki' w harfini 'W' ile değiştirin.
s = "Hello world"
result7 = s[0:6] + 'W' + s[-4:]
print(result7)


# 8- 'abc' ifadesini yan yana 3 defa yazdiriniz.
result8 = 'abc ' * 3
print(result8)
import random

result = dir(random)
# print(result)


result1 = random.random() #0.0-1.0 sayıları arası
print(result1)
result2 = random.random()*100
print(result2)
result3 = int(random.uniform(10,100))
print(result3)
result4 = random.randint(1,10) #1-10 arasında rastgele sayı gelir int olarak
print(result4)

names = ["Ali", "Ahmet", "Furkan", "Gökdeniz"]
result5 = names[random.randint(0, len(names)-1)]
print(result5)
result6 = random.choice(names)
print(result6)

liste1 = list(range(10))
random.shuffle(liste1) #listeyi karışık yapar
result7 = liste1
print(result7)

liste2 = list(range(100))
result8 = random.sample(liste2, 3) #1-100 arasında sayıları arasında rastgele üçünü seçip yazdırır
print(result8)


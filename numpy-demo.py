import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisini oluşturunuz.

result1 = np.array([10,15,30,45,60])
print(result1)
 
# 2- (5-15) arasındaki sayılarla numpy dizisini oluşturunuz.
result2 = np.arange(5,15)
print(result2)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisini oluşturunuz.
result3 = np.arange(50,100,5)
print(result3)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result4 = np.zeros(10)
print(result4)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
result5 = np.ones(10)
print(result5)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
result6 = np.linspace(0,100,5)
print(result6)

# 7- (10-30) arasında rastgele 5 tane tam sayı üretin.
result7 = np.random.randint(10,30,5)
print(result7)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
result8 = np.random.uniform(-1,1,10)
print(result8)

# 9- (3x5) boyutlarda (10-50) arasında rastgele bir matris oluşturunuz.
result9 = np.random.randint(10,50, 15).reshape(3,5)
print(result9)

# 10- Üretilen matrisin satır ve sütünların toplamlarını hesaplayınız.
result10 = result9.sum(axis=1)
result11 = result9.sum(axis=0)
print(result10) #satir top
print(result11) #sutun top

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması ne?
result12 = result9.max()
result13 = result9.min()
result14 = result9.mean()
print(result12)
print(result13)
print(result14)

# 12- Üretilen matrisinin en büyük değerinin indexi ne ?
result15 = result9.argmax()
print(result15)

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
result16 = np.arange(10,20)
print(result16[:3])
 
# 14- Üretilen dizinin elemanlarını tersten yazdırın.
print(result16[::-1])

# 15- Üretilen matrisin ilk satırını seçiniz.
print(result9[0])

# 16- Üretilen matrisin 2. satır 3. sütündaki elemanı hangisidir?
print(result9[1,2])

# 17- Üretilen matrsinin tüm satırlardaki ilk elemanı seçiniz.
print(result9[:,0])

# 18- Üretilen matrisin her bir elemanını karesini alınız.
print(result9 ** 2)

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır? Aralığı (-50, +50) arasında yapınız.
result17 = np.arange(-50, 50)
print(result17[(result17 > 0) & (result17 % 2 == 0)])

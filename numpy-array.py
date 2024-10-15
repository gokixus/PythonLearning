import numpy

result1 = numpy.arange(1, 10)
print(result1)
result2 = result1.reshape(3, 3)
print(result2)
result3 = result2.sum(axis=0) #sütünların toplamı
result4 = result2.sum(axis=1) #satırların toplamı
print(result3)
print(result4)
result5 = result1.mean() # sayıların ortalamasını verir
print(result3)
print(result5)
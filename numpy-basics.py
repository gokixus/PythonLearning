import numpy


np_array = numpy.array([1,2,3,4,5,6,7,8,9])
np_multi = np_array.reshape(3,3) #3x3 matris
print(np_multi)

print(np_array.ndim) #tek boyutlu
print(np_multi.ndim) #iki boyutlu

print(np_array.shape)
print(np_multi.shape)

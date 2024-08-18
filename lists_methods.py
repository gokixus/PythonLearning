numbers = [1, 5, 40, 29, 32, 4]
harfler = ["a", "b", "g", "c", "z", "y"]

message1 = max(numbers) #max ve minleri bulur
message2 = min(numbers)
message3 = max(harfler)
message4 = min(harfler)

print(message1, message2)
print(message3, message4)


message5 = numbers[1:4]
print(message5)

numbers.append(40) #listenin sonuna yeni bir eleman ekler.
print(numbers)
numbers[-1] = 49
print(numbers)

numbers.insert(1, 23) # (1, 23) kısmındaki 1 kısmına 1 eklenerak 2. pozisyona 23 eklenir listeye.
print(numbers)

numbers.pop(4) #indekse 1 eklenerek oradaki pozisyondaki elemanı siler.
print(numbers)

numbers.remove(49) #parantez içindeki elemanı kaldırır
print(numbers)

numbers.sort() #en küçükten en büyüğe sıralar.
harfler.sort()
print(numbers)
print(harfler)

numbers.reverse() #elemanları ters çevirir
print(numbers)
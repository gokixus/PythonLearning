for sayi1 in range(10):                 #range metodu
    print(sayi1)
print(" ") 
for sayi2 in range(10, 20, 5):
    print(sayi2)
print(" ")
print(list(range(5,100,20)))            #list metodu
print(" ")
kelime = "Merhaba"                      #enumerate metodu
for harfler in enumerate(kelime):
    print(harfler)
print(" ")
for index, harfler in enumerate(kelime):
    print(harfler)
print(" ")
for index, harfler in enumerate(kelime):
    print(f"İndex: {index} ve harfler: {harfler}")
print(" ")
list1 = [1,2,3,4,5]                     #zip metodu
list2 = ["a", "b", "c", "d", "e", "f"]
print(list(zip(list1,list2)))
print(" ")
for item in zip(list1, list2):
    print(item)
for a, b in zip(list1, list2):
    print(a, "->", b)
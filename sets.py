fruits = {"Orange", "Apple", "Banana"}
 
#print(fruits[0]) indekslenemez bir liste

for x in fruits:
    print(x)
    
fruits.add("Cherry")
fruits.update(["Mango", "Grape"])
print(fruits)

myList = [2,3,4,5,6,2,1,2,1,3,5,6]
print(myList)
print(set(myList))
print(len(set(myList)))
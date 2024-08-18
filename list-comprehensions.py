for x in range(10):
    print(x)
    
print("")

numbers1 = [x for x in range(10)]
print(numbers1)

numbers2 = []
for x in range(10):
    numbers2.append(x)
print(numbers2)
print("")

for x in range(10):
    print(x**2)
    
numbers3 = [x**2 for x in range(10)]
print(numbers3)
print("")

numbers4 = [x*x for x in range(10) if x%3==0]
print(numbers4)
print("")

myString = "Hello"
myList1 = []

for letter in myString:
        myList1.append(letter)
print(myList1)

myList2 = [letter for letter in myString]
print(myList2)
print("")

years = [1983, 1999, 2008, 1957, 1986]
ages = [2024-year for year in years]
print(ages)
print("")

results1 = [x if x%2 == 0 else "TEK" for x in range(1, 10)]
print(results1)
print("")

results2 = []
for x in range(3):
    for y in range(3):
        results2.append((x,y))
print(results2)
print("")
results3 = [(x,y) for x in range(3) for y in range(3)]
print(results3)

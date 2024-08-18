def add(*parametreler):
    sum = 0
    for n in parametreler:
        sum += n
    return sum

print(add(100, 51))

def displayUser(**args):
    for ad, age in args.items():
        print("{} is {}".format(ad, age))
        
displayUser(name = "Çınar", age = 2, city = "İstanbul")
displayUser(name = "John", age = 24, city = "New York", phone = "Iphone 14")
displayUser(name = "Recep", age = 34, city = "Ankara", phone = "Iphone 15 Pro")

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
myFunc(10, 20, 30, 40, 50, key1 = "Value 1", key2 = "Value 2") 
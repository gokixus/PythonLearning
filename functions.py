def sayHello1(name1 = "User"):
    print("Hello " + name1)
sayHello1("Gökdeniz")
sayHello1("Derya")
sayHello1()

def sayHello2(name2):
    return "Hello " + name2
msg = sayHello2("Burak")
print(msg)    

def total(num1, num2):
    return num1 + num2
result1 = total(10,20)
print(result1)
result2 = total(15,20)
print(result2)

def yasHesapla(dogumYili):
    return 2024-dogumYili

ageGokdeniz = yasHesapla(2003)
ageFehmi = yasHesapla(2001)
ageSelen = yasHesapla(2004)
print(ageGokdeniz, ageFehmi, ageSelen)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65-yas
    
    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emeklisiniz.")
emekliligeKacYilKaldi(1983, "Ali")
emekliligeKacYilKaldi(1951, "Resul")
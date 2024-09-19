def usAlma(number):
    def inner(power):
        return number ** power
    return inner

two = usAlma(2)
print(two(6))

def yetkiSorgu(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner
            
admin_user1 = yetkiSorgu("Product Edit")
print(admin_user1("Admin123"))

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *=i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma
    
toplama = islem("toplama")
print(toplama(4, 6))
carpma = islem("carpma")
print(carpma(5, 10))
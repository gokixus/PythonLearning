#sayıları liste[23, 21, 9] halinde değil de tek tek yazdırmak istiyorsak.
def cube():  
    for i in range(5):
        yield i**3

for sayi in cube():
    print(sayi)


# generator = (i**3 for i in range(5))
# for i in generator:
#     print(i)
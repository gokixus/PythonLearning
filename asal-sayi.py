# Soru: Girilen bir sayının asal olup olmadığını bulun.
# * Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.

sayi = int(input("Sayı giriniz: "))
asalMi = True

if(sayi == 1):
    print("1 sayisi asal değildir.")

for i in range(2, sayi):
    if (sayi % i == 0):
        asalMi = False
        break
    
if asalMi:
    print(f"{sayi} sayisi asaldır.")
else:
    print(f"{sayi} sayisi asal değildir.")
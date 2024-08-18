hesapA = {
    "Ad": "Gökdeniz Yılmaz",
    "HesapNo": "12345678",
    "Bakiye": 10000,
    "EkHesap": 2000,
}
hesapB = {
    "Ad": "Ali Turan",
    "HesapNo": "12345679",
    "Bakiye": 5000,
    "EkHesap": 1000,
}
hesapC = {
    "Ad": "Hazar Akgöz",
    "HesapNo": "12345670",
    "Bakiye": 80000,
    "EkHesap": 4000,
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap["Ad"]}")
    
    if hesap["Bakiye"] >= miktar:
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["Bakiye"] + hesap["EkHesap"]
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek Hesabınız kullanılsın mı ? (e/h): ")
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["Bakiye"]
                hesap["Bakiye"] = 0
                hesap["EkHesap"] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap["HesapNo"]} nolu hesabınızda {hesap["Bakiye"]} bulunmaktadır.")
        else:
            print("Üzgünüz bakiyeniz yetersiz.")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap["HesapNo"]} nolu hesabınızda {hesap["Bakiye"]} TL bulunmaktadır.")

paraCek(hesapA, 12000)

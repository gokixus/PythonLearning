mesaj1 = "hello There. My name is Gokdeniz Yilmaz"
mesaj2 = "  hello There. My name is Gokdeniz Yilmaz"
mesaj3 = "Selamlar! Ben Gökdeniz Yilmaz. Nasilsiniz?"
kelimeler = ["Merhaba", "Dünya!"]

message1 = mesaj1.upper() #tüm harfleri büyük yapar
print(message1)

message2 = mesaj1.lower() #tüm harfleri küçük yapar
print(message2)

message3 = mesaj1.title() #her keliminn ilk harfini büyük yapar
print(message3)

message4 = mesaj1.capitalize() #sadece ilk kelimenin harfini büyük yapar, geri kalan büyük harfler varsa onlari küçük yapar
print(message4)

message5 = mesaj2.strip() #ilk karakterler ve son karakterler boşluk ise onlari siler sadece sondaki boşluklar için rstrip(), ilk karakterler içinse lsstrip()
print(message5)

message6 = mesaj1.startswith("H") #parantez içindeki kelime cümledeki ilk harf ile aynıysa true yazdirir değilse de false
print(message6)
message7 = mesaj1.startswith("h")
print(message7)

message8 = mesaj1.endswith("z") #startswith gibi ama cümle sonunda
print(message8) 

message9 = mesaj3.split() #her kelimeyi parçalara ayrırır.
print(message9)
print(message9[2])
message10 = mesaj3.split(".") # "." karakterine kadar kelimeleri parçalara ayrırır.
print(message10)
print(message10[1])

message11 = " ".join(message9) #kelimeleri birlestirir.
print(message11)
message12 = "---".join(message9)
print(message12)
message13 = " ".join(kelimeler)
print(message13)

message14 = mesaj1.find("name") #aranan kelime bulunduysa kaçıncı pozisyondan itibaren yazdigini bulur. bulunmadiysa da -1 yazdirir
print(message14)
message15 = mesaj1.find("namee")
print(message15)
message16 = mesaj1.find("name", 10, 20) #10. ve 20. pozisyon arasinda var mi bakar varsa kaçıncı pozisyondan başlıyor onu yazar
print(message16)

message17 = mesaj1.center(50) #fazladan pozisyon ekler. 50 nin yanında birşey yoksa boşluk ekleyip cümleyi ortalar.
print(message17)
message18 = mesaj1.center(60, "*") #boşluk değil de * 'yi soldan sağdan ekler. Aynı şekilde cümleyi ortalar.
print(message18)

message19 = mesaj1.isalpha() #Tüm karakterler alfabetik olup olmadığı kontrol eder 1 tanesi bile alfabetik değilse false döndürür
print(message19)

message20 = mesaj1.isdigit() #isalpha gibi ama sayılar için
print(message20)

message21 = mesaj3.count("am") #aranan kelime kaç tane yazildigini söyler
message22 = mesaj3.count("a")
print(message21, message22)

message23 = mesaj3.index("Ben") # .find gibi çalışır
print(message23)
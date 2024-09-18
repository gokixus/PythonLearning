# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

def listeDuzlestir(liste):
    duzlestirilmis_liste = []
    def duz(item):
        if isinstance(item, list):
            for sub_item in item:
                duz(sub_item)
        else:
            duzlestirilmis_liste.append(item)
    duz(liste)
    return duzlestirilmis_liste
inputList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(listeDuzlestir(inputList))

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

def listeDondur(liste):
    tersListe = liste[::-1]
    for i in range(len(tersListe)):
        if isinstance(tersListe[i], list):
            tersListe[i] = tersListe[i][::-1]
    return tersListe
inputList = [[1, 2], [3, 4], [5, 6, 7]]
print(listeDondur(inputList))
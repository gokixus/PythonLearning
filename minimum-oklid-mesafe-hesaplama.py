# Öklid mesafesi, Öklid uzayındaki iki nokta arasındaki "sıradan" düz çizgi mesafesidir. Bu program düzlemde veya üç boyutlu uzayda iki nokta arasındaki mesafeyi bulabilirsiniz.
# Formül = d = √(x₂-x₁)²+(y₂-y₁)²

import math

noktalar = [(1, 2), (3, 4), (5, 6), (7, 8)]

def oklidMesafeBul(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    return math.sqrt((x2- x1)**2 + (y2-y1)**2)

mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafeBul(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)
        
min_mesafe = min(mesafeler)
print("Minimum mesafe: ", min_mesafe)

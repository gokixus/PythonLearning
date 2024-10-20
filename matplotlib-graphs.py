import matplotlib.pyplot as plt

# yil = [2011,2012,2013,2014,2015]

# oyuncu1 = [8,10,12,7,9]
# oyuncu2 = [7,12,5,15,21]
# oyuncu3 = [18,20,22,25,19]

# plt.plot([],[],color="y",label="Oyuncu1")
# plt.plot([],[],color="r",label="Oyuncu2")
# plt.plot([],[],color="b",label="Oyuncu3")
# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
# plt.title("Yıllara göre atılan goller")




# goal_types = "Penaltı", "Kaleye Atılan Şut", "Serbest Vuruş"
# goals = [12,35,7]
# colors = ["y", "r", "b"]
# plt.pie(goals,labels=goal_types,colors=colors)




# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20], label="BMW")
# plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60], label="Audi")
# plt.legend()
# plt.xlabel("Gün")
# plt.ylabel("Mesafe(km)")
# plt.title("Araç Bilgileri")




yaslar = [22,33,25,12,66,28,95,34,25,21,6,12,5,8,4,2,66,45,67,89,76,99,21,23,1,6,7,8,55,44,22,33,66,7,55,54,53,52,101,104,100,45,109]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype='bar',rwidth=0.8)
plt.xlabel("Yaş Grupları")
plt.ylabel("Kişi sayısı")
plt.title("Histogram Grafiği")



plt.show()
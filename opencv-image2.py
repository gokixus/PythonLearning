import cv2
import matplotlib.pyplot as plt

kizKulesi_resmi = cv2.imread("images/kizkulesi.png", 0)
cv2.imshow("Kiz Kulesi", kizKulesi_resmi)
plt.imshow(kizKulesi_resmi, cmap="gray")
plt.show()


if cv2.waitKey(0) == ord("q"):
    print("q tuşuna basılarak resim kapatıldı.")
    cv2.imwrite("images/kizkulesigray.png", kizKulesi_resmi)
    cv2.destroyAllWindows()
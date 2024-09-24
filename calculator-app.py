import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        
        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()
        
    def initUI(self):
        self.label_sayi1 = QLabel(self)
        self.label_sayi1.setText("Sayı 1: ")
        self.label_sayi1.move(50,30)
        self.text_sayi1 = QLineEdit(self)
        self.text_sayi1.move(150,30)
        self.text_sayi1.resize(200,32)
        
        self.label_sayi2 = QLabel(self)
        self.label_sayi2.setText("Sayı 2: ")
        self.label_sayi2.move(50,80)
        self.text_sayi2 = QLineEdit(self)
        self.text_sayi2.move(150,80)
        self.text_sayi2.resize(200,32)
        
        self.buton_topla = QPushButton(self)
        self.buton_topla.setText("Topla")
        self.buton_topla.move(150,130)
        self.buton_topla.clicked.connect(self.toplama)
        
        self.buton_cikar = QPushButton(self)
        self.buton_cikar.setText("Çıkar")
        self.buton_cikar.move(150,170)
        self.buton_cikar.clicked.connect(self.cikarma)
        
        self.buton_carp = QPushButton(self)
        self.buton_carp.setText("Çarp")
        self.buton_carp.move(150,210)
        self.buton_carp.clicked.connect(self.carpma)
        
        self.buton_bol = QPushButton(self)
        self.buton_bol.setText("Böl")
        self.buton_bol.move(150,250)
        self.buton_bol.clicked.connect(self.bolme)
        
        self.label_sonuc = QLabel(self)
        self.label_sonuc.setText("Sonuç: ")
        self.label_sonuc.move(150,290)
        
    def toplama(self):
        result = int(self.text_sayi1.text()) + int(self.text_sayi2.text())
        self.label_sonuc.setText("Sonuç: " + str(result))
    
    def cikarma(self):
        result = int(self.text_sayi1.text()) - int(self.text_sayi2.text())
        self.label_sonuc.setText("Sonuç: " + str(result))
    
    def carpma(self):
        result = int(self.text_sayi1.text()) * int(self.text_sayi2.text())
        self.label_sonuc.setText("Sonuç: " + str(result))
    
    def bolme(self):
        result = int(self.text_sayi1.text()) / int(self.text_sayi2.text())
        self.label_sonuc.setText("Sonuç: " + str(result))
        
        
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
    
app()
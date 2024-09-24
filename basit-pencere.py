import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QLabel

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()
        self.buton.clicked.connect(self.tiklandi)
    
    def ozellikEkle(self):
        self.resize(500, 700)
        self.move(700, 100)
        self.setWindowTitle("Basit Pencere")
        
    def ekOzellikEkle(self):
        self.input = QLineEdit("Bir şey yaz", self)
        self.input.setGeometry(20,10,200,25)
        
        self.buton = QPushButton("Ekrana yaz", self)
        self.buton.setGeometry(10,50,200,75)
        
        self.label = QLabel("Sonuc", self)
        self.label.setGeometry(10,110,200,75)
        
    def tiklandi(self):
        self.label.setText(self.input.text())
        
app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())
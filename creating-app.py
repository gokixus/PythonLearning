import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    win.setWindowTitle("First Application")
    win.setGeometry(200, 200, 500, 600)
    
   
    
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Name: ")
    lbl_name.move(50,30)
    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Surname: ")
    lbl_surname.move(50,70)
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)
    
    def clicked(self):
        print("Butona tıklandı.")
    
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(150,100)
    btn_save.clicked.connect(clicked)
    
    win.show()
    sys.exit(app.exec_())
window()
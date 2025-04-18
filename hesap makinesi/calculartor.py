from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_bolme.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_Cikarma.clicked.connect(self.hesapla)
        self.ui.btn_Toplama.clicked.connect(self.hesapla)
    def hesapla(self):
        sender = self.sender().text()
        result = 0
        if sender == 'Toplama':
            result = int(self.ui.txt_sayi1.toPlainText()) + int(self.ui.txt_sayi2.toPlainText())
        elif sender == 'Çıkarma':
            result = int(self.ui.txt_sayi1.toPlainText()) - int(self.ui.txt_sayi2.toPlainText())
        elif sender == 'Çarpma':
            result = int(self.ui.txt_sayi1.toPlainText()) * int(self.ui.txt_sayi2.toPlainText())
        elif sender == 'Bölme':
            result = int(self.ui.txt_sayi1.toPlainText()) / int(self.ui.txt_sayi2.toPlainText())
        self.ui.label_3.setText('SONUC : ' + str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())



app()

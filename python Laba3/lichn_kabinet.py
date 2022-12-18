

from Learning_SQLite3 import MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *
from shifr import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow
import sys


class Ui_Dialog(QMainWindow):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(496, 265)
        self.Encrypt_btn = QtWidgets.QPushButton(Dialog)
        self.Encrypt_btn.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.Encrypt_btn.setObjectName("Encrypt_btn")
        self.text_encrypt = QtWidgets.QPlainTextEdit(Dialog)
        self.text_encrypt.setGeometry(QtCore.QRect(20, 0, 456, 50))
        self.text_encrypt.setObjectName("text_encrypt")
        self.Result_decrypt = QtWidgets.QLabel(Dialog)
        self.Result_decrypt.setGeometry(QtCore.QRect(20, 120, 456, 50))
        self.Result_decrypt.setObjectName("Result_decrypt")
        self.Decrypt_btn = QtWidgets.QPushButton(Dialog)
        self.Decrypt_btn.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.Decrypt_btn.setObjectName("Decrypt_btn")
        self.Next_btn = QtWidgets.QPushButton(Dialog)
        self.Next_btn.setGeometry(QtCore.QRect(410, 230, 75, 23))
        self.Next_btn.setObjectName("Next_btn")

        self.retranslateUi(Dialog)

        self.add_functions()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Encrypt_btn.setText(_translate("Dialog", "Encrypt"))
        self.Result_decrypt.setText(_translate("Dialog", "Result:"))
        self.Decrypt_btn.setText(_translate("Dialog", "Decrypt"))
        self.Next_btn.setText(_translate("Dialog", "Next"))




    def add_functions(self):
        self.Encrypt_btn.clicked.connect(lambda: self.encrypting())
        self.Decrypt_btn.clicked.connect(lambda: self.decrypting())
        self.Next_btn.clicked.connect(lambda: self.add_exit())

    @QtCore.pyqtSlot()
    def encrypting(self):
        fname = QFileDialog.getSaveFileName(self)[0]
        T_encrypt = self.text_encrypt.toPlainText()
        if len(T_encrypt) == 0:
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили поле.')
        else:
            try:
                f = open(fname, 'w', encoding='utf-8')
                res_encrypt = trippledesencrypt(T_encrypt)
                f.write(res_encrypt)
                f.close()
            except FileNotFoundError:
                print("No such file")

    def decrypting(self):
        fname = QFileDialog.getOpenFileName(self)[0]
        try:
            f = open(fname, 'r', encoding='utf-8')
            with f:
                data = trippledesdecrypt(f.read())
                self.Result_decrypt.setText("Result: " + data)
            f.close()
        except FileNotFoundError:
            print("No such file")

    @QtCore.pyqtSlot()
    def add_exit(self):
        self.exit = MainWindow()
        self.exit.show()
        self.hide()

class MainKab(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    # app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    # w = MainKab()
    # w.show()
    # sys.exit(app.exec_())

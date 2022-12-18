from PyQt5.Qt import *
# from RegLab3 import MainDialog
from PyQt5 import QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 283)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(120, 30, 231, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(140, 120, 211, 51))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # self.main_btn = QPushButton(MainWindow)
        # self.main_btn.setGeometry(QRect(290, 230, 51, 23))
        # self.main_btn.setObjectName("signup_btn")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        # self.btn_function()
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Странца выхода."))
        self.label_2.setText(_translate("MainWindow", "Хорошего вам дня!"))
        # self.main_btn.setText(_translate("MainWindow", "Главная"))

    # def btn_function(self):
    #     self.main_btn.clicked.connect(lambda: self.opening())
    #
    # @QtCore.pyqtSlot()
    # def opening(self):
    #     self.main = MainDialog()
    #     self.main.show()
    #     self.hide()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, name=''):
        super().__init__()
        self.setupUi(self)

        self.label.setText('{} {}'.format(self.label.text(), name))
        gridLayout = QGridLayout(self.centralwidget)
        gridLayout.addWidget(self.label)
        gridLayout.addWidget(self.label_2)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
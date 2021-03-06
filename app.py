# GUI with PyQt5
import random
import string

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 603)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 30, 291, 171))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(0, 170, 0);")
        self.title.setObjectName("title")
        self.chars = QtWidgets.QComboBox(self.centralwidget)
        self.chars.setGeometry(QtCore.QRect(0, 360, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.chars.setFont(font)
        self.chars.setStyleSheet("color: rgb(0, 170, 0);")
        self.chars.setObjectName("chars")
        self.chars.addItem("")
        self.chars.addItem("")
        self.text_chars = QtWidgets.QLabel(self.centralwidget)
        self.text_chars.setGeometry(QtCore.QRect(10, 290, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.text_chars.setFont(font)
        self.text_chars.setObjectName("text_chars")
        font = QtGui.QFont()
        font.setPointSize(28)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 470, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(490, 330, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.text_numbers = QtWidgets.QLabel(self.centralwidget)
        self.text_numbers.setGeometry(QtCore.QRect(340, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.text_numbers.setFont(font)
        self.text_numbers.setObjectName("text_numbers")
        self.number = QtWidgets.QComboBox(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(360, 360, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.number.setFont(font)
        self.number.setStyleSheet("color: rgb(0, 170, 0);")
        self.number.setObjectName("number")
        self.number.addItem("")
        self.number.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.click)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):

        num = None

        is_number = self.number.currentText()

        nums = None
        nums2 = None
        nums3 = None

        if is_number == "Yes":
            num = string.digits

        length_str = self.chars.currentText()
        if length_str == "8+":
            length = 15
        else:
            length = 8

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase

        all = None

        if length_str == "8-" and is_number == "Yes":
            all = lower + num

        elif length_str == "8-" and is_number == "No":
            all = lower + upper

        elif length_str == "8+" and is_number == "Yes":
            all = lower + upper + num

        elif length_str == "8+" and is_number == "No":
            all = lower + upper

        now = "".join(random.sample(all, length))

        self.label.setText(now)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Password"))
        self.chars.setItemText(0, _translate("MainWindow", "8-"))
        self.chars.setItemText(1, _translate("MainWindow", "8+"))
        self.text_chars.setText(_translate("MainWindow", "Chars"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.text_numbers.setText(_translate("MainWindow", "Number"))
        self.number.setItemText(0, _translate("MainWindow", "Yes"))
        self.number.setItemText(1, _translate("MainWindow", "No"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

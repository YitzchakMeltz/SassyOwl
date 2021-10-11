from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# I know this is bad programming. Just doing this for the example
outputText = ""

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setFixedSize(331, 411)
       
        self.centralwidget = mainwidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(20, 190, 71, 41))
        self.button_7.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_7.setAutoDefault(True)
        self.button_7.setDefault(False)
        self.button_7.setFlat(True)
        self.button_7.setObjectName("button_7")
        self.button_7.clicked.connect(self.click_and_update)

        self.screenOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.screenOutput.setGeometry(QtCore.QRect(20, 30, 291, 20))
        self.screenOutput.setStyleSheet("border: none; background: transparent;"
        "font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(190, 190, 190);")
        self.screenOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.screenOutput.setObjectName("eqInput")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " MRE"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.screenOutput.setText(_translate("MainWindow", "Do Something"))

    def update_screen(self):
        self.screenOutput.setText(outputText)
        return


    def equal_click(self):
        global outputText
        outputText = "Pressed Key"
        self.update_screen()
        return

    def click_and_update(self):
        global outputText
        outputText+=" 7"
        self.update_screen()
        return

    from mainwidget import CommandLineEdit,mainwidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

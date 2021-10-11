
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen 
from mainBackend110 import*
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class mainwidget(QtWidgets.QWidget):
    allowedKeys = (
        Qt.Key_0, 
        Qt.Key_1, 
        Qt.Key_2, 
        Qt.Key_3, 
        Qt.Key_4, 
        Qt.Key_5, 
        Qt.Key_6, 
        Qt.Key_7, 
        Qt.Key_8, 
        Qt.Key_9, 
    )
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() in self.allowedKeys:
            super().keyPressEvent(event)
            print("worked")

class CommandLineEdit(QtWidgets.QLineEdit):
    allowedKeys = (
        Qt.Key_0, 
        Qt.Key_1, 
        Qt.Key_2, 
        Qt.Key_3, 
        Qt.Key_4, 
        Qt.Key_5, 
        Qt.Key_6, 
        Qt.Key_7, 
        Qt.Key_8, 
        Qt.Key_9, 
    )
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() in self.allowedKeys:
            super().keyPressEvent(event)
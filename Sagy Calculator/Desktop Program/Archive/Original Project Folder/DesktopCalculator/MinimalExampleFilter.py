from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from MinimalExample import Ui_MainWindow


class KeyHelper(QtCore.QObject):
    keyPressed = QtCore.pyqtSignal(QtCore.Qt.Key)

    def __init__(self, window):
        super().__init__(window)
        self._window = window

        self.window.installEventFilter(self)

    @property
    def window(self):
        return self._window

    def eventFilter(self, obj, event):
        if obj is self.window and event.type() == QtCore.QEvent.KeyPress:
            self.keyPressed.emit(event.key())
        return super().eventFilter(obj, event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def handle_key_pressed(self, key):
        if key in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            self.update_text()

    def update_text(self):
        text = self.ui.screenOutput.text() + "7"
        self.ui.screenOutput.setText(text)


if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    helper = KeyHelper(w.windowHandle())
    helper.keyPressed.connect(w.handle_key_pressed)

    sys.exit(app.exec_())
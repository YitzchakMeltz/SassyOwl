from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QDialogButtonBox


app = QApplication([])

msg = QMessageBox()
grid_layout = msg.layout()

qt_msgboxex_icon_label = msg.findChild(QLabel, "qt_msgboxex_icon_label")
qt_msgboxex_icon_label.deleteLater()

qt_msgbox_label = msg.findChild(QLabel, "qt_msgbox_label")
qt_msgbox_label.setAlignment(Qt.AlignCenter)
grid_layout.removeWidget(qt_msgbox_label)

qt_msgbox_buttonbox = msg.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
grid_layout.removeWidget(qt_msgbox_buttonbox)

grid_layout.addWidget(qt_msgbox_label, 0, 0, alignment=Qt.AlignCenter)
grid_layout.addWidget(qt_msgbox_buttonbox, 1, 0, alignment=Qt.AlignCenter)


msg.setWindowTitle("Software Update")
msg.setText("A software update is available.<br>Do you want to update now?<br>")
msg.setStandardButtons(QMessageBox.Ok)
msg.setStyleSheet("QLabel{min-width: 700px;}")

msg.exec_()
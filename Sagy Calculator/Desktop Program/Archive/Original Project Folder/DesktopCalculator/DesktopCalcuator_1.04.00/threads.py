from PyQt5.QtCore import QObject, QThread, pyqtSignal
from updateProgramCode140 import updateCalc
import updateProgramCode140
import atexit, sys, os

# Create a worker class
class DownloadThread(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, dlg):
        super(DownloadThread, self).__init__()
        from mainControl import mainControl
        self.dlg = dlg

    def run(self):
        """Long-running task."""
        updateProgramCode140.updateCalc(self.dlg)
        installer = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates',
                                'SagyCalculatorSetup.exe')
        atexit.register(os.execl, installer, installer)
        self.finished.emit()
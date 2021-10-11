from functools import partial

class calcCtrl:
    def __init__(self,MainWindow):
        self._MainWindow = MainWindow
        self._connectSignals()

    def _connectSignals(self):
        self._MainWindow.button_0.clicked.connect(self.testController)

    def testController(self):
        print("Controller Test Complete")
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QObject, QEvent

import random

from main_ui import Ui_MainWindow


class Namora(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Namora, self).__init__()
        self.setupUi(self)
        
        self.button_no.clicked.connect(self.moveButton)
        self.button_yes.clicked.connect(self.euTeAmo)
        
        self.frame_no.installEventFilter(self)
        
    def moveButton(self):
          self.frame_no.move(random.randint(0,300), random.randint(0,300))
          
          
    def euTeAmo(self):
          self.label.setText("Eu te Amo!!")
          self.button_yes.setEnabled(False)
          self.button_no.setEnabled(False)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
                self.moveButton()
                return True
        else:
            return False


app = QtWidgets.QApplication(sys.argv)

window = Namora()
window.show()
app.exec()

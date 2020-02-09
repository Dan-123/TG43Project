import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from TG43_GUI import Ui_Dialog
from TG43 import *

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


    def create_dose_ref_point(self):
        x = self.ui.dose_ref_x
        y = self.ui.dose_ref_y
        z = self.ui.dose_ref_z

    def button_pressed(self):
        if self.ui.add_dose_point.clicked:
            print('clicked')






app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())


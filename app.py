import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from TG43_GUI_v1_2 import Ui_Dialog
import TG43

class AppWindow(QDialog):

    source_list = []
    refpoint_list = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


    def addSource(self):

        x, y, z = self.ui.source_x.value(),\
                  self.ui.source_y.value(),\
                  self.ui.source_z.value()
        activity = self.ui.source_activity.value()
        source = TG43.Source(x, y, z, activity)
        print(source.coordinates)
        print(source.activity)
        print('Source Added')

    def addRefPoint(self):
        _translate = QtCore.QCoreApplication.translate
        x, y, z = round(self.ui.dose_ref_x.value(), 1),\
                  round(self.ui.dose_ref_y.value(), 1),\
                  round(self.ui.dose_ref_z.value(), 1)
        ref = TG43.DoseRefPoint(x, y, z)
        self.refpoint_list.append(ref)
        row_pos = self.ui.refpoint_table.rowCount()
        self.ui.refpoint_table.insertRow(row_pos)
        self.ui.refpoint_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(x)))
        self.ui.refpoint_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(y)))
        self.ui.refpoint_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(z)))
        print(ref.cartesian)
        print('Reference Point Added')

    def clearRefPoint(self):
        pass


app = QApplication(sys.argv)
w = AppWindow()
w.show()

w.ui.add_source.clicked.connect(w.addSource)
w.ui.add_dose_point.clicked.connect(w.addRefPoint)
w.ui.close_all.clicked.connect(QtWidgets.qApp.closeAllWindows)

sys.exit(app.exec_())
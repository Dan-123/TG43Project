import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from mpl_toolkits.mplot3d import Axes3D

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from TG43_GUI_v1_8 import Ui_Dialog
# import TG43_v_1_1 as TG43
import TG43

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

class AppWindow(QDialog):

    source_list = []    # To store input sources
    refpoint_list = []  # To store input reference points

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def getSourcePos(self):
        """
        Method to find user's desired source info
        :return: x, y, z, activity, time
        """
        x, y, z, activity, time = round(self.ui.source_x.value(), 1),\
                                  round(self.ui.source_y.value(), 1),\
                                  round(self.ui.source_z.value(), 1),\
                                  round(self.ui.source_activity.value(), 1),\
                                  round(self.ui.source_time.value(), 1)
        return x, y, z, activity, time


    def addSource(self):
        """
        Method used to add and update the source to source list
        :return:
        """

        x, y, z = round(self.ui.source_x.value(), 1),\
                  round(self.ui.source_y.value(), 1),\
                  round(self.ui.source_z.value(), 1)
        activity = round(self.ui.source_activity.value(), 1)
        time = round(self.ui.source_time.value(), 1)
        source = TG43.Source(x, y, z, activity, time)
        self.source_list.append(source)
        row_pos = self.ui.source_table.rowCount()
        self.ui.source_table.insertRow(row_pos)
        self.ui.source_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(source.type)))
        self.ui.source_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(x)))
        self.ui.source_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(y)))
        self.ui.source_table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(str(z)))
        self.ui.source_table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(str(activity)))
        self.ui.source_table.setItem(row_pos, 5, QtWidgets.QTableWidgetItem(str(time)))

    def addRefPoint(self):
        """
        Method used to add reference point to list. This also computes the dose for that
        reference point. This kind of causes an issue if user inputs reference points before
        the sources.
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        x, y, z = round(self.ui.dose_ref_x.value(), 1),\
                  round(self.ui.dose_ref_y.value(), 1),\
                  round(self.ui.dose_ref_z.value(), 1)
        ref = TG43.DoseRefPoint(x, y, z)
        dose = ref.computeDose(self.source_list)
        total_dose = round(np.sum(dose), 2)
        mr_dose = ref.computeMeisbergerRatio(self.source_list)
        total_mr_dose = round(np.sum(mr_dose), 2)
        percent_diff = 100 * (total_mr_dose - total_dose) / ((total_dose + total_mr_dose)/2)
        percent_diff = round(percent_diff, 2)
        self.refpoint_list.append(ref)
        row_pos = self.ui.refpoint_table.rowCount()
        self.ui.refpoint_table.insertRow(row_pos)
        self.ui.refpoint_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(x)))
        self.ui.refpoint_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(y)))
        self.ui.refpoint_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(z)))
        self.ui.refpoint_table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(str(total_dose)))
        self.ui.refpoint_table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(str(total_mr_dose)))
        self.ui.refpoint_table.setItem(row_pos, 5, QtWidgets.QTableWidgetItem(str(percent_diff)))

    def runExample(self):
        """
        Function used to run example for project
        """
        self.ui.refpoint_table.setRowCount(0)
        self.ui.source_table.setRowCount(0)
        self.source_list = [TG43.Source(0, 0, 0, 10, 10),
                            TG43.Source(0, 2, 0, 10, 10),
                            TG43.Source(0, -2, 0, 10, 10),
                            TG43.Source(3, 1, 0, 10, 10),
                            TG43.Source(3, -1, 0, 10, 10)]
        row_pos = 0
        for source in self.source_list:
            self.ui.source_table.insertRow(row_pos)
            self.ui.source_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(source.type)))
            self.ui.source_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(source.x)))
            self.ui.source_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(source.y)))
            self.ui.source_table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(str(source.z)))
            self.ui.source_table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(str(source.activity)))
            self.ui.source_table.setItem(row_pos, 5, QtWidgets.QTableWidgetItem(str(source.time)))
            row_pos += 1

        self.refpoint_list = []

        self.refpoint_list = [TG43.DoseRefPoint(-2.0, 0, 0),
                              TG43.DoseRefPoint(1.5, 0, 0),
                              TG43.DoseRefPoint(1.5, 3, 0),
                              TG43.DoseRefPoint(1.5, 4, 0),
                              TG43.DoseRefPoint(4, 0, 0)]

        row_pos = 0
        for refpoint in self.refpoint_list:
            dose = round(np.sum(refpoint.computeDose(self.source_list)))
            mr = round(np.sum(refpoint.computeMeisbergerRatio(self.source_list)))
            self.ui.refpoint_table.insertRow(row_pos)
            self.ui.refpoint_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(str(refpoint.x)))
            self.ui.refpoint_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(refpoint.y)))
            self.ui.refpoint_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(refpoint.z)))
            self.ui.refpoint_table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(str(dose)))
            self.ui.refpoint_table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(str(mr)))
            percent_diff = 100 * (mr - dose)/((dose + mr)/2)
            self.ui.refpoint_table.setItem(row_pos, 5, QtWidgets.QTableWidgetItem(str(round(percent_diff, 2))))
            row_pos += 1


    def clearRefPoint(self):
        """
        Clears reference point list
        :return:
        """
        self.ui.refpoint_table.setRowCount(0)
        self.refpoint_list = []

    def clearSources(self):
        """
        Clears the source list
        :return:
        """
        self.ui.source_table.setRowCount(0)
        self.source_list = []

    def plotLayout(self):
        """
        Creates a pop-up graph of input sources and reference points
        :return:
        """

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        source_x = []
        source_y = []
        source_z = []
        for source in self.source_list:
            source_x.append(source.x)
            source_y.append(source.y)
            source_z.append(source.z)

        ref_x = []
        ref_y = []
        ref_z = []
        for ref in self.refpoint_list:
            ref_x.append(ref.x)
            ref_y.append(ref.y)
            ref_z.append(ref.z)

        ax.scatter(source_x, source_y, source_z, marker='o', label='Sources')
        ax.scatter(ref_x, ref_y, ref_z, marker='x', label='Dose Reference Points')

        ax.set_xlabel('x (cm)')
        ax.set_ylabel('y (cm)')
        ax.set_zlabel('z (cm)')

        ax.legend()

        plt.show()


    def printToExcel(self):
        """
        Doesn't actually  print to excel. I found printing the dose contributions to the terminal
        as sufficient
        :return:
        """

        TG43_doselist, MR_doselist = self.computeDoseList()
        idx_names = []
        column_names = []
        for idx in range(len(TG43_doselist)): idx_names.append(f'Reference Point {idx + 1}')
        for col in range(len(TG43_doselist[0])): column_names.append(f'Dose From Source # {col + 1}')

        TG43_df = pd.DataFrame(TG43_doselist, columns=column_names, index=idx_names)
        MR_df = pd.DataFrame(MR_doselist, columns=column_names, index=idx_names)


        # fig, ax = plt.subplots(1, 1)
        # table(ax, TG43_df)

        print('\033[1m'+'Dose Contributions (all units in cGy):')
        print('\033[0m'+f'TG-43 Dose Contributions:\n {TG43_df}\n')
        print(f'Meisburger Ratio Dose Contributions:\n {MR_df}')


    def computeDoseList(self):
        """
        Used to compute dose for a given doselist with TG43 and Meisberger ratio procedures
        :return: TG43 and Meisberger ratio doselists
        """
        TG43_doselist = []
        MR_doselist = []
        for refpoint in self.refpoint_list:
            TG43_doselist.append(refpoint.computeDose(self.source_list))
            MR_doselist.append(refpoint.computeMeisbergerRatio(self.source_list))

        return TG43_doselist, MR_doselist




app = QApplication(sys.argv)
w = AppWindow()
w.show()

w.ui.add_source.clicked.connect(w.addSource)
w.ui.add_dose_point.clicked.connect(w.addRefPoint)
w.ui.close_all.clicked.connect(QtWidgets.qApp.closeAllWindows)
w.ui.run_example.clicked.connect(w.runExample)
w.ui.delete_refpoint.clicked.connect(w.clearRefPoint)
w.ui.delete_source.clicked.connect(w.clearSources)
w.ui.export_btn.clicked.connect(w.printToExcel)
w.ui.plot_btn.clicked.connect(w.plotLayout)

sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TG43_9.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(646, 917)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(340, 10, 301, 131))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dose_ref_y = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dose_ref_y.setFont(font)
        self.dose_ref_y.setMouseTracking(False)
        self.dose_ref_y.setAcceptDrops(False)
        self.dose_ref_y.setAutoFillBackground(False)
        self.dose_ref_y.setStyleSheet("")
        self.dose_ref_y.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.dose_ref_y.setAlignment(QtCore.Qt.AlignCenter)
        self.dose_ref_y.setProperty("showGroupSeparator", False)
        self.dose_ref_y.setDecimals(1)
        self.dose_ref_y.setMinimum(-1000.0)
        self.dose_ref_y.setMaximum(1000.0)
        self.dose_ref_y.setSingleStep(0.1)
        self.dose_ref_y.setObjectName("dose_ref_y")
        self.verticalLayout.addWidget(self.dose_ref_y)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.dose_ref_x = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dose_ref_x.setFont(font)
        self.dose_ref_x.setMouseTracking(False)
        self.dose_ref_x.setAcceptDrops(False)
        self.dose_ref_x.setAutoFillBackground(False)
        self.dose_ref_x.setStyleSheet("")
        self.dose_ref_x.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.dose_ref_x.setAlignment(QtCore.Qt.AlignCenter)
        self.dose_ref_x.setProperty("showGroupSeparator", False)
        self.dose_ref_x.setDecimals(1)
        self.dose_ref_x.setMinimum(-1000.0)
        self.dose_ref_x.setMaximum(1000.0)
        self.dose_ref_x.setSingleStep(0.1)
        self.dose_ref_x.setObjectName("dose_ref_x")
        self.verticalLayout_3.addWidget(self.dose_ref_x)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.dose_ref_z = QtWidgets.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dose_ref_z.setFont(font)
        self.dose_ref_z.setMouseTracking(False)
        self.dose_ref_z.setAcceptDrops(False)
        self.dose_ref_z.setAutoFillBackground(False)
        self.dose_ref_z.setStyleSheet("")
        self.dose_ref_z.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.dose_ref_z.setAlignment(QtCore.Qt.AlignCenter)
        self.dose_ref_z.setProperty("showGroupSeparator", False)
        self.dose_ref_z.setDecimals(1)
        self.dose_ref_z.setMinimum(-1000.0)
        self.dose_ref_z.setMaximum(1000.0)
        self.dose_ref_z.setSingleStep(0.1)
        self.dose_ref_z.setObjectName("dose_ref_z")
        self.verticalLayout_2.addWidget(self.dose_ref_z)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.add_dose_point = QtWidgets.QDialogButtonBox(self.groupBox)
        self.add_dose_point.setToolTip("")
        self.add_dose_point.setStatusTip("")
        self.add_dose_point.setInputMethodHints(QtCore.Qt.ImhNone)
        self.add_dose_point.setOrientation(QtCore.Qt.Horizontal)
        self.add_dose_point.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.add_dose_point.setCenterButtons(True)
        self.add_dose_point.setObjectName("add_dose_point")
        self.gridLayout.addWidget(self.add_dose_point, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 311, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.source_type = QtWidgets.QComboBox(self.groupBox_2)
        self.source_type.setGeometry(QtCore.QRect(12, 32, 281, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.source_type.setFont(font)
        self.source_type.setEditable(False)
        self.source_type.setObjectName("source_type")
        self.source_type.addItem("")
        self.source_type.addItem("")
        self.source_type.addItem("")
        self.source_type.addItem("")
        self.source_type.addItem("")
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(12, 240, 287, 5))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(12, 72, 287, 5))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(6)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.source_time = QtWidgets.QSpinBox(self.groupBox_2)
        self.source_time.setGeometry(QtCore.QRect(110, 200, 84, 29))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.source_time.setFont(font)
        self.source_time.setMouseTracking(False)
        self.source_time.setAcceptDrops(False)
        self.source_time.setAutoFillBackground(False)
        self.source_time.setStyleSheet("")
        self.source_time.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.source_time.setAlignment(QtCore.Qt.AlignCenter)
        self.source_time.setProperty("showGroupSeparator", False)
        self.source_time.setObjectName("source_time")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(90, 170, 128, 17))
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(10, 160, 287, 5))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(5)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 260, 91, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.source_y = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.source_y.setFont(font)
        self.source_y.setMouseTracking(False)
        self.source_y.setAcceptDrops(False)
        self.source_y.setAutoFillBackground(False)
        self.source_y.setStyleSheet("")
        self.source_y.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.source_y.setAlignment(QtCore.Qt.AlignCenter)
        self.source_y.setProperty("showGroupSeparator", False)
        self.source_y.setDecimals(1)
        self.source_y.setMinimum(-1000.0)
        self.source_y.setMaximum(1000.0)
        self.source_y.setSingleStep(0.1)
        self.source_y.setObjectName("source_y")
        self.verticalLayout_8.addWidget(self.source_y)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 260, 91, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.source_x = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.source_x.setFont(font)
        self.source_x.setMouseTracking(False)
        self.source_x.setAcceptDrops(False)
        self.source_x.setAutoFillBackground(False)
        self.source_x.setStyleSheet("")
        self.source_x.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.source_x.setAlignment(QtCore.Qt.AlignCenter)
        self.source_x.setProperty("showGroupSeparator", False)
        self.source_x.setDecimals(1)
        self.source_x.setMinimum(-1000.0)
        self.source_x.setMaximum(1000.0)
        self.source_x.setSingleStep(0.1)
        self.source_x.setObjectName("source_x")
        self.verticalLayout_7.addWidget(self.source_x)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(207, 260, 91, 54))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.source_z = QtWidgets.QDoubleSpinBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.source_z.setFont(font)
        self.source_z.setMouseTracking(False)
        self.source_z.setAcceptDrops(False)
        self.source_z.setAutoFillBackground(False)
        self.source_z.setStyleSheet("")
        self.source_z.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.source_z.setAlignment(QtCore.Qt.AlignCenter)
        self.source_z.setProperty("showGroupSeparator", False)
        self.source_z.setDecimals(1)
        self.source_z.setMinimum(-1000.0)
        self.source_z.setMaximum(1000.0)
        self.source_z.setSingleStep(0.1)
        self.source_z.setObjectName("source_z")
        self.verticalLayout_9.addWidget(self.source_z)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(90, 90, 128, 17))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.source_activity = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.source_activity.setGeometry(QtCore.QRect(110, 120, 84, 29))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.source_activity.setFont(font)
        self.source_activity.setMouseTracking(False)
        self.source_activity.setAcceptDrops(False)
        self.source_activity.setAutoFillBackground(False)
        self.source_activity.setStyleSheet("")
        self.source_activity.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.source_activity.setAlignment(QtCore.Qt.AlignCenter)
        self.source_activity.setProperty("showGroupSeparator", False)
        self.source_activity.setDecimals(1)
        self.source_activity.setMaximum(1000.0)
        self.source_activity.setSingleStep(0.1)
        self.source_activity.setObjectName("source_activity")
        self.add_source = QtWidgets.QDialogButtonBox(self.groupBox_2)
        self.add_source.setGeometry(QtCore.QRect(210, 320, 91, 25))
        self.add_source.setInputMethodHints(QtCore.Qt.ImhNone)
        self.add_source.setOrientation(QtCore.Qt.Horizontal)
        self.add_source.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.add_source.setCenterButtons(True)
        self.add_source.setObjectName("add_source")
        self.close_all = QtWidgets.QDialogButtonBox(Dialog)
        self.close_all.setGeometry(QtCore.QRect(430, 310, 81, 31))
        self.close_all.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_all.setObjectName("close_all")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 640, 651, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.refpoint_table = QtWidgets.QTableWidget(self.groupBox_3)
        self.refpoint_table.setGeometry(QtCore.QRect(0, 20, 631, 192))
        self.refpoint_table.setAlternatingRowColors(True)
        self.refpoint_table.setObjectName("refpoint_table")
        self.refpoint_table.setColumnCount(6)
        self.refpoint_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.refpoint_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.refpoint_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.refpoint_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.refpoint_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.refpoint_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.refpoint_table.setHorizontalHeaderItem(5, item)
        self.refpoint_table.horizontalHeader().setCascadingSectionResizes(False)
        self.refpoint_table.horizontalHeader().setStretchLastSection(True)
        self.refpoint_table.verticalHeader().setCascadingSectionResizes(False)
        self.refpoint_table.verticalHeader().setSortIndicatorShown(False)
        self.refpoint_table.verticalHeader().setStretchLastSection(False)
        self.delete_refpoint = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_refpoint.setGeometry(QtCore.QRect(0, 230, 131, 25))
        self.delete_refpoint.setAutoFillBackground(False)
        self.delete_refpoint.setObjectName("delete_refpoint")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 370, 621, 261))
        self.groupBox_4.setObjectName("groupBox_4")
        self.source_table = QtWidgets.QTableWidget(self.groupBox_4)
        self.source_table.setGeometry(QtCore.QRect(0, 20, 611, 201))
        self.source_table.setAlternatingRowColors(True)
        self.source_table.setObjectName("source_table")
        self.source_table.setColumnCount(6)
        self.source_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.source_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.source_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.source_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.source_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.source_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.source_table.setHorizontalHeaderItem(5, item)
        self.source_table.horizontalHeader().setSortIndicatorShown(True)
        self.source_table.horizontalHeader().setStretchLastSection(True)
        self.source_table.verticalHeader().setSortIndicatorShown(False)
        self.source_table.verticalHeader().setStretchLastSection(False)
        self.delete_source = QtWidgets.QPushButton(self.groupBox_4)
        self.delete_source.setGeometry(QtCore.QRect(0, 230, 111, 25))
        self.delete_source.setAutoFillBackground(False)
        self.delete_source.setObjectName("delete_source")
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(410, 180, 130, 89))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.run_example = QtWidgets.QPushButton(self.layoutWidget3)
        self.run_example.setObjectName("run_example")
        self.gridLayout_2.addWidget(self.run_example, 0, 0, 1, 1)
        self.plot_btn = QtWidgets.QPushButton(self.layoutWidget3)
        self.plot_btn.setObjectName("plot_btn")
        self.gridLayout_2.addWidget(self.plot_btn, 1, 0, 1, 1)
        self.export_btn = QtWidgets.QPushButton(self.layoutWidget3)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout_2.addWidget(self.export_btn, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.close_all.clicked['QAbstractButton*'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dose_ref_x, self.dose_ref_y)
        Dialog.setTabOrder(self.dose_ref_y, self.dose_ref_z)
        Dialog.setTabOrder(self.dose_ref_z, self.source_type)
        Dialog.setTabOrder(self.source_type, self.source_activity)
        Dialog.setTabOrder(self.source_activity, self.source_time)
        Dialog.setTabOrder(self.source_time, self.source_x)
        Dialog.setTabOrder(self.source_x, self.source_y)
        Dialog.setTabOrder(self.source_y, self.source_z)
        Dialog.setTabOrder(self.source_z, self.refpoint_table)
        Dialog.setTabOrder(self.refpoint_table, self.source_table)
        Dialog.setTabOrder(self.source_table, self.delete_refpoint)
        Dialog.setTabOrder(self.delete_refpoint, self.delete_source)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Add Dose Reference Point"))
        self.label.setText(_translate("Dialog", "Y (cm)"))
        self.label_3.setText(_translate("Dialog", "X (cm)"))
        self.label_2.setText(_translate("Dialog", "Z (cm)"))
        self.groupBox_2.setTitle(_translate("Dialog", "Add Brachy Source"))
        self.source_type.setItemText(0, _translate("Dialog", "Select Source Type"))
        self.source_type.setItemText(1, _translate("Dialog", "Isodose Control HDR 192Ir Flexisource"))
        self.source_type.setItemText(2, _translate("Dialog", "GammaMed HDR 192Ir Plus"))
        self.source_type.setItemText(3, _translate("Dialog", "SPEC in. Co. HDR 192IR M-19"))
        self.source_type.setItemText(4, _translate("Dialog", "Varian HDR 192IR VS2000"))
        self.label_11.setText(_translate("Dialog", "Source Time (min)"))
        self.label_8.setText(_translate("Dialog", "Y (cm)"))
        self.label_7.setText(_translate("Dialog", "X (cm)"))
        self.label_9.setText(_translate("Dialog", "Z (cm)"))
        self.label_10.setText(_translate("Dialog", "Source Activity (Ci)"))
        self.groupBox_3.setTitle(_translate("Dialog", "Reference Points"))
        self.refpoint_table.setSortingEnabled(True)
        item = self.refpoint_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "X (cm)"))
        item = self.refpoint_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Y (cm)"))
        item = self.refpoint_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Z (cm)"))
        item = self.refpoint_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "TG-43 (cGy)"))
        item = self.refpoint_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "MR (cGy)"))
        item = self.refpoint_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "% Diff"))
        self.delete_refpoint.setText(_translate("Dialog", "Clear Ref Points"))
        self.groupBox_4.setTitle(_translate("Dialog", "Sources"))
        item = self.source_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Type"))
        item = self.source_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "X (cm)"))
        item = self.source_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Y (cm)"))
        item = self.source_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Z (cm)"))
        item = self.source_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Activity (Ci)"))
        item = self.source_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Time (min)"))
        self.delete_source.setText(_translate("Dialog", "Clear Sources"))
        self.run_example.setText(_translate("Dialog", "Example Scenario"))
        self.plot_btn.setText(_translate("Dialog", "Plot"))
        self.export_btn.setText(_translate("Dialog", "Dose Info"))


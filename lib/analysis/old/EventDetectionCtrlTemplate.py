# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/analysis/old/EventDetectionCtrlTemplate.ui'
#
# Created: Wed Jan  4 18:01:31 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EventDetectionCtrlForm(object):
    def setupUi(self, EventDetectionCtrlForm):
        EventDetectionCtrlForm.setObjectName(_fromUtf8("EventDetectionCtrlForm"))
        EventDetectionCtrlForm.resize(264, 340)
        self.verticalLayout_3 = QtGui.QVBoxLayout(EventDetectionCtrlForm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(EventDetectionCtrlForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.preFilterList = FilterList(self.groupBox_2)
        self.preFilterList.setObjectName(_fromUtf8("preFilterList"))
        self.gridLayout_3.addWidget(self.preFilterList, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(EventDetectionCtrlForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.detectMethodCombo = QtGui.QComboBox(self.groupBox)
        self.detectMethodCombo.setObjectName(_fromUtf8("detectMethodCombo"))
        self.detectMethodCombo.addItem(_fromUtf8(""))
        self.detectMethodCombo.addItem(_fromUtf8(""))
        self.detectMethodCombo.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.detectMethodCombo)
        self.detectMethodStack = QtGui.QStackedWidget(self.groupBox)
        self.detectMethodStack.setObjectName(_fromUtf8("detectMethodStack"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_6 = QtGui.QLabel(self.page_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stThresholdSpin = SpinBox(self.page_3)
        self.stThresholdSpin.setProperty(_fromUtf8("value"), 3.0)
        self.stThresholdSpin.setObjectName(_fromUtf8("stThresholdSpin"))
        self.gridLayout_4.addWidget(self.stThresholdSpin, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.detectMethodStack.addWidget(self.page_3)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.page_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.zcSumAbsThresholdSpin = SpinBox(self.page_2)
        self.zcSumAbsThresholdSpin.setObjectName(_fromUtf8("zcSumAbsThresholdSpin"))
        self.gridLayout.addWidget(self.zcSumAbsThresholdSpin, 1, 2, 1, 1)
        self.zcAmpAbsThresholdSpin = SpinBox(self.page_2)
        self.zcAmpAbsThresholdSpin.setEnabled(True)
        self.zcAmpAbsThresholdSpin.setObjectName(_fromUtf8("zcAmpAbsThresholdSpin"))
        self.gridLayout.addWidget(self.zcAmpAbsThresholdSpin, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.page_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.page_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.zcAmpRelThresholdSpin = QtGui.QDoubleSpinBox(self.page_2)
        self.zcAmpRelThresholdSpin.setEnabled(False)
        self.zcAmpRelThresholdSpin.setProperty(_fromUtf8("value"), 8.0)
        self.zcAmpRelThresholdSpin.setObjectName(_fromUtf8("zcAmpRelThresholdSpin"))
        self.gridLayout.addWidget(self.zcAmpRelThresholdSpin, 2, 3, 1, 1)
        self.zcSumRelThresholdSpin = QtGui.QDoubleSpinBox(self.page_2)
        self.zcSumRelThresholdSpin.setProperty(_fromUtf8("value"), 8.0)
        self.zcSumRelThresholdSpin.setObjectName(_fromUtf8("zcSumRelThresholdSpin"))
        self.gridLayout.addWidget(self.zcSumRelThresholdSpin, 1, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.page_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_2.setEnabled(False)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.gridLayout.addWidget(self.doubleSpinBox_2, 3, 3, 1, 1)
        self.zcLenAbsThresholdSpin = QtGui.QSpinBox(self.page_2)
        self.zcLenAbsThresholdSpin.setMaximum(100000)
        self.zcLenAbsThresholdSpin.setProperty(_fromUtf8("value"), 3)
        self.zcLenAbsThresholdSpin.setObjectName(_fromUtf8("zcLenAbsThresholdSpin"))
        self.gridLayout.addWidget(self.zcLenAbsThresholdSpin, 3, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.detectMethodStack.addWidget(self.page_2)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.cbThresholdSpin = QtGui.QDoubleSpinBox(self.page)
        self.cbThresholdSpin.setProperty(_fromUtf8("value"), 4.0)
        self.cbThresholdSpin.setObjectName(_fromUtf8("cbThresholdSpin"))
        self.gridLayout_2.addWidget(self.cbThresholdSpin, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.cbRiseTauSpin = QtGui.QDoubleSpinBox(self.page)
        self.cbRiseTauSpin.setProperty(_fromUtf8("value"), 0.01)
        self.cbRiseTauSpin.setObjectName(_fromUtf8("cbRiseTauSpin"))
        self.gridLayout_2.addWidget(self.cbRiseTauSpin, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.page)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.cbFallTauSpin = QtGui.QDoubleSpinBox(self.page)
        self.cbFallTauSpin.setProperty(_fromUtf8("value"), 0.01)
        self.cbFallTauSpin.setObjectName(_fromUtf8("cbFallTauSpin"))
        self.gridLayout_2.addWidget(self.cbFallTauSpin, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.detectMethodStack.addWidget(self.page)
        self.verticalLayout.addWidget(self.detectMethodStack)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(EventDetectionCtrlForm)
        self.detectMethodCombo.setCurrentIndex(1)
        self.detectMethodStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(EventDetectionCtrlForm)

    def retranslateUi(self, EventDetectionCtrlForm):
        EventDetectionCtrlForm.setWindowTitle(QtGui.QApplication.translate("EventDetectionCtrlForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setToolTip(QtGui.QApplication.translate("EventDetectionCtrlForm", "Pre-processing options. Used for processing data before any event detection takes place. Processing is performed in the order listed.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("EventDetectionCtrlForm", "Pre-processing", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("EventDetectionCtrlForm", "Event Detection", None, QtGui.QApplication.UnicodeUTF8))
        self.detectMethodCombo.setItemText(0, QtGui.QApplication.translate("EventDetectionCtrlForm", "Stdev. Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.detectMethodCombo.setItemText(1, QtGui.QApplication.translate("EventDetectionCtrlForm", "Zero-crossing", None, QtGui.QApplication.UnicodeUTF8))
        self.detectMethodCombo.setItemText(2, QtGui.QApplication.translate("EventDetectionCtrlForm", "Clements-Bekkers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Sum Thresh.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Amp. Thresh.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Abs.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Len. Thresh.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Rel.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Rise Tau", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("EventDetectionCtrlForm", "Fall Tau", None, QtGui.QApplication.UnicodeUTF8))

from FilterList import FilterList
from SpinBox import SpinBox

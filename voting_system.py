# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_wid.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from presidents import Ui_Form


class Ui_TabWidget(object):
    def setupUi(self, TabWidget, user):
        self.username = user
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(444, 293)
        self.window = QtWidgets.QWidget()
        self.uii = Ui_Form()
        self.uii.setupUi(self.window,self.username)
        self.window.setObjectName("tab1")
        TabWidget.addTab(self.window, "")
        #TabWidget.insertTab(1, self.window, "")

        self.retranslateUi(TabWidget)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Voting System"))
        TabWidget.setTabText(TabWidget.indexOf(self.window), _translate("TabWidget", "Presidents"))




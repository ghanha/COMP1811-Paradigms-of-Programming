 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uni-proj2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from voting_system import Ui_TabWidget
from datetime import date
import project_images
import sqlite3
import sys
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):

    def checkDate(self):
        self.today = date.today()
        self.date1 = self.today.strftime("%Y-%m-%d")
        connection = sqlite3.connect("login.db")
        date2 = connection.execute("SELECT * FROM ELECTION_DATE")
        date2 = (date2.fetchone()[0])
        return self.date1 > date2
    
    def voting(self,user):
        print (user)
        self.window = QtWidgets.QTabWidget()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self.window, user)
        Form.hide()
        self.window.show()
    
    def loginCheck(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if self.checkDate() == True:
            
            connection = sqlite3.connect("login.db")
            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
            if(len(result.fetchall()) > 0):
                
                self.voting(username)
                connection.close()
            else:
                self.label_4.show()
                return
        else:
            self.label_4.setText('The Election period has not yet been started')
            self.label_4.show()
            
    def setupUi(self, Form):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo_gre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setObjectName("Form")
        Form.resize(704, 555)
        Form.setToolTipDuration(0)
        Form.setStyleSheet("#Form\n"
"{\n"
"  background:url(:/rsz_1uni.jpg);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(140, 90, 441, 351))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"  background-color:rgba(51, 51, 51, 210);\n"
"  border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 40, 141, 41))
        self.label.setStyleSheet("*{\n"
"    font-family:Rawson;\n"
"    font-size:24px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 290, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"  background-color:rgb(255,0,0,210);\n"
"  color:white;\n"
"  border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"  background:#57B6D2;\n"
"  color:red;\n"
"  border-radius:15px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginCheck)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
" font-size:16px;\n"
" color:white;\n"
" background:transparent;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid red;\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 210, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid red;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
" font-size:16px;\n"
" color:white;\n"
" background:transparent;\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 260, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"color:red;\n"
"background:rgb(255, 237, 187,210);\n"
"background-image: url(:/warning1.png);\n"
"background-repeat: no-repeat;\n"
"padding-left: 30px;\n"
"display: block;\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(310, 50, 91, 81))
        self.toolButton.setStyleSheet("QToolButton\n"
"{\n"
"  background:red;\n"
"  border-radius:30px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/stu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(128, 128))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GSU Login"))
        self.label.setText(_translate("Form", "gsu elections"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_2.setText(_translate("Form", "Username"))
        self.lineEdit.setText(_translate("Form", "Student ID"))
        self.lineEdit_2.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Incorrect StudentID or Password"))
        self.toolButton.setText(_translate("Form", "..."))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


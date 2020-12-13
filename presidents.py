# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prova_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys

class Ui_Form(object):
    def setupUi(self, Form, user):
        self.username = user
        Form.setObjectName("Form")
        Form.resize(400, 300)
        # create table:
        self.buttonGroup0 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup1 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup3 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup4 = QtWidgets.QButtonGroup(Form)
        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(30, 10, 381, 191))
        self.table.setRowCount(4)
        self.table.setColumnCount(6)
        #Add title
        item = QtWidgets.QTableWidgetItem('Candidates')
        self.table.setHorizontalHeaderItem(0,item)
        item = QtWidgets.QTableWidgetItem('1')
        self.table.setHorizontalHeaderItem(1,item)
        item = QtWidgets.QTableWidgetItem('2')
        self.table.setHorizontalHeaderItem(2,item)
        item = QtWidgets.QTableWidgetItem('3')
        self.table.setHorizontalHeaderItem(3,item)
        item = QtWidgets.QTableWidgetItem('4')
        self.table.setHorizontalHeaderItem(4,item)
        item = QtWidgets.QTableWidgetItem('None')
        self.table.setHorizontalHeaderItem(5,item)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #pushButton
        self.pushButton = QtWidgets.QPushButton("Sumbit Vote",Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 111, 31)) 
        self.pushButton.setObjectName("pushButton")
        #label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 211, 441, 20))
        self.label.setText('Check all the checkbox')
        self.label.hide()
            
        def load_candidates():
            connection = sqlite3.connect("login.db")
            connection.row_factory = lambda cursor, row: row[0]
            c = connection.cursor()
            ids = c.execute("SELECT NAME FROM Candidates WHERE POSITION='GSU_Officer'").fetchall()
            return ids
        
        def add_item(rows):
            for i in range(1,6):
                ch = QtWidgets.QCheckBox(parent=self.table)
                b = str(rows)
                self.rp = eval("self.buttonGroup"+b)
                self.rp.addButton(ch, id=i)
                self.table.setCellWidget(rows, int(i), ch)
                
        for i, letter in enumerate(load_candidates()):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(letter))
            
        self.a = len(list(load_candidates()))
        
        for x in range(self.a):
            add_item(x)
        self.pushButton.clicked.connect(lambda checked, row=0, col=i: self.checkbox_state(row,checked))
        
    def checkbox_state(self,row,checked):
        states = []
        for x in range(self.a):
            b = str(x)
            self.group_name = eval("self.buttonGroup"+b)
            for y in range(5):
                indexOfChecked = self.group_name.buttons()[y].isChecked()
                states.append(indexOfChecked)
        if states.count(True) == 4:
            self.submit_vote(row,checked)           
        else:
            self.label.show()
            

    def submit_vote(self,row,checked):
        username = self.username
        for x in range(self.a):
            b = str(x)
            self.pq = eval("self.buttonGroup"+b)
            score = self.pq.checkedId()
            name = self.table.item(x,0)
            name = name.text()
            connection = sqlite3.connect("login.db")
            if score is 5:#if score is None(dont do anything)
                pass
            else:
                vote = connection.execute("INSERT INTO COUNTING (USERNAME, POSITION, CANDIDATE, PREFERENCE) VALUES (? ,'GSU_Officer', ?, ?)",(username,name,score))
                print (score,name)
                connection.commit()
        connection.close
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())





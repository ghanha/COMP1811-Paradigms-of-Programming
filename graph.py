

from __future__ import unicode_literals
import sys
import os,sqlite3
import random
import matplotlib
import numpy as np
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def count_votes(self):
        counts = {}
        c = sqlite3.connect("login.db")
        ids = c.execute("SELECT NAME FROM Candidates WHERE POSITION='GSU_Officer'").fetchall()
        for x in ids:
            name = (x[0])
            votes = c.execute("SELECT COUNT(*) FROM COUNTING WHERE CANDIDATE = ?;",(name,)).fetchone()[0]
            counts[name] = votes
        #Single Transferable vote
        highest = max(counts, key=counts.get)
        value = counts[highest]
        return counts
    def quota(self):
        seats = 1
        c = sqlite3.connect("login.db")
        total_votes = c.execute("SELECT COUNT(*) FROM COUNTING WHERE POSITION = 'GSU_Officer';").fetchone()[0]
        quota = (total_votes/(seats+1))+1
        return quota

    def compute_initial_figure(self):
        y = self.quota()
        self.axes.axhline(y, color='r', linestyle='-')
        D = self.count_votes()
        self.axes.bar(*zip(*D.items()))

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)


qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("Election Result")
aw.show()
sys.exit(qApp.exec_())

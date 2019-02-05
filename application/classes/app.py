try:
    import Tkinter as tk
    import tkFileDialog as filedialog
except ImportError:
    import tkinter as tk
    from tkinter import filedialog

import sys, time, os


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from functions.parser import *
from functions.nucleoReader import *
from functions.basePairReader import *
from functions.visualizeWithBase import *
from functions.visualizeNoBase import *
from classes.BIOImage import *

class App(QWidget):

    fileName = None
    outputfile = None
    bio = BIOImage((640, 640), 'white')
    nobase = None
    base = None
    loadinfo = None
    message = None
    bio.save("temp.png")

    root = tk.Tk()
    root.withdraw()

    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.interface()

    def interface(self):
        loadfile = QLabel("Select file with data to visualize (McAnnotate format)", self)
        loadfilebutton =  QPushButton("&load", self)
        convertbutton = QPushButton("&visualize", self)
        savefilebutton = QPushButton("&save", self)
        self.loadinfo = QLabel(self)
        self.radiobox = QLabel("Show non-canonical base pairs?", self)
        self.nobase =  QRadioButton("Yes", self)
        self.base = QRadioButton("No", self)
        self.outputfile = QLabel(self)
        self.message = QLabel(self)
        pixmap = QPixmap("temp.png")
        pixmap = pixmap.scaled(640, 640)
        self.outputfile.setPixmap(pixmap)
        self.outputfile.resize(pixmap.width(), pixmap.height())
        self.nobase.setChecked(True)

        layer1 = QHBoxLayout()
        layer1.addWidget(self.nobase)
        layer1.addWidget(self.base)
        self.radiogroup = QGroupBox(self)
        self.radiogroup.setLayout(layer1)

# ====================================================================

        loadfile.move(30,30)
        loadfilebutton.move(30,60)
        self.loadinfo.setGeometry(120,20,600,100)
        self.radiobox.move(30,100)
        self.radiogroup.move(200,90)
        convertbutton.move(30,130)
        savefilebutton.move(120, 130)
        self.message.setGeometry(220,90 ,100,100)
        self.outputfile.move(30,170)


# ====================================================================

        loadfilebutton.clicked.connect(self.load)
        convertbutton.clicked.connect(self.visualize)
        savefilebutton.clicked.connect(self.save)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        QtCore.Qt.WindowCloseButtonHint
        self.resize(700, 850)
        self.setFixedSize(self.size())
        self.setWindowTitle("JJA-RNA")
        self.show()

    def load(self):
        self.fileName = filedialog.askopenfilename()
        self.loadinfo.setText(self.fileName)

    def save(self):
        saveFile = filedialog.asksaveasfilename(defaultextension=".png",filetypes=(("png", "*.png"), ("All Files", "*.*")),initialfile='canoniacal')
        self.bio.save(saveFile)


    def visualize(self):
        if(self.fileName):
            parser(self.fileName)
            nucleoList = nucleoReader(self.fileName)
            baseList = basePairReader('output.txt', nucleoList)
            if self.nobase.isChecked():
                self.bio = visualizeWithBase(nucleoList, baseList)
            if self.base.isChecked():
                self.bio = visualizeNoBase(nucleoList, baseList)
            pixmap = QPixmap("temp.png")
            pixmap = pixmap.scaledToWidth(640, QtCore.Qt.SmoothTransformation)
            self.outputfile.setPixmap(pixmap)
            self.outputfile.resize(pixmap.width(), pixmap.height())
            self.message.setText('Done!')
        else:
            self.message.setText('Please load a file')

    def closeEvent(self, event):
        os.remove("temp.png")

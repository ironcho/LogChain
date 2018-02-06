import os

from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class NodeWidget (QWidget):
    def __init__ (self, parent = None):
        super(NodeWidget, self).__init__(parent)

        self.horizontalGroupBox = QGroupBox("Node Lists")

        self.textQVBoxLayout = QVBoxLayout(self)
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)

        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)

        self.horizontalGroupBox.setLayout(self.allQHBoxLayout)

        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(255, 255, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(90, 90, 90);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        print(scriptDir + os.path.sep + imagePath)
        self.iconQLabel.setPixmap(QtGui.QPixmap(scriptDir + os.path.sep + imagePath))

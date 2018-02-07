import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

class NodeWidget (QWidget):
    def __init__ (self, parent = None):
        super(NodeWidget, self).__init__(parent)

        self.textQVBoxLayout = QVBoxLayout(self)
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)

        self.allQHBoxLayout  = QVBoxLayout(self)
        self.iconQLabel = QLabel(self)
        self.iconQLabel.setScaledContents(True)
        self.iconQLabel.resize(24, 24)

        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)

        self.setLayout(self.allQHBoxLayout)

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
        pixmap = QPixmap(imagePath)
        self.iconQLabel.setPixmap(pixmap)
        # scriptDir = os.path.dirname(os.path.realpath(__file__))
        # print(scriptDir + os.path.sep + imagePath)
        # self.iconQLabel.setPixmap(QPixmap(scriptDir + os.path.sep + imagePath))

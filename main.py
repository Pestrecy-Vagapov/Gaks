import sys
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import random, copy


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.title = "PyQt5 окружности"
        self.draw - None
        self.InitWindow()

    def InitWindow(self):
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
            #qp.SetBrush(QBrush(Qt.red, Qt.SolidPattern))
            rad = random.randrange(255)
            x = random.randrange(355)
            y = random.randrange(355)
            qp.drawEllipse(x, y, rad, rad)
            qp.end()

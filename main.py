import sys
import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(427, 514)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 340, 241, 91))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        self.qp = QPainter()
        self.qp.begin(self)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Press Me"))


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.initDrawOval)
        self.x = -30
        self.y = -30
        self.reg = 0

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        if self.reg == 1:
            for i in range(1, random.randrange(2, 10)):
                self.painOval()
        self.qp.end()

    def initDrawOval(self):
        self.reg = 1
        self.update()

    def painOval(self):
        self.x = random.randrange(50, 200)
        self.y = random.randrange(50, 200)
        self.r = random.randrange(10, 50)
        self.R = random.randrange(0, 256)
        self.G = random.randrange(0, 256)
        self.B = random.randrange(0, 256)
        self.qp.setBrush(QColor(self.R, self.G, self.B))
        self.qp.drawEllipse(self.x, self.y, self.r, self.r)



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())


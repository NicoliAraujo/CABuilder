# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainguimain.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DMain(object):
    def setupUi(self, DMain):
        DMain.setObjectName("DMain")
        DMain.resize(282, 180)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DMain.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(DMain)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonGenNumSeq = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonGenNumSeq.setFont(font)
        self.pushButtonGenNumSeq.setObjectName("pushButtonGenNumSeq")
        self.verticalLayout.addWidget(self.pushButtonGenNumSeq)
        self.pushButtonGenImg = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonGenImg.setFont(font)
        self.pushButtonGenImg.setObjectName("pushButtonGenImg")
        self.verticalLayout.addWidget(self.pushButtonGenImg)
        self.pushButtonGenNumSeqFromImg = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonGenNumSeqFromImg.setFont(font)
        self.pushButtonGenNumSeqFromImg.setObjectName("pushButtonGenNumSeqFromImg")
        self.verticalLayout.addWidget(self.pushButtonGenNumSeqFromImg)
        self.pushButtonManNumSeq = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonManNumSeq.setFont(font)
        self.pushButtonManNumSeq.setObjectName("pushButtonManNumSeq")
        self.verticalLayout.addWidget(self.pushButtonManNumSeq)

        self.retranslateUi(DMain)
        self.pushButtonGenNumSeq.clicked.connect(DMain.close)
        self.pushButtonGenImg.clicked.connect(DMain.close)
        self.pushButtonGenNumSeqFromImg.clicked.connect(DMain.close)
        self.pushButtonManNumSeq.clicked.connect(DMain.close)
        QtCore.QMetaObject.connectSlotsByName(DMain)

    def retranslateUi(self, DMain):
        _translate = QtCore.QCoreApplication.translate
        DMain.setWindowTitle(_translate("DMain", "Main"))
        self.pushButtonGenNumSeq.setText(_translate("DMain", "Generate Number Sequence"))
        self.pushButtonGenImg.setText(_translate("DMain", "Generate Image"))
        self.pushButtonGenNumSeqFromImg.setText(_translate("DMain", "Generate Number Sequence From Image"))
        self.pushButtonManNumSeq.setText(_translate("DMain", "Manipulate Number Sequence"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DMain = QtWidgets.QDialog()
    ui = Ui_DMain()
    ui.setupUi(DMain)
    DMain.show()
    sys.exit(app.exec_())


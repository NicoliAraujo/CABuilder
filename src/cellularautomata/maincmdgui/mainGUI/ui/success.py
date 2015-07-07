# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Success(object):
    def setupUi(self, Success):
        Success.setObjectName("Success")
        Success.resize(182, 159)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Success.setWindowIcon(icon)
        self.labelSuccess = QtWidgets.QLabel(Success)
        self.labelSuccess.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelSuccess.setFont(font)
        self.labelSuccess.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSuccess.setObjectName("labelSuccess")
        self.pushButtonClose = QtWidgets.QPushButton(Success)
        self.pushButtonClose.setGeometry(QtCore.QRect(40, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.pushButtonMain = QtWidgets.QPushButton(Success)
        self.pushButtonMain.setGeometry(QtCore.QRect(50, 72, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonMain.setFont(font)
        self.pushButtonMain.setObjectName("pushButtonMain")
        self.line = QtWidgets.QFrame(Success)
        self.line.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Success)
        self.pushButtonMain.clicked.connect(Success.close)
        self.pushButtonClose.clicked.connect(Success.close)
        QtCore.QMetaObject.connectSlotsByName(Success)

    def retranslateUi(self, Success):
        _translate = QtCore.QCoreApplication.translate
        Success.setWindowTitle(_translate("Success", "Success"))
        self.labelSuccess.setText(_translate("Success", "Successfully Generated!"))
        self.pushButtonClose.setText(_translate("Success", "Close Program"))
        self.pushButtonMain.setText(_translate("Success", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Success = QtWidgets.QDialog()
    ui = Ui_Success()
    ui.setupUi(Success)
    Success.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gennumseqfromimg.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DGenNumSeqFromImg(object):
    def setupUi(self, DGenNumSeqFromImg):
        DGenNumSeqFromImg.setObjectName("DGenNumSeqFromImg")
        DGenNumSeqFromImg.resize(423, 356)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DGenNumSeqFromImg.setWindowIcon(icon)
        self.pushButtonGenerate = QtWidgets.QPushButton(DGenNumSeqFromImg)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(70, 290, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGenerate.setFont(font)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.line = QtWidgets.QFrame(DGenNumSeqFromImg)
        self.line.setGeometry(QtCore.QRect(10, 100, 401, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEditOldFilePath = QtWidgets.QLineEdit(DGenNumSeqFromImg)
        self.lineEditOldFilePath.setGeometry(QtCore.QRect(220, 60, 121, 20))
        self.lineEditOldFilePath.setObjectName("lineEditOldFilePath")
        self.labelInfo = QtWidgets.QLabel(DGenNumSeqFromImg)
        self.labelInfo.setGeometry(QtCore.QRect(10, 120, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.labelInfo.setFont(font)
        self.labelInfo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelInfo.setTextFormat(QtCore.Qt.AutoText)
        self.labelInfo.setScaledContents(False)
        self.labelInfo.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelInfo.setWordWrap(True)
        self.labelInfo.setObjectName("labelInfo")
        self.labelImgFile = QtWidgets.QLabel(DGenNumSeqFromImg)
        self.labelImgFile.setGeometry(QtCore.QRect(20, 60, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelImgFile.setFont(font)
        self.labelImgFile.setObjectName("labelImgFile")
        self.lineEditInfo = QtWidgets.QLineEdit(DGenNumSeqFromImg)
        self.lineEditInfo.setGeometry(QtCore.QRect(10, 240, 401, 20))
        self.lineEditInfo.setObjectName("lineEditInfo")
        self.labelRule = QtWidgets.QLabel(DGenNumSeqFromImg)
        self.labelRule.setGeometry(QtCore.QRect(20, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelRule.setFont(font)
        self.labelRule.setObjectName("labelRule")
        self.lineEditRule = QtWidgets.QLineEdit(DGenNumSeqFromImg)
        self.lineEditRule.setGeometry(QtCore.QRect(260, 10, 41, 20))
        self.lineEditRule.setText("")
        self.lineEditRule.setObjectName("lineEditRule")
        self.labelInfo.setBuddy(self.lineEditInfo)
        self.labelImgFile.setBuddy(self.lineEditOldFilePath)
        self.labelRule.setBuddy(self.lineEditRule)

        self.retranslateUi(DGenNumSeqFromImg)
        self.pushButtonGenerate.clicked.connect(DGenNumSeqFromImg.close)
        QtCore.QMetaObject.connectSlotsByName(DGenNumSeqFromImg)
        DGenNumSeqFromImg.setTabOrder(self.lineEditRule, self.lineEditOldFilePath)
        DGenNumSeqFromImg.setTabOrder(self.lineEditOldFilePath, self.lineEditInfo)
        DGenNumSeqFromImg.setTabOrder(self.lineEditInfo, self.pushButtonGenerate)

    def retranslateUi(self, DGenNumSeqFromImg):
        _translate = QtCore.QCoreApplication.translate
        DGenNumSeqFromImg.setWindowTitle(_translate("DGenNumSeqFromImg", "Generate Number Sequence From Image"))
        self.pushButtonGenerate.setText(_translate("DGenNumSeqFromImg", "Generate Number Sequence From Image!"))
        self.labelInfo.setText(_translate("DGenNumSeqFromImg", "It will be generated a new text file (\".txt\") composed by integres. Each number represents a cell state, which is represented by a color in the parent image. A new file will be saved in \" /Output/txtoutput/fromimg/(automaton\'s type)/(rule).txt \". If there is another file with the same name on this folder, it will be overwritten. If you want to add some information to the file name, type it below:"))
        self.labelImgFile.setText(_translate("DGenNumSeqFromImg", "Image File Name (ex: \"45.png\") : "))
        self.labelRule.setText(_translate("DGenNumSeqFromImg", "Cellular Automaton\'s Number of States: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DGenNumSeqFromImg = QtWidgets.QDialog()
    ui = Ui_DGenNumSeqFromImg()
    ui.setupUi(DGenNumSeqFromImg)
    DGenNumSeqFromImg.show()
    sys.exit(app.exec_())


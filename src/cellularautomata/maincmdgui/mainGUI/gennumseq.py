# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gennumseq.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from util import IntKBase

from PyQt5 import QtCore, QtGui, QtWidgets

from cellularautomata.modules.CAOutput import AutomataText
from cellularautomata.modules.CellularAutomata import TotalisticCode, ElementaryCode, \
    CellularAutomata


class Ui_DGenNumSeq(object):
    def setupUi(self, DGenNumSeq):
        DGenNumSeq.setObjectName("DGenNumSeq")
        DGenNumSeq.resize(441, 477)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DGenNumSeq.setWindowIcon(icon)
        self.line_2 = QtWidgets.QFrame(DGenNumSeq)
        self.line_2.setGeometry(QtCore.QRect(10, 140, 421, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButtonGenerate = QtWidgets.QPushButton(DGenNumSeq)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(100, 420, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGenerate.setFont(font)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.labelSideIt = QtWidgets.QLabel(DGenNumSeq)
        self.labelSideIt.setGeometry(QtCore.QRect(10, 160, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.labelSideIt.setFont(font)
        self.labelSideIt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelSideIt.setTextFormat(QtCore.Qt.AutoText)
        self.labelSideIt.setScaledContents(False)
        self.labelSideIt.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.labelSideIt.setWordWrap(True)
        self.labelSideIt.setObjectName("labelSideIt")
        self.labelIt = QtWidgets.QLabel(DGenNumSeq)
        self.labelIt.setGeometry(QtCore.QRect(260, 240, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelIt.setFont(font)
        self.labelIt.setAccessibleName("")
        self.labelIt.setAutoFillBackground(False)
        self.labelIt.setObjectName("labelIt")
        self.radioButtonElementar = QtWidgets.QRadioButton(DGenNumSeq)
        self.radioButtonElementar.setGeometry(QtCore.QRect(20, 50, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonElementar.setFont(font)
        self.radioButtonElementar.setObjectName("radioButtonElementar")
        self.labelInfo = QtWidgets.QLabel(DGenNumSeq)
        self.labelInfo.setGeometry(QtCore.QRect(10, 290, 421, 71))
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
        self.lineEditInfo = QtWidgets.QLineEdit(DGenNumSeq)
        self.lineEditInfo.setGeometry(QtCore.QRect(10, 370, 421, 20))
        self.lineEditInfo.setObjectName("lineEditInfo")
        self.line_3 = QtWidgets.QFrame(DGenNumSeq)
        self.line_3.setGeometry(QtCore.QRect(10, 280, 421, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.labelStates = QtWidgets.QLabel(DGenNumSeq)
        self.labelStates.setGeometry(QtCore.QRect(140, 110, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelStates.setFont(font)
        self.labelStates.setObjectName("labelStates")
        self.lineEditSeed = QtWidgets.QLineEdit(DGenNumSeq)
        self.lineEditSeed.setEnabled(True)
        self.lineEditSeed.setGeometry(QtCore.QRect(380, 110, 31, 20))
        self.lineEditSeed.setText("")
        self.lineEditSeed.setObjectName("lineEditSeed")
        self.lineEditRule = QtWidgets.QLineEdit(DGenNumSeq)
        self.lineEditRule.setGeometry(QtCore.QRect(60, 110, 41, 20))
        self.lineEditRule.setText("")
        self.lineEditRule.setObjectName("lineEditRule")
        self.lineEditIt = QtWidgets.QLineEdit(DGenNumSeq)
        self.lineEditIt.setGeometry(QtCore.QRect(360, 240, 61, 20))
        self.lineEditIt.setText("")
        self.lineEditIt.setObjectName("lineEditIt")
        self.lineEditSide = QtWidgets.QLineEdit(DGenNumSeq)
        self.lineEditSide.setGeometry(QtCore.QRect(150, 240, 61, 20))
        self.lineEditSide.setText("")
        self.lineEditSide.setObjectName("lineEditSide")
        self.radioButtonTotalistico = QtWidgets.QRadioButton(DGenNumSeq)
        self.radioButtonTotalistico.setGeometry(QtCore.QRect(20, 70, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonTotalistico.setFont(font)
        self.radioButtonTotalistico.setObjectName("radioButtonTotalistico")
        self.labelTypeCA = QtWidgets.QLabel(DGenNumSeq)
        self.labelTypeCA.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTypeCA.setFont(font)
        self.labelTypeCA.setObjectName("labelTypeCA")
        self.labelRule = QtWidgets.QLabel(DGenNumSeq)
        self.labelRule.setGeometry(QtCore.QRect(20, 110, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelRule.setFont(font)
        self.labelRule.setObjectName("labelRule")
        self.labelSeed = QtWidgets.QLabel(DGenNumSeq)
        self.labelSeed.setGeometry(QtCore.QRect(340, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSeed.setFont(font)
        self.labelSeed.setObjectName("labelSeed")
        self.lineEditK = QtWidgets.QLineEdit(DGenNumSeq)
        self.lineEditK.setEnabled(True)
        self.lineEditK.setGeometry(QtCore.QRect(270, 110, 31, 20))
        self.lineEditK.setText("")
        self.lineEditK.setObjectName("lineEditK")
        self.labelSide = QtWidgets.QLabel(DGenNumSeq)
        self.labelSide.setGeometry(QtCore.QRect(10, 240, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelSide.setFont(font)
        self.labelSide.setObjectName("labelSide")
        self.labelIt.setBuddy(self.lineEditIt)
        self.labelInfo.setBuddy(self.lineEditInfo)
        self.labelStates.setBuddy(self.lineEditK)
        self.labelRule.setBuddy(self.lineEditRule)
        self.labelSeed.setBuddy(self.lineEditSeed)
        self.labelSide.setBuddy(self.lineEditSide)

        self.retranslateUi(DGenNumSeq)
        self.radioButtonElementar.clicked['bool'].connect(self.lineEditK.setDisabled)       
        self.radioButtonElementar.clicked['bool'].connect(self.lineEditSeed.setDisabled)
        self.radioButtonTotalistico.clicked['bool'].connect(self.lineEditK.setEnabled)
        self.radioButtonTotalistico.clicked['bool'].connect(self.lineEditSeed.setEnabled)

        self.getEntries()

        self.pushButtonGenerate.clicked.connect(DGenNumSeq.close)       
        QtCore.QMetaObject.connectSlotsByName(DGenNumSeq)
        DGenNumSeq.setTabOrder(self.radioButtonElementar, self.radioButtonTotalistico)
        DGenNumSeq.setTabOrder(self.radioButtonTotalistico, self.lineEditRule)
        DGenNumSeq.setTabOrder(self.lineEditRule, self.lineEditK)
        DGenNumSeq.setTabOrder(self.lineEditK, self.lineEditSeed)
        DGenNumSeq.setTabOrder(self.lineEditSeed, self.lineEditSide)
        DGenNumSeq.setTabOrder(self.lineEditSide, self.lineEditIt)
        DGenNumSeq.setTabOrder(self.lineEditIt, self.lineEditInfo)
        DGenNumSeq.setTabOrder(self.lineEditInfo, self.pushButtonGenerate)
        
    def getEntries(self):

        info = str(self.pushButtonGenerate.clicked.connect(self.lineEditInfo.text))

        side = int(self.pushButtonGenerate.clicked.connect(self.lineEditSide.text))
        it = int(self.pushButtonGenerate.clicked.connect(self.lineEditIt.text))
        rule = int(self.pushButtonGenerate.clicked.connect(self.lineEditRule.text))
        k = int(self.pushButtonGenerate.clicked.connect(self.lineEditK.text))
        seed = int(self.pushButtonGenerate.clicked.connect(self.lineEditSeed.text))
        el = self.pushButtonGenerate.clicked.connect(self.radioButtonElementar.clicked['bool'])
        tot = self.pushButtonGenerate.clicked.connect(self.radioButtonTotalistico.clicked['bool'])
        catype = ''
        if (el == True):

            catype = 'Elementary'
        elif (tot == True):

            catype = 'Totalistic'

        self.pushButtonGenerate.clicked.connect(self.genNumSeq(catype, rule, k, seed, side, it,  info))
        print('oeee1')
        
    def genNumSeq(self, catype, rule, k, seed, size, it,  info):
        ca1 = ElementaryCode(30)
        if catype == 'Elementary':
            ca1 = ElementaryCode(rule)
        elif catype == 'Totalistic':
            ca1 = TotalisticCode(rule, k, seed)
        catxt = AutomataText(size, it, ca1, info)
        
              
    def retranslateUi(self, DGenNumSeq):
        _translate = QtCore.QCoreApplication.translate
        DGenNumSeq.setWindowTitle(_translate("DGenNumSeq", "Generate Number Sequence"))
        self.pushButtonGenerate.setText(_translate("DGenNumSeq", "Generate Number Sequence!"))
        self.labelSideIt.setText(_translate("DGenNumSeq", "It will be generated a text file (.txt) composed by integers. Each number represents a state. The file shows the automaton\'s evolution as time passes. Thus, each row\'s number  correspond a cell in the automaton, and each row represent the automaton\' state in that instant."))
        self.labelIt.setText(_translate("DGenNumSeq", "Quantity of lines:"))
        self.radioButtonElementar.setText(_translate("DGenNumSeq", "Elementary"))
        self.labelInfo.setText(_translate("DGenNumSeq", "The text file with the sequence of generated numbers will be saved in \" /Output/txtoutput/original/(automaton\'s type)/ (rule).txt \". If there is another file with the same name in this folder, it will be overwritten. If you want to add some information to the file name, type it below:"))
        self.labelStates.setText(_translate("DGenNumSeq", "Number of States (k):"))
        self.radioButtonTotalistico.setText(_translate("DGenNumSeq", "Totalistic"))
        self.labelTypeCA.setText(_translate("DGenNumSeq", "Cellular Automaton\'s Type:"))
        self.labelRule.setText(_translate("DGenNumSeq", "Rule:"))
        self.labelSeed.setText(_translate("DGenNumSeq", "Seed:"))
        self.labelSide.setText(_translate("DGenNumSeq", "Quantity of cells in a line:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    DGenNumSeq = QtWidgets.QDialog()

    ui = Ui_DGenNumSeq()

    ui.setupUi(DGenNumSeq)

    DGenNumSeq.show()

    sys.exit(app.exec_())

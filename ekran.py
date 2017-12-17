# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekran.ui'
#
# Created: Thu Dec 14 11:25:16 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1088, 421)
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 60, 500, 286))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView2 = QtGui.QGraphicsView(Dialog)
        self.graphicsView2.setGeometry(QtCore.QRect(570, 60, 500, 286))
        self.graphicsView2.setObjectName(_fromUtf8("graphicsView2"))
        self.horizontalSlider = QtGui.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(440, 380, 211, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.orginal = QtGui.QLabel(Dialog)
        self.orginal.setGeometry(QtCore.QRect(20, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.orginal.setFont(font)
        self.orginal.setObjectName(_fromUtf8("orginal"))
        self.orginal_2 = QtGui.QLabel(Dialog)
        self.orginal_2.setGeometry(QtCore.QRect(570, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.orginal_2.setFont(font)
        self.orginal_2.setObjectName(_fromUtf8("orginal_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(650, 360, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.orginal_3 = QtGui.QLabel(Dialog)
        self.orginal_3.setGeometry(QtCore.QRect(440, 360, 211, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.orginal_3.setFont(font)
        self.orginal_3.setObjectName(_fromUtf8("orginal_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.orginal.setText(_translate("Dialog", "Orjinal", None))
        self.orginal_2.setText(_translate("Dialog", "Skeletonization", None))
        self.label.setText(_translate("Dialog", "0", None))
        self.orginal_3.setText(_translate("Dialog", "Skeletonization Değeri :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


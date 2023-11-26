# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(637, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../.designer/backup/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.entry_html_lineEdit = QtWidgets.QLineEdit(Form)
        self.entry_html_lineEdit.setText("")
        self.entry_html_lineEdit.setMaxLength(100000)
        self.entry_html_lineEdit.setObjectName("entry_html_lineEdit")
        self.horizontalLayout_2.addWidget(self.entry_html_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.out_html_lineEdit = QtWidgets.QLineEdit(Form)
        self.out_html_lineEdit.setText("")
        self.out_html_lineEdit.setMaxLength(100000)
        self.out_html_lineEdit.setObjectName("out_html_lineEdit")
        self.verticalLayout.addWidget(self.out_html_lineEdit)
        self.clickHere_pushButton = QtWidgets.QPushButton(Form)
        self.clickHere_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clickHere_pushButton.sizePolicy().hasHeightForWidth())
        self.clickHere_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.clickHere_pushButton.setFont(font)
        self.clickHere_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clickHere_pushButton.setMouseTracking(False)
        self.clickHere_pushButton.setTabletTracking(False)
        self.clickHere_pushButton.setStyleSheet("background-color: rgb(150, 200, 100);\n"
"color: rgb(255, 200, 100);")
        self.clickHere_pushButton.setObjectName("clickHere_pushButton")
        self.verticalLayout.addWidget(self.clickHere_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "HTML compressor (by aymen mahmoudi) - Version 1.0"))
        self.entry_html_lineEdit.setPlaceholderText(_translate("Form", "Paste the original text here"))
        self.out_html_lineEdit.setPlaceholderText(_translate("Form", "Generated format will appear here"))
        self.clickHere_pushButton.setToolTip(_translate("Form", "this is toolTIP"))
        self.clickHere_pushButton.setText(_translate("Form", "Generate compressed format"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

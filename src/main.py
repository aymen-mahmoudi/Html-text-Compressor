##############################################################################
##
# This file is part of Moiré parameter project
##
# Copyright 2023 / AYMEN MAHMOUDI, FRANCE
##
# The files of this project are free and open source: you can redistribute them and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# This project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
##############################################################################

__author__ = ["Aymen Mahmoudi"]
__license__ = "GPL"
__date__ = "26/03/2023"

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui, QtCore
from functions import *


import sys
from functions import *

#  import the gui :
#ui, _ = loadUiType('gui.ui')
from gui import Ui_Form as ui

    


class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)

        # # self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        # self.setUi_changes()
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # function to setup buttons
        self.HandleButtons()

    def HandleButtons(self):
        self.clickHere_pushButton.clicked.connect(self.essential_values) 
        self.clickHere_pushButton.clicked.connect(self.set_out_html)
        

  

  

    def essential_values(self):
        # Global Varilables
        self.entry_html = ''
        self.out_html = ''
        

        self.entry_html = self.get_entry_html()
        self.out_html = compress(self.entry_html)
        

    def get_entry_html(self):
        entry_html = self.entry_html_lineEdit.text()
        return entry_html

    def set_out_html(self):
        self.out_html_lineEdit.setText(self.out_html)



        
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()


if __name__ == "__main__":
    main()

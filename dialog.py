# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:32:04 2017

@author: ESER
"""
import sys
from PyQt4 import QtGui
from main import MainWindow

def main():
    app=QtGui.QApplication(sys.argv)
    
    mainWindow=MainWindow()
    mainWindow.show()
    return app.exec_()
    
    

if __name__=="__main__":
    main()
    
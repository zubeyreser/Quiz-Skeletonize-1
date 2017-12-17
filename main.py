# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:33:30 2017

@author: ESER
"""
     
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from skimage import io
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib.widgets as widgets
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from skimage import color


from ekran import Ui_Dialog
  
class MainWindow(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.yuzde)
        w,h=self.graphicsView.width()-5,self.graphicsView.height()-5
        self.graphicsView.setScene(self.show_image('./at.png',w,h))
        img=cv2.imread('at.png',0)
        skel=np.zeros(img.shape,np.uint8) #  (0 - 255)- uint8 , img.shape - sutun, satır ve kanal sayısı ,  np.zeros 562 tene
        cv2.imwrite('./skel.png',skel)
        w2,h2=self.graphicsView2.width()-5,self.graphicsView2.height()-5
        self.graphicsView2.setScene(self.show_image('./skel.png',w2,h2))
       
        
    def show_image(self, img_name,width,height):
        pixMap = QtGui.QPixmap(img_name)   
        pixMap=pixMap.scaled(width,height)  
        pixItem = QtGui.QGraphicsPixmapItem(pixMap)
        scene2 = QGraphicsScene()
        scene2.addItem(pixItem)   
        return scene2
  
    def yuzde(self):
        deger=self.horizontalSlider.value()
        self.label.setText(str(deger))
        img=cv2.imread('at.png',0)
        skel=np.zeros(img.shape,np.uint8) #  (0 - 255)- uint8 , img.shape - sutun, satır ve kanal sayısı ,  np.zeros 562 tene
        blur= cv2.GaussianBlur(img,(5,5),0)
        ret,thrs=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #gürültü temizleyerek ikilik çevirir
        inv=cv2.bitwise_not(thrs)
        element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        done = True
        say=0
        while(done):
            eroded = cv2.erode(inv,element)
            temp = cv2.dilate(eroded,element)
            temp = cv2.subtract(inv,temp)
            skel = cv2.bitwise_or(skel,temp)
            inv = eroded.copy()
            if say==int(self.horizontalSlider.value()):
                cv2.imwrite('./skel.png',skel)
                w2,h2=self.graphicsView2.width()-5,self.graphicsView2.height()-5
                self.graphicsView2.setScene(self.show_image('./skel.png',w2,h2))
                done = False
            say=say+1
       
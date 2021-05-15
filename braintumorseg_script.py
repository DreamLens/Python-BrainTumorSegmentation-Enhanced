
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'es.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import numpy as np
global a
import glob, os, os.path
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900,600)
        MainWindow.setStyleSheet("background-color: #005bea;")
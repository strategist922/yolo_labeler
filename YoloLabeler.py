import sys
import os
import pickle

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from YLSideBar import YLSideBar
from YLQLabel import YLQLabel

class YoloLabeler(QMainWindow):
    
  def __init__(self, img_dir):
    super().__init__()
    self.title = 'YOLO Labeler'
    self.width = 1000
    self.height = 1000
    self.images = []
    self.img_dir = img_dir
    self.img_index = 0
    self.labels = {}
    self.img_box = YLQLabel(self)

    self.loadLabels()
    self.initUI()        

  def loadLabels(self):
    labels_path = self.img_dir + '/labels.p'
    if os.path.exists(labels_path):
      self.labels = pickle.load(open(labels_path, 'rb'))
      self.images = list(self.labels.keys())
    else:
      for root, dirs, files in os.walk(self.img_dir):  
        for filename in files:
          if filename.endswith('.jpg'):
            self.images.append(filename)
            self.labels[filename] = {'class': '', 'anchor_box': '', 'bc': '', 'bul': '', 'blr': ''}


  def positionWindow(self):
    self.resize(self.width, self.height)
    fg = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    fg.moveCenter(cp)
    self.move(fg.topLeft())

  def addCentralWidget(self):
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    self.central_widget = central_widget 

    # Create grid layout for central widget
    grid = QGridLayout()
    grid.setColumnStretch(0, 1)
    grid.setColumnStretch(1, 5)

    central_widget.setLayout(grid)
    central_widget.grid = grid

  def setTitle(self):
    self.setWindowTitle(self.title)

  def initUI(self):      
    self.positionWindow()
    self.addCentralWidget()
    self.setTitle()
    self.createMenuBar() 
    self.createYLSideBar()
    self.createYLImageContainer()
    self.show()
     
  def createMenuBar(self):
    menubar = self.menuBar()
    menubar.setNativeMenuBar(False)
    menubar.setStyleSheet("""
      QMenuBar {
          background-color: rgb(49,49,49);
          color: rgb(255,255,255);
          border: 1px solid ;
      }

      QMenuBar::item {
          background-color: rgb(49,49,49);
          color: rgb(255,255,255);
      }

      QMenuBar::item::selected {
          background-color: rgb(30,30,30);
      }
      """) 
    fileMenu = menubar.addMenu('File')
      
    impMenu = QMenu('Import', self)
    impAct = QAction('Import mail', self) 
    impMenu.addAction(impAct)
      
    newAct = QAction('New', self)        
      
    fileMenu.addAction(newAct)
    fileMenu.addMenu(impMenu)

  def createYLSideBar(self):
    self.side_bar = YLSideBar(self)
    self.central_widget.grid.addWidget(self.side_bar, 0, 0, 10, 1)

  def createYLImageContainer(self):
    image_container = QWidget()
    image_container.setStyleSheet("""
      QWidget {
          background-color: rgb(49,49,49);
          color: rgb(255,255,255);
          border: 1px solid ;
      }
      """) 
    grid = QGridLayout()
    image_container.grid = grid
    image_container.setLayout(grid)
    full_path = "{}/{}".format(self.img_dir,self.images[0])
    pixmap = QPixmap(full_path)
    self.img_box.setPixmap(pixmap)
    self.img_box.resize(pixmap.width(),pixmap.height())

    grid.addWidget(self.img_box, 0, 0, Qt.AlignTop)

    self.central_widget.grid.addWidget(image_container, 0, 1, 10, 1)


  def closeEvent(self, event):
    pickle.dump(self.labels, open(self.img_dir + '/labels.p', 'wb'))

import sys
import os
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from YLImageNavButton import YLImageNavButton
from YLQLineEdit import YLQLineEdit

class YLSideBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    self.img_index = 0
    self.highlighted_field = None
    self.initUI()

  def initUI(self):
    self.createLayout()
    self.createImageNav()
    self.createLabelFields()

  def createLayout(self):
    self.grid = QGridLayout()
    self.setLayout(self.grid)

  def createImageNav(self):
    prev_button = YLImageNavButton(self, 'Previous Image')
    next_button = YLImageNavButton(self, 'Next Image')
    prev_button.clicked.connect(prev_button.buttonClicked)  
    next_button.clicked.connect(next_button.buttonClicked)  
    self.grid.addWidget(prev_button, 0, 0)
    self.grid.addWidget(next_button, 1, 0)

  def createLabelFields(self):
    items = [] 

    class_label = QLabel('Class Number')
    class_field = YLQLineEdit(self)
    self.class_field = class_field
    items.append(class_label)
    items.append(class_field)

    anchor_box_label = QLabel('Anchor Box Number')
    anchor_box_field = YLQLineEdit(self)
    self.anchor_box_field = anchor_box_field
    items.append(anchor_box_label)
    items.append(anchor_box_field)

    bc_label = QLabel('Box Center (x,y)')
    bc_field = YLQLineEdit(self) 
    self.bc_field = bc_field
    items.append(bc_label)
    items.append(bc_field)

    bul_label = QLabel('Box Upper Left Corner (x,y)')
    bul_field = YLQLineEdit(self) 
    self.bul_field = bul_field
    items.append(bul_label)
    items.append(bul_field)

    blr_label = QLabel('Box Lower Right Corner (x,y)')
    blr_field = YLQLineEdit(self)
    self.blr_field = blr_field
    items.append(blr_label)
    items.append(blr_field)

    index = 2
    for item in items:
      self.grid.addWidget(item, index, 0, 1, 1)
      index += 1

    self.grid.addWidget(QLabel(''), index, 0, 10, 1)
    self.updateFieldValues()

  def updateFieldValues(self):
    current_img = self.window().images[self.img_index]
    current_img_labels = self.window().labels[current_img]

    self.class_field.setText(current_img_labels['class'])
    self.anchor_box_field.setText(current_img_labels['anchor_box'])
    self.bc_field.setText(current_img_labels['bc'])
    self.bul_field.setText(current_img_labels['bul'])
    self.blr_field.setText(current_img_labels['blr'])

  def saveFieldValues(self):
    current_img = self.window().images[self.img_index]
    current_img_labels = self.window().labels[current_img]

    current_img_labels['class'] = self.class_field.text()
    current_img_labels['anchor_box'] = self.anchor_box_field.text()
    current_img_labels['bc'] = self.bc_field.text()
    current_img_labels['bul'] = self.bul_field.text()
    current_img_labels['blr'] = self.blr_field.text()
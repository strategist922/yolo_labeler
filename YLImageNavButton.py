import sys
import os
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class YLImageNavButton(QPushButton):
  def __init__(self, parent, label):
    super().__init__(parent)
    self.parent = parent
    self.setText(label)

  def buttonClicked(self):   
    self.parent.saveFieldValues()
    if self.text() == 'Previous Image':
      self.parent.img_index -= 1
    else:
      self.parent.img_index += 1

    filename = self.window().images[self.parent.img_index]
    self.parent.updateFieldValues()
    img_dir = self.window().img_dir
    pixmap = QPixmap("{}/{}".format(img_dir,filename))
    self.window().img_box.setPixmap(pixmap)
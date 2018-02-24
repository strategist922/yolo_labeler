import sys
import os
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class YLQLabel(QLabel):
  def __init__(self, parent):
    super().__init__(parent)

  clicked = pyqtSignal()
  rightClicked = pyqtSignal()

  def mousePressEvent(self, e):
    x = e.x()
    y = e.y()
    text = "{},{}".format(x,y)
    self.window().side_bar.highlighted_field.setText(text)
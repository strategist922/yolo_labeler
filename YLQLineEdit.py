import sys
import os
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class YLQLineEdit(QLineEdit):
  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent

  def focusInEvent(self, e):
    self.parent.highlighted_field = self
#! /usr/bin/env python

import sys
from PyQt5.QtWidgets import *
from YoloLabeler import YoloLabeler
        
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = YoloLabeler(sys.argv[1])
  sys.exit(app.exec_())
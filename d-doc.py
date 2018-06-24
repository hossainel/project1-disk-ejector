# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:26:09 2018

@author: M Safayet El Hossain
"""

import sys
from PyQt5.QtWidgets import QApplication

from basket import Window

app = QApplication(sys.argv)

QApplication.setQuitOnLastWindowClosed(False)

window = Window()
window.show()
sys.exit(app.exec_())

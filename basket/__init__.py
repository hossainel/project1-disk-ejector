#Main class goes here

import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QDialog,  QGroupBox, QHBoxLayout,
                             QLabel, QMessageBox, QMenu, QPushButton, QSpinBox , QSystemTrayIcon, QVBoxLayout)

from basket.cd import CD as cd

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.data()
        self.CDTrayTimeSetBox()
        self.CDTrayCommand()
#        self.USBcommand()

        self.Actions()
        self.TrayIcon()

        self.showIconCheckBox.toggled.connect(self.trayIcon.setVisible)
        self.trayIcon.activated.connect(self.iconActivated)

        mainLayout = QVBoxLayout() #one down after one
        #layout to add
        mainLayout.addWidget(self.cdGroupBox)
#        mainLayout.addWidget(self.usbGroupBox)
        mainLayout.addWidget(self.commandGroupBox)
        self.setLayout(mainLayout)

        icon = QIcon('icon.png')
        self.trayIcon.setIcon(icon)
        self.trayIcon.show()

        self.setWindowTitle("D-Doc")
        self.setWindowIcon(icon)
        self.resize(300, 150)

    def closeEvent(self, event):
        self.hide()

    def data(self):
        fob = open('a.dd', 'r')
        self.t = int(fob.readline())

    def task(self):
        self.data()
        cd(self.t)

    def updater(self):
        x = self.durationSpinBox.value()
        fob = open('a.dd', 'w')
        fob.write(str(x))
        self.t = x


    def CDTrayTimeSetBox(self):
        self.cdGroupBox = QGroupBox("CD Tray Time settings:")
        self.durationLabel = QLabel("Open Duration:")

        self.durationSpinBox = QSpinBox()
        self.durationSpinBox.setRange(3, 30)
        self.durationSpinBox.setSuffix(" s")
        self.durationSpinBox.setValue(self.t)

        self.updateButton = QPushButton("Set")
        self.updateButton.clicked.connect(self.updater)

        self.showIconCheckBox = QCheckBox("Show icon")
        self.showIconCheckBox.setChecked(True)

        iconLayout = QHBoxLayout()
        iconLayout.addWidget(self.durationLabel)
        iconLayout.addWidget(self.durationSpinBox)
        iconLayout.addWidget(self.updateButton)
        iconLayout.addStretch()
        iconLayout.addWidget(self.showIconCheckBox)

        self.cdGroupBox.setLayout(iconLayout)

    def aboutApp(self):
        QMessageBox.about(self, 'About D-Doc', "<h3>D-Doc</h3> D-Doc is an drive handling assistant. \
                          It usually used to open and then close CD drive automatically.\
                          We hope you will give us some more ideas to use it with\na batter \
                          way. <br>It's open for you all to use. For anything else, \
                          you can connect with us through \
                          <strong><a href='alzestors.site123.me'>Alzestors</a></strong>.")

    def helpFun(self):
        os.system("start help/index.html")

    def CDTrayCommand(self):
        self.commandGroupBox = QGroupBox("CD Tray Commands:")

        self.CDOpenButton = QPushButton("Open CD ROM")
        self.helpButton = QPushButton("Help")
        self.aboutButton = QPushButton("About")

        self.aboutButton.clicked.connect(self.aboutApp)
        self.helpButton.clicked.connect(self.helpFun)
        self.CDOpenButton.clicked.connect(self.task)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.CDOpenButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.helpButton)
        buttonLayout.addWidget(self.aboutButton)

        self.commandGroupBox.setLayout(buttonLayout)

#    def USBcommand(self):
#        self.usbGroupBox = QGroupBox("USB options:")
#
#        usbtitleLabel = QLabel("Passoword:")
#        self.usbtitleEdit = QLineEdit("")
#        self.usbtitleEdit.setPlaceholderText("USB insertion will require this passowrd")
#        self.usbCBox = QCheckBox("Active Password")
#        self.usbCBox.setChecked(True)
#
#        usbLayout = QHBoxLayout()
#        usbLayout.addWidget(usbtitleLabel)
#        usbLayout.addWidget(self.usbtitleEdit)
#        usbLayout.addStretch()
#        usbLayout.addWidget(self.usbCBox)
#        self.usbGroupBox.setLayout(usbLayout)

    def Actions(self):
        self.minimizeAction = QAction("Clo&se", self, triggered=self.hide)
        self.maximizeAction = QAction("Con&figure", self,
                triggered=self.showNormal)
        self.restoreAction = QAction("&About", self,
                triggered=self.aboutApp)
        self.quitAction = QAction("&Quit", self,
                triggered=QApplication.instance().quit)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.task()

    def TrayIcon(self):
         self.trayIconMenu = QMenu(self)
         self.trayIconMenu.addAction(self.minimizeAction)
         self.trayIconMenu.addAction(self.maximizeAction)
         self.trayIconMenu.addAction(self.restoreAction)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.addAction(self.quitAction)

         self.trayIcon = QSystemTrayIcon(self)
         self.trayIcon.setContextMenu(self.trayIconMenu)

    def visiblity(self, visible):
        super(Window, self).visiblity(visible)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dictionary.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dictionary = QtWidgets.QListView(self.centralwidget)
        self.dictionary.setGeometry(QtCore.QRect(410, 50, 171, 321))
        self.dictionary.setObjectName("dictionary")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 371, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input = QtWidgets.QLineEdit(self.layoutWidget)
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.search = QtWidgets.QPushButton(self.layoutWidget)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 371, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.output = QtWidgets.QLabel(self.gridLayoutWidget)
        self.output.setText("")
        self.output.setStyleSheet("background-color: white;")
        self.output.setAlignment(Qt.AlignTop)
        self.output.setMargin(8)
        self.output.setWordWrap(True)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 22))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.helpContent = QtWidgets.QAction(MainWindow)
        self.helpContent.setObjectName("helpContent")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.file.addAction(self.exit)
        self.help.addAction(self.helpContent)
        self.help.addAction(self.about)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bangla Dictionary"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.file.setTitle(_translate("MainWindow", "File"))
        self.help.setTitle(_translate("MainWindow", "Help"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.helpContent.setText(_translate("MainWindow", "Help"))
        self.about.setText(_translate("MainWindow", "About"))


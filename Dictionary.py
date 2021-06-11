import os
import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox
from DictionaryUI import Ui_MainWindow

dic = {}

path = os.getcwd() + "/dict"
dirList = sorted(os.listdir(path))

for x in dirList:
	listOfFiles = list()
	dirName = path + "/" + x
	for (dirpath, dirnames, filenames) in os.walk(dirName):
		listOfFiles += [os.path.join(dirpath, file) for file in filenames]
		file = sorted(filenames)
		fileDir = sorted(listOfFiles)
		for i in range(len(file)):
			dic[file[i].lower()] = fileDir[i]

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.setFixedSize(601, 420)
		self.ui.setupUi(self)
		self.ui.search.clicked.connect(self.btnClicked)
		self.ui.exit.triggered.connect(self.btnExit)
		self.ui.help.triggered.connect(self.btnHelp)
		self.ui.about.triggered.connect(self.btnAbout)

	def btnClicked(self):
		word = self.ui.input.text().lower()
		if word in dic:
			with Image.open(dic[word]) as img:
				qimage = ImageQt(img)
				pixmap = QtGui.QPixmap.fromImage(qimage)
				self.ui.output.setPixmap(pixmap)

	def btnExit(self):
		sys.exit(0)

	def btnHelp(self):
		hBox = QMessageBox()
		hBox.setText("Input Word \nAnd\n Click Search Button")
		hBox.setStandardButtons(QMessageBox.Ok)
		hBox.exec_()

	def btnAbout(self):
		aBox = QMessageBox()
		aBox.setText("Abdullah Al Mamun")
		aBox.setStandardButtons(QMessageBox.Ok)
		aBox.exec_()

app = QtWidgets.QApplication([])
# app_icon = QtGui.QIcon(os.getcwd()+"/icon.png")
# app.setWindowIcon(app_icon)
app.setWindowIcon(QtGui.QIcon('icon.png'))
application = mywindow()
application.show()
sys.exit(app.exec())
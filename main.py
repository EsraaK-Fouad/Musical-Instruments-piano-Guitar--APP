# ****************************************Libraries*****************************************************************#
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from UI import Ui_Musical_Instruments
from Guitar_Piano import CreateChord , CreateFretNote, piano_key
from threading import Thread
#*********************************************************** Basic constant ********************************************#
"""                                                          Guitar                                                   """



Guitar_dict={"noteE": 105,"noteA": 110, "noteD": 115,"noteG":120,"noteB":124 ,"noteE2":129,"C_major":[0 ,3 ,2 , 0 , 1 , 0],"G_major":[3, 2 , 0 , 0 , 0 ,3]
,"E_minor":[0 , 2  ,2 ,0 ,0 , 0],"A_minor":[0 , 0, 2 , 3 , 1 ,0]}



"""                                                             Piano                                                   """



Piano_dict={"B":493.8833 , "A":440 , "G":391.995,"F":349.2282,"E":329.6276 ,"D":293.6648,"C":261.6256 ,"E2":659 ,"C5":523 ,"D2":587}


# ********************************************************** codee implemented ****************************************#

class MainWindowUI(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.UI=Ui_Musical_Instruments()
		self.th={}
		self.UI.setupUi(self)
		self.fret=self.UI.combo.currentIndex()
		
		self.i=0
		while self.i < 10 :
			self.UI.btnArray[self.i].clicked.connect(self.run_thread)
			self.UI.btnArray2[self.i].clicked.connect(self.run_threads)
			self.i+=1
		

		
#*************************************************************
	def play_Guitar_notes(self,string):
		
		if (string == "E_minor" or string == "A_minor" or string == "G_major" or string == "C_major" ):
			
			CreateChord(Guitar_dict[string])
		else :
			CreateFretNote(Guitar_dict[string], self.fret) 
			
#*********************************************************
	def play_Piano_notes(self,string):

		piano_key(Piano_dict[string])

#**********************************************************
	def run_threads(self):
		self.th[self.sender().objectName()] = Thread(target = self.play_Piano_notes, args = ("{}".format(self.sender().objectName()),)) 
		self.th[self.sender().objectName()].start()
		self.th[self.sender().objectName()].join()
	def run_thread(self):
		self.th[self.sender().objectName()] = Thread(target = self.play_Guitar_notes, args = ("{}".format(self.sender().objectName()),)) 
		self.th[self.sender().objectName()].start()
		self.th[self.sender().objectName()].join()	

# ========================================Execute code===============================================================================
def main():
	app = QtWidgets.QApplication(sys.argv)
	application =MainWindowUI()
	application .show()
	app.exec_()


if __name__ == '__main__':
	main()

import sys, os
from PyQt5 import QtCore, QtWidgets
import subprocess

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        buttonReply = QtWidgets.QMessageBox.question(self, 'Download from server', "update?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            self._update()
        else:
            self.close()

    def _update(self):
        # comand = 'pip install git+https://github.com/lgm8/update.git#egg=update'
        stash ='git stash'
        comand = 'git pull --rebase'
        popStash = 'git stash pop'
        os.system(stash)
        os.system(comand)
        os.system(popStash)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit( app.exec_() )
#!/usr/bin/env python

import os
import sys
from functools import partial
from PyQt4 import QtGui
from PyQt4 import QtCore

class SpinUI(QtGui.QWidget):

    def __init__(self):
        super(SpinUI, self).__init__()
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setWindowTitle('Spin Settings')
        
        self.ui()

    def ui(self):

        layout = QtGui.QHBoxLayout(self)

        for o in [ 'normal', 'inverted', 'left', 'right' ]:
            button = QtGui.QPushButton('', self)
            button.clicked.connect( partial( self.set_orientation, o))
            button.setIcon(QtGui.QIcon('/home/ragnar/Code/spin/{0}.png'.format(o)))
            button.setIconSize(QtCore.QSize(128,128))
            button.setAutoFillBackground(False)
            layout.addWidget(button)

        self.show()

    def buttonClicked(self):
        print("OTHER")

    def set_orientation(self, orientation="Why NOT"):
        try:
            conf_dir = os.getenv('XDG_CONFIG_HOME', "{home}/.config/".format(home = os.environ['HOME']))
            settings_path = os.path.join(conf_dir, 'spin')
            settings = open(settings_path, 'w')
            settings.write(orientation)
            settings.close()
        except IOError:
            print("Something went wrong")
        print(orientation)
        self.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    spinui =SpinUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
                        



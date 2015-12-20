#!/usr/bin/env python

import os
import sys
import socket
from functools import partial
from PyQt4 import QtGui
from PyQt4 import QtCore

class SpinUI(QtGui.QWidget):

    UI_SOCKET = "/tmp/yoga_spin.socket"

    def __init__(self):
        super(SpinUI, self).__init__()
        self.connect_to_socket()
        self.ui()


    def connect_to_socket(self):
        if os.path.exists(self.UI_SOCKET):
            self.ui_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
            try:
                self.ui_socket.connect(self.UI_SOCKET)
            except:
                print("Failed to connect to the socket")
            print("Ready")
            #self.ui_socket.close()

        
    def ui(self):
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setWindowTitle('Spin Settings')
        layout = QtGui.QHBoxLayout(self)
        for o in [ 'normal', 'inverted', 'left', 'right' ]:
            button = QtGui.QPushButton('', self)
            button.clicked.connect( partial( self.set_orientation, o))
            button.setIcon(QtGui.QIcon('/home/ragnar/Code/spin/{0}.png'.format(o)))
            button.setIconSize(QtCore.QSize(128,128))
            button.setAutoFillBackground(False)
            layout.addWidget(button)

        self.show()


    def set_orientation(self, orientation="Why NOT"):
        try:
            conf_dir = os.getenv('XDG_CONFIG_HOME', "{home}/.config/".format(home = os.environ['HOME']))
            settings_path = os.path.join(conf_dir, 'spin')
            settings = open(settings_path, 'w')
            settings.write(orientation)
            try:
                self.ui_socket.send( orientation )
            except:
                pass
            settings.close()
        except IOError:
            print("Something went wrong")
        self.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    spinui =SpinUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
                        



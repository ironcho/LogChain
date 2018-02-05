import time, threading, queue, datetime
import os
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import QListWidgetItem

monitoring_queue = queue.Queue()

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("monitoring" + os.sep +"monitoring.ui")
        #self.ui.setWindowFlags(Qt.SplashScreen)                            윈도우 타이틀 없애기

        queue_thread = threading.Thread(target=self.read_queue)
        queue_thread.daemon = True
        queue_thread.start()

        self.ui.show()

    def change_status_text(self, message):
        self.ui.label_7.setText(""+message)

    def add_log_item(self,log):
        item = QListWidgetItem(log)
        self.ui.listWidget.addItem(item)

    def add_block_item(self,log):
        item = QListWidgetItem(log)
        self.ui.listWidget_3.addItem(item)

    def add_transaction_item(self,log):
        item = QListWidgetItem(log)
        self.ui.listWidget_2.addItem(item)

    def change_frame_color(self, r, g, b):
        stylesheet = "background-color: rgb({0}, {1}, {2})".format(r,g,b)
        widget_list = [self.ui.widget,self.ui.widget_2,self.ui.widget_3,self.ui.widget_4,self.ui.widget_5]
        
        for widget in widget_list:
            widget.setStyleSheet(stylesheet)
            # widget.setAutoFillBackground(True)
            # pt = widget.palette()
            # pt.setColor(widget.backgroundRole(),QColor(r,g,b))
            # widget.setPalette(pt)
            # print(p.name(), widget.autoFillBackground(), widget.updatesEnabled())

        # stylesheet = "background-color: rgb({0}, {1}, {2})".format(r,g,b)
        # print(stylesheet)
        # self.ui.widget.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_2.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_3.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_4.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_5.setStyleSheet(stylesheet)
        # print(stylesheet)

    def add_queue_data(self,data):
        monitoring_queue.put(data)

    def read_queue(self):
        while True:
            self.change_status_text('Server Status : NOMAL            ' + time.strftime('%H:' + '%M:' + '%S'))
            if(monitoring_queue.qsize() > 0):
                datas = monitoring_queue.get()
                
                data = datas.split('.')

                if data[0] == 'log':
                    self.add_log_item(data[1])
                    self.change_frame_color(44, 132, 238)
                elif data[0] == 'block':
                    self.add_block_item(data[1])
                    self.change_frame_color(231,76,60)
                elif data[0] == 'transaction':
                    self.add_transaction_item(data[1])
                    self.change_frame_color(241, 196, 15)
            time.sleep(1)
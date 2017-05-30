# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multi_tab.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import sys
import types
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(298, 40, 161, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        dict2 = { 'path1' : 'A', 'path2' : 'B', 'path3' : 'C'}
        tree = {'root': {
                    "1": [dict2['path1'], dict2['path2'], dict2['path3']],
                    "2": {
                        "2-1": ["G", "H", "I"],
                        "2-2": ["J", "K", "L"]},
                    "3": ["D", "E", "F"]}
        }
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 20, 181, 451))
        self.treeView.setObjectName("treeView")
        root_model = QStandardItemModel()
        self.treeView.setModel(root_model)
        self._populateTree(tree, root_model.invisibleRootItem())
        self.treeView.doubleClicked.connect(self.treeMedia_doubleClicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

    def _populateTree(self, children, parent):
        for child in sorted(children):
            child_item = QStandardItem(child)
            child_item.setEditable(False)
            parent.appendRow(child_item)
            if isinstance(children, dict):
                self._populateTree(children[child], child_item)

    def treeMedia_doubleClicked(self,index):
        item = self.treeView.selectedIndexes()[0]
        #print(item.model().itemFromIndex(index).text())
        s = item.model().itemFromIndex(index).text()
        #print(type(item.model().itemFromIndex(index).text()))
        if s:
            tab = QtWidgets.QWidget()
            self.tabWidget.addTab(tab, 'hello')
            tablayout = QtWidgets   .QGridLayout(tab)
            self.tabWidget.setLayout(tablayout)

    def closeTab(self, currentIndex):
        self.tabWidget.removeTab(currentIndex)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

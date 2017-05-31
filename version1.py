# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import fnmatch
import pyqtgraph as pg
import pandas as pd
import numpy as np

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


class ConsoleWidget(RichJupyterWidget):


    def __init__(self, customBanner=None, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        if customBanner is not None:
            self.banner = customBanner

        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt().exit()

        self.exit_requested.connect(stop)

    def push_vars(self, variableDict):
        """
        Given a dictionary containing name / value pairs, push those variables
        to the Jupyter console widget
        """
        self.kernel_manager.kernel.shell.push(variableDict)

    def clear(self):
        """
        Clears the terminal
        """
        self._control.clear()

        # self.kernel_manager

    def print_text(self, text):
        """
        Prints some plain text to the console
        """
        self._append_plain_text(text)

    def execute_command(self, command):
        """
        Execute a command in the frame of the console widget
        """
        self._execute(command, False)


class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.ExistingFiles)
        btns = self.findChildren(QtWidgets.QPushButton)
        self.openBtn = [x for x in btns if 'open' in str(x.text()).lower()][0]
        self.openBtn.clicked.disconnect()
        self.openBtn.clicked.connect(self.openClicked)
        self.tree = self.findChild(QtWidgets.QTreeView)

    def openClicked(self):
        inds = self.tree.selectionModel().selectedIndexes()
        files = []
        for i in inds:
            if i.column() == 0:
                files.append(os.path.join(str(self.directory().absolutePath()),str(i.data())))
                # print(str(i.data().toString()))
        self.selectedFiles = files
        # print(files)
        matches= []
        for f in files:
            for root, dirnames, filenames in os.walk(f):
                for filename in fnmatch.filter(filenames, '*.csv'):
                    matches.append(os.path.join(root, filename))
        # print(matches)
        self.hide()

    def filesSelected(self):
        return self.selectedFiles


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 749)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setMinimumSize(QtCore.QSize(198, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(198, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.header().setVisible(True)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleButton)
        self.verticalLayout_4.addWidget(self.pushButton)
        self.treeView = QtWidgets.QTreeView(self.widget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_4.addWidget(self.treeView)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.mdiArea = QtWidgets.QMdiArea(self.layoutWidget)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout_3.addWidget(self.mdiArea)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        widget = ConsoleWidget()
        self.verticalLayout.addWidget(widget)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_2.addWidget(self.textBrowser_2)
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/cut.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../.designer/backup/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../.designer/backup/paste.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon2)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../.designer/backup/Find.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon3)
        self.actionFind.setObjectName("actionFind")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../.designer/backup/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon4)
        self.actionDelete.setObjectName("actionDelete")
        self.actionClip = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../.designer/backup/clip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClip.setIcon(icon5)
        self.actionClip.setObjectName("actionClip")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../.designer/backup/plot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon6)
        self.actionPlot.setObjectName("actionPlot")
        self.actionLine_Plot = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../.designer/backup/line_plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLine_Plot.setIcon(icon7)
        self.actionLine_Plot.setObjectName("actionLine_Plot")
        self.actionGrid_Plot = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../.designer/backup/grid plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGrid_Plot.setIcon(icon8)
        self.actionGrid_Plot.setObjectName("actionGrid_Plot")
        self.actionMagnify = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../.designer/backup/zoom in.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMagnify.setIcon(icon9)
        self.actionMagnify.setObjectName("actionMagnify")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../.designer/backup/zoom out.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon10)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionDrag = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../../.designer/backup/Drag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDrag.setIcon(icon11)
        self.actionDrag.setObjectName("actionDrag")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar_2.addAction(self.actionPlot)
        self.toolBar_2.addAction(self.actionLine_Plot)
        self.toolBar_2.addAction(self.actionGrid_Plot)
        self.toolBar_2.addAction(self.actionMagnify)
        self.toolBar_2.addAction(self.actionZoom_Out)
        self.toolBar_2.addAction(self.actionDrag)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionClip)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handleButton(self):
        global fileList
        dialog = FileDialog()
        dialog.setNameFilters(["CSV files (*.csv)", "Images (*.png *.jpg)"])
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            print(dialog.selectedFiles) 
        l= []
        l = dialog.filesSelected()
        for i in range(0,len(l)):
            df= pd.read_csv(l[i])
            df = df.as_matrix()
            # p1.plot(df[:,1],df[:,2])
        # print(l)
        fileList = l
        # self.fileList
        print(fileList)
        win = pg.GraphicsWindow("testing ")
        p = win.addPlot()
        # plotWidget = pg.plot(title=" ")
        if fileList:
            df = pd.read_csv(fileList[0])
            df= df.as_matrix()
            p.plot(df[:,1], df[:,2], pen=(255,255,0))
        # self.sub = win
        self.mdiArea.addSubWindow(win)
        win.show()
        self.mdiArea.tileSubWindows()    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Module Tree"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Main Module #1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Display"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Analysis"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Processing"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Road Data Analysis #2"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Sub Module #1"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Sub module #2"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Data Files"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.label_4.setText(_translate("MainWindow", "Plot Area"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "4"))
        self.label.setText(_translate("MainWindow", "Python Interpreter"))
        self.label_2.setText(_translate("MainWindow", "Visual Aid"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setToolTip(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "Paste"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setToolTip(_translate("MainWindow", "Find"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setToolTip(_translate("MainWindow", "Delete"))
        self.actionClip.setText(_translate("MainWindow", "Clip"))
        self.actionClip.setToolTip(_translate("MainWindow", "Clip"))
        self.actionPlot.setText(_translate("MainWindow", "Plot"))
        self.actionPlot.setToolTip(_translate("MainWindow", "Plot "))
        self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot"))
        self.actionLine_Plot.setToolTip(_translate("MainWindow", "Line Plot"))
        self.actionGrid_Plot.setText(_translate("MainWindow", "Grid Plot"))
        self.actionGrid_Plot.setToolTip(_translate("MainWindow", "Grid Plot"))
        self.actionMagnify.setText(_translate("MainWindow", "Magnify"))
        self.actionMagnify.setToolTip(_translate("MainWindow", "Magnify Image"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setToolTip(_translate("MainWindow", "Zoom Out"))
        self.actionDrag.setText(_translate("MainWindow", "Drag"))
        self.actionDrag.setToolTip(_translate("MainWindow", "Drag"))


if __name__ == "__main__":
    import sys
    global fileList
    fileList = []
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


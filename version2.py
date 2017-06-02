# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import fnmatch
import sys
import types
import pyqtgraph as pg
import pandas as pd
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager

def scan_dir(dir):
    fDict={}
    fList = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            p = path.split('/')[-1]
            if p.split('.')[-1] == 'csv':
                df = pd.read_csv(path)
                fList = list(df)
                fDict[path] = fList
        else:
            fileDict = {}
            fileDict = scan_dir(path)
            if bool(fileDict):
                fDict[path] = fileDict
    return fDict

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
        # print(files)
        for f in files:
            if os.path.isfile(f):
                matches = []
                df = pd.read_csv(f)
                matches =list(df)
                dict2[f] = matches
            else:
                temp_dict = scan_dir(f)
                if bool(temp_dict):
                    dict2[f] = temp_dict
        matches =[]
        for f in files:
            if os.path.isfile(f):
                matches.append(f)        
            for root, dirnames, filenames in os.walk(f):
                for filename in fnmatch.filter(filenames, '*.csv'):
                    matches.append(os.path.join(root, filename))
        self.selectedFiles = matches 
        # print(matches)       
        # print(dict2)
        self.hide()

    def filesSelected(self):
        return self.selectedFiles

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.ModuleTree = QtWidgets.QDockWidget(MainWindow)
        self.ModuleTree.setObjectName("ModuleTree")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_4.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.ModuleTree.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.ModuleTree)
        self.PythonInterpreter = QtWidgets.QDockWidget("Python Interpreter",MainWindow)
        self.PythonInterpreter.setObjectName("PythonInterpreter")
        self.dockWidgetContents_2 = ConsoleWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # self.listView = QtWidgets.QListView(self.dockWidgetContents_2)
        # self.listView.setObjectName("listView")
        # self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 1)
        self.PythonInterpreter.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.PythonInterpreter)
        self.VisualAid = QtWidgets.QDockWidget(MainWindow)
        self.VisualAid.setObjectName("VisualAid")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.VisualAid.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.VisualAid)
        self.WindowName = QtWidgets.QDockWidget(MainWindow)
        self.WindowName.setObjectName("WindowName")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listView_2 = QtWidgets.QListView(self.dockWidgetContents_4)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_6.addWidget(self.listView_2, 0, 0, 1, 1)
        self.WindowName.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.WindowName)
        self.DataFiles = QtWidgets.QDockWidget(MainWindow)
        self.DataFiles.setObjectName("DataFiles")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleOpenButton)
        self.verticalLayout.addWidget(self.pushButton)
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents_5)
        self.treeView.setObjectName("treeView")
        self.root_model = QStandardItemModel()
        nameList =['File Structure']
        self.root_model.setHorizontalHeaderLabels(nameList)
        self.treeView.setModel(self.root_model)
        self.verticalLayout.addWidget(self.treeView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.DataFiles.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.DataFiles)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_6 = QtWidgets.QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.dockWidgetContents_6)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mdiArea = QtWidgets.QMdiArea(self.page)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_5.addWidget(self.mdiArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_7 = QtWidgets.QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents_7)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_7)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_8.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Intern/images/cut.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Intern/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Intern/images/paste.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon2)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Intern/images/Find.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon3)
        self.actionFind.setObjectName("actionFind")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Intern/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon4)
        self.actionDelete.setObjectName("actionDelete")
        self.actionClip = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Intern/images/clip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClip.setIcon(icon5)
        self.actionClip.setObjectName("actionClip")
        self.actionPlot = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../Intern/images/plot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon6)
        self.actionPlot.setObjectName("actionPlot")
        self.actionLine_Plot = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../Intern/images/line_plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLine_Plot.setIcon(icon7)
        self.actionLine_Plot.setObjectName("actionLine_Plot")
        self.actionGrid_Plot = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../Intern/images/grid plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGrid_Plot.setIcon(icon8)
        self.actionGrid_Plot.setObjectName("actionGrid_Plot")
        self.actionMagnify = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../Intern/images/zoom in.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMagnify.setIcon(icon9)
        self.actionMagnify.setObjectName("actionMagnify")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../Intern/images/zoom out.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon10)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionDrag = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../../Intern/images/Drag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDrag.setIcon(icon11)
        self.actionDrag.setObjectName("actionDrag")
        self.actionPython_Interpreter = QtWidgets.QAction(MainWindow)
        self.actionPython_Interpreter.setCheckable(True)
        self.actionPython_Interpreter.setChecked(True)
        self.actionPython_Interpreter.setObjectName("actionPython_Interpreter")
        self.actionVisual_Aid = QtWidgets.QAction(MainWindow)
        self.actionVisual_Aid.setCheckable(True)
        self.actionVisual_Aid.setChecked(True)
        self.actionVisual_Aid.setObjectName("actionVisual_Aid")
        self.actionModule_Tree = QtWidgets.QAction(MainWindow)
        self.actionModule_Tree.setCheckable(True)
        self.actionModule_Tree.setChecked(True)
        self.actionModule_Tree.setObjectName("actionModule_Tree")
        self.actionData_Files = QtWidgets.QAction(MainWindow)
        self.actionData_Files.setCheckable(True)
        self.actionData_Files.setChecked(True)
        self.actionData_Files.setObjectName("actionData_Files")
        self.actionPlot_Area = QtWidgets.QAction(MainWindow)
        self.actionPlot_Area.setCheckable(True)
        self.actionPlot_Area.setChecked(True)
        self.actionPlot_Area.setObjectName("actionPlot_Area")
        self.menuView.addAction(self.actionModule_Tree)
        self.menuView.addAction(self.actionData_Files)
        self.menuView.addAction(self.actionPlot_Area)
        self.menuView.addAction(self.actionPython_Interpreter)
        self.menuView.addAction(self.actionVisual_Aid)
        self.menuView.addSeparator()


        self.actionPython_Interpreter.changed.connect(self.state_changed)
        self.PythonInterpreter.visibilityChanged.connect(self.check_changed)
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
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def state_changed(self):
        if(self.actionPython_Interpreter.isChecked()):
            self.PythonInterpreter.show()
        else:
            self.PythonInterpreter.hide()

    def check_changed(self):
        if(self.PythonInterpreter.isVisible()):
            self.actionPython_Interpreter.setChecked(True)
        else:
            self.actionPython_Interpreter.setChecked(False)

    def handleOpenButton(self):
        global fileList
        dialog = FileDialog()
        dialog.setNameFilters(["CSV files (*.csv)", "Images (*.png *.jpg)"])
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            print(dialog.selectedFiles)

        fileList = dialog.filesSelected()
        # print(fileList)
        # for i in range(0,len(l)):
        #     df= pd.read_csv(l[i])
        #     df = df.as_matrix()
        #     # p1.plot(df[:,1],df[:,2])
        # # print(l)
        
        ## for name in fileList:
        ##     temp_list = []
        ##     temp_list.append(name.split('/')[-1])
        ##     dict2[name.split('/')[-1]] = temp_list
        ## self.fileList
        ## print(fileList)
        ##dict2['Files Directory'] = fileNameList
        win = pg.GraphicsWindow("PlotWindow")
        # plotWidget = pg.plot(title=" ")
        for f in fileList:
            p = win.addPlot()
            df = pd.read_csv(f)
            df= df.as_matrix()
            p.plot(df[:,-1], pen=(255,0,0))
            win.nextRow()
        # # self.sub = win
        self.mdiArea.addSubWindow(win)
        win.show()
        self.mdiArea.tileSubWindows()
        self._populateTree(dict2, self.root_model.invisibleRootItem())
        # print(mapDict)
        dict2.clear()

    def _populateTree(self, children, parent):
        for child in sorted(children):
            # print(type(child))
            mapDict[child.split('/')[-1]] = child
            child_item = QStandardItem(child)
            child_item.setEditable(False)
            child_item.setText(child.split('/')[-1])
            #if (child_item != 'Do not print'):
            parent.appendRow(child_item)
            # print(type(child_item))
            if isinstance(children, dict):
                self._populateTree(children[child], child_item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Module"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Main Module #1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Processing"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Analysis"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Visualization"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Road Data Analysis #2"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Sub Module #1"))
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(0, _translate("MainWindow", "New Subitem"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Sub-Module #2"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "Add Files"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
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
        self.actionPython_Interpreter.setText(_translate("MainWindow", "Python Interpreter"))
        self.actionVisual_Aid.setText(_translate("MainWindow", "Visual Aid"))
        self.actionModule_Tree.setText(_translate("MainWindow", "Module Tree"))
        self.actionData_Files.setText(_translate("MainWindow", "Data Files"))
        self.actionPlot_Area.setText(_translate("MainWindow", "Plot Area"))


if __name__ == "__main__":
    import sys
    global fileList
    fileList = []
    global dict2
    dict2 = {}
    global mapDict
    mapDict = {}
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


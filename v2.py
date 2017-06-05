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

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

##
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
                fList = [s + '-' + path for s in fList]
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
                matches = [s + '-' + f for s in matches]
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
        print(dict2)
        self.hide()

    def filesSelected(self):
        return self.selectedFiles

# #
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.treeView = QtWidgets.QTreeView(self.widget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.listWidgetX = QtWidgets.QListWidget(self.widget1)
        self.listWidgetX.setObjectName("listWidgetX")
        self.verticalLayout_3.addWidget(self.listWidgetX)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.listWidgetY = QtWidgets.QListWidget(self.widget1)
        self.listWidgetY.setObjectName("listWidgetY")
        self.verticalLayout_4.addWidget(self.listWidgetY)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.mdiArea = QtWidgets.QMdiArea(self.splitter)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_11.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 19))
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
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        MainWindow.insertToolBarBreak(self.toolBar_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_10 = QtWidgets.QWidget()
        self.dockWidgetContents_10.setObjectName("dockWidgetContents_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dockWidgetContents_10)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.dockWidgetContents_10)
        self.treeWidget_3.setObjectName("treeWidget_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout_3.addWidget(self.treeWidget_3, 0, 0, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_10)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.PythonInterpreter = QtWidgets.QDockWidget("Python Interpreter",MainWindow)
        self.PythonInterpreter.setObjectName("PythonInterpreter")
        self.dockWidgetContents_11 = ConsoleWidget()
        self.dockWidgetContents_11.setObjectName("dockWidgetContents_11")
        self.PythonInterpreter.setWidget(self.dockWidgetContents_11)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.PythonInterpreter)
        self.dockWidget_5 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_5.setObjectName("dockWidget_5")
        self.dockWidgetContents_12 = QtWidgets.QListWidget()
        self.dockWidgetContents_12.setObjectName("dockWidgetContents_12")
        self.dockWidget_5.setWidget(self.dockWidgetContents_12)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_5)
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
        self.actionPython_Interpreter.setObjectName("actionPython_Interpreter")
        self.actionVisual_Aid = QtWidgets.QAction(MainWindow)
        self.actionVisual_Aid.setCheckable(True)
        self.actionVisual_Aid.setObjectName("actionVisual_Aid")
        self.actionModule_Tree = QtWidgets.QAction(MainWindow)
        self.actionModule_Tree.setCheckable(True)
        self.actionModule_Tree.setObjectName("actionModule_Tree")
        self.actionData_Files = QtWidgets.QAction(MainWindow)
        self.actionData_Files.setCheckable(True)
        self.actionData_Files.setObjectName("actionData_Files")
        self.actionPlot_Area = QtWidgets.QAction(MainWindow)
        self.actionPlot_Area.setCheckable(True)
        self.actionPlot_Area.setObjectName("actionPlot_Area")
        self.menuView.addAction(self.actionModule_Tree)
        self.menuView.addAction(self.actionData_Files)
        self.menuView.addAction(self.actionPlot_Area)
        self.menuView.addAction(self.actionPython_Interpreter)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionVisual_Aid)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionClip)
        self.toolBar.addSeparator()
##
        self.radio1 = QtWidgets.QRadioButton()
        self.toolBar_2.addWidget(self.radio1)
        self.radio1.setIcon(icon6)
        self.radio2 = QtWidgets.QRadioButton()
        self.toolBar_2.addWidget(self.radio2)
        self.radio2.setIcon(icon7)

        self.combo = QtWidgets.QComboBox()
        self.toolBar_2.addWidget(self.combo)
        self.combo.insertItems(1,["1","2","3","4","5","6"])

        self.root_model = QStandardItemModel()
        nameList =['File Structure']
        self.root_model.setHorizontalHeaderLabels(nameList)
        self.treeView.setModel(self.root_model)
        # self.treeWidget_2.setAcceptDrops(True)
        self.actionPython_Interpreter.setChecked(True)
        self.actionVisual_Aid.setChecked(True)
        self.actionModule_Tree.setChecked(True)
        self.actionData_Files.setChecked(True)
        self.actionPlot_Area.setChecked(True)
        self.pushButton_3.clicked.connect(self.handleOpenButton)
        self.pushButton_4.clicked.connect(self.handleSimulate)
        self.pushButton_5.clicked.connect(self.handleNext)
        self.actionPython_Interpreter.changed.connect(self.state_changed)
        self.PythonInterpreter.visibilityChanged.connect(self.check_changed)

        self.treeView.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.treeView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.listWidgetX.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidgetX.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidgetX.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetX.setAcceptDrops(True)

        self.listWidgetY.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidgetY.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidgetY.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetY.setAcceptDrops(True)

        self.Xindex = 0
        self.Yindex = 0

        self.min_val = 0

        # self.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        # self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        # self.setAcceptDrops(True)



##
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def state_changed(self):
        if(self.actionPython_Interpreter.isChecked()):
            self.toolBar_2.show()
            self.PythonInterpreter.show()
        else:
            self.toolBar_2.hide()
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
        print(fileList)
        # if fileList:    
        #     for f in fileList:
        #         p = win.addPlot()
        #         df = pd.read_csv(f)
        #         df= df.as_matrix()
        #         p.plot(df[:,-1], pen=(255,0,0))
        #         win.nextRow()
        # # # self.sub = win
        # self.mdiArea.addSubWindow(win)
        # win.show()
        # self.mdiArea.tileSubWindows()
        self._populateTree(dict2, self.root_model.invisibleRootItem())
        # print(mapDict)
        dict2.clear()

    def handleSimulate(self):
        self.Xindex = 0
        self.Yindex = 0
        w = self.mdiArea.currentSubWindow()
        if w:
            self.mdiArea.removeSubWindow(w)
        win = pg.GraphicsWindow("PlotWindow")
        text = int(self.combo.currentText())
        countX = self.listWidgetX.count()
        countY = self.listWidgetY.count()
        self.min_val = min(countX,countY)
        self.min_val = min(self.min_val,text)
        for i in range(0,self.min_val):    
            s1 = self.listWidgetX.item(i).text()
            s2 = self.listWidgetY.item(i).text()

            col1 , path1 = s1.split('-',1)
            col2 , path2 = s2.split('-',1)

            df1 = pd.read_csv(path1)
            df2 = pd.read_csv(path2)

            p = win.addPlot()
            p.plot(df1[col1],df2[col2], pen=(255,0,0))
            win.nextRow()

        self.mdiArea.addSubWindow(win)
        win.show()
        self.mdiArea.tileSubWindows()
        self.Xindex += self.min_val
        self.Yindex += self.min_val

    def handleNext(self):
        w = self.mdiArea.currentSubWindow()
        if w:
            self.mdiArea.removeSubWindow(w)

        countX = self.listWidgetX.count()
        countY = self.listWidgetY.count()
        win = pg.GraphicsWindow("PlotWindow")
        b_bool = False
        if(self.min_val == min(countX,countY)):
            pass
        else:
            for i in range(0, self.min_val):
                if((self.Xindex) >= min(countX,countY) or (self.Yindex) >= min(countX,countY) ):
                    self.Xindex = 0
                    self.Yindex = 0
                    # self.handleSimulate()
                    break
                b_bool = True
                s1 = self.listWidgetX.item(self.Xindex).text()
                s2 = self.listWidgetY.item(self.Yindex).text()
                col1 , path1 = s1.split('-',1)
                col2 , path2 = s2.split('-',1)

                df1 = pd.read_csv(path1)
                df2 = pd.read_csv(path2)

                p = win.addPlot()
                p.plot(df1[col1],df2[col2], pen=(255,0,0))
                win.nextRow()
                self.Xindex += 1
                self.Yindex += 1
            if b_bool:
                self.mdiArea.addSubWindow(win)
                win.show()
                self.mdiArea.tileSubWindows()
            else:
                self.handleSimulate()








    def _populateTree(self, children, parent):
        for child in sorted(children):
            # print(type(child))
            mapDict[child.split('/')[-1]] = child
            child_item = QStandardItem(child)
            child_item.setEditable(False)
            if child[0] == '/':
                child_item.setText(child.split('/')[-1])
            else:
                child_item.setText(child)
            #if (child_item != 'Do not print'):
            parent.appendRow(child_item)
            # print(type(child_item))
            if isinstance(children, dict):
                self._populateTree(children[child], child_item)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Add FIles"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.pushButton_4.setText(_translate("MainWindow", "Simulate"))
        self.pushButton_5.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Display 01"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "Module Tree"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "Module #1"))
        self.treeWidget_3.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Data Analysis"))
        self.treeWidget_3.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Data Processing"))
        self.treeWidget_3.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Data Visualization"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "Module #2"))
        self.treeWidget_3.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Sub-Module #1"))
        self.treeWidget_3.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Sub-Module #2"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
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

        self.radio1.setToolTip(_translate("MainWindow", "LinePlot"))
        self.radio2.setToolTip(_translate("MainWindow", "GridPlot"))


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


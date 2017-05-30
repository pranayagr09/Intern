#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import types
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainFrame(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        dict2 = { 'path1' : 'A', 'path2' : 'B', 'path3' : 'C'}
        tree = {'root': {
                    "1": [dict2['path1'], dict2['path2'], dict2['path3']],
                    "2": {
                        "2-1": ["G", "H", "I"],
                        "2-2": ["J", "K", "L"]},
                    "3": ["D", "E", "F"]}
        }

        self.tree = QTreeView(self)
        #self.tree.editTriggers
        layout = QHBoxLayout(self)
        layout.addWidget(self.tree)

        root_model = QStandardItemModel()
        self.tree.setModel(root_model)
        self._populateTree(tree, root_model.invisibleRootItem())

    def _populateTree(self, children, parent):
        for child in sorted(children):
            child_item = QStandardItem(child)
            child_item.setEditable(False)
            parent.appendRow(child_item)
            if isinstance(children, dict):
                self._populateTree(children[child], child_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainFrame()
    main.show()
    sys.exit(app.exec_())

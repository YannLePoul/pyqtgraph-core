from PyQt4 import QtGui, QtCore
from lib.analysis.AnalysisModule import AnalysisModule
#import lib.analysis.modules.EventDetector as EventDetector
#import MapCtrlTemplate
import DatabaseGui
#from flowchart import *
#import flowchart.library.EventDetection as FCEventDetection
import os
from collections import OrderedDict
import debug
import ColorMapper
import pyqtgraph as pg
#import pyqtgraph.TreeWidget as TreeWidget


class DatabaseExplorer(AnalysisModule):
    
    def __init__(self, host):
        AnalysisModule.__init__(self, host)
        
        self.dbIdentity = 'Explorer'
        
        self.dbCtrl = DBCtrl(host, self.dbIdentity)
        self.ctrl = PlotCtrl(host, self.dbIdentity)
        
        self._elements = OrderedDict([
            ('Database', {'type': 'ctrl', 'object':self.dbCtrl, 'size': (200, 300), 'host': self}),
            ('Scatter Plot', {'type': 'plot', 'pos':('right',), 'size': (800, 600)}),
            ('Plot Opts', {'type': 'ctrl', 'object': self.ctrl, 'pos':('bottom', 'Database'), 'size':(200,300)})
            ])
        

        
class DBCtrl(QtGui.QWidget):
    
    def __init__(self, host, identity):
        QtGui.QWidget.__init__(self)
        self.host = host
        self.dm = host.dataManager()
        self.db = self.dm.currentDatabase()
        
        self.layout = QtGui.QVBoxLayout()
        self.setLayout(self.layout)
        self.dbgui = DatabaseGui.DatabaseGui(self.dm, tables={})

        self.layout.addWidget(self.dbgui)
        #self.layout.addWidget(self.storeBtn)
        for name in ['getTableName', 'getDb']:
            setattr(self, name, getattr(self.dbgui, name))
            
class PlotCtrl(QtGui.QWidget):
    
    def __init__(self, host, identity):
        QtGui.QWidget.__init__(self)
        self.host = host
        self.dm = host.dataManager()
        
        
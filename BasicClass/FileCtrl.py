import wx
import sys,os
import pandas as pd
from collections import defaultdict

class FileCtrl(wx.ListCtrl):
    def __init__(self,*args,**kwargs):
        super(FileCtrl,self).__init__(*args,**kwargs)
        self.SetBackgroundColour = wx.BLACK

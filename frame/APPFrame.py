import sys,os
import wx






class AppFrame(wx.Frame):

    def __init__(self, title = 'Demo', file_path = None):

        super(AppFrame,self).__init__(parent = None, id = -1, title = title, size = (800,600))

        # self.SetBackgroundColour(wx.WHITE)
        self.file_path = None
        self.currentDirectory = os.getcwd()

        panel = wx.Panel(self,-1,size  = (500,300))
        
        self.textctrl = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
        btn = wx.Button(self, label='Open Text File')
        btn.Bind(wx.EVT_BUTTON, self.onOpen)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.textctrl, 1, wx.ALL|wx.EXPAND)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(sizer)

    def onOpen(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        path = dialog.GetPath()

        if os.path.exists(path):
            with open(path) as fobj:
                i = 0
                for line in fobj:
                    i = i +1
                    self.textctrl.WriteText(line)
                    if i == 30:
                        break
        dialog.Destroy()



    

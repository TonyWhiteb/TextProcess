import wx
import wx.grid as grid

class ButtonPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent = parent)

        button = wx.Button(self, label = "Comfirm")
        button.Bind(wx.EVT_BUTTON, self.onButton)

        btn_vert = wx.BoxSizer(wx.VERTICAL)
        btn_vert.AddSpacer(5)
        btn_vert.Add(button)
        btn_vert.AddSpacer(5)


        btn_horz = wx.BoxSizer(wx.HORIZONTAL)
        btn_horz.Add(btn_vert,flag = wx.EXPAND)
        btn_horz.AddSpacer(25)
        self.SetSizer(btn_horz)
        self.Layout()
    def onButton(self, event):
        pass

class GridPanel(wx.Panel):

    def __init__(self, parent,NumOfRows,column_list,col_dict):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        print(col_dict)
        MyGrid=grid.Grid(self)
        MyGrid.CreateGrid(NumOfRows,len(column_list))
        for i in range(len(column_list)):
            MyGrid.SetColLabelValue(i,column_list[i])
            MyGrid.AutoSizeColLabelSize(i)
            value_list = col_dict[column_list[i]]
            for row in range(len(value_list)):
                MyGrid.SetCellValue(row,i,value_list[row])
            # for value in col_dict[column_list[i]]:
                
            #     row = col_dict[column_list[i]].index(value)
            #     MyGrid.SetCellValue(row,i,value)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(MyGrid, 0, wx.EXPAND)
        self.SetSizer(sizer)
    



class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self,NumOfRows ,column_list,col_dict):
        """Constructor"""
        wx.Frame.__init__(self,None,title="Preview", size=(800,600))

        panel = wx.Panel(self,-1)
        self.btn_pnl = ButtonPanel(panel)
        self.grid_pnl = GridPanel(panel,NumOfRows,column_list,col_dict)

        box_h = wx.BoxSizer(wx.VERTICAL)
        box_v = wx.BoxSizer(wx.HORIZONTAL)
        box_v.AddSpacer(25)
        box_v.Add(self.grid_pnl,1,wx.EXPAND)
        box_v.AddSpacer(25)
        box_v.Add(self.btn_pnl,0,wx.EXPAND)

        box_h.AddSpacer(20)
        box_h.Add(box_v,-1,wx.EXPAND)
        box_h.AddSpacer(20)

        panel.SetSizer(box_h)
        panel.Fit()
        self.Centre()


    def AddPanel(self):
        self.newPanel = ButtonPanel(self, 1, 1)
        self.sizer.Add(self.newPanel, 1, wx.EXPAND)
        self.sizer.Layout()

# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     frame.Show()
#     app.MainLoop()
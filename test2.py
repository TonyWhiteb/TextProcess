import os
import wx
import itertools
from itertools import chain, islice

wildcard = "TXT files (*.txt)|*.txt"

class MyText(wx.TextCtrl):
    def __init__(self, *args, **kwargs):
        super(MyText,self).__init__(*args,**kwargs)

        self.HideNativeCaret



# class MyPanel(wx.Panel):

#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)
#         # self.currentDirectory = os.getcwd()
#         # self.file_name = None
#         # self.delimiter = None
#         # self.keyword = None

#         self.my_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
#         self.my_text.HideNativeCaret()
        # open_btn = wx.Button(self, label='Open Text File')
        # open_btn.Bind(wx.EVT_BUTTON, self.onOpen)
        # save_btn =  wx.Button(self, label ='Split and Save')
        # save_btn.Bind(wx.EVT_BUTTON, self.onSave)

        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.my_text, 1, wx.ALL|wx.EXPAND)
        # sizer.Add(open_btn, 0, wx.ALL|wx.CENTER, 5)
        # sizer.Add(save_btn, 0, wx.ALL|wx.CENTER, 5)

        # self.SetSizer(sizer)
    # def pairwise(self,iterable):
    #     a, b = itertools.tee(iterable)
    #     next(b, None)
    #     return zip(a, b)
    # # def chunks(self,iterable,n):
    # #     iterable = iter(iterable)
    # #     while True:
    # #         i= 1
    # #         print(i)
    # #         print(next(iterable))
    # #         print('-'*50)
            
    # #         yield chain([next(iterable)],islice(iterable, n-1))
    # def chunks(self,iterable, n):
    #     iterable = iter(iterable)
    #     while True:
    #         i= 1
    #         print(i)
    #         print(next(iterable))
    #         print('-'*50)
    #         for it_start, it_end in self.pairwise(n):
    #             # next_start, next_end = next(pairewise)
    #             print(it_start,it_end)
    #             yield  chain([next(iterable)],islice(iterable,it_start,it_end))
    # def readFile(self,fullpath):
    #     with open(fullpath) as f:
    #         i  = 0
    #         for line in f:
    #             i = i +1
    #             self.my_text.WriteText(line)
    #             if i == 30:
    #                 break
    # def onOpen(self, event):
        
    #     dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
    #                            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    #     if dialog.ShowModal() == wx.ID_CANCEL:
    #         return

    #     self.fullpath = dialog.GetPath()
    #     self.file_name = dialog.GetFilename()
    #     namelist = self.file_name.split('.')
    #     self.filetype = namelist[len(namelist)-1]
    #     self.filename = namelist[0]
    #     self.delimiter = None
    #     print(self.file_name)
    #     if os.path.exists(self.fullpath):
    #         self.readFile(self.fullpath)
    #         with open(self.fullpath) as f:
    #             i = 0
    #             self.delimiter = []
    #             num_lines = sum(1 for line in open(self.fullpath))
    #             for line in f:
    #                 rm_space = " ".join(line.split())
    #                 line_list = rm_space.split()
    #                 if 'Page' in line_list:
    #                     self.delimiter.append(i)
    #                 i = i+ 1
    #             self.delimiter.append(num_lines)




    # def onSave(self,event):
    #     dlg = wx.FileDialog(
    #         self,message = "Save File As",
    #         defaultDir = self.currentDirectory,
    #         defaultFile = "", wildcard = wildcard,
    #         style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
    #     )
    #     if dlg.ShowModal() == wx.ID_OK:
    #         fullpath = dlg.GetPath()
    #         basename = os.path.split(fullpath)
    #         file_name = dlg.GetFilename()
    #         namelist = file_name.split('.')
    #         filename = namelist[0]
    #         loop_token = len(self.delimiter)-1
    #         for i in range(loop_token):
    #             it_start = self.delimiter[i]
    #             it_end = self.delimiter[i+1]
    #             with open(self.fullpath) as full:
    #                 with open((filename + '{0}' +'.'+self.filetype).format(i),'w') as f:
    #                     for index, lines in enumerate(islice(full,it_start,it_end)):
    #                         f.writelines(lines)


            # with open(self.fullpath) as f:
            #     for i, lines in enumerate(self.chunks(f,self.delimiter)):
            #         # print(i,lines)
            #         os.chdir(basename[0])
            #         with open((filename + '{0}' +'.'+self.filetype).format(i),'w') as f:
            #             f.writelines(lines)
                # for i, lines in enumerate(self.chunks(f,60)):
                #     with open((filename + '{0}' +'.'+self.filetype).format(i),'w') as fobj:
                #         fobj.writelines(lines)

class BtnPanel(wx.Panel):

    def __init__(self, parent, id= -1, onOpen = None, onSave = None, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE):

        super(BtnPanel, self).__init__(parent = parent, id = id, size = size, style = style)

        Open_btn = wx.Button(self,-1,'Open Text File')
        Save_btn = wx.Button(self,-1,'Save as...')
        self.kw_pnl = wx.TextCtrl(self,-1)

        Open_btn.Bind(wx.EVT_LEFT_DOWN, onOpen)
        Save_btn.Bind(wx.EVT_LEFT_DOWN, onSave)

        btn_horz = wx.BoxSizer(wx.HORIZONTAL)
        btn_horz.AddSpacer(5)
        btn_horz.Add(self.kw_pnl)
        btn_horz.AddSpacer(5)
        btn_horz.Add(Open_btn)
        btn_horz.AddSpacer(5)
        btn_horz.Add(Save_btn)
        btn_horz.AddSpacer(5)
        
        btn_vert = wx.BoxSizer(wx.VERTICAL)
        btn_vert.AddStretchSpacer(prop =-1)
        btn_vert.Add(btn_horz, flag = wx.EXPAND)
        btn_vert.AddSpacer(25)

        self.SetSizer(btn_vert)
        self.Centre()
        self.Layout()

    



class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Text File Reader',size = (800,400))
        self.currentDirectory = os.getcwd()
        self.file_name = None
        self.delimiter = None
        self.keyword = None

        panel = wx.Panel(self,-1)

        # self.txt_pnl = MyPanel(self)
        self.txt_pnl = MyText(panel,size = (550,300),style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.txt_pnl.HideNativeCaret()

        self.btn_pnl = BtnPanel(panel, onOpen= self.onOpen, onSave= self.onSave, size = (300,-1))

        box_h = wx.BoxSizer(wx.HORIZONTAL)
        box_v = wx.BoxSizer(wx.VERTICAL)
        box_v.AddSpacer(25)
        box_v.Add(self.txt_pnl,1,wx.EXPAND)
        box_v.AddSpacer(5)
        box_v.Add(self.btn_pnl,1,wx.CENTER)

        box_h.AddSpacer(20)
        box_h.Add(box_v,-1,wx.EXPAND)
        box_h.AddSpacer(20)

        panel.SetSizer(box_h)
        panel.Fit()
        self.Centre()
        self.Show()


    def readFile(self,fullpath):
        with open(fullpath) as f:
            i  = 0
            for line in f:
                i = i +1
                self.txt_pnl.WriteText(line)
                if i == 30:
                    break

    def onOpen(self, event):
        
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        self.fullpath = dialog.GetPath()
        self.file_name = dialog.GetFilename()
        namelist = self.file_name.split('.')
        self.filetype = namelist[len(namelist)-1]
        self.filename = namelist[0]
        self.delimiter = None
        print(self.file_name)
        if os.path.exists(self.fullpath):
            self.readFile(self.fullpath)
            # with open(self.fullpath) as f:
            #     i = 0
            #     self.delimiter = []
            #     num_lines = sum(1 for line in open(self.fullpath))
            #     for line in f:
            #         rm_space = " ".join(line.split())
            #         line_list = rm_space.split()
            #         if 'Page' in line_list:
            #             self.delimiter.append(i)
            #         i = i+ 1
            #     self.delimiter.append(num_lines)


    # def delimiter(self):
    #     with open(self.fullpath) as f:
    #         i = 0
    #         self.delimiter = []
    #         numlines= sum(1 for line in open(self.fullpath))
    #         for line in f:
    #             rm_space = " ".join(line.split())
    #             line_list = rm_space.split()
    #             if self.keyword in line_list:
    #                 self.delimiter.append(i)
    #             i = i + 1
    #         self.delimiter.append(num_lines)



    def onSave(self,event):

        try:
            self.keyword = self.btn_pnl.kw_pnl.GetValue()
            if not self.keyword:
                raise ValueError('Please enter a delimiter to continue')
            else:
                with open(self.fullpath) as f:
                    print(self.fullpath)
                    i = 0
                    self.delimiter = []
                    num_lines= sum(1 for line in open(self.fullpath))
                    for line in f:
                        print(line)
                        rm_space = " ".join(line.split())
                        line_list = rm_space.split()
                        if self.keyword in line_list:
                            self.delimiter.append(i)
                        i = i + 1
                    self.delimiter.append(num_lines)
                    if len(self.delimiter) == 1:
                        raise kwException(('{0} is not exist in this text file').format(self.keyword))               
                
        except ValueError:
            self.Warn('Please enter a delimiter to continue')
        except kwException:
            self.Warn(('{0} is not exist in this text file').format(self.keyword))
        else:
            dlg = wx.FileDialog(
                self,message = "Save File As",
                defaultDir = self.currentDirectory,
                defaultFile = "", wildcard = wildcard,
                style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
            )
            if dlg.ShowModal() == wx.ID_OK:
                fullpath = dlg.GetPath()
                basename = os.path.split(fullpath)
                file_name = dlg.GetFilename()
                namelist = file_name.split('.')
                filename = namelist[0]
                loop_token = len(self.delimiter)-1
                for i in range(loop_token):
                    it_start = self.delimiter[i]
                    it_end = self.delimiter[i+1]
                    with open(self.fullpath) as full:
                        with open((filename + '{0}' +'.'+self.filetype).format(i),'w') as f:
                            for index, lines in enumerate(islice(full,it_start,it_end)):
                                f.writelines(lines)            
            


    def Warn(self, message, caption = 'Warning!'):
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()    

class kwException(Exception):
    pass


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
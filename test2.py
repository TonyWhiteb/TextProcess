import os
import wx
import itertools
from itertools import chain, islice

wildcard = "TXT files (*.txt)|*.txt"

class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.currentDirectory = os.getcwd()
        self.file_name = None
        self.delimiter = None
        self.keyword = None

        self.my_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.my_text.HideNativeCaret()
        open_btn = wx.Button(self, label='Open Text File')
        open_btn.Bind(wx.EVT_BUTTON, self.onOpen)
        save_btn =  wx.Button(self, label ='Split and Save')
        save_btn.Bind(wx.EVT_BUTTON, self.onSave)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.my_text, 1, wx.ALL|wx.EXPAND)
        sizer.Add(open_btn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(save_btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(sizer)
    def pairwise(self,iterable):
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)
    # def chunks(self,iterable,n):
    #     iterable = iter(iterable)
    #     while True:
    #         i= 1
    #         print(i)
    #         print(next(iterable))
    #         print('-'*50)
            
    #         yield chain([next(iterable)],islice(iterable, n-1))
    def chunks(self,iterable, n):
        iterable = iter(iterable)
        while True:
            i= 1
            print(i)
            print(next(iterable))
            print('-'*50)
            for it_start, it_end in self.pairwise(n):
                # next_start, next_end = next(pairewise)
                print(it_start,it_end)
                yield  chain([next(iterable)],islice(iterable,it_start,it_end))
    def readFile(self,fullpath):
        with open(fullpath) as f:
            i  = 0
            for line in f:
                i = i +1
                self.my_text.WriteText(line)
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
            with open(self.fullpath) as f:
                i = 0
                self.delimiter = []
                num_lines = sum(1 for line in open(self.fullpath))
                for line in f:
                    rm_space = " ".join(line.split())
                    line_list = rm_space.split()
                    if 'Page' in line_list:
                        self.delimiter.append(i)
                    i = i+ 1
                self.delimiter.append(num_lines)




    def onSave(self,event):
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


            # with open(self.fullpath) as f:
            #     for i, lines in enumerate(self.chunks(f,self.delimiter)):
            #         # print(i,lines)
            #         os.chdir(basename[0])
            #         with open((filename + '{0}' +'.'+self.filetype).format(i),'w') as f:
            #             f.writelines(lines)
                # for i, lines in enumerate(self.chunks(f,60)):
                #     with open((filename + '{0}' +'.'+self.filetype).format(i),'w') as fobj:
                #         fobj.writelines(lines)


        pass



class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Text File Reader')

        panel = MyPanel(self)

        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
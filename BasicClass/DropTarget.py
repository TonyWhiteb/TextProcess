import wx
import os,sys

class DropTarget(wx.FileDropTarget):
    def __init__(self,targetControl):
        self.targetControl = targetControl

        wx.FileDropTarget.__init__(self)

    def OnDropFiles(self, xOrd, yOrd, pathList):

        path_list = []
        basename_list = []
        filetype_list = []
        col_dict = {}
        dict_col = {}
        for aPath in pathList :
            pathname, aBasename = os.path.split(aPath)
            namelist = aBasename.split('.')
            filetype = namelist[len(namelist)-1]

            

            os.chdir(pathname)
            if filetype == 'errors':

                with open(aBasename) as afile:
                    for line in afile:
                        col_info= {}
                        afile_list = line.split('\t') 
                        col_info = col_info.fromkeys(afile_list)
                        break
                        
            path_list.append(pathname)
            basename_list.append(aBasename)
            filetype_list.append(filetype)
            dict_col[aBasename] = col_info
            col_dict[pathname] = dict_col

        filenameDropDict = {}
        filenameDropDict['coord'] = (xOrd,yOrd)
        filenameDropDict['pathList'] = pathList
        filenameDropDict['pathname'] = path_list
        filenameDropDict['basenameList'] = basename_list
        filenameDropDict['filetype'] = filetype_list
        filenameDropDict['col_info'] = col_dict

        if (hasattr( self.targetControl, 'dropFunc' ))  and  \
           (self.targetControl.dropFunc != None) :

            # Call the callback function with the processed drop data.
            self.targetControl.dropFunc( filenameDropDict )
        
       # HIGHL: 
        # How to add a function dynamically

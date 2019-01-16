from frame import NewAPPFrame
import sys,os, platform
import wx

if __name__ == '__main__':
    args = sys.argv
    THISPYFILE = args.pop(0)
    argc = len(args)
    path = os.path.dirname(os.path.abspath(__file__))
    app = wx.App(redirect = False)
    appFrame = NewAPPFrame.AppFrame(args, argc
                                   ,file_path = path)
    import wx.lib.inspection
    app.MainLoop()

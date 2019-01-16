from frame import APPFrame
import wx


if __name__ == "__main__":
    app = wx.App(False)
    frame = APPFrame.AppFrame()
    frame.Show()
    app.MainLoop()
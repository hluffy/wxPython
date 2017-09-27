import wx

class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title = title,size = (600,200))
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        lb1 = wx.StaticText(panel,-1,style = wx.ALIGN_CENTER)

        txt1 = "Python GUI development"
        txt2 = "using wxPython"
        txt3 = " Python port of wxWidget"
        txt = txt1 + "\n" + txt2 + "\n" + txt3

        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        lb1.SetFont(font)
        lb1.SetLabel(txt)

        box.Add(lb1, 0, wx.ALIGN_CENTER)
        lb1wrap = wx.StaticText(panel, -1, style = wx.ALIGN_RIGHT)
        txt = txt1 + txt2 + txt3

        lb1wrap.SetLabel(txt)
        lb1wrap.Wrap(200)
        box.Add(lb1wrap, 0, wx.ALIGN_LEFT)

        lbl1 = wx.StaticText(panel, -1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE)
        lbl1.SetLabel(txt)
        lbl1.SetForegroundColour((255, 0, 0))
        lbl1.SetBackgroundColour((0, 0, 0))

        font = self.GetFont()
       # font.SetTutorialsSize(18)
        lbl1.SetFont(font)

        box.Add(lbl1, 0, wx.ALIGN_LEFT)
        panel.SetSizer(box)
        self.Centre()
        self.Show()


app = wx.App()
Mywin(None , "StaticText demo")
app.MainLoop()

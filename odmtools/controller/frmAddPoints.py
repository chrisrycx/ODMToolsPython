"""Subclass of MyDialog1, which is generated by wxFormBuilder."""

import wx

import clsAddPoints



# Implementing AddPoints
class AddPoints(clsAddPoints.AddPoints):
    def __init__(self, parent):
        #super(AddPoints, self).__init__(parent)
        clsAddPoints.AddPoints.__init__(self, parent)

    # Handlers for AddPoints events.
    def onClickAdd(self, event):

        pass

    def onClose(self, event):
        # TODO: Implement onClose
        self.Destroy()
        pass

    def onSelected(self, event):
        object = event.GetEventObject()
        editingObject = object.innerList[object.FocusedItem]


class Example(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        wx.Frame.__init__(self, parent, *args, **kwargs)
        m = AddPoints(parent)
        m.Show()


if __name__ == '__main__':
    app = wx.App(useBestVisual=True)
    ex = Example(None)
    app.MainLoop()
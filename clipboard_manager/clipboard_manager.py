'''
This tool is basically a multiline clipboard.

It copies and displays multiple texts in a list.

Using this, multiple text copies can be viewed and on clicking any line, text of the line is automatically copied to
clipboard. Just paste it in the required place, where you want to paste it!!

'''

import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
import pyperclip

   
class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):

    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT |
                wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

class ClipboardCopierUI(wx.Frame):
            
    def __init__(self, *args, **kw):
        super(ClipboardCopierUI, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)

        leftPanel = wx.Panel(panel)
        rightPanel = wx.Panel(panel)
        
        self.list = CheckListCtrl(rightPanel)
        self.list.InsertColumn(0, 'CopiedText', width=140)         

        startButton = wx.Button(leftPanel, label='Start')
        stopButton = wx.Button(leftPanel, label='Stop')
        selBtn = wx.Button(leftPanel, label='Select All')
        desBtn = wx.Button(leftPanel, label='Deselect All')
        removeButton = wx.Button(leftPanel, label='Remove')

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.loadItems, self.timer)
        self.Bind(wx.EVT_BUTTON, self.Start, id=startButton.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnstopButton, id=stopButton.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnremoveButton, id=removeButton.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=selBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeselectAll, id=desBtn.GetId())

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemActivated, self.list) 

        vbox2.Add(startButton, 0, wx.BOTTOM, 5)
        vbox2.Add(stopButton, 0, wx.BOTTOM, 5)
        vbox2.Add(selBtn, 0, wx.BOTTOM, 5)
        vbox2.Add(desBtn, 0, wx.BOTTOM, 5)
        vbox2.Add(removeButton, 0, wx.BOTTOM, 5)
   
        leftPanel.SetSizer(vbox2)

        vbox.Add(self.list, 4, wx.EXPAND | wx.TOP, 3)
   
        rightPanel.SetSizer(vbox)

        hbox.Add(leftPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(rightPanel, 1, wx.EXPAND)

        panel.SetSizer(hbox)

        self.SetTitle('Clipboard Manager')

        #List to hold clipboard values
        self.clipboardValue = []

    def reloadListItems(self):
        self.list.DeleteAllItems()         
        idx = 0
        for item in self.clipboardValue:
            index = self.list.InsertItem(idx, item)    
            idx += 1

    def loadItems(self,event):
        self.reloadListItems()
        self.Start(None)

    def OnItemActivated(self,event):
        pyperclip.copy(self.list.GetItem(self.list.GetFocusedItem(), 0).GetText())
        
    def Start(self, event):
        if pyperclip.paste() not in self.clipboardValue:
            self.clipboardValue.append(pyperclip.paste())                
        self.timer.Start(100)

    def OnstopButton(self, event):
        self.timer.Stop()

    def OnremoveButton(self, event):
        num = self.list.GetItemCount()        
        for i in range(num):
            if self.list.IsChecked(i):
                self.clipboardValue.remove(self.list.GetItem(i,0).GetText())
        self.reloadListItems()

    def OnSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)

    def OnDeselectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)                

def main():

    app = wx.App()
    ex = ClipboardCopierUI(None)
    ex.Show()            
    app.MainLoop()


if __name__ == '__main__':
    main()

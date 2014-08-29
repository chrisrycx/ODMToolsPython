"""Subclass of pnlExisting, which is generated by wxFormBuilder."""

import wx
from odmtools.view import clsExisting
from odmtools.odmdata import series
import wx.wizard as wiz

# Implementing pnlExisting
#class pnlExisting(clsExisting.pnlExisting):
#    def __init__(self, parent):
#        clsExisting.pnlExisting.__init__(self, parent)

########################################################################
class pageExisting(wiz.WizardPageSimple):
    def __init__(self, parent, title, service_man, site):
        """Constructor"""
        wiz.WizardPageSimple.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = sizer
        self.SetSizer(sizer)
        #self.series = series

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 10, wx.ALIGN_CENTRE | wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 5, wx.EXPAND | wx.ALL, 5)
        self.panel = clsExisting.pnlExisting(self)  #, id=wxID_PNLEXISTING, name=u'pnlExisting',
        #pos=wx.Point(536, 285), size=wx.Size(439, 357),
        #style=wx.TAB_TRAVERSAL)#, sm = service_man, series = series)
        self.sizer.Add(self.panel, 85, wx.ALL, 5)
        self._init_data(service_man.get_series_service(), site.id)


    def _init_data(self, series_serv, site_id):
        index = 0
        self.initTable(series_serv, site_id)

        #if q.code == self.qcl.code:
        #    index = i
        self.panel.olvSeriesList.Focus(index)
        self.panel.olvSeriesList.Select(index)





    # Handlers for pnlExisting events.
    def OnOLVItemSelected(self, event):
        # TODO: Implement OnOLVItemSelected
        pass

    def getSeries(self):
        selectedObject = self.panel.olvSeriesList.GetSelectedObject()
        return selectedObject.method, selectedObject.quality_control_level, selectedObject.variable

    def initTable(self, dbservice, site_id):
        """Set up columns and objects to be used in the objectlistview to be visible in the series selector"""

        seriesColumns = [clsExisting.ColumnDefn(key, align="left", minimumWidth=-1, valueGetter=value)
                         for key, value in series.returnDict().iteritems()]

        self.panel.olvSeriesList.SetColumns(seriesColumns)
        objects = dbservice.get_series_by_site(site_id= site_id)
        self.panel.olvSeriesList.SetObjects(objects)

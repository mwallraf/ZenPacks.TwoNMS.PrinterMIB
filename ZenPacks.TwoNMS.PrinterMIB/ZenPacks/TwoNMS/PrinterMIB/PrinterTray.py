######################################################################
#
# ZenPacks.TwoNMS.PrinterMIB.Tray object class
#
######################################################################

__doc__=""" 

Tray is a component of a ZenPacks.TwoNMS.PrinterMIB.Printer

$Id: $"""

__version__ = "$Revision: $"[11:-2]

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity

import logging
log = logging.getLogger('PrinterMIB.Tray')

class PrinterTray(DeviceComponent, ManagedEntity):
    """a PrinterMIB.Tray object"""

    portal_type = meta_type = 'PrinterTray'
    
    #**************Custom data Variables here from modeling************************
    
    supplyId = ""
    prtCapacityUnit = ""
    prtInputCurrentLevel = 0
    prtInputMaxCapacity = 0
    prtInputDescription = ""
    prtInputMediaName = ""
    prtInputModel =""
    prtInputName = ""
    prtInputType = ""
    usagepct = ""

    
    #**************END CUSTOM VARIABLES *****************************
    
    
    #*************  Those should match this list below *******************
    _properties = (
        {'id':'supplyId', 'type':'string', 'mode':''},
        {'id':'prtCapacityUnit', 'type':'string', 'mode':''},
        {'id':'prtInputCurrentLevel', 'type':'int', 'mode':''},
        {'id':'prtInputMaxCapacity', 'type':'int', 'mode':''},
        {'id':'prtInputDescription', 'type':'string', 'mode':''},
        {'id':'prtInputMediaName', 'type':'string', 'mode':''},
        {'id':'prtInputModel', 'type':'string', 'mode':''},
        {'id':'prtInputName', 'type':'string', 'mode':''},
        {'id':'prtInputType', 'type':'string', 'mode':''},
        {'id':'usagepct', 'type':'string', 'mode':''},
        )
    #****************
    
    _relations = (
        ("printermibprinter", ToOne(ToManyCont, "ZenPacks.TwoNMS.PrinterMIB.Printer", "printermibtray")),
        )

    def device(self):
        return self.printermibprinter()

    def viewName(self):
        return self.supplyId

    #def monitored(self):
    #    return True

    titleOrId = name = viewName

    # this allows editable fields in the Details pane
    isUserCreatedFlag = True

    def isUserCreated(self):
        return self.isUserCreatedFlag

    # define additional panes in the component section (dropdown menu)
    factory_type_information = (
        {
            'id': 'PrinterTray',
            'meta_type': 'PrinterTray',
            'description': """PrinterMIB PrinterTray component""",
            'actions': (
                 {
                     'id': 'viewHistory',
                     'name': 'Modifications',
                     'action': 'viewHistory',
                     'permissions': (ZEN_VIEW, )
                 },                
            )
        },
    )


InitializeClass(PrinterTray)


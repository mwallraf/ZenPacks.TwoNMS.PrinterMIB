######################################################################
#
# ZenPacks.TwoNMS.PrinterMIB.Toner object class
#
######################################################################

__doc__=""" 

Supply is a component of a ZenPacks.TwoNMS.PrinterMIB.Printer

$Id: $"""

__version__ = "$Revision: $"[11:-2]

from Globals import DTMLFile
from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity

import logging
log = logging.getLogger('PrinterMIB.Toner')

class PrinterToner(DeviceComponent, ManagedEntity):
    """a PrinterMIB.Toner object"""

    portal_type = meta_type = 'PrinterToner'
    
    #**************Custom data Variables here from modeling************************
    
    supplyId = ""
    prtMarkerSuppliesColorantValue = ""
    prtMarkerSuppliesDescription =""
    prtMarkerSuppliesLevel = 0
    prtMarkerSuppliesMaxCapacity = 0
    prtMarkerSuppliesSupplyUnit = 0
    prtMarkerSuppliesType = ""
    rgbColorCode = ""
    usagepct = 0

    #prtMarkerSuppliesDescription = ""
    #prtMarkerColorantValue = ""
    #prtMarkerColorantIndex = -1
    #prtMarkerSuppliesMaxCapacity = 0
    #prtMarkerSuppliesLevel = 0
    #rgbColorCode = "000000"
    #PrtMarkerSuppliesTypeTC = ""
    #PrtMarkerSuppliesSupplyUnitTC = ""

    
    #**************END CUSTOM VARIABLES *****************************
    
    
    #*************  Those should match this list below *******************
    _properties = (
        {'id':'supplyId', 'type':'string', 'mode':''},
        {'id':'prtMarkerSuppliesColorantValue', 'type':'string', 'mode':''},
        {'id':'prtMarkerSuppliesDescription', 'type':'string', 'mode':''},
        {'id':'prtMarkerSuppliesLevel', 'type':'int', 'mode':''},
        {'id':'prtMarkerSuppliesMaxCapacity', 'type':'int', 'mode':''},
        {'id':'prtMarkerSuppliesSupplyUnit', 'type':'string', 'mode':''},
        {'id':'prtMarkerSuppliesType', 'type':'string', 'mode':''},
        {'id':'rgbColorCode', 'type':'string', 'mode':''},
        {'id':'usagepct', 'type':'string', 'mode':''},
        )
    #****************
    
    _relations = (
        ("printermibprinter", ToOne(ToManyCont, "ZenPacks.TwoNMS.PrinterMIB.Printer", "printermibtoner")),
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
            'id': 'PrinterToner',
            'meta_type': 'PrinterToner',
            'description': """PrinterMIB PrinterToner component""",
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


InitializeClass(PrinterToner)


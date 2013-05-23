######################################################################
#
# ZenPacks.TwoNMS.PrinterMIB.Printer object class
#
######################################################################

__doc__=""" 

Printer is a Device object of a ZenPacks.TwoNMS.PrinterMIB

$Id: $"""

__version__ = "$Revision: $"[11:-2]


from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from copy import deepcopy

import logging
log = logging.getLogger('PrinterMIB.Printer')

class Printer(Device):
    """A Printer Device"""

    #**************Custom data Variables here from modeling************************
    
    prtGeneralPrinterName = ""
    prtGeneralSerialNumber = ""
    prtAlertCriticalEvents = -1  # unsupported if -1
    prtAlertAllEvents = -1		 # unsupported if -1
    
    #**************END CUSTOM VARIABLES *****************************
    
    
    #*************  Those should match this list below *******************
    _properties = (
        {'id':'prtGeneralPrinterName', 'type':'string', 'mode':''},
        {'id':'prtGeneralSerialNumber', 'type':'string', 'mode':''},
        {'id':'prtAlertCriticalEvents', 'type':'int', 'mode':''},
        {'id':'prtAlertAllEvents', 'type':'int', 'mode':''},
        )
    #****************

    _relations = Device._relations + (
        ('printermibtray', ToManyCont(ToOne, 'ZenPacks.TwoNMS.PrinterMIB.PrinterTray', 'printermibprinter')),
        ('printermibsupply', ToManyCont(ToOne, 'ZenPacks.TwoNMS.PrinterMIB.PrinterSupply', 'printermibprinter')),
        ('printermibtoner', ToManyCont(ToOne, 'ZenPacks.TwoNMS.PrinterMIB.PrinterToner', 'printermibprinter'))
        )

    factory_type_information = deepcopy(Device.factory_type_information)

    # keep this section if you need an extra menu item in left side menu of zenoss 3
#    factory_type_information[0]['actions'] += (
#            { 'id'              : 'BridgeInt'
#            , 'name'            : 'Bridge Interfaces'
#            , 'action'          : 'BridgeDeviceDetail'
#            , 'permissions'     : (ZEN_VIEW, ) },
#            )


    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()


InitializeClass(Printer)


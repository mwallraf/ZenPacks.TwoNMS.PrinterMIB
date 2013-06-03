__doc__="""info.py

Representation PrinterMIB Supply

$Id: info.py,v 1.2 2010/12/14 20:45:46 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
#from Products.ZenUtils.Utils import convToUnits
from ZenPacks.TwoNMS.PrinterMIB import interfaces


## this is for PrinterSupply
class PrinterMIBInfo(ComponentInfo):
    implements(interfaces.IPrinterMIBInfo)


    Description = ProxyProperty("prtMarkerSuppliesDescription")
    MaxLevel = ProxyProperty("prtMarkerSuppliesMaxCapacity")
    CurrentLevel = ProxyProperty("prtMarkerSuppliesLevel")
    CurrentUsage = ProxyProperty("usagepct")
    SupplyType = ProxyProperty("prtMarkerSuppliesType")
    SupplyTypeUnit = ProxyProperty("prtMarkerSuppliesSupplyUnit")


## this is for PrinterToner
class PrinterMIBTonerInfo(ComponentInfo):
    implements(interfaces.IPrinterMIBTonerInfo)


    Description = ProxyProperty("prtMarkerSuppliesDescription")
    Color = ProxyProperty("prtMarkerSuppliesColorantValue")
    MaxLevel = ProxyProperty("prtMarkerSuppliesMaxCapacity")
    CurrentLevel = ProxyProperty("prtMarkerSuppliesLevel")
    rgbColorCode = ProxyProperty("rgbColorCode")
    SupplyType = ProxyProperty("prtMarkerSuppliesType")
    SupplyTypeUnit = ProxyProperty("prtMarkerSuppliesSupplyUnit")
    CurrentUsage = ProxyProperty("usagepct")


## this is for PrinterTray
class PrinterMIBTrayInfo(ComponentInfo):
    implements(interfaces.IPrinterMIBTrayInfo)

    InputName = ProxyProperty("prtInputName")
    Model = ProxyProperty("prtInputModel")
    Type = ProxyProperty("prtInputType")
    CurrentUsage = ProxyProperty("usagepct")
    CurrentLevel = ProxyProperty("prtInputCurrentLevel")
    MaxLevel = ProxyProperty("prtInputMaxCapacity")
    Unit = ProxyProperty("prtCapacityUnit")
    Description = ProxyProperty("prtInputDescription")
    MediaName = ProxyProperty("prtInputMediaName")


from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

# this is for PrinterSupply
class IPrinterMIBInfo(IComponentInfo):
    """
Info adapter for PrinterMIB Supply component
"""
    Description = schema.Text(title=u"Supply Description", readonly=True, group='Details')
    MaxLevel = schema.Text(title=u"Maximum Level", readonly=True, group='Details')
    CurrentLevel = schema.Text(title=u"Current Level", readonly=True, group='Details')
    CurrentUsage = schema.Text(title=u"Current Usage", readonly=True, group='Details')
    SupplyType = schema.Text(title=u"Supply Type", readonly=True, group='Details')
    SupplyTypeUnit = schema.Text(title=u"Supply Type Measurement Unit", readonly=True, group='Details')



# this is for PrinterToner
class IPrinterMIBTonerInfo(IComponentInfo):
    """
Info adapter for PrinterMIB Supply component
"""
    Color = schema.Text(title=u"Color", readonly=True, group='Details')
    Description = schema.Text(title=u"Supply Description", readonly=True, group='Details')
    MaxLevel = schema.Text(title=u"Maximum Level", readonly=True, group='Details')
    CurrentLevel = schema.Text(title=u"Current Level", readonly=True, group='Details')
    CurrentUsage = schema.Text(title=u"Current Usage", readonly=True, group='Details')
    SupplyType = schema.Text(title=u"Supply Type", readonly=True, group='Details')
    SupplyTypeUnit = schema.Text(title=u"Supply Type Measurement Unit", readonly=True, group='Details')
    rgbColorCode = schema.Text(title=u"RGB Color Code", readonly=False, group='Details')

# this is for PrinterTray
class IPrinterMIBTrayInfo(IComponentInfo):
    """
Info adapter for PrinterMIB Tray component
"""
    InputName = schema.Text(title=u"Name", readonly=True, group='Details')
    Model = schema.Text(title=u"Model", readonly=True, group='Details')
    Type = schema.Text(title=u"Type", readonly=True, group='Details')
    CurrentUsage = schema.Text(title=u"Current Usage", readonly=True, group='Details')
    CurrentLevel = schema.Text(title=u"Current Level", readonly=True, group='Details')
    MaxLevel = schema.Text(title=u"Maximum Level", readonly=True, group='Details')
    Unit = schema.Text(title=u"Unit", readonly=True, group='Details')
    Description = schema.Text(title=u"Description", readonly=True, group='Details')
    MediaName = schema.Text(title=u"Media Name", readonly=True, group='Details')


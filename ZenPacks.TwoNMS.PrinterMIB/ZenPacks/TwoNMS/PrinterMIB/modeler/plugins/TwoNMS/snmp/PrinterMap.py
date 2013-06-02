######################################################################
#
# ZenPacks.TwoNMS.PrinterMIB PrinterMap modeler plugin (RFC3805)
#
######################################################################

__doc__=""" PrinterMap

PrinterMib maps Printer Supplies on ZenPacks.TwoNMS.PrinterMIB.Printer objects

$Id: $"""

__version__ = '$Revision: $'[11:-2]

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap

class PrinterMap(SnmpPlugin):
    
    # these are set specifically for each relmap() and objectMap()
    # needed because I use 1 modeler for multiple components
    #relname = "printermibsupply"
    #modname = "ZenPacks.TwoNMS.PrinterMIB.PrinterSupply"

#    compname = ""
    
    # New classification stuff uses weight to help it determine what class a
    # device should be in. Higher weight pushes the device to towards the
    # class were this plugin is defined.
    weight = 15

    # Values for encoding the state of a particular cover or
    # access panel on the printer case or enclosure
    PrtCoverStatusTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '3':    'coverOpen',
        '4':    'coverClosed',
        '5':    'interlockOpen',
        '6':    'interlockClosed',
        }
    
    # Values for reading and writing the prtGeneralReset object
    PrtGeneralResetTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '3':    'notResetting',
        '4':    'powerCycleReset',
        '5':    'resetToNVRAM',
        '6':    'resetToFactoryDefaults',
        }

    # The type of technology (discriminated primarily according to
    # feeder mechanism type) employed by a specific component or
    # components
    PrtInputTypeTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'sheetFeedAutoRemovableTray',
        '4':    'sheetFeedAutoNonRemovableTray',
        '5':    'sheetFeedManual',
        '6':    'continuousRoll',
        '7':    'continuousFanFold',
        }

    # The Type of technology supported by this output subunit
    PrtOutputTypeTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'removableBin',
        '4':    'unRemovableBin',
        '5':    'continuousRollDevice',
        '6':    'mailBox',
        '7':    'continuousFanFold',
        }

    # The type of marking technology used for this marking subunit
    PrtOutputTypeTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'electrophotographicLED',
        '4':    'electrophotographicLaser',
        '5':    'electrophotographicOther',
        '6':    'impactMovingHeadDotMatrix9pin',
        '7':    'impactMovingHeadDotMatrix24pin',
        '8':    'impactMovingHeadDotMatrixOther',
        '9':    'impactMovingHeadFullyFormed',
        '10':    'impactBand',
        '11':    'impactOther',
        '12':    'inkjetAqueous',
        '13':    'inkjetSolid',
        '14':    'inkjetOther',
        '15':    'pen',
        '16':    'thermalTransfer',
        '17':    'thermalSensitive',
        '18':    'thermalDiffusion',
        '19':    'thermalOther',
        '20':    'electroerosion',
        '21':    'electrostatic',
        '22':    'photographicMicrofiche',
        '23':    'photographicImagesetter',
        '24':    'photographicOther',
        '25':    'ionDeposition',
        '26':    'eBeam',
        '27':    'typesetter',
        }

    # PREVIOUS: cartType
    # The type of this supply
    PrtMarkerSuppliesTypeTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
         '1': 'other',
         '2': 'unknown',
         '3': 'toner',
         '4': 'wasteToner',
         '5': 'ink',
         '6': 'inkCartridge',
         '7': 'inkRibbon',
         '8': 'wasteInk',
         '9': 'opc',    # photo conductor
         '10': 'developer',
         '11': 'fuserOil',
         '12': 'solidWax',
         '13': 'ribbonWax',
         '14': 'wasteWax',
         '15': 'fuser',
         '16': 'coronaWire',
         '17': 'fuserOilWick',
         '18': 'cleanerUnit',
         '19': 'fuserCleaningPad',
         '20': 'transferUnit',
         '21': 'tonerCartridge',
         '22': 'fuserOiler',
         '23': 'water',
         '24': 'wasteWater',
         '25': 'glueWaterAdditive',
         '26': 'wastePaper',
         '27': 'bindingSupply',
         '28': 'bandingSupply',
         '29': 'stitchingWire',
         '30': 'shrinkWrap',
         '31': 'paperWrap',
         '32': 'staples',
         '33': 'inserts',
         '34': 'covers',
         }


    # The type of the media path for this media path
    PrtMediaPathTypeTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'longEdgeBindingDuplex',
        '4':    'shortEdgeBindingDuplex',
        '5':    'simplex',
        }

    # The color of this light
    PrtConsoleColorTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'white',
        '4':    'red',
        '5':    'green',
        '6':    'blue',
        '7':    'cyan',
        '8':    'magenta',
        '9':    'yellow',
        '10':    'orange',
        }

    # This value indicates whether or not input is accepted from
    # the operator console.  A value of 'enabled' indicates that
    # input is accepted from the console, and a value of 'disabled'
    # indicates that input is not accepted from the console
    PrtConsoleDisableTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '3':    'enabled',
        '4':    'disabled',
        }

    # The level of training required to handle this alert, if
    # human intervention is required
    PrtAlertTrainingLevelTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'untrained',
        '4':    'trained',
        '5':    'fieldService',
        '6':    'management',
        '7':    'noInterventionRequired',
        }

    # The type of subunit within the printer model that this alert
    # is related
    PrtAlertGroupTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '3':    'hostResourcesMIBStorageTable',
        '4':    'hostResourcesMIBDeviceTable',
        '5':    'generalPrinter',
        '6':    'cover',
        '7':    'localization',
        '8':    'input',
        '9':    'output',
        '10':    'marker',
        '11':    'markerSupplies',
        '12':    'markerColorant',
        '13':    'mediaPath',
        '14':    'channel',
        '15':    'interpreter',
        '16':    'consoleDisplayBuffer',
        '17':    'consoleLights',
        '18':    'alert',
        '30':    'finDevice',
        '31':    'finSupply',
        '32':    'finSupplyMediaInput',
        '33':    'finAttribute',
        }
        

    # The code that describes the type of alert for this entry in
    # the table
    PrtAlertCodeTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '2':    'unknown',
        '3':    'coverOpen',
        '4':    'coverClosed',
        '5':    'interlockOpen',
        '6':    'interlockClosed',
        '7':    'configurationChange',
        '8':    'jam',
        '9':    'subunitMissing',
        '10':    'subunitLifeAlmostOver',
        '11':    'subunitLifeOver',
        '12':    'subunitAlmostEmpty',
        '13':    'subunitEmpty',
        '14':    'subunitAlmostFull',
        '15':    'subunitFull',
        '16':    'subunitNearLimit',
        '17':    'subunitAtLimit',
        '18':    'subunitOpened',
        '19':    'subunitClosed',
        '20':    'subunitTurnedOn',
        '21':    'subunitTurnedOff',
        '22':    'subunitOffline',
        '23':    'subunitPowerSaver',
        '24':    'subunitWarmingUp',
        '25':    'subunitAdded',
        '26':    'subunitRemoved',
        '27':    'subunitResourceAdded',
        '28':    'subunitResourceRemoved',
        '29':    'subunitRecoverableFailure',
        '30':    'subunitUnrecoverableFailure',
        '31':    'subunitRecoverableStorageError',
        '32':    'subunitUnrecoverableStorageError',
        '33':    'subunitMotorFailure',
        '34':    'subunitMemoryExhausted',
        '35':    'subunitUnderTemperature',
        '36':    'subunitOverTemperature',
        '37':    'subunitTimingFailure',
        '38':    'subunitThermistorFailure',
        '501':    'doorOpen',
        '502':    'doorClosed',
        '503':    'powerUp',
        '504':    'powerDown',
        '505':    'printerNMSReset',
        '506':    'printerManualReset',
        '507':    'printerReadyToPrint',
        '801':    'inputMediaTrayMissing',
        '802':    'inputMediaSizeChange',
        '803':    'inputMediaWeightChange',
        '804':    'inputMediaTypeChange',
        '805':    'inputMediaColorChange',
        '806':    'inputMediaFormPartsChange',
        '807':    'inputMediaSupplyLow',
        '808':    'inputMediaSupplyEmpty',
        '809':    'inputMediaChangeRequest',
        '810':    'inputManualInputRequest',
        '811':    'inputTrayPositionFailure',
        '812':    'inputTrayElevationFailure',
        '813':    'inputCannotFeedSizeSelected',
        '901':    'outputMediaTrayMissing',
        '902':    'outputMediaTrayAlmostFull',
        '903':    'outputMediaTrayFull',
        '904':    'outputMailboxSelectFailure',
        '1001':    'markerFuserUnderTemperature',
        '1002':    'markerFuserOverTemperature',
        '1003':    'markerFuserTimingFailure',
        '1004':    'markerFuserThermistorFailure',
        '1005':    'markerAdjustingPrintQuality',
        '1101':    'markerTonerEmpty',
        '1102':    'markerInkEmpty',
        '1103':    'markerPrintRibbonEmpty',
        '1104':    'markerTonerAlmostEmpty',
        '1105':    'markerPrintRibbonAlmostEmpty',
        '1106':    'markerPrintRibbonAlmostEmpty',
        '1107':    'markerWasteTonerReceptacleAlmostFull',
        '1108':    'markerWasteInkReceptacleAlmostFull',
        '1109':    'markerWasteTonerReceptacleFull',
        '1110':    'markerWasteInkReceptacleFull',
        '1111':    'markerOpcLifeAlmostOver',
        '1112':    'markerOpcLifeOver',
        '1113':    'markerDeveloperAlmostEmpty',
        '1114':    'markerDeveloperEmpty',
        '1115':    'markerTonerCartridgeMissing',
        '1301':    'mediaPathMediaTrayMissing',
        '1302':    'mediaPathMediaTrayAlmostFull',
        '1303':    'mediaPathMediaTrayFull',
        '1501':    'interpreterMemoryIncrease',
        '1502':    'interpreterMemoryDecrease',
        '1503':    'interpreterCartridgeAdded',
        '1504':    'interpreterCartridgeDeleted',
        '1505':    'interpreterResourceAdded',
        '1506':    'interpreterResourceDeleted',
        '1507':    'interpreterResourceUnavailable',
        '1509':    'interpreterComplexPageEncountered',
        '1801':    'alertRemovalOfBinaryChangeEntry',
        }

    # The level of severity of this alert table entry
    PrtAlertSeverityLevelTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '1':    'other',
        '3':    'critical',
        '4':    'warning',
        '5':    'warningBinaryChangeEvent',
        }



    # was cartUnit
    # Unit of this marker supply container/receptacle
    PrtMarkerSuppliesSupplyUnitTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
         '1': 'other',
         '2': 'unknown',
         '3': 'tenThousandthsOfInches',
         '4': 'micrometers',
         '7': 'impressions',
         '8': 'sheets',
         '11': 'hours',
         '12': 'thousandthsOfOunces',
         '13': 'tenthsOfGrams',
         '14': 'hundrethsOfFluidOunces',
         '15': 'tenthsOfMilliliters',
         '16': 'feet',
         '17': 'meters',
         '18': 'items',
         '19': 'percent',
         }

    # Synonym
    PrtCapacityUnitTC = PrtMarkerSuppliesSupplyUnitTC;

    # The unit that will be used by the printer when reporting
    # counter values for this marking sub-unit
    PrtMarkerCounterUnitTC = {
        'na':    'UNKNOWN',    # TO NOT BREAK UNSUPPORTED PRINTERS
        '3':    'tenThousandthsOfInches',
        '4':    'micrometers',
        '5':    'characters',
        '6':    'lines',
        '7':    'impressions',
        '8':    'sheets',
        '9':    'dotRow',
        '11':    'hours',
        '16':    'feet',
        '17':    'meters',
        }


    # general info
    prtGeneral_columns = {
        '.16': 'prtGeneralPrinterName',    # printer name
        '.17': 'prtGeneralSerialNumber',    # S/N ex. JPBTB16GDH
        '.18': 'prtAlertCriticalEvents',    # number of critical events counted
        '.19': 'prtAlertAllEvents',        # total number of events counted
    }

    # input trays
    prtInput_columns = {
        '.2.1': 'prtInputTypeTC',            # Input Type
        '.8.1': 'prtCapacityUnitTC',        # capacity unit ex. sheets
        '.9.1': 'prtInputMaxCapacity',        # max capacity
        '.10.1': 'prtInputCurrentLevel',    # current capacity level
        '.12.1': 'prtInputMediaName',        # media name ex.Plain or any
        '.13.1': 'prtInputName',            # input media name ex. Tray 1
        '.15.1': 'prtInputModel',            # input model
        '.18.1': 'prtInputDescription',      # input supply description
    }
    
    prtMarkerSupplies_columns = {
         '.2.1': 'prtMarkerSuppliesMarkerIndex', # snmp index
         '.3.1': 'prtMarkerSuppliesColorantIndex', # snmp index
         '.5.1': 'prtMarkerSuppliesTypeTC', # see prtMarkerSuppliesType
         '.6.1': 'prtMarkerSuppliesDescription',  # "ex. "Black Toner Cartridge HP Q6000A""
         '.7.1': 'prtMarkerSuppliesSupplyUnitTC', # see PrtMarkerSuppliesSupplyUnitTC
         '.8.1': 'prtMarkerSuppliesMaxCapacity',  # Max level
         '.9.1': 'prtMarkerSuppliesLevel', # current level
         }
    
    prtMarkerColorant_columns = {
        '.2.1': 'prtMarkerColorantIndex', #snmp index
        '.4.1': 'prtMarkerColorantValue', # color ex. "black"
        }
    
    snmpGetTableMaps = (
        ## general info about printers - if supported
        GetTableMap('prtGeneral', '.1.3.6.1.2.1.43.5.1.1', prtGeneral_columns),

        ## get all input tray information - if supported
        GetTableMap('prtInput', '.1.3.6.1.2.1.43.8.2.1', prtInput_columns),

        ## get all printer supplies like toners, power, etc
        GetTableMap('prtMarkerSupplies', '.1.3.6.1.2.1.43.11.1.1', prtMarkerSupplies_columns),

		## get the table that defines the colors for toners
        GetTableMap('prtMarkerColorant', '.1.3.6.1.2.1.43.12.1.1', prtMarkerColorant_columns),
    )

    rgbColorCodes = {
        'na': 'CC0000',
        'other': 'CC0000',
        'unknown': 'CC0000',
        'white': 'FFFFFF',
        'red': 'CC3333',
        'green': '339933',
        'blue': '336699',
        'cyan': '00E6E6',
        'magenta': 'E600E6',
        'yellow': 'E6E600',
        'black': '000000',
    }
    
    def process(self, device, results, log):
        
        log.info('processing %s for device %s', self.name(), device.id)
        mapSupplies = self.relMap()
        mapToners = self.relMap()
        mapTrays = self.relMap()
        mapGeneral = self.objectMap()
        
        # put the output of the SNMP results in two variables for easy reading
        # getOtherOID = output of OIDs we didn't request
        # getMyOID = output of OIDs we request
        getOtherOID, getMyOID = results
        log.debug("getOtherOID table = %s ", getOtherOID)
        log.debug("getMyOID table = %s ", getMyOID)
        
        # put each of our requested tables in separate variables for ease of reading
        tblGeneral = getMyOID.get("prtGeneral")
        tblTrays = getMyOID.get("prtInput")
        tblSupplies = getMyOID.get("prtMarkerSupplies")
        tblColors = getMyOID.get("prtMarkerColorant")

        # if none of the tables have any output the return empty
        if not (tblGeneral or tblTrays or tblSupplies or tblColors):
            log.warn('Device %s for the %s plugin does not support the PrinterMIB for general info, toners, supplies or colors', device.id, self.name() )
            return

        # for each table print some output if it's supported
        if tblGeneral:
            log.info('Device %s for the %s plugin supports PrinterMIB general info', device.id, self.name())
            log.debug('tblGeneral = %s', tblGeneral)
            mapGeneral = self.processTblGeneral(tblGeneral, log)
        if tblTrays:
            log.info('Device %s for the %s plugin supports PrinterMIB info trays', device.id, self.name())
            log.debug('tblTrays = %s', tblTrays)
            mapTrays = self.processTblTrays(tblTrays, log)
        if tblSupplies or tblColors:
            if tblSupplies:
                log.info('Device %s for the %s plugin supports PrinterMIB supplies', device.id, self.name())
                log.debug('tblSupplies = %s', tblSupplies)
            if tblColors:
                log.info('Device %s for the %s plugin supports PrinterMIB color toners', device.id, self.name())
                log.debug('tblColors = %s', tblColors)
            mapSupplies, mapToners = self.processTblSupplies(tblSupplies, tblColors, log)

        # now return all our results for the different components        
        return mapGeneral, mapSupplies, mapToners, mapTrays


    def processTblGeneral(self, tblGeneral, log):
        # put the info in a Printer objectMap
        tempObj = self.objectMap(tblGeneral["1"])
        # if a general sn or printer name is found then re-write HWSerialNumber + HWTag
        if tempObj.prtGeneralSerialNumber:
            tempObj.setHWSerialNumber = tempObj.prtGeneralSerialNumber
            log.debug("Found a general serial number, resetting setHWSerialNumber")
        if tempObj.prtGeneralPrinterName:
            tempObj.setHWTag = tempObj.prtGeneralPrinterName
            log.debug("Found a general printer name, resetting setHWTag")
        tempObj.modname = "ZenPacks.TwoNMS.PrinterMIB.Printer"
        return tempObj


    # get a relationshipMap for the printer input trays if supported
    def processTblTrays(self, tblTrays, log):
        mapTrays = RelationshipMap(modname='ZenPacks.TwoNMS.PrinterMIB.PrinterTray', relname='printermibtray')
        
        # iterate each tray and translate the mibs
        for trayId, trayData in tblTrays.iteritems():
            # create an input Tray object
            trayObj = self.objectMap(trayData)
            trayObj.id = self.prepId(trayId)

            # translate prtInputTypeTC
            try:
                if (self.PrtInputTypeTC[str(trayObj.prtInputTypeTC)] != None):
                    trayObj.prtInputType = self.PrtInputTypeTC[str(trayObj.prtInputTypeTC)]
            except AttributeError:
                log.warn("Tray does not support the prtInputTypeTC oid")
                trayObj.prtInputType = self.PrtInputTypeTC['na']
                continue

            # translate PrtCapacityUnitTC
            try:
                if (self.PrtCapacityUnitTC[str(trayObj.prtCapacityUnitTC)] != None):
                    trayObj.prtCapacityUnit = self.PrtCapacityUnitTC[str(trayObj.prtCapacityUnitTC)]
            except AttributeError:
                log.warn("Tray does not support the PrtCapacityUnitTC oid")
                trayObj.prtCapacityUnit = self.prtCapacityUnitTC['na']
                continue

            # add a percentage value of the usage
            try:
                if (trayObj.prtInputMaxCapacity != 0):
                    trayObj.usagepct = "{0:.0f} %".format(100 - (float(trayObj.prtInputCurrentLevel)/trayObj.prtInputMaxCapacity * 100))
            except:
                log.warn("Error calculating the usage percentage.")
                trayObj.usagepct = -1
                #continue

            # assign object to the relationsipMap
            trayObj.modname = "ZenPacks.TwoNMS.PrinterMIB.PrinterTray"
            trayObj.supplyId = trayObj.id
            trayObj.snmpindex = trayObj.id
            log.debug("New input tray found: %s", trayObj)
            mapTrays.append(trayObj)
            
        return mapTrays




    # combine the supplies + color tables and return 
    # a relationshipMap for all supplies
    # and a relationshipMap for all the ink cartridges (toners)
    def processTblSupplies(self, tblSupplies, tblColors, log):

        # initialize seperate maps for toners and other supplies
        # use RelationshipMap() because I want to specify the relationship since there's only 1 modeler
        # for more components
        mapSupplies = RelationshipMap(modname='ZenPacks.TwoNMS.PrinterMIB.PrinterSupply', relname='printermibsupply')
        mapToners = RelationshipMap(modname='ZenPacks.TwoNMS.PrinterMIB.PrinterToner', relname='printermibtoner')


        # simplify the tblColors map to make the code easier to read
        colors = {}
        for cId, cInfo in tblColors.iteritems():
            colors[str(cId)] = cInfo['prtMarkerColorantValue']
        log.debug("colors table = %s", colors)

        # go over each supply and classifiy as toner (ink cartridge) or other supply
        for supplyId, supplyData in tblSupplies.iteritems():
	
            # create a temp map first because we don't know yet what kind of supply we have
            mapTemp = self.objectMap(supplyData)
            mapTemp.id = self.prepId(supplyId)
            isToner = False

            # check if it's a toner or other supply, color toners have prtMarkerSuppliesColorantIndex > 0
            # translate the color id
            try:
                if mapTemp.prtMarkerSuppliesColorantIndex > 0:
                    isToner = True
                    # overwrite the index with the color value
                    if (colors[str(mapTemp.prtMarkerSuppliesColorantIndex)] != None):
                        mapTemp.prtMarkerSuppliesColorantValue = colors[str(mapTemp.prtMarkerSuppliesColorantIndex)]
                        mapTemp.rgbColorCode = self.rgbColorCodes[mapTemp.prtMarkerSuppliesColorantValue.lower()]
                    else:
                        mapTemp.prtMarkerSuppliesColorantValue = self.PrtConsoleColorTC['na']
            except AttributeError:
                log.warn("Supply does not support the prtMarkerSuppliesColorantIndex oid")
                mapTemp.prtMarkerSuppliesColorantValue = self.PrtConsoleColorTC['na']
                mapTemp.rgbColorCode = self.rgbColorCodes['na']
                continue
            except KeyError:
                log.warn("KeyError occurred")
                mapTemp.prtMarkerSuppliesColorantValue = self.PrtConsoleColorTC['na']
                mapTemp.rgbColorCode = self.rgbColorCodes['na']
                #continue
            except:
                log.warn("Unknown error occurred")
                mapTemp.prtMarkerSuppliesColorantValue = self.PrtConsoleColorTC['na']
                mapTemp.rgbColorCode = self.rgbColorCodes['na']
                #continue

            # translate the supply unit type id
            try:
                if (self.PrtMarkerSuppliesSupplyUnitTC[str(mapTemp.prtMarkerSuppliesSupplyUnitTC)] != None):
                    mapTemp.prtMarkerSuppliesSupplyUnit = self.PrtMarkerSuppliesSupplyUnitTC[str(mapTemp.prtMarkerSuppliesSupplyUnitTC)]
            except AttributeError:
                log.warn("Supply does not support the prtMarkerSuppliesSupplyUnitTC oid")
                mapTemp.prtMarkerSuppliesSupplyUnit = self.PrtMarkerSuppliesSupplyUnitTC['na']
                continue

            # translate the supply type id
            try:
                if (self.PrtMarkerSuppliesTypeTC[str(mapTemp.prtMarkerSuppliesTypeTC)] != None):
                    mapTemp.prtMarkerSuppliesType = self.PrtMarkerSuppliesTypeTC[str(mapTemp.prtMarkerSuppliesTypeTC)]
            except AttributeError:
                log.warn("Supply does not support the prtMarkerSuppliesTypeTC oid")
                mapTemp.prtMarkerSuppliesType = self.PrtMarkerSuppliesTypeTC['na']
                continue
            
            # add a percentage value of the usage
            try:
                if (mapTemp.prtMarkerSuppliesMaxCapacity != 0):
                    mapTemp.usagepct = "{0:.0f} %".format(100 - (float(mapTemp.prtMarkerSuppliesLevel)/mapTemp.prtMarkerSuppliesMaxCapacity * 100))
            except:
                mapTemp.usagepct = -1
                #continue

            # add the temp map to the toner or supply map
            if (isToner == True):
                mapTemp.modname = "ZenPacks.TwoNMS.PrinterMIB.PrinterToner"
                mapTemp.supplyId = mapTemp.id
                mapTemp.snmpindex = mapTemp.id
                log.debug("New toner found: %s", mapTemp)
                mapToners.append(mapTemp)
            else:
                mapTemp.modname = "ZenPacks.TwoNMS.PrinterMIB.PrinterSupply"
                mapTemp.supplyId = mapTemp.id
                mapTemp.snmpindex = mapTemp.id
                log.debug("New supply found: %s", mapTemp)
                mapSupplies.append(mapTemp)

        return mapSupplies, mapToners


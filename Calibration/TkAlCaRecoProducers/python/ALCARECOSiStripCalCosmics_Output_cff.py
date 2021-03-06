import FWCore.ParameterSet.Config as cms

# AlCaReco for track based calibration using Cosmics events
OutALCARECOSiStripCalCosmics_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalCosmics')
    ),
    outputCommands = cms.untracked.vstring( 
        'keep *_ALCARECOSiStripCalCosmics_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*',
        'keep DetIdedmEDCollection_siStripDigis_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_TriggerResults_*_*')
    )

import copy
OutALCARECOSiStripCalCosmics=copy.deepcopy(OutALCARECOSiStripCalCosmics_noDrop)
OutALCARECOSiStripCalCosmics.outputCommands.insert(0,"drop *")

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.register('sampletype', "DATA", VarParsing.multiplicity.singleton, VarParsing.varType.string, "sampletype: DATA/MC/PrivateMC")
options.register('ScaleIDRange', "-999,-999", VarParsing.multiplicity.singleton, VarParsing.varType.string, "PDF Scale ID range: 1,9")
options.register('PDFErrorIDRange', "-999,-999", VarParsing.multiplicity.singleton, VarParsing.varType.string, "PDF Error ID range: 1001,1100")
options.register('PDFAlphaSIDRange', "-999,-999", VarParsing.multiplicity.singleton, VarParsing.varType.string, "PDF AlphaS ID range: 1101,1102")
options.register('PDFAlphaSScaleValue', "-999,-999", VarParsing.multiplicity.singleton, VarParsing.varType.string, "PDF AlphaS Scale values: 1.5,1.5")
options.register('year',-1, VarParsing.multiplicity.singleton, VarParsing.varType.string, "year: Which year? 2016preVFP, 2016postVFP, 2017, 2018")
options.parseArguments()

import sys

Is2016preVFP = False
Is2016postVFP = False
Is2017 = False
Is2018 = False
if options.year=='2016preVFP':
  Is2016preVFP = True
if options.year=='2016postVFP':
  Is2016postVFP = True
elif options.year=='2017':
  Is2017 = True
elif options.year=='2018':
  Is2018 = True
else:
  ErrorMgs = "year is not correct; "+str(options.year)
  sys.exit(ErrorMgs)

isMC = True
if "data" in options.sampletype.lower():
  isMC = False
if "mc" in options.sampletype.lower():
  isMC = True
isPrivateSample = False
if "private" in options.sampletype.lower():
  isPrivateSample = True

options.outputFile = "SKFlatNtuple.root"
if len(options.inputFiles)==0:
  if Is2016preVFP:
    if isMC:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/80DBA5F3-16BE-E811-854E-A0369FC5E530.root')
      options.outputFile = "SKFlatNtuple_2016_MC.root"
    else:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/306DAB6C-068C-E811-9E30-0242AC1C0501.root')
      options.outputFile = "SKFlatNtuple_2016_DATA.root"
  if Is2016postVFP:
    if isMC:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/120000/80DBA5F3-16BE-E811-854E-A0369FC5E530.root')
      options.outputFile = "SKFlatNtuple_2016_MC.root"
    else:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/306DAB6C-068C-E811-9E30-0242AC1C0501.root')
      options.outputFile = "SKFlatNtuple_2016_DATA.root"
  elif Is2017:
    if isMC:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/mc/RunIISummer19UL17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/260000/04B074CC-43FC-6045-ACD2-D49AC762E5A6.root')
      options.outputFile = "SKFlatNtuple_2017_MC.root"
    else:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/210000/49E82EBF-E7AF-8645-B5C7-6F2B208F3F5F.root')
      options.outputFile = "SKFlatNtuple_2017_DATA.root"
  elif Is2018:
    if isMC:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/120000/B3F93EA2-04C6-E04E-96AF-CB8FAF67E6BA.root')
      options.outputFile = "SKFlatNtuple_2018_MC.root"
    else:
      options.inputFiles.append('root://cms-xrd-global.cern.ch//store/data/Run2018A/SingleMuon/MINIAOD/17Sep2018-v2/00000/11697BCC-C4AB-204B-91A9-87F952F9F2C6.root')
      options.outputFile = "SKFlatNtuple_2018_DATA.root"

ScaleIDRange = [int(options.ScaleIDRange.split(',')[0]), int(options.ScaleIDRange.split(',')[1])]
PDFErrorIDRange = [int(options.PDFErrorIDRange.split(',')[0]), int(options.PDFErrorIDRange.split(',')[1])]
PDFAlphaSIDRange = [int(options.PDFAlphaSIDRange.split(',')[0]), int(options.PDFAlphaSIDRange.split(',')[1])]
PDFAlphaSScaleValue = [float(options.PDFAlphaSScaleValue.split(',')[0]), float(options.PDFAlphaSScaleValue.split(',')[1])]

print 'isMC = '+str(isMC)
print 'isPrivateSample = '+str(isPrivateSample)
print 'ScaleIDRange = ',
print ScaleIDRange
print 'PDFErrorIDRange = ',
print PDFErrorIDRange
print 'PDFAlphaSIDRange = ',
print PDFAlphaSIDRange
print 'PDFAlphaSScaleValue = ',
print PDFAlphaSScaleValue
print 'year = '+str(options.year)


#### Global Tag
#### https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable

GT_MC = ''
GT_DATA = ''

if Is2016preVFP:
  GT_MC = '106X_mcRun2_asymptotic_preVFP_v9'
  GT_DATA = '106X_dataRun2_v32'
if Is2016postVFP:
  GT_MC = '106X_mcRun2_asymptotic_v15'
  GT_DATA = '106X_dataRun2_v32'
elif Is2017:
  GT_MC = '106X_mc2017_realistic_v8'
  GT_DATA = '106X_dataRun2_v32'
elif Is2018:
  GT_MC = '106X_upgrade2018_realistic_v15_L1v1'
  GT_DATA = '106X_dataRun2_v32'

print 'GT_MC = '+GT_MC
print 'GT_DATA = '+GT_DATA

####################################################################################################################

process = cms.Process("NTUPLE")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

## Options and Output Report
process.options   = cms.untracked.PSet( 
  SkipEvent = cms.untracked.vstring('ProductNotFound'),
  wantSummary = cms.untracked.bool(True) 
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring( options.inputFiles ),
  #skipEvents=cms.untracked.uint32(5),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

# -- Geometry and Detector Conditions (needed for a few patTuple production steps) -- #
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
#process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

# -- Global Tags -- #
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

if isMC == True:
  process.GlobalTag.globaltag = cms.string(GT_MC)
else:
  process.GlobalTag.globaltag = cms.string(GT_DATA) #prompt-reco global tag


process.TFileService = cms.Service("TFileService",
  fileName = cms.string( options.outputFile )
)

#################
# -- DY Tree -- #
#################
from SKFlatMaker.SKFlatMaker.SKFlatMaker_cfi import *

process.recoTree = SKFlatMaker.clone()
process.recoTree.DataYear = cms.untracked.int32(int(options.year[0:4]))
process.recoTree.DebugLevel = cms.untracked.int32(0)
process.recoTree.StoreHLTObjectFlag = False ##FIXME

# -- Objects without Corrections -- # 
process.recoTree.Muon = cms.untracked.InputTag("slimmedMuons") # -- miniAOD -- #
process.recoTree.Electron = cms.untracked.InputTag("slimmedElectrons") # -- miniAOD -- #
process.recoTree.Photon = cms.untracked.InputTag("slimmedPhotons") # -- miniAOD -- #
process.recoTree.Jet = cms.untracked.InputTag("slimmedJets") # -- miniAOD -- #
process.recoTree.FatJet = cms.untracked.InputTag("slimmedJetsAK8")
process.recoTree.MET = cms.InputTag("slimmedMETs")
process.recoTree.GenParticle = cms.untracked.InputTag("prunedGenParticles") # -- miniAOD -- #

process.recoTree.ScaleIDRange = cms.untracked.vint32(ScaleIDRange)
process.recoTree.PDFErrorIDRange = cms.untracked.vint32(PDFErrorIDRange)
process.recoTree.PDFAlphaSIDRange = cms.untracked.vint32(PDFAlphaSIDRange)
process.recoTree.PDFAlphaSScaleValue = cms.untracked.vdouble(PDFAlphaSScaleValue)

if isPrivateSample:
  process.recoTree.LHEEventProduct = cms.untracked.InputTag("source")
  process.recoTree.LHERunInfoProduct = cms.untracked.InputTag("source")

process.recoTree.rho = cms.untracked.InputTag("fixedGridRhoFastjetAll")
process.recoTree.conversionsInputTag = cms.untracked.InputTag("reducedEgamma:reducedConversions") # -- miniAOD -- #

# -- for Track & Vertex -- #
process.recoTree.PrimaryVertex = cms.untracked.InputTag("offlineSlimmedPrimaryVertices") # -- miniAOD -- #

# -- Else -- #
process.recoTree.PileUpInfo = cms.untracked.InputTag("slimmedAddPileupInfo")

# -- Filters -- #
process.recoTree.ApplyFilter = False

# -- Store Flags -- #
process.recoTree.StoreMuonFlag = True
process.recoTree.StoreElectronFlag = True
process.recoTree.StorePhotonFlag = True # -- photon part should be updated! later when it is necessary -- #
process.recoTree.StoreJetFlag = True
process.recoTree.StoreMETFlag = True
process.recoTree.StoreGENFlag = isMC
process.recoTree.KeepAllGen = isMC
process.recoTree.StoreLHEFlag = isMC

#### EGamma ####

myEleID =  [
'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV70_cff',
'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff',
'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V2_cff',
'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V2_cff',
]
myPhoID =  [
'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Fall17_94X_V2_cff',
'RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Fall17_94X_V2_cff',
]

if Is2016preVFP:

  print "################"
  print "Running 2016preVFP"
  print "################"

  ###########################
  #### Rerun EGammaPostReco
  ###########################

  from EgammaUser.EgammaPostRecoTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
  setupEgammaPostRecoSeq(process,
                         runVID=True,
                         era='2016-Legacy',
                         eleIDModules=myEleID,
                         phoIDModules=myPhoID,
                         #runEnergyCorrections=False ## when False, VID not reran.. I dunno why..
  )

  #################
  ### Reapply JEC
  ### https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrPatJets
  #################

  from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

  #### AK4

  updateJetCollection(
     process,
     jetSource = cms.InputTag('slimmedJets'),
     labelName = 'UpdatedJECslimmedJets',
     jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
  )
  process.recoTree.Jet = cms.untracked.InputTag("updatedPatJetsUpdatedJECslimmedJets")

  #### AK8

  updateJetCollection(
     process,
     jetSource = cms.InputTag('slimmedJetsAK8'),
     labelName = 'UpdatedJECslimmedJetsAK8',
     jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
  )
  process.recoTree.FatJet = cms.untracked.InputTag("updatedPatJetsUpdatedJECslimmedJetsAK8")

  #### JEC Sequence

  process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJECslimmedJets *
    process.updatedPatJetsUpdatedJECslimmedJets *
    process.patJetCorrFactorsUpdatedJECslimmedJetsAK8 *
    process.updatedPatJetsUpdatedJECslimmedJetsAK8
  )

  #################
  #### Update MET
  #### https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription
  #### This is independent of jecSequence, but it rather reapply JEC/JER using GT withing this MET corrector module
  #################

  from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
  runMetCorAndUncFromMiniAOD(process,
                           isData=(not isMC),
                           )


  #########################
  #### L1Prefire reweight
  #########################

  from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
  process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
    DataEra = cms.string("2016BtoH"), #Use 2016BtoH for 2016
    ThePhotons = cms.InputTag("slimmedPhotons"),
    TheJets = cms.InputTag("slimmedJets"),
    UseJetEMPt = cms.bool(True),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings = False)

  ###########################
  #### Rochester correction
  ###########################
  process.recoTree.roccorPath = cms.string('SKFlatMaker/SKFlatMaker/data/roccor.Run2.v3/RoccoR2016.txt')

  ###########
  #### Path
  ###########

  process.p = cms.Path(
    process.egammaPostRecoSeq *
    process.jecSequence *
    process.fullPatMetSequence
  )
  if isMC:
    process.recoTree.StoreL1PrefireFlag = cms.untracked.bool(True)
    process.p *= process.prefiringweight

  process.p *= process.recoTree

elif Is2017:

  print "################"
  print "Running 2017"
  print "################"

  ###########################
  #### Rerun EGammaPostReco
  ###########################
  # Not needed for Summer20MiniAODv2 since it have already scale and smearing corrections
  # But, for Summer19MiniAOD.
  # https://twiki.cern.ch/twiki/bin/view/CMS/EgammaUL2016To2018
  from EgammaUser.EgammaPostRecoTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
  setupEgammaPostRecoSeq(process,
                         runVID=False, #saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
                         era='2017-UL',
#                         eleIDModules=myEleID,
#                         phoIDModules=myPhoID,
  )
  #a sequence egammaPostRecoSeq has now been created and should be added to your path, eg process.p=cms.Path(process.egammaPostRecoSeq)

  ###########################
  #### MET EE Noise
  ###########################
  # Not needed for UL.
  # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetMET#Quick_links_to_current_recommend

  #################
  ### Reapply JEC
  ### https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrPatJets
  #################
  # JEC loaded by global tag. For UL17, global tag including JEC is not yet announced.
  # https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC#2017_Data

  from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

  #### AK4

  updateJetCollection(
     process,
     jetSource = cms.InputTag('slimmedJets'),
     labelName = 'UpdatedJECslimmedJets',
     jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
  )
  process.recoTree.Jet = cms.untracked.InputTag("updatedPatJetsUpdatedJECslimmedJets")

  #### AK8

  updateJetCollection(
     process,
     jetSource = cms.InputTag('slimmedJetsAK8'),
     labelName = 'UpdatedJECslimmedJetsAK8',
     jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
  )
  process.recoTree.FatJet = cms.untracked.InputTag("updatedPatJetsUpdatedJECslimmedJetsAK8")

  #### JEC Sequence

  process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJECslimmedJets *
    process.updatedPatJetsUpdatedJECslimmedJets *
    process.patJetCorrFactorsUpdatedJECslimmedJetsAK8 *
    process.updatedPatJetsUpdatedJECslimmedJetsAK8
  )

  ##########
  #### JER
  #### https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution#2017_data
  ##########
  # currently the JER-SF (in the following MC .tar or .db files) are not evaluated separately for each Era
  # they are NOT in a Pt-dependent format, the previously strong pt dependency at high eta is however observed to be reduced in UL

  # Only for AK4 currently
  process.recoTree.AK4Jet_JER_PtRes_filepath = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Summer19UL17_JRV2_MC/Summer19UL17_JRV2_MC_PtResolution_AK4PFchs.txt')
  process.recoTree.AK4Jet_JER_SF_filepath    = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Summer19UL17_JRV2_MC/Summer19UL17_JRV2_MC_SF_AK4PFchs.txt')

  # No JER for AK8Jet. Use old one temporary.
  process.recoTree.AK8Jet_JER_PtRes_filepath = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Fall17_V3_MC/Fall17_V3_MC_PtResolution_AK8PFPuppi.txt')
  process.recoTree.AK8Jet_JER_SF_filepath    = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Fall17_V3_MC/Fall17_V3_MC_SF_AK8PFPuppi.txt')

  #######################################
  #### ecalBadCalibReducedMINIAODFilter
  #### https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#How_to_run_ecal_BadCalibReducedM
  ########################################
  # WIP for UL. comment out for now. check process.p and SKFlatMaker.cc when updating
#
#  process.load('RecoMET.METFilters.ecalBadCalibFilter_cfi')
#
#  baddetEcallist = cms.vuint32(
#    [872439604,872422825,872420274,872423218,
#     872423215,872416066,872435036,872439336,
#     872420273,872436907,872420147,872439731,
#     872436657,872420397,872439732,872439339,
#     872439603,872422436,872439861,872437051,
#     872437052,872420649,872421950,872437185,
#     872422564,872421566,872421695,872421955,
#     872421567,872437184,872421951,872421694,
#     872437056,872437057,872437313,872438182,
#     872438951,872439990,872439864,872439609,
#     872437181,872437182,872437053,872436794,
#     872436667,872436536,872421541,872421413,
#     872421414,872421031,872423083,872421439]
#  )
#
#  process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter(
#    "EcalBadCalibFilter",
#    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
#    ecalMinEt        = cms.double(50.),
#    baddetEcal    = baddetEcallist, 
#    taggingMode = cms.bool(True),
#    debug = cms.bool(False)
#  )

  #########################
  #### L1Prefire reweight
  #### https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1ECALPrefiringWeightRecipe
  #########################

  from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
  process.prefiringweight= l1ECALPrefiringWeightProducer.clone(
    TheJets = cms.InputTag("updatedPatJetsUpdatedJECslimmedJets"), #this should be the slimmedJets collection with up to date JECs !
    L1Maps = cms.string("L1PrefiringMaps_WithUL17.root"),
    DataEra = cms.string('UL2017BtoF'),
    UseJetEMPt = cms.bool(False),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings = False
    )

  ###########################
  #### Rochester correction
  ###########################
  process.recoTree.roccorPath = cms.string('SKFlatMaker/SKFlatMaker/data/roccor.Run2.v5/RoccoR2017UL.txt')

  ###########
  #### Path
  ###########

  process.p = cms.Path(
    process.egammaPostRecoSeq *
    process.jecSequence *
    process.fullPatMetSequenceModifiedMET 
#   * process.ecalBadCalibReducedMINIAODFilter
  )
  if isMC:
    process.recoTree.StoreL1PrefireFlag = cms.untracked.bool(True)
    process.p *= process.prefiringweight

  process.p *= process.recoTree

elif Is2018:

  print "################"
  print "Running 2018"
  print "################"

  ###########################
  #### Rerun EGammaPostReco
  ###########################

  from EgammaUser.EgammaPostRecoTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
  setupEgammaPostRecoSeq(process,
                         era='2018-Prompt')  
  #a sequence egammaPostRecoSeq has now been created and should be added to your path, eg process.p=cms.Path(process.egammaPostRecoSeq)

  #################
  ### Reapply JEC
  ### https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrPatJets
  #################

  from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

  #### AK4

  updateJetCollection(
     process,
     jetSource = cms.InputTag('slimmedJets'),
     labelName = 'UpdatedJECslimmedJets',
     jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
  )
  process.recoTree.Jet = cms.untracked.InputTag("updatedPatJetsUpdatedJECslimmedJets")

  #### AK8

  updateJetCollection(
     process,
     jetSource = cms.InputTag('slimmedJetsAK8'),
     labelName = 'UpdatedJECslimmedJetsAK8',
     jetCorrections = ('AK8PFPuppi', cms.vstring(['L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  # Update: Safe to always add 'L2L3Residual' as MC contains dummy L2L3Residual corrections (always set to 1)
  )
  process.recoTree.FatJet = cms.untracked.InputTag("updatedPatJetsUpdatedJECslimmedJetsAK8")

  #### JEC Sequence

  process.jecSequence = cms.Sequence(
    process.patJetCorrFactorsUpdatedJECslimmedJets *
    process.updatedPatJetsUpdatedJECslimmedJets *
    process.patJetCorrFactorsUpdatedJECslimmedJetsAK8 *
    process.updatedPatJetsUpdatedJECslimmedJetsAK8
  )

  ##########
  #### JER
  ##########

  process.recoTree.AK4Jet_JER_PtRes_filepath = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Autumn18_V7b_MC/Autumn18_V7b_MC_PtResolution_AK4PFchs.txt')
  process.recoTree.AK4Jet_JER_SF_filepath    = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Autumn18_V7b_MC/Autumn18_V7b_MC_SF_AK4PFchs.txt')
  process.recoTree.AK8Jet_JER_PtRes_filepath = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Autumn18_V7b_MC/Autumn18_V7b_MC_PtResolution_AK8PFPuppi.txt')
  process.recoTree.AK8Jet_JER_SF_filepath    = cms.string('SKFlatMaker/SKFlatMaker/data/JRDatabase/textFiles/Autumn18_V7b_MC/Autumn18_V7b_MC_SF_AK8PFPuppi.txt')

  #################
  #### Update MET
  #### https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription
  #### This is independent of jecSequence, but it rather reapply JEC/JER using GT withing this MET corrector module
  #################

  from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
  runMetCorAndUncFromMiniAOD(process,
                           isData=(not isMC),
                           )

  #######################################
  #### ecalBadCalibReducedMINIAODFilter
  #### https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#How_to_run_ecal_BadCalibReducedM
  ########################################

  process.load('RecoMET.METFilters.ecalBadCalibFilter_cfi')

  baddetEcallist = cms.vuint32(
    [872439604,872422825,872420274,872423218,
     872423215,872416066,872435036,872439336,
     872420273,872436907,872420147,872439731,
     872436657,872420397,872439732,872439339,
     872439603,872422436,872439861,872437051,
     872437052,872420649,872421950,872437185,
     872422564,872421566,872421695,872421955,
     872421567,872437184,872421951,872421694,
     872437056,872437057,872437313,872438182,
     872438951,872439990,872439864,872439609,
     872437181,872437182,872437053,872436794,
     872436667,872436536,872421541,872421413,
     872421414,872421031,872423083,872421439]
  )

  process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter(
    "EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal    = baddetEcallist,
    taggingMode = cms.bool(True),
    debug = cms.bool(False)
  )

  ###########################
  #### Rochester correction
  ###########################
  process.recoTree.roccorPath = cms.string('SKFlatMaker/SKFlatMaker/data/roccor.Run2.v3/RoccoR2018.txt')

  ###########
  #### Path
  ###########

  process.p = cms.Path(
    process.egammaPostRecoSeq *
    process.jecSequence *
    process.fullPatMetSequence *
    process.ecalBadCalibReducedMINIAODFilter *
    process.recoTree
  )

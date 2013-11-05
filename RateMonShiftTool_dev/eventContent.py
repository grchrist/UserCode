
full = [
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*']

requiredEventContent={
    'A': full,
    'B': full,
    'AlcaPi0': [
      'keep *_hltAlCaEtaEBUncalibrator_*_*',
      'keep *_hltAlCaEtaEEUncalibrator_*_*',
      'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*',
      'keep *_hltAlCaPi0EBUncalibrator_*_*',
      'keep *_hltAlCaPi0EEUncalibrator_*_*',
      'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*'],
    'AlcaPhiSym': [
      'keep *_hltAlCaPhiSymUncalibrator_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*'],
    'AlcaLumiPixel': [
      'keep *_hltFEDSelectorLumiPixels_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*'],
    'Calibration': [#'drop *_hlt*_*_*',
      'keep *_hltDTCalibrationRaw_*_*',
      'keep *_hltEcalCalibrationRaw_*_*',
      'keep *_hltHcalCalibrationRaw_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*'],
    'DQM': full,
    'EcalCalibration': [
      'keep *_hltEcalCalibrationRaw_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*'],
    'Express': full,
    'HLTDQM':  [
      'keep *_hltTriggerSummaryAOD_*_*',
      'keep DcsStatuss_hltScalersRawToDigi_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep LumiScalerss_hltScalersRawToDigi_*_*',
      'keep edmTriggerResults_*_*_*'],
    #'HLTMON':HLTMONContent,
    'NanoDST':[
      'keep *_hltFEDSelector_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep L1MuGMTReadoutCollection_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*'],
    'PhysicsDST':[
      'keep *_hltActivityPhotonClusterShape_*_*',
      'keep *_hltActivityPhotonEcalIso_*_*',
      'keep *_hltActivityPhotonHcalForHE_*_*',
      'keep *_hltActivityPhotonHcalIso_*_*',
      'keep *_hltCaloJetIDPassed_*_*',
      'keep *_hltElectronActivityDetaDphi_*_*',
      'keep *_hltHitElectronActivityTrackIsol_*_*',
      'keep *_hltKT6CaloJets_rho*_*',
      'keep *_hltL3MuonCandidates_*_*',
      'keep *_hltL3MuonCombRelIsolations_*_*',
      'keep *_hltMetClean_*_*',
      'keep *_hltMet_*_*',
      'keep *_hltPixelMatchElectronsActivity_*_*',
      'keep *_hltPixelVertices_*_*',
      'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*'],
    'RPCMON':[
      'keep *_hltCscSegments_*_*',
      'keep *_hltDt4DSegments_*_*',
      'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
      'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
      'keep *_hltMuonDTDigis_*_*',
      'keep *_hltMuonRPCDigis_*_*',
      'keep *_hltRpcRecHits_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep L1MuGMTCands_hltGtDigis_*_*',
      'keep L1MuGMTReadoutCollection_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*'],
    'TrackerCalibration':[
      'keep *_hltTrackerCalibrationRaw_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*'],
    }

HLTMONContent = [
      'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4L1HLTMatched_*_*',
      'keep *_hltDoublePFTau25TrackPt5MediumIsolationProng4_*_*',
      'keep *_hltDoublePFTau25TrackPt5MediumIsolation_*_*',
      'keep *_hltDoublePFTau25TrackPt5_*_*',
      'keep *_hltDoublePFTau25_*_*',
      'keep *_hltEle20CaloIdVTTrkIdTDphiFilter_*_*',
      'keep *_hltIter1Merged_*_*',
      'keep *_hltIter2Merged_*_*',
      'keep *_hltIter3Merged_*_*',
      'keep *_hltIter4Merged_*_*',
      'keep *_hltL1extraParticlesCentral_*_*',
      'keep *_hltL1extraParticlesNonIsolated_*_*',
      'keep *_hltL1extraParticlesTau_*_*',
      'keep *_hltL1extraParticles_*_*',
      'keep *_hltL1sDoubleTauJet44erorDoubleJetC64_*_*',
      'keep *_hltL1sL1EG18er_*_*',
      'keep *_hltL1sL1ETM36or40_*_*',
      'keep *_hltL1sMu16Eta2p1_*_*',
      'keep *_hltL3TkTracksFromL2_*_*',
      'keep *_hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoRhoFiltered0p15_*_*',
      'keep *_hltOverlapFilterEle20LooseIsoPFTau20OldVersion_*_*',
      'keep *_hltOverlapFilterIsoMu18LooseIsoPFTau20_*_*',
      'keep *_hltOverlapFilterIsoMu18PFTau25TrackPt5Prong4_*_*',
      'keep *_hltPFTau20IsoMuVertex_*_*',
      'keep *_hltPFTau20TrackLooseIso_*_*',
      'keep *_hltPFTau20Track_*_*',
      'keep *_hltPFTau20_*_*',
      'keep *_hltPFTau25TrackPt5MediumIsolationProng4IsoMuVertex_*_*',
      'keep *_hltPFTau25TrackPt5MediumIsolationProng4_*_*',
      'keep *_hltPFTau25TrackPt5MediumIsolation_*_*',
      'keep *_hltPFTau25TrackPt5_*_*',
      'keep *_hltPFTau25_*_*',
      'keep *_hltPFTau35TrackPt20LooseIsoProng2_*_*',
      'keep *_hltPFTau35TrackPt20LooseIso_*_*',
      'keep *_hltPFTau35TrackPt20_*_*',
      'keep *_hltPFTau35Track_*_*',
      'keep *_hltPFTau35_*_*',
      'keep *_hltPFTauEleVertex20_*_*',
      'keep *_hltPixelTracks_*_*',
      'keep *_hltPixelVertices3DbbPhi_*_*',
      'keep *_hltPixelVertices_*_*',
      'keep *_hltTriggerSummaryAOD_*_*',
      'keep *_hltTriggerSummaryRAW_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_rawDataRepacker_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep recoCaloJets_*_*_*',
      'keep recoCaloMETs_*_*_*',
      'keep recoCompositeCandidates_*_*_*',
      'keep recoElectrons_*_*_*',
      'keep recoIsolatedPixelTrackCandidates_*_*_*',
      'keep recoMETs_*_*_*',
      'keep recoPFJets_*_*_*',
      'keep recoPFTaus_*_*_*',
      'keep recoRecoChargedCandidates_*_*_*',
      'keep recoRecoEcalCandidates_*_*_*',
      'keep triggerTriggerEventWithRefs_*_*_*',
      'keep triggerTriggerEvent_*_*_*',
      'keep triggerTriggerFilterObjectWithRefs_*_*_*']

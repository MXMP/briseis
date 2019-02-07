# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

sysUpTime = {
    #    UP            .1.3.6.1.2.1.1.3.0					sysUpTimeInstance
    'UP.': '.1.3.6.1.2.1.1.3.0'
}

FWVer = {
    #    FW            .1.3.6.1.4.1.171.12.1.2.7.1.2			swMultiImageVersion
    'FW.': '.1.3.6.1.4.1.171.12.1.2.7.1.2.1'
}

Errors = {
    # RX_crc     .1.3.6.1.2.1.16.1.1.1.8    etherStatsCRCAlignErrors
    'RX_crc.1': '.1.3.6.1.2.1.16.1.1.1.8.1',
    'RX_crc.2': '.1.3.6.1.2.1.16.1.1.1.8.2',
    'RX_crc.3': '.1.3.6.1.2.1.16.1.1.1.8.3',
    'RX_crc.4': '.1.3.6.1.2.1.16.1.1.1.8.4',
    'RX_crc.5': '.1.3.6.1.2.1.16.1.1.1.8.5',
    'RX_crc.6': '.1.3.6.1.2.1.16.1.1.1.8.6',
    'RX_crc.7': '.1.3.6.1.2.1.16.1.1.1.8.7',
    'RX_crc.8': '.1.3.6.1.2.1.16.1.1.1.8.8',
    'RX_crc.9': '.1.3.6.1.2.1.16.1.1.1.8.9',
    'RX_crc.10': '.1.3.6.1.2.1.16.1.1.1.8.10',
}

RX_Undersize = {
    # RX_und     .1.3.6.1.2.1.16.1.1.1.9    etherStatsUndersizePkts
    'RX_und.1': '.1.3.6.1.2.1.16.1.1.1.9.1',
    'RX_und.2': '.1.3.6.1.2.1.16.1.1.1.9.2',
    'RX_und.3': '.1.3.6.1.2.1.16.1.1.1.9.3',
    'RX_und.4': '.1.3.6.1.2.1.16.1.1.1.9.4',
    'RX_und.5': '.1.3.6.1.2.1.16.1.1.1.9.5',
    'RX_und.6': '.1.3.6.1.2.1.16.1.1.1.9.6',
    'RX_und.7': '.1.3.6.1.2.1.16.1.1.1.9.7',
    'RX_und.8': '.1.3.6.1.2.1.16.1.1.1.9.8',
    'RX_und.9': '.1.3.6.1.2.1.16.1.1.1.9.9',
    'RX_und.10': '.1.3.6.1.2.1.16.1.1.1.9.10'
}

RX_Oversize = {
    # RX_over     .1.3.6.1.2.1.16.1.1.1.10    etherStatsOversizePkts
    'RX_over.1': '.1.3.6.1.2.1.16.1.1.1.10.1',
    'RX_over.2': '.1.3.6.1.2.1.16.1.1.1.10.2',
    'RX_over.3': '.1.3.6.1.2.1.16.1.1.1.10.3',
    'RX_over.4': '.1.3.6.1.2.1.16.1.1.1.10.4',
    'RX_over.5': '.1.3.6.1.2.1.16.1.1.1.10.5',
    'RX_over.6': '.1.3.6.1.2.1.16.1.1.1.10.6',
    'RX_over.7': '.1.3.6.1.2.1.16.1.1.1.10.7',
    'RX_over.8': '.1.3.6.1.2.1.16.1.1.1.10.8',
    'RX_over.9': '.1.3.6.1.2.1.16.1.1.1.10.9',
    'RX_over.10': '.1.3.6.1.2.1.16.1.1.1.10.10'
}

RX_Fragments = {
    # RX_frag     .1.3.6.1.2.1.16.1.1.1.11    etherStatsFragments
    'RX_frag.1': '.1.3.6.1.2.1.16.1.1.1.11.1',
    'RX_frag.2': '.1.3.6.1.2.1.16.1.1.1.11.2',
    'RX_frag.3': '.1.3.6.1.2.1.16.1.1.1.11.3',
    'RX_frag.4': '.1.3.6.1.2.1.16.1.1.1.11.4',
    'RX_frag.5': '.1.3.6.1.2.1.16.1.1.1.11.5',
    'RX_frag.6': '.1.3.6.1.2.1.16.1.1.1.11.6',
    'RX_frag.7': '.1.3.6.1.2.1.16.1.1.1.11.7',
    'RX_frag.8': '.1.3.6.1.2.1.16.1.1.1.11.8',
    'RX_frag.9': '.1.3.6.1.2.1.16.1.1.1.11.9',
    'RX_frag.10': '.1.3.6.1.2.1.16.1.1.1.11.10'
}

RX_Jabber = {
    # RX_jab     .1.3.6.1.2.1.16.1.1.1.12    etherStatsJabbers
    'RX_jab.1': '.1.3.6.1.2.1.16.1.1.1.12.1',
    'RX_jab.2': '.1.3.6.1.2.1.16.1.1.1.12.2',
    'RX_jab.3': '.1.3.6.1.2.1.16.1.1.1.12.3',
    'RX_jab.4': '.1.3.6.1.2.1.16.1.1.1.12.4',
    'RX_jab.5': '.1.3.6.1.2.1.16.1.1.1.12.5',
    'RX_jab.6': '.1.3.6.1.2.1.16.1.1.1.12.6',
    'RX_jab.7': '.1.3.6.1.2.1.16.1.1.1.12.7',
    'RX_jab.8': '.1.3.6.1.2.1.16.1.1.1.12.8',
    'RX_jab.9': '.1.3.6.1.2.1.16.1.1.1.12.9',
    'RX_jab.10': '.1.3.6.1.2.1.16.1.1.1.12.10'
}

TX_Collisions = {
    # TX_col     .1.3.6.1.2.1.16.1.1.1.13    etherStatsCollisions
    'TX_col.1': '.1.3.6.1.2.1.16.1.1.1.13.1',
    'TX_col.2': '.1.3.6.1.2.1.16.1.1.1.13.2',
    'TX_col.3': '.1.3.6.1.2.1.16.1.1.1.13.3',
    'TX_col.4': '.1.3.6.1.2.1.16.1.1.1.13.4',
    'TX_col.5': '.1.3.6.1.2.1.16.1.1.1.13.5',
    'TX_col.6': '.1.3.6.1.2.1.16.1.1.1.13.6',
    'TX_col.7': '.1.3.6.1.2.1.16.1.1.1.13.7',
    'TX_col.8': '.1.3.6.1.2.1.16.1.1.1.13.8',
    'TX_col.9': '.1.3.6.1.2.1.16.1.1.1.13.9',
    'TX_col.10': '.1.3.6.1.2.1.16.1.1.1.13.10'
}

TX_SingleCollisions = {
    # TX_scol     .1.3.6.1.2.1.10.7.2.1.4   dot3StatsSingleCollisionFrames
    'TX_scol.1': '.1.3.6.1.2.1.10.7.2.1.4.1',
    'TX_scol.2': '.1.3.6.1.2.1.10.7.2.1.4.2',
    'TX_scol.3': '.1.3.6.1.2.1.10.7.2.1.4.3',
    'TX_scol.4': '.1.3.6.1.2.1.10.7.2.1.4.4',
    'TX_scol.5': '.1.3.6.1.2.1.10.7.2.1.4.5',
    'TX_scol.6': '.1.3.6.1.2.1.10.7.2.1.4.6',
    'TX_scol.7': '.1.3.6.1.2.1.10.7.2.1.4.7',
    'TX_scol.8': '.1.3.6.1.2.1.10.7.2.1.4.8',
    'TX_scol.9': '.1.3.6.1.2.1.10.7.2.1.4.9',
    'TX_scol.10': '.1.3.6.1.2.1.10.7.2.1.4.10'
}

TX_Deferred = {
    # TX_def     .1.3.6.1.2.1.10.7.2.1.7   dot3StatsDeferredTransmissions
    'TX_def.1': '.1.3.6.1.2.1.10.7.2.1.7.1',
    'TX_def.2': '.1.3.6.1.2.1.10.7.2.1.7.2',
    'TX_def.3': '.1.3.6.1.2.1.10.7.2.1.7.3',
    'TX_def.4': '.1.3.6.1.2.1.10.7.2.1.7.4',
    'TX_def.5': '.1.3.6.1.2.1.10.7.2.1.7.5',
    'TX_def.6': '.1.3.6.1.2.1.10.7.2.1.7.6',
    'TX_def.7': '.1.3.6.1.2.1.10.7.2.1.7.7',
    'TX_def.8': '.1.3.6.1.2.1.10.7.2.1.7.8',
    'TX_def.9': '.1.3.6.1.2.1.10.7.2.1.7.9',
    'TX_def.10': '.1.3.6.1.2.1.10.7.2.1.7.10'
}

TX_LateCollisions = {
    # TX_lcol     .1.3.6.1.2.1.10.7.2.1.8   dot3StatsLateCollisions
    'TX_lcol.1': '.1.3.6.1.2.1.10.7.2.1.8.1',
    'TX_lcol.2': '.1.3.6.1.2.1.10.7.2.1.8.2',
    'TX_lcol.3': '.1.3.6.1.2.1.10.7.2.1.8.3',
    'TX_lcol.4': '.1.3.6.1.2.1.10.7.2.1.8.4',
    'TX_lcol.5': '.1.3.6.1.2.1.10.7.2.1.8.5',
    'TX_lcol.6': '.1.3.6.1.2.1.10.7.2.1.8.6',
    'TX_lcol.7': '.1.3.6.1.2.1.10.7.2.1.8.7',
    'TX_lcol.8': '.1.3.6.1.2.1.10.7.2.1.8.8',
    'TX_lcol.9': '.1.3.6.1.2.1.10.7.2.1.8.9',
    'TX_lcol.10': '.1.3.6.1.2.1.10.7.2.1.8.10'
}

TX_ExcessiveCollisions = {
    # TX_ecol     .1.3.6.1.2.1.10.7.2.1.9   dot3StatsExcessiveCollisions
    'TX_ecol.1': '.1.3.6.1.2.1.10.7.2.1.9.1',
    'TX_ecol.2': '.1.3.6.1.2.1.10.7.2.1.9.2',
    'TX_ecol.3': '.1.3.6.1.2.1.10.7.2.1.9.3',
    'TX_ecol.4': '.1.3.6.1.2.1.10.7.2.1.9.4',
    'TX_ecol.5': '.1.3.6.1.2.1.10.7.2.1.9.5',
    'TX_ecol.6': '.1.3.6.1.2.1.10.7.2.1.9.6',
    'TX_ecol.7': '.1.3.6.1.2.1.10.7.2.1.9.7',
    'TX_ecol.8': '.1.3.6.1.2.1.10.7.2.1.9.8',
    'TX_ecol.9': '.1.3.6.1.2.1.10.7.2.1.9.9',
    'TX_ecol.10': '.1.3.6.1.2.1.10.7.2.1.9.10'
}

RxTx = {
    #     RX           .1.3.6.1.2.1.31.1.1.1.6				ifHCInOctets
    '~RX.1': '.1.3.6.1.2.1.31.1.1.1.6.1',
    '~RX.2': '.1.3.6.1.2.1.31.1.1.1.6.2',
    '~RX.3': '.1.3.6.1.2.1.31.1.1.1.6.3',
    '~RX.4': '.1.3.6.1.2.1.31.1.1.1.6.4',
    '~RX.5': '.1.3.6.1.2.1.31.1.1.1.6.5',
    '~RX.6': '.1.3.6.1.2.1.31.1.1.1.6.6',
    '~RX.7': '.1.3.6.1.2.1.31.1.1.1.6.7',
    '~RX.8': '.1.3.6.1.2.1.31.1.1.1.6.8',
    '~RX.9': '.1.3.6.1.2.1.31.1.1.1.6.9',
    '~RX.10': '.1.3.6.1.2.1.31.1.1.1.6.10',
    #     TX           .1.3.6.1.2.1.31.1.1.1.10				ifHCOutOctets
    '~TX.1': '.1.3.6.1.2.1.31.1.1.1.10.1',
    '~TX.2': '.1.3.6.1.2.1.31.1.1.1.10.2',
    '~TX.3': '.1.3.6.1.2.1.31.1.1.1.10.3',
    '~TX.4': '.1.3.6.1.2.1.31.1.1.1.10.4',
    '~TX.5': '.1.3.6.1.2.1.31.1.1.1.10.5',
    '~TX.6': '.1.3.6.1.2.1.31.1.1.1.10.6',
    '~TX.7': '.1.3.6.1.2.1.31.1.1.1.10.7',
    '~TX.8': '.1.3.6.1.2.1.31.1.1.1.10.8',
    '~TX.9': '.1.3.6.1.2.1.31.1.1.1.10.9',
    '~TX.10': '.1.3.6.1.2.1.31.1.1.1.10.10',
}

DuplexStatus = {
    #    DS            .1.3.6.1.2.1.10.7.2.1.19				dot3StatsDuplexStatus
    'DS.1': '.1.3.6.1.2.1.10.7.2.1.19.1',
    'DS.2': '.1.3.6.1.2.1.10.7.2.1.19.2',
    'DS.3': '.1.3.6.1.2.1.10.7.2.1.19.3',
    'DS.4': '.1.3.6.1.2.1.10.7.2.1.19.4',
    'DS.5': '.1.3.6.1.2.1.10.7.2.1.19.5',
    'DS.6': '.1.3.6.1.2.1.10.7.2.1.19.6',
    'DS.7': '.1.3.6.1.2.1.10.7.2.1.19.7',
    'DS.8': '.1.3.6.1.2.1.10.7.2.1.19.8',
    'DS.9': '.1.3.6.1.2.1.10.7.2.1.19.9',
    'DS.10': '.1.3.6.1.2.1.10.7.2.1.19.10',
}

CPUutil = {
    #    CPU           .1.3.6.1.4.1.171.12.1.1.6.3				agentCPUutilizationIn5min
    'CPU.': '.1.3.6.1.4.1.171.12.1.1.6.3.0'
}

PORTutil = {
    # PORTutil     .1.3.6.1.4.1.171.12.1.1.8.1.4  agentPORTutilizationUtil
    'PORTutil.1': '.1.3.6.1.4.1.171.12.1.1.8.1.4.1',
    'PORTutil.2': '.1.3.6.1.4.1.171.12.1.1.8.1.4.2',
    'PORTutil.3': '.1.3.6.1.4.1.171.12.1.1.8.1.4.3',
    'PORTutil.4': '.1.3.6.1.4.1.171.12.1.1.8.1.4.4',
    'PORTutil.5': '.1.3.6.1.4.1.171.12.1.1.8.1.4.5',
    'PORTutil.6': '.1.3.6.1.4.1.171.12.1.1.8.1.4.6',
    'PORTutil.7': '.1.3.6.1.4.1.171.12.1.1.8.1.4.7',
    'PORTutil.8': '.1.3.6.1.4.1.171.12.1.1.8.1.4.8',
    'PORTutil.9': '.1.3.6.1.4.1.171.12.1.1.8.1.4.9',
    'PORTutil.10': '.1.3.6.1.4.1.171.12.1.1.8.1.4.10',
    'PORTutil.11': '.1.3.6.1.4.1.171.12.1.1.8.1.4.11',
    'PORTutil.12': '.1.3.6.1.4.1.171.12.1.1.8.1.4.12',
    'PORTutil.13': '.1.3.6.1.4.1.171.12.1.1.8.1.4.13',
    'PORTutil.14': '.1.3.6.1.4.1.171.12.1.1.8.1.4.14',
    'PORTutil.15': '.1.3.6.1.4.1.171.12.1.1.8.1.4.15',
    'PORTutil.16': '.1.3.6.1.4.1.171.12.1.1.8.1.4.16',
    'PORTutil.17': '.1.3.6.1.4.1.171.12.1.1.8.1.4.17',
    'PORTutil.18': '.1.3.6.1.4.1.171.12.1.1.8.1.4.18',
    'PORTutil.19': '.1.3.6.1.4.1.171.12.1.1.8.1.4.19',
    'PORTutil.20': '.1.3.6.1.4.1.171.12.1.1.8.1.4.20',
    'PORTutil.21': '.1.3.6.1.4.1.171.12.1.1.8.1.4.21',
    'PORTutil.22': '.1.3.6.1.4.1.171.12.1.1.8.1.4.22',
    'PORTutil.23': '.1.3.6.1.4.1.171.12.1.1.8.1.4.23',
    'PORTutil.24': '.1.3.6.1.4.1.171.12.1.1.8.1.4.24',
    'PORTutil.25': '.1.3.6.1.4.1.171.12.1.1.8.1.4.25',
    'PORTutil.26': '.1.3.6.1.4.1.171.12.1.1.8.1.4.26',
    'PORTutil.27': '.1.3.6.1.4.1.171.12.1.1.8.1.4.27',
    'PORTutil.28': '.1.3.6.1.4.1.171.12.1.1.8.1.4.28',
}

FLASHutil = {
    # FLASH    .1.3.6.1.4.1.171.12.1.1.10.1.4 agentFLASHutilizationUnitID
    'FLASH.': '.1.3.6.1.4.1.171.12.1.1.10.1.4.0'
}

DRAMutil = {
    # DRAM    .1.3.6.1.4.1.171.12.1.1.9.1.4  agentDRAMutilizationUnitID
    'DRAM.': '.1.3.6.1.4.1.171.12.1.1.9.1.4.0'
}

CNS = {
    #    CNS           .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4		swL2PortCtrlNwayState
    'CNS..1': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.1.100',
    'CNS..2': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.2.100',
    'CNS..3': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.3.100',
    'CNS..4': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.4.100',
    'CNS..5': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.5.100',
    'CNS..6': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.6.100',
    'CNS..7': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.7.100',
    'CNS..8': '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.8.100',
}

P1L = {
    #   P1L .1.3.6.1.4.1.171.12.58.1.1.1.8. swEtherCableDiagPair1Length
    'P1L.1': '.1.3.6.1.4.1.171.12.58.1.1.1.8.1',
    'P1L.2': '.1.3.6.1.4.1.171.12.58.1.1.1.8.2',
    'P1L.3': '.1.3.6.1.4.1.171.12.58.1.1.1.8.3',
    'P1L.4': '.1.3.6.1.4.1.171.12.58.1.1.1.8.4',
    'P1L.5': '.1.3.6.1.4.1.171.12.58.1.1.1.8.5',
    'P1L.6': '.1.3.6.1.4.1.171.12.58.1.1.1.8.6',
    'P1L.7': '.1.3.6.1.4.1.171.12.58.1.1.1.8.7',
    'P1L.8': '.1.3.6.1.4.1.171.12.58.1.1.1.8.8',
}

P2L = {
    #   P2L .1.3.6.1.4.1.171.12.58.1.1.1.9	swEtherCableDiagPair2Length
    'P2L.1': '.1.3.6.1.4.1.171.12.58.1.1.1.9.1',
    'P2L.2': '.1.3.6.1.4.1.171.12.58.1.1.1.9.2',
    'P2L.3': '.1.3.6.1.4.1.171.12.58.1.1.1.9.3',
    'P2L.4': '.1.3.6.1.4.1.171.12.58.1.1.1.9.4',
    'P2L.5': '.1.3.6.1.4.1.171.12.58.1.1.1.9.5',
    'P2L.6': '.1.3.6.1.4.1.171.12.58.1.1.1.9.6',
    'P2L.7': '.1.3.6.1.4.1.171.12.58.1.1.1.9.7',
    'P2L.8': '.1.3.6.1.4.1.171.12.58.1.1.1.9.8',
}

P1S = {
    #          .1.3.6.1.4.1.171.12.58.1.1.1.4.		swEtherCableDiagPair1Status
    'P1S.1': '.1.3.6.1.4.1.171.12.58.1.1.1.4.1',
    'P1S.2': '.1.3.6.1.4.1.171.12.58.1.1.1.4.2',
    'P1S.3': '.1.3.6.1.4.1.171.12.58.1.1.1.4.3',
    'P1S.4': '.1.3.6.1.4.1.171.12.58.1.1.1.4.4',
    'P1S.5': '.1.3.6.1.4.1.171.12.58.1.1.1.4.5',
    'P1S.6': '.1.3.6.1.4.1.171.12.58.1.1.1.4.6',
    'P1S.7': '.1.3.6.1.4.1.171.12.58.1.1.1.4.7',
    'P1S.8': '.1.3.6.1.4.1.171.12.58.1.1.1.4.8',
}

P2S = {
    # .1.3.6.1.4.1.171.12.58.1.1.1.5			swEtherCableDiagPair2Status
    'P2S.1': '.1.3.6.1.4.1.171.12.58.1.1.1.5.1',
    'P2S.2': '.1.3.6.1.4.1.171.12.58.1.1.1.5.2',
    'P2S.3': '.1.3.6.1.4.1.171.12.58.1.1.1.5.3',
    'P2S.4': '.1.3.6.1.4.1.171.12.58.1.1.1.5.4',
    'P2S.5': '.1.3.6.1.4.1.171.12.58.1.1.1.5.5',
    'P2S.6': '.1.3.6.1.4.1.171.12.58.1.1.1.5.6',
    'P2S.7': '.1.3.6.1.4.1.171.12.58.1.1.1.5.7',
    'P2S.8': '.1.3.6.1.4.1.171.12.58.1.1.1.5.8',
}

CfgUpload = [
    #     .1.3.6.1.4.1.171.12.1.2.1.1.3					agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3', '3', '10.200.201.180', 'IPADDR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.5					agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5', '3', 'backup', 'OCTETSTR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.7					agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7', '3', '2', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.8					agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8', '3', '3', 'INTEGER'],
]

CfgSave = [
    #     .1.3.6.1.4.1.171.12.1.2.6						agentSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.6', '0', '2', 'INTEGER'],
]

CfgDownload = [
    #     .1.3.6.1.4.1.171.12.1.2.1.1.3                                     agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3', '3', '10.200.201.180', 'IPADDR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.5                                     agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5', '3', 'config', 'OCTETSTR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.9                                     agentBscSwFileBIncrement
    ['.1.3.6.1.4.1.171.12.1.2.1.1.9', '3', '1', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.7                                     agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7', '3', '3', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.8                                     agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8', '3', '3', 'INTEGER'],
]

SafeCfgDownload = [
    #     .1.3.6.1.4.1.171.12.1.2.1.1.3                                     agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3', '3', '10.200.201.180', 'IPADDR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.5                                     agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5', '3', 'mon_log', 'OCTETSTR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.9                                     agentBscSwFileBIncrement
    ['.1.3.6.1.4.1.171.12.1.2.1.1.9', '3', '1', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.7                                     agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7', '3', '3', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.8                                     agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8', '3', '3', 'INTEGER'],
]

PortsDescDownload = [
    #     .1.3.6.1.4.1.171.12.1.2.1.1.3                                     agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3', '3', '10.200.201.180', 'IPADDR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.5                                     agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5', '3', 'pdesc', 'OCTETSTR'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.9                                     agentBscSwFileBIncrement
    ['.1.3.6.1.4.1.171.12.1.2.1.1.9', '3', '1', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.7                                     agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7', '3', '3', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.1.1.8                                     agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8', '3', '3', 'INTEGER'],
]

CableDiagInit = [
    #     .1.3.6.1.4.1.171.12.58.1.1.1.12 - swEtherCableDiagAction
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '1', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '2', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '3', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '4', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '5', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '6', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '7', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '8', '1', 'INTEGER'],
]

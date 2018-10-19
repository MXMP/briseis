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
    #    RX_crc        .1.3.6.1.2.1.16.1.1.1.8				etherStatsCRCAlignErrors
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
    'RX_crc.11': '.1.3.6.1.2.1.16.1.1.1.8.11',
    'RX_crc.12': '.1.3.6.1.2.1.16.1.1.1.8.12',
    'RX_crc.13': '.1.3.6.1.2.1.16.1.1.1.8.13',
    'RX_crc.14': '.1.3.6.1.2.1.16.1.1.1.8.14',
    'RX_crc.15': '.1.3.6.1.2.1.16.1.1.1.8.15',
    'RX_crc.16': '.1.3.6.1.2.1.16.1.1.1.8.16',
    'RX_crc.17': '.1.3.6.1.2.1.16.1.1.1.8.17',
    'RX_crc.18': '.1.3.6.1.2.1.16.1.1.1.8.18',
    'RX_crc.19': '.1.3.6.1.2.1.16.1.1.1.8.19',
    'RX_crc.20': '.1.3.6.1.2.1.16.1.1.1.8.20',
    'RX_crc.21': '.1.3.6.1.2.1.16.1.1.1.8.21',
    'RX_crc.22': '.1.3.6.1.2.1.16.1.1.1.8.22',
    'RX_crc.23': '.1.3.6.1.2.1.16.1.1.1.8.23',
    'RX_crc.24': '.1.3.6.1.2.1.16.1.1.1.8.24',
    'RX_crc.25': '.1.3.6.1.2.1.16.1.1.1.8.25',
    'RX_crc.26': '.1.3.6.1.2.1.16.1.1.1.8.26',
    'RX_crc.27': '.1.3.6.1.2.1.16.1.1.1.8.27',
    'RX_crc.28': '.1.3.6.1.2.1.16.1.1.1.8.28',
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
    '~RX.11': '.1.3.6.1.2.1.31.1.1.1.6.11',
    '~RX.12': '.1.3.6.1.2.1.31.1.1.1.6.12',
    '~RX.13': '.1.3.6.1.2.1.31.1.1.1.6.13',
    '~RX.14': '.1.3.6.1.2.1.31.1.1.1.6.14',
    '~RX.15': '.1.3.6.1.2.1.31.1.1.1.6.15',
    '~RX.16': '.1.3.6.1.2.1.31.1.1.1.6.16',
    '~RX.17': '.1.3.6.1.2.1.31.1.1.1.6.17',
    '~RX.18': '.1.3.6.1.2.1.31.1.1.1.6.18',
    '~RX.19': '.1.3.6.1.2.1.31.1.1.1.6.19',
    '~RX.20': '.1.3.6.1.2.1.31.1.1.1.6.20',
    '~RX.21': '.1.3.6.1.2.1.31.1.1.1.6.21',
    '~RX.22': '.1.3.6.1.2.1.31.1.1.1.6.22',
    '~RX.23': '.1.3.6.1.2.1.31.1.1.1.6.23',
    '~RX.24': '.1.3.6.1.2.1.31.1.1.1.6.24',
    '~RX.25': '.1.3.6.1.2.1.31.1.1.1.6.25',
    '~RX.26': '.1.3.6.1.2.1.31.1.1.1.6.26',
    '~RX.27': '.1.3.6.1.2.1.31.1.1.1.6.27',
    '~RX.28': '.1.3.6.1.2.1.31.1.1.1.6.28',
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
    '~TX.11': '.1.3.6.1.2.1.31.1.1.1.10.11',
    '~TX.12': '.1.3.6.1.2.1.31.1.1.1.10.12',
    '~TX.13': '.1.3.6.1.2.1.31.1.1.1.10.13',
    '~TX.14': '.1.3.6.1.2.1.31.1.1.1.10.14',
    '~TX.15': '.1.3.6.1.2.1.31.1.1.1.10.15',
    '~TX.16': '.1.3.6.1.2.1.31.1.1.1.10.16',
    '~TX.17': '.1.3.6.1.2.1.31.1.1.1.10.17',
    '~TX.18': '.1.3.6.1.2.1.31.1.1.1.10.18',
    '~TX.19': '.1.3.6.1.2.1.31.1.1.1.10.19',
    '~TX.20': '.1.3.6.1.2.1.31.1.1.1.10.20',
    '~TX.21': '.1.3.6.1.2.1.31.1.1.1.10.21',
    '~TX.22': '.1.3.6.1.2.1.31.1.1.1.10.22',
    '~TX.23': '.1.3.6.1.2.1.31.1.1.1.10.23',
    '~TX.24': '.1.3.6.1.2.1.31.1.1.1.10.24',
    '~TX.25': '.1.3.6.1.2.1.31.1.1.1.10.25',
    '~TX.26': '.1.3.6.1.2.1.31.1.1.1.10.26',
    '~TX.27': '.1.3.6.1.2.1.31.1.1.1.10.27',
    '~TX.28': '.1.3.6.1.2.1.31.1.1.1.10.28',
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
    'DS.11': '.1.3.6.1.2.1.10.7.2.1.19.11',
    'DS.12': '.1.3.6.1.2.1.10.7.2.1.19.12',
    'DS.13': '.1.3.6.1.2.1.10.7.2.1.19.13',
    'DS.14': '.1.3.6.1.2.1.10.7.2.1.19.14',
    'DS.15': '.1.3.6.1.2.1.10.7.2.1.19.15',
    'DS.16': '.1.3.6.1.2.1.10.7.2.1.19.16',
    'DS.17': '.1.3.6.1.2.1.10.7.2.1.19.17',
    'DS.18': '.1.3.6.1.2.1.10.7.2.1.19.18',
    'DS.19': '.1.3.6.1.2.1.10.7.2.1.19.19',
    'DS.20': '.1.3.6.1.2.1.10.7.2.1.19.20',
    'DS.21': '.1.3.6.1.2.1.10.7.2.1.19.21',
    'DS.22': '.1.3.6.1.2.1.10.7.2.1.19.22',
    'DS.23': '.1.3.6.1.2.1.10.7.2.1.19.23',
    'DS.24': '.1.3.6.1.2.1.10.7.2.1.19.24',
    'DS.25': '.1.3.6.1.2.1.10.7.2.1.19.25',
    'DS.26': '.1.3.6.1.2.1.10.7.2.1.19.26',
    'DS.27': '.1.3.6.1.2.1.10.7.2.1.19.27',
    'DS.28': '.1.3.6.1.2.1.10.7.2.1.19.28',
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
    #    CNS           .1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4		swL2PortCtrlNwayState
    'CNS..1': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.1.100',
    'CNS..2': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.2.100',
    'CNS..3': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.3.100',
    'CNS..4': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.4.100',
    'CNS..5': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.5.100',
    'CNS..6': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.6.100',
    'CNS..7': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.7.100',
    'CNS..8': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.8.100',
    'CNS..9': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.9.100',
    'CNS..10': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.10.100',
    'CNS..11': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.11.100',
    'CNS..12': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.12.100',
    'CNS..13': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.13.100',
    'CNS..14': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.14.100',
    'CNS..15': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.15.100',
    'CNS..16': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.16.100',
    'CNS..17': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.17.100',
    'CNS..18': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.18.100',
    'CNS..19': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.19.100',
    'CNS..20': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.20.100',
    'CNS..21': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.21.100',
    'CNS..22': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.22.100',
    'CNS..23': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.23.100',
    'CNS..24': '.1.3.6.1.4.1.171.11.113.1.3.2.2.2.1.4.24.100',
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
    'P1L.9': '.1.3.6.1.4.1.171.12.58.1.1.1.8.9',
    'P1L.10': '.1.3.6.1.4.1.171.12.58.1.1.1.8.10',
    'P1L.11': '.1.3.6.1.4.1.171.12.58.1.1.1.8.11',
    'P1L.12': '.1.3.6.1.4.1.171.12.58.1.1.1.8.12',
    'P1L.13': '.1.3.6.1.4.1.171.12.58.1.1.1.8.13',
    'P1L.14': '.1.3.6.1.4.1.171.12.58.1.1.1.8.14',
    'P1L.15': '.1.3.6.1.4.1.171.12.58.1.1.1.8.15',
    'P1L.16': '.1.3.6.1.4.1.171.12.58.1.1.1.8.16',
    'P1L.17': '.1.3.6.1.4.1.171.12.58.1.1.1.8.17',
    'P1L.18': '.1.3.6.1.4.1.171.12.58.1.1.1.8.18',
    'P1L.19': '.1.3.6.1.4.1.171.12.58.1.1.1.8.19',
    'P1L.20': '.1.3.6.1.4.1.171.12.58.1.1.1.8.20',
    'P1L.21': '.1.3.6.1.4.1.171.12.58.1.1.1.8.21',
    'P1L.22': '.1.3.6.1.4.1.171.12.58.1.1.1.8.22',
    'P1L.23': '.1.3.6.1.4.1.171.12.58.1.1.1.8.23',
    'P1L.24': '.1.3.6.1.4.1.171.12.58.1.1.1.8.24',
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
    'P2L.9': '.1.3.6.1.4.1.171.12.58.1.1.1.9.9',
    'P2L.10': '.1.3.6.1.4.1.171.12.58.1.1.1.9.10',
    'P2L.11': '.1.3.6.1.4.1.171.12.58.1.1.1.9.11',
    'P2L.12': '.1.3.6.1.4.1.171.12.58.1.1.1.9.12',
    'P2L.13': '.1.3.6.1.4.1.171.12.58.1.1.1.9.13',
    'P2L.14': '.1.3.6.1.4.1.171.12.58.1.1.1.9.14',
    'P2L.15': '.1.3.6.1.4.1.171.12.58.1.1.1.9.15',
    'P2L.16': '.1.3.6.1.4.1.171.12.58.1.1.1.9.16',
    'P2L.17': '.1.3.6.1.4.1.171.12.58.1.1.1.9.17',
    'P2L.18': '.1.3.6.1.4.1.171.12.58.1.1.1.9.18',
    'P2L.19': '.1.3.6.1.4.1.171.12.58.1.1.1.9.19',
    'P2L.20': '.1.3.6.1.4.1.171.12.58.1.1.1.9.20',
    'P2L.21': '.1.3.6.1.4.1.171.12.58.1.1.1.9.21',
    'P2L.22': '.1.3.6.1.4.1.171.12.58.1.1.1.9.22',
    'P2L.23': '.1.3.6.1.4.1.171.12.58.1.1.1.9.23',
    'P2L.24': '.1.3.6.1.4.1.171.12.58.1.1.1.9.24',
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
    'P1S.9': '.1.3.6.1.4.1.171.12.58.1.1.1.4.9',
    'P1S.10': '.1.3.6.1.4.1.171.12.58.1.1.1.4.10',
    'P1S.11': '.1.3.6.1.4.1.171.12.58.1.1.1.4.11',
    'P1S.12': '.1.3.6.1.4.1.171.12.58.1.1.1.4.12',
    'P1S.13': '.1.3.6.1.4.1.171.12.58.1.1.1.4.13',
    'P1S.14': '.1.3.6.1.4.1.171.12.58.1.1.1.4.14',
    'P1S.15': '.1.3.6.1.4.1.171.12.58.1.1.1.4.15',
    'P1S.16': '.1.3.6.1.4.1.171.12.58.1.1.1.4.16',
    'P1S.17': '.1.3.6.1.4.1.171.12.58.1.1.1.4.17',
    'P1S.18': '.1.3.6.1.4.1.171.12.58.1.1.1.4.18',
    'P1S.19': '.1.3.6.1.4.1.171.12.58.1.1.1.4.19',
    'P1S.20': '.1.3.6.1.4.1.171.12.58.1.1.1.4.20',
    'P1S.21': '.1.3.6.1.4.1.171.12.58.1.1.1.4.21',
    'P1S.22': '.1.3.6.1.4.1.171.12.58.1.1.1.4.22',
    'P1S.23': '.1.3.6.1.4.1.171.12.58.1.1.1.4.23',
    'P1S.24': '.1.3.6.1.4.1.171.12.58.1.1.1.4.24',
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
    'P2S.9': '.1.3.6.1.4.1.171.12.58.1.1.1.5.9',
    'P2S.10': '.1.3.6.1.4.1.171.12.58.1.1.1.5.10',
    'P2S.11': '.1.3.6.1.4.1.171.12.58.1.1.1.5.11',
    'P2S.12': '.1.3.6.1.4.1.171.12.58.1.1.1.5.12',
    'P2S.13': '.1.3.6.1.4.1.171.12.58.1.1.1.5.13',
    'P2S.14': '.1.3.6.1.4.1.171.12.58.1.1.1.5.14',
    'P2S.15': '.1.3.6.1.4.1.171.12.58.1.1.1.5.15',
    'P2S.16': '.1.3.6.1.4.1.171.12.58.1.1.1.5.16',
    'P2S.17': '.1.3.6.1.4.1.171.12.58.1.1.1.5.17',
    'P2S.18': '.1.3.6.1.4.1.171.12.58.1.1.1.5.18',
    'P2S.19': '.1.3.6.1.4.1.171.12.58.1.1.1.5.19',
    'P2S.20': '.1.3.6.1.4.1.171.12.58.1.1.1.5.20',
    'P2S.21': '.1.3.6.1.4.1.171.12.58.1.1.1.5.21',
    'P2S.22': '.1.3.6.1.4.1.171.12.58.1.1.1.5.22',
    'P2S.23': '.1.3.6.1.4.1.171.12.58.1.1.1.5.23',
    'P2S.24': '.1.3.6.1.4.1.171.12.58.1.1.1.5.24',
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
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '9', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '10', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '11', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '12', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '13', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '14', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '15', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '16', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '17', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '18', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '19', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '20', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '21', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '22', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '23', '1', 'INTEGER'],
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '24', '1', 'INTEGER'],
]

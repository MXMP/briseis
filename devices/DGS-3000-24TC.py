# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

sysUpTime = {
    #    UP            .1.3.6.1.2.1.1.3.0					sysUpTimeInstance
    'UP.': '.1.3.6.1.2.1.1.3.0'
}

FWVer = {
    #    FW            .1.3.6.1.2.1.16.19.2					probeSoftwareRev
    'FW.': '.1.3.6.1.2.1.16.19.2.0'
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
    'RX_crc.24': '.1.3.6.1.2.1.16.1.1.1.8.24'
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
    'RX_und.10': '.1.3.6.1.2.1.16.1.1.1.9.10',
    'RX_und.11': '.1.3.6.1.2.1.16.1.1.1.9.11',
    'RX_und.12': '.1.3.6.1.2.1.16.1.1.1.9.12',
    'RX_und.13': '.1.3.6.1.2.1.16.1.1.1.9.13',
    'RX_und.14': '.1.3.6.1.2.1.16.1.1.1.9.14',
    'RX_und.15': '.1.3.6.1.2.1.16.1.1.1.9.15',
    'RX_und.16': '.1.3.6.1.2.1.16.1.1.1.9.16',
    'RX_und.17': '.1.3.6.1.2.1.16.1.1.1.9.17',
    'RX_und.18': '.1.3.6.1.2.1.16.1.1.1.9.18',
    'RX_und.19': '.1.3.6.1.2.1.16.1.1.1.9.19',
    'RX_und.20': '.1.3.6.1.2.1.16.1.1.1.9.20',
    'RX_und.21': '.1.3.6.1.2.1.16.1.1.1.9.21',
    'RX_und.22': '.1.3.6.1.2.1.16.1.1.1.9.22',
    'RX_und.23': '.1.3.6.1.2.1.16.1.1.1.9.23',
    'RX_und.24': '.1.3.6.1.2.1.16.1.1.1.9.24'
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
    'RX_over.10': '.1.3.6.1.2.1.16.1.1.1.10.10',
    'RX_over.11': '.1.3.6.1.2.1.16.1.1.1.10.11',
    'RX_over.12': '.1.3.6.1.2.1.16.1.1.1.10.12',
    'RX_over.13': '.1.3.6.1.2.1.16.1.1.1.10.13',
    'RX_over.14': '.1.3.6.1.2.1.16.1.1.1.10.14',
    'RX_over.15': '.1.3.6.1.2.1.16.1.1.1.10.15',
    'RX_over.16': '.1.3.6.1.2.1.16.1.1.1.10.16',
    'RX_over.17': '.1.3.6.1.2.1.16.1.1.1.10.17',
    'RX_over.18': '.1.3.6.1.2.1.16.1.1.1.10.18',
    'RX_over.19': '.1.3.6.1.2.1.16.1.1.1.10.19',
    'RX_over.20': '.1.3.6.1.2.1.16.1.1.1.10.20',
    'RX_over.21': '.1.3.6.1.2.1.16.1.1.1.10.21',
    'RX_over.22': '.1.3.6.1.2.1.16.1.1.1.10.22',
    'RX_over.23': '.1.3.6.1.2.1.16.1.1.1.10.23',
    'RX_over.24': '.1.3.6.1.2.1.16.1.1.1.10.24'
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
    'RX_frag.10': '.1.3.6.1.2.1.16.1.1.1.11.10',
    'RX_frag.11': '.1.3.6.1.2.1.16.1.1.1.11.11',
    'RX_frag.12': '.1.3.6.1.2.1.16.1.1.1.11.12',
    'RX_frag.13': '.1.3.6.1.2.1.16.1.1.1.11.13',
    'RX_frag.14': '.1.3.6.1.2.1.16.1.1.1.11.14',
    'RX_frag.15': '.1.3.6.1.2.1.16.1.1.1.11.15',
    'RX_frag.16': '.1.3.6.1.2.1.16.1.1.1.11.16',
    'RX_frag.17': '.1.3.6.1.2.1.16.1.1.1.11.17',
    'RX_frag.18': '.1.3.6.1.2.1.16.1.1.1.11.18',
    'RX_frag.19': '.1.3.6.1.2.1.16.1.1.1.11.19',
    'RX_frag.20': '.1.3.6.1.2.1.16.1.1.1.11.20',
    'RX_frag.21': '.1.3.6.1.2.1.16.1.1.1.11.21',
    'RX_frag.22': '.1.3.6.1.2.1.16.1.1.1.11.22',
    'RX_frag.23': '.1.3.6.1.2.1.16.1.1.1.11.23',
    'RX_frag.24': '.1.3.6.1.2.1.16.1.1.1.11.24'
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
    'RX_jab.10': '.1.3.6.1.2.1.16.1.1.1.12.10',
    'RX_jab.11': '.1.3.6.1.2.1.16.1.1.1.12.11',
    'RX_jab.12': '.1.3.6.1.2.1.16.1.1.1.12.12',
    'RX_jab.13': '.1.3.6.1.2.1.16.1.1.1.12.13',
    'RX_jab.14': '.1.3.6.1.2.1.16.1.1.1.12.14',
    'RX_jab.15': '.1.3.6.1.2.1.16.1.1.1.12.15',
    'RX_jab.16': '.1.3.6.1.2.1.16.1.1.1.12.16',
    'RX_jab.17': '.1.3.6.1.2.1.16.1.1.1.12.17',
    'RX_jab.18': '.1.3.6.1.2.1.16.1.1.1.12.18',
    'RX_jab.19': '.1.3.6.1.2.1.16.1.1.1.12.19',
    'RX_jab.20': '.1.3.6.1.2.1.16.1.1.1.12.20',
    'RX_jab.21': '.1.3.6.1.2.1.16.1.1.1.12.21',
    'RX_jab.22': '.1.3.6.1.2.1.16.1.1.1.12.22',
    'RX_jab.23': '.1.3.6.1.2.1.16.1.1.1.12.23',
    'RX_jab.24': '.1.3.6.1.2.1.16.1.1.1.12.24'
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
    'TX_col.10': '.1.3.6.1.2.1.16.1.1.1.13.10',
    'TX_col.11': '.1.3.6.1.2.1.16.1.1.1.13.11',
    'TX_col.12': '.1.3.6.1.2.1.16.1.1.1.13.12',
    'TX_col.13': '.1.3.6.1.2.1.16.1.1.1.13.13',
    'TX_col.14': '.1.3.6.1.2.1.16.1.1.1.13.14',
    'TX_col.15': '.1.3.6.1.2.1.16.1.1.1.13.15',
    'TX_col.16': '.1.3.6.1.2.1.16.1.1.1.13.16',
    'TX_col.17': '.1.3.6.1.2.1.16.1.1.1.13.17',
    'TX_col.18': '.1.3.6.1.2.1.16.1.1.1.13.18',
    'TX_col.19': '.1.3.6.1.2.1.16.1.1.1.13.19',
    'TX_col.20': '.1.3.6.1.2.1.16.1.1.1.13.20',
    'TX_col.21': '.1.3.6.1.2.1.16.1.1.1.13.21',
    'TX_col.22': '.1.3.6.1.2.1.16.1.1.1.13.22',
    'TX_col.23': '.1.3.6.1.2.1.16.1.1.1.13.23',
    'TX_col.24': '.1.3.6.1.2.1.16.1.1.1.13.24'
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
    'TX_scol.10': '.1.3.6.1.2.1.10.7.2.1.4.10',
    'TX_scol.11': '.1.3.6.1.2.1.10.7.2.1.4.11',
    'TX_scol.12': '.1.3.6.1.2.1.10.7.2.1.4.12',
    'TX_scol.13': '.1.3.6.1.2.1.10.7.2.1.4.13',
    'TX_scol.14': '.1.3.6.1.2.1.10.7.2.1.4.14',
    'TX_scol.15': '.1.3.6.1.2.1.10.7.2.1.4.15',
    'TX_scol.16': '.1.3.6.1.2.1.10.7.2.1.4.16',
    'TX_scol.17': '.1.3.6.1.2.1.10.7.2.1.4.17',
    'TX_scol.18': '.1.3.6.1.2.1.10.7.2.1.4.18',
    'TX_scol.19': '.1.3.6.1.2.1.10.7.2.1.4.19',
    'TX_scol.20': '.1.3.6.1.2.1.10.7.2.1.4.20',
    'TX_scol.21': '.1.3.6.1.2.1.10.7.2.1.4.21',
    'TX_scol.22': '.1.3.6.1.2.1.10.7.2.1.4.22',
    'TX_scol.23': '.1.3.6.1.2.1.10.7.2.1.4.23',
    'TX_scol.24': '.1.3.6.1.2.1.10.7.2.1.4.24'
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
    'TX_def.10': '.1.3.6.1.2.1.10.7.2.1.7.10',
    'TX_def.11': '.1.3.6.1.2.1.10.7.2.1.7.11',
    'TX_def.12': '.1.3.6.1.2.1.10.7.2.1.7.12',
    'TX_def.13': '.1.3.6.1.2.1.10.7.2.1.7.13',
    'TX_def.14': '.1.3.6.1.2.1.10.7.2.1.7.14',
    'TX_def.15': '.1.3.6.1.2.1.10.7.2.1.7.15',
    'TX_def.16': '.1.3.6.1.2.1.10.7.2.1.7.16',
    'TX_def.17': '.1.3.6.1.2.1.10.7.2.1.7.17',
    'TX_def.18': '.1.3.6.1.2.1.10.7.2.1.7.18',
    'TX_def.19': '.1.3.6.1.2.1.10.7.2.1.7.19',
    'TX_def.20': '.1.3.6.1.2.1.10.7.2.1.7.20',
    'TX_def.21': '.1.3.6.1.2.1.10.7.2.1.7.21',
    'TX_def.22': '.1.3.6.1.2.1.10.7.2.1.7.22',
    'TX_def.23': '.1.3.6.1.2.1.10.7.2.1.7.23',
    'TX_def.24': '.1.3.6.1.2.1.10.7.2.1.7.24'
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
    'TX_lcol.10': '.1.3.6.1.2.1.10.7.2.1.8.10',
    'TX_lcol.11': '.1.3.6.1.2.1.10.7.2.1.8.11',
    'TX_lcol.12': '.1.3.6.1.2.1.10.7.2.1.8.12',
    'TX_lcol.13': '.1.3.6.1.2.1.10.7.2.1.8.13',
    'TX_lcol.14': '.1.3.6.1.2.1.10.7.2.1.8.14',
    'TX_lcol.15': '.1.3.6.1.2.1.10.7.2.1.8.15',
    'TX_lcol.16': '.1.3.6.1.2.1.10.7.2.1.8.16',
    'TX_lcol.17': '.1.3.6.1.2.1.10.7.2.1.8.17',
    'TX_lcol.18': '.1.3.6.1.2.1.10.7.2.1.8.18',
    'TX_lcol.19': '.1.3.6.1.2.1.10.7.2.1.8.19',
    'TX_lcol.20': '.1.3.6.1.2.1.10.7.2.1.8.20',
    'TX_lcol.21': '.1.3.6.1.2.1.10.7.2.1.8.21',
    'TX_lcol.22': '.1.3.6.1.2.1.10.7.2.1.8.22',
    'TX_lcol.23': '.1.3.6.1.2.1.10.7.2.1.8.23',
    'TX_lcol.24': '.1.3.6.1.2.1.10.7.2.1.8.24'
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
    'TX_ecol.10': '.1.3.6.1.2.1.10.7.2.1.9.10',
    'TX_ecol.11': '.1.3.6.1.2.1.10.7.2.1.9.11',
    'TX_ecol.12': '.1.3.6.1.2.1.10.7.2.1.9.12',
    'TX_ecol.13': '.1.3.6.1.2.1.10.7.2.1.9.13',
    'TX_ecol.14': '.1.3.6.1.2.1.10.7.2.1.9.14',
    'TX_ecol.15': '.1.3.6.1.2.1.10.7.2.1.9.15',
    'TX_ecol.16': '.1.3.6.1.2.1.10.7.2.1.9.16',
    'TX_ecol.17': '.1.3.6.1.2.1.10.7.2.1.9.17',
    'TX_ecol.18': '.1.3.6.1.2.1.10.7.2.1.9.18',
    'TX_ecol.19': '.1.3.6.1.2.1.10.7.2.1.9.19',
    'TX_ecol.20': '.1.3.6.1.2.1.10.7.2.1.9.20',
    'TX_ecol.21': '.1.3.6.1.2.1.10.7.2.1.9.21',
    'TX_ecol.22': '.1.3.6.1.2.1.10.7.2.1.9.22',
    'TX_ecol.23': '.1.3.6.1.2.1.10.7.2.1.9.23',
    'TX_ecol.24': '.1.3.6.1.2.1.10.7.2.1.9.24'
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
}

swTempCurr = {
    #    CT            .1.3.6.1.4.1.171.12.11.1.8.1.2			swTemperatureCurrent
    'CT.': '.1.3.6.1.4.1.171.12.11.1.8.1.2.1'
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
    #    CNS           .1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5		swL2PortCtrlNwayState
    'CNS..1': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.1.100',
    'CNS..2': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.2.100',
    'CNS..3': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.3.100',
    'CNS..4': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.4.100',
    'CNS..5': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.5.100',
    'CNS..6': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.6.100',
    'CNS..7': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.7.100',
    'CNS..8': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.8.100',
    'CNS..9': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.9.100',
    'CNS..10': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.10.100',
    'CNS..11': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.11.100',
    'CNS..12': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.12.100',
    'CNS..13': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.13.100',
    'CNS..14': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.14.100',
    'CNS..15': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.15.100',
    'CNS..16': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.16.100',
    'CNS..17': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.17.100',
    'CNS..18': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.18.100',
    'CNS..19': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.19.100',
    'CNS..20': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.20.100',
    'CNS..21': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.21.100',
    'CNS..22': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.22.100',
    'CNS..23': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.23.100',
    'CNS..24': '.1.3.6.1.4.1.171.11.133.4.1.2.3.2.1.5.24.100',
}

CfgUpload = [
    #     .1.3.6.1.4.1.171.12.1.2.18.1.1.3					agentBscFileSystemServerAddr
    ['.1.3.6.1.4.1.171.12.1.2.18.1.1.3', '3', '10.200.201.180', 'IPADDR'],
    #     .1.3.6.1.4.1.171.12.1.2.18.1.1.5					agentBscFileSystemServerFileName
    ['.1.3.6.1.4.1.171.12.1.2.18.1.1.5', '3', 'backup', 'OCTETSTR'],
    #     .1.3.6.1.4.1.171.12.1.2.18.1.1.8					agentBscFileSystemLoadType
    ['.1.3.6.1.4.1.171.12.1.2.18.1.1.8', '3', '2', 'INTEGER'],
    #     .1.3.6.1.4.1.171.12.1.2.18.1.1.12					agentBscFileSystemCtrl
    ['.1.3.6.1.4.1.171.12.1.2.18.1.1.12', '3', '3', 'INTEGER'],
]

CfgSave = [
    #     .1.3.6.1.4.1.171.12.1.2.18.4					agentBscFileSystemSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.18.4', '0', '2', 'INTEGER'],
]

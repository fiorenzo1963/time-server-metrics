#!/usr/bin/python3

from pysnmp.hlapi import *
from SYMM_SMI_MIB import lookup_symm_mib
import dateutil.parser

target_server = "192.168.101.231"
oid_iso = "iso.3.6.1.4.1.9070"
oid_num = "1.3.6.1.4.1.9070"

#
# full list of MIB variables we get -- we don't use all of them
#
# symm.ntpSysLeap(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.1.0) = 0
# symm.ntpSysStratum(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.2.0) = 1
# symm.ntpSysPrecision(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.3.0) = -20
# symm.ntpSysRootDelay(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.4.0) = 0.000000
# symm.ntpSysRootDispersion(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.5.0) = 0.000267
# symm.ntpSysRefID(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.6.0) = GPS
# symm.ntpSysRefTime(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.7.0) = 3803072501.26656
# symm.ntpSysPoll(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.8.0) = 6
# symm.ntpSysPeer(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.9.0) = 2981759
# symm.ntpSysPhase(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.10.0) = 0.000000
# symm.ntpSysFreq(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.11.0) = -1.009140 PPM
# symm.ntpSysError(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.12.0) = No error
# symm.ntpSysClock(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.13.0) = Tue Jul  7 01:01:43 2020
# symm.ntpSysSystem(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.14.0) = Symmetricom SyncServer
# symm.ntpSysProcessor(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.15.0) = X86 Processor
# symm.ntpSysNotrust(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.16.0) = 1
# symm.ntpSysPktsReceived(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.17.0) = 1917
# symm.ntpSysMode(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.18.0) = 3
# symm.ntpSysVersion(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.19.0) = ntpd 4.2.4p8@1.1607-o Thu Mar 10 18:46:30 UTC 2016 (1)
# symm.tymingStatus(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.1.0) = Good
# symm.tymingSource(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.2.0) = 1
# symm.tymingTime(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.3.0) = Tue Jul  7 01:01:43 2020
# symm.tymingVersion(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.4.0) = 2.103
# symm.tymingFlyPeriod(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.5.0) = 0
# symm.gpsPosition(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.1.0) = 1 47 34 0 837 -1 122 7 42 32 198
# symm.gpsUTCOffset(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.2.0) = 18
# symm.gpsHealth(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.3.0) = Receiver Health: 8
# symm.gpsSatlist(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.4.0) = 7,20,-164,C,15,-156,C,21,-155,C,10,-150,C,27,-156,C,8,-164,C,18,-157,C
# symm.gpsMode(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.5.0) = Receiver Mode: Survey
# symm.etcVersion(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.1.0) = 2.83.2
# symm.etcSerialNbr(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.2.0) = 1126A63108
# symm.etcModel(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.3.0) = S300
# symm.etcUpgrade(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.4.0) = Update value: 0
# symm.etcUpgradeServer(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.5.0) = www.symmetricom.com
# symm.etcAlarmString(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.6.0) = 

def get_symm_vars(target_host):
    symm_vars = { }
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((target_host, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid_iso)),
                lookupMib=False):
        if errorIndication:
            print(errorIndication)
            continue
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            continue
        else:
            for varBind in varBinds:
                #print(' = '.join([x.prettyPrint() for x in varBind]))
                #print(' = '.join([x.prettyPrint() for x in varBind]))
                #for x in varBind:
                #    print("    --> " + str(x))
                var = str(varBind[0])
                value = str(varBind[1])
                if var.startswith(oid_num):
                    varname = lookup_symm_mib(var)
                    if varname is not None:
                        # these variables are not collected
                        if varname == 'symm.ntpSysSystem':
                            continue
                        if varname == 'symm.ntpSysProcessor':
                            continue
                        if varname == 'symm.ntpSysVersion':
                            continue
                        if varname == 'symm.tymingVersion':
                            continue
                        if varname == 'symm.tymingFlyPeriod':
                            continue
                        if varname == 'symm.etcVersion':
                            continue
                        if varname == 'symm.etcSerialNbr':
                            continue
                        if varname == 'symm.etcModel':
                            continue
                        if varname == 'symm.etcUpgrade':
                            continue
                        if varname == 'symm.etcUpgradeServer':
                            continue
                        print(varname + "(" + var + ")" + " = " + value)
                        symm_vars[varname] = value
    return symm_vars

INT_VARS = ( 
    'symm.ntpSysLeap',
    'symm.ntpSysStratum',
    'symm.ntpSysPrecision',
    'symm.ntpSysPoll',
    'symm.ntpSysPeer',
    'symm.ntpSysNotrust',
    'symm.ntpSysPktsReceived',
    'symm.ntpSysMode',
    'symm.tymingSource',
    'symm.gpsUTCOffset'
)
FLOAT_VARS = (
    'symm.ntpSysRootDelay',
    'symm.ntpSysRootDispersion',
    'symm.ntpSysRefTime',
    'symm.ntpSysPhase'
)

def dmg_to_float(c_deg, c_min, c_sec, c_s):
    ret = c_deg
    ret = ret + c_min / 60.0
    ret = ret + c_sec / 3600.0
    if c_s == -1:
        ret = -ret
    return ret

# format sample: Tue Jul  7 01:13:50 2020
def symm_to_utc_iso(s):
    d = dateutil.parser.parse(s)
    return d.isoformat() + 'Z'

def parse_symm_vars(symm_vars):
    p_symm_vars = { }
    for key in symm_vars.keys():
        if key in INT_VARS:
            #print("parse_symm_vars: var=" + key + ", value='" + symm_vars[key] + "': INT PARSE")
            p_symm_vars[key] = int(symm_vars[key])
            continue
        if key in FLOAT_VARS:
            #print("parse_symm_vars: var=" + key + ", value='" + symm_vars[key] + "': FLOAT PARSE")
            p_symm_vars[key] = float(symm_vars[key])
            continue
        #print("parse_symm_vars: var=" + key + ", value='" + symm_vars[key] + "': SPECIAL PARSING")
        #symm.ntpSysRefID(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.6.0) = GPS
        if key == 'symm.ntpSysRefID':
            p_symm_vars[key] = symm_vars[key]
            continue
        #symm.ntpSysFreq(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.11.0) = -1.009064 PPM
        if key == 'symm.ntpSysFreq':
            p_symm_vars[key] = float(symm_vars[key].replace(' PPM', ''))
            continue
        #symm.ntpSysError(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.12.0) = No error
        if key == 'symm.ntpSysError':
            p_symm_vars[key] = symm_vars[key]
            if p_symm_vars[key] == 'No error':
                p_symm_vars[key] = ''
            continue
        #symm.ntpSysClock(1.3.6.1.4.1.9070.1.2.3.1.5.1.1.13.0) = Tue Jul  7 01:13:50 2020
        if key == 'symm.ntpSysClock':
            p_symm_vars['sym.ntpSysClock'] = symm_to_utc_iso(symm_vars[key])
            continue
        #symm.tymingStatus(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.1.0) = Good
        if key == 'symm.tymingStatus':
            p_symm_vars[key] = symm_vars[key]
            continue
        #symm.tymingTime(1.3.6.1.4.1.9070.1.2.3.1.5.1.2.3.0) = Tue Jul  7 01:13:50 2020
        if key == 'symm.tymingTime':
            p_symm_vars['sym.tymingTime_s'] = symm_to_utc_iso(symm_vars[key])
            continue
        #symm.gpsPosition(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.1.0) = 1 47 34 0 534 -1 122 7 42 65 188
        if key == 'symm.gpsPosition':
            p_values = symm_vars[key].split()
            if p_values[0] == "1":
                lat_sign = 1
                lat_s = "N"
            else:
                lat_sign = -1
                lat_s = "S"
            if p_values[5] == "1":
                long_sign = 1
                long_s = "E"
            else:
                long_sign = -1
                long_s = "W"
            lat_deg = p_values[1]
            lat_min = p_values[2]
            lat_sec = p_values[3] + "." + p_values[4]
            latitude_s = lat_deg + " " + lat_min + " " + lat_sec + " " + lat_s
            long_deg = p_values[6]
            long_min = p_values[7]
            long_sec = p_values[8] + "." + p_values[9]
            longitude_s = long_deg + " " + long_min + " " + long_sec + " " + long_s
            elevation = p_values[10]
            p_symm_vars['symm.gpsPosition.latitude_s'] = latitude_s
            p_symm_vars['symm.gpsPosition.longitude_s'] = longitude_s
            p_symm_vars['symm.gpsPosition.elevation'] = float(elevation)
            p_symm_vars['symm.gpsPosition.latitude_f'] = dmg_to_float(float(lat_deg), float(lat_min), float(lat_sec), lat_sign)
            p_symm_vars['symm.gpsPosition.longitude_f'] = dmg_to_float(float(long_deg), float(long_min), float(long_sec), long_sign)
            continue
        #symm.gpsHealth(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.3.0) = Receiver Health: 8
        if key == 'symm.gpsHealth':
            p_symm_vars[key] = int(symm_vars[key].replace('Receiver Health: ', ''))
            continue
        #symm.gpsSatlist(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.4.0) = 9,20,-161,C,32,-160,C,15,-160,C,21,-158,C,10,-154,C,24,-167,C,27,-159,C,8,-161,C,18,-160,C
        if key == 'symm.gpsSatlist':
            p_values = symm_vars[key].split(',')
            satellites = int(p_values[0])
            p_symm_vars['symm.gpsSatList.satellites'] = satellites
            #print("satellites = " + str(satellites))
            p_symm_vars['symm.gpsSatList.satellite'] = { }
            for i in range(0, satellites - 1):
                sat_number = int(p_values[1 + (i * 3) + 0])
                sat_dbW = int(p_values[1 + (i * 3) + 1])
                sat_status = p_values[1 + (i * 3) + 2]
                #print("sat " + str(sat_number) + ": dbW=" + str(sat_dbW) + ", status=" + sat_status)
                p_symm_vars['symm.gpsSatList.satellite'][sat_number] = { }
                p_symm_vars['symm.gpsSatList.satellite'][sat_number]['sat_number'] = sat_number
                p_symm_vars['symm.gpsSatList.satellite'][sat_number]['sat_dbW'] = sat_dbW
                p_symm_vars['symm.gpsSatList.satellite'][sat_number]['sat_status'] = sat_status
        #symm.gpsMode(1.3.6.1.4.1.9070.1.2.3.1.5.1.3.5.0) = Receiver Mode: Survey
        if key == 'symm.gpsMode':
            p_symm_vars[key] = symm_vars[key].replace('Receiver Mode: ', '')
            continue
        #symm.etcAlarmString(1.3.6.1.4.1.9070.1.2.3.1.5.1.6.6.0) = 
        if key == 'symm.etcAlarmString':
            p_symm_vars[key] = symm_vars[key]
            continue
    return p_symm_vars

symm_vars = get_symm_vars(target_server)
print("symm_vars = " + str(symm_vars))
parsed_symm_vars = parse_symm_vars(symm_vars)
print("parsed_symm_vars = " + str(parsed_symm_vars))

#!/usr/bin/python3

from pysnmp.hlapi import *
from SYMM_SMI_MIB import lookup_symm_mib

target_server = "192.168.101.231"
oid_iso = "iso.3.6.1.4.1.9070"
oid_num = "1.3.6.1.4.1.9070"

for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(SnmpEngine(),
                CommunityData('public'),
                UdpTransportTarget((target_server, 161)),
                ContextData(),
                ObjectType(ObjectIdentity(oid_iso)),
                lookupMib=False):
    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
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
                    print(varname + "(" + var + ")" + " = " + value)
                else:
                    print(var + " = " + value)

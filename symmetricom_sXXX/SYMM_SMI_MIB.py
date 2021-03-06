#!/usr/bin/python3

#
# COPY/PASTED FROM SYMM-SMI.json
#
SYMM_MIB = {
  "imports": {
    "class": "imports",
    "SNMPv2-CONF": [
      "NOTIFICATION-GROUP",
      "MODULE-COMPLIANCE"
    ],
    "SNMPv2-SMI": [
      "IpAddress",
      "TRAP-TYPE",
      "OBJECT-IDENTITY",
      "TimeTicks",
      "Counter64",
      "OBJECT-TYPE",
      "MODULE-IDENTITY",
      "Integer32",
      "Unsigned32",
      "Bits",
      "Counter32",
      "iso",
      "NOTIFICATION-TYPE",
      "Gauge32",
      "enterprises",
      "MibIdentifier"
    ],
    "SNMPv2-TC": [
      "TEXTUAL-CONVENTION",
      "DisplayString"
    ]
  },
  "symmetricom": {
    "name": "symmetricom",
    "oid": "1.3.6.1.4.1.9070",
    "class": "moduleidentity",
    "revisions": [
      {
        "revision": "1910-02-06 12:00",
        "description": "jflory - updated NTP, tyming, and etc descriptions"
      }
    ]
  },
  "symmNetworkManagement": {
    "name": "symmNetworkManagement",
    "oid": "1.3.6.1.4.1.9070.1",
    "class": "objectidentity",
    "status": "current"
  },
  "symmCmipManagement": {
    "name": "symmCmipManagement",
    "oid": "1.3.6.1.4.1.9070.1.1",
    "class": "objectidentity",
    "status": "current"
  },
  "symmSnmpManagement": {
    "name": "symmSnmpManagement",
    "oid": "1.3.6.1.4.1.9070.1.2",
    "class": "objectidentity",
    "status": "current"
  },
  "symmTimePictra": {
    "name": "symmTimePictra",
    "oid": "1.3.6.1.4.1.9070.1.2.1",
    "class": "objectidentity",
    "status": "current"
  },
  "symmBroadband": {
    "name": "symmBroadband",
    "oid": "1.3.6.1.4.1.9070.1.2.2",
    "class": "objectidentity",
    "status": "current"
  },
  "symmTTM": {
    "name": "symmTTM",
    "oid": "1.3.6.1.4.1.9070.1.2.3",
    "class": "objectidentity",
    "status": "current"
  },
  "products": {
    "name": "products",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1",
    "class": "objectidentity"
  },
  "experiment": {
    "name": "experiment",
    "oid": "1.3.6.1.4.1.9070.1.2.3.99",
    "class": "objectidentity"
  },
  "ts2000": {
    "name": "ts2000",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.1",
    "class": "objectidentity"
  },
  "nts": {
    "name": "nts",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.2",
    "class": "objectidentity"
  },
  "ts2100": {
    "name": "ts2100",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.3",
    "class": "objectidentity"
  },
  "s100": {
    "name": "s100",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.4",
    "class": "objectidentity"
  },
  "syncserver": {
    "name": "syncserver",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5",
    "class": "objectidentity"
  },
  "xli": {
    "name": "xli",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.6",
    "class": "objectidentity"
  },
  "version": {
    "name": "version",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1",
    "class": "objectidentity"
  },
  "ntpSystem": {
    "name": "ntpSystem",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1",
    "class": "objectidentity"
  },
  "tyming": {
    "name": "tyming",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.2",
    "class": "objectidentity"
  },
  "gps": {
    "name": "gps",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.3",
    "class": "objectidentity"
  },
  "dialup": {
    "name": "dialup",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.4",
    "class": "objectidentity"
  },
  "net": {
    "name": "net",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.5",
    "class": "objectidentity"
  },
  "etc": {
    "name": "etc",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6",
    "class": "objectidentity"
  },
  "ntpSysLeap": {
    "name": "ntpSysLeap",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.1",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "INTEGER",
      "class": "type",
      "constraints": {
        "enumeration": {
          "noWarning": 0,
          "addSecond": 1,
          "subtractSecond": 2,
          "alarm": 3
        }
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysStratum": {
    "name": "ntpSysStratum",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.2",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "Integer32",
      "class": "type",
      "constraints": {
        "range": [
          {
            "min": 0,
            "max": 255
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysPrecision": {
    "name": "ntpSysPrecision",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.3",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "Integer32",
      "class": "type"
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysRootDelay": {
    "name": "ntpSysRootDelay",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.4",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "OCTET STRING",
      "class": "type"
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysRootDispersion": {
    "name": "ntpSysRootDispersion",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.5",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "OCTET STRING",
      "class": "type"
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysRefID": {
    "name": "ntpSysRefID",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.6",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysRefTime": {
    "name": "ntpSysRefTime",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.7",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysPoll": {
    "name": "ntpSysPoll",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.8",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "Integer32",
      "class": "type"
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysPeer": {
    "name": "ntpSysPeer",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.9",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "Unsigned32",
      "class": "type"
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysPhase": {
    "name": "ntpSysPhase",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.10",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysFreq": {
    "name": "ntpSysFreq",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.11",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysError": {
    "name": "ntpSysError",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.12",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysClock": {
    "name": "ntpSysClock",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.13",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysSystem": {
    "name": "ntpSysSystem",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.14",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysProcessor": {
    "name": "ntpSysProcessor",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.15",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "ntpSysNotrust": {
    "name": "ntpSysNotrust",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.16",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "INTEGER",
      "class": "type",
      "constraints": {
        "range": [
          {
            "min": 0,
            "max": 1
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "mandatory"
  },
  "ntpSysPktsReceived": {
    "name": "ntpSysPktsReceived",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.17",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "INTEGER",
      "class": "type",
      "constraints": {
        "range": [
          {
            "min": 0,
            "max": 32768
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "mandatory"
  },
  "ntpSysMode": {
    "name": "ntpSysMode",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.18",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "INTEGER",
      "class": "type",
      "constraints": {
        "enumeration": {
          "unspecified": 0,
          "symactive": 1,
          "sympassive": 2,
          "client": 3,
          "server": 4,
          "broadcast": 5,
          "reservedctl": 6,
          "reservedpriv": 7
        }
      }
    },
    "maxaccess": "read-only",
    "status": "mandatory"
  },
  "ntpSysVersion": {
    "name": "ntpSysVersion",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.1.19",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "tymingStatus": {
    "name": "tymingStatus",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.2.1",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "tymingSource": {
    "name": "tymingSource",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.2.2",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "tymingTime": {
    "name": "tymingTime",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.2.3",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "tymingVersion": {
    "name": "tymingVersion",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.2.4",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "tymingFlyPeriod": {
    "name": "tymingFlyPeriod",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.2.5",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "INTEGER",
      "class": "type"
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "gpsPosition": {
    "name": "gpsPosition",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.3.1",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "gpsUTCOffset": {
    "name": "gpsUTCOffset",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.3.2",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "INTEGER",
      "class": "type",
      "constraints": {
        "range": [
          {
            "min": 0,
            "max": 127
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "gpsHealth": {
    "name": "gpsHealth",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.3.3",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "gpsSatlist": {
    "name": "gpsSatlist",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.3.4",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 128
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "gpsMode": {
    "name": "gpsMode",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.3.5",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcVersion": {
    "name": "etcVersion",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6.1",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 80
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcSerialNbr": {
    "name": "etcSerialNbr",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6.2",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcModel": {
    "name": "etcModel",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6.3",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 40
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcUpgrade": {
    "name": "etcUpgrade",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6.4",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 1024
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcUpgradeServer": {
    "name": "etcUpgradeServer",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6.5",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 1,
            "max": 1024
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcAlarmString": {
    "name": "etcAlarmString",
    "oid": "1.3.6.1.4.1.9070.1.2.3.1.5.1.6.6",
    "nodetype": "scalar",
    "class": "objecttype",
    "syntax": {
      "type": "DisplayString",
      "class": "type",
      "constraints": {
        "size": [
          {
            "min": 0,
            "max": 1024
          }
        ]
      }
    },
    "maxaccess": "read-only",
    "status": "current"
  },
  "etcAlarm": {
    "name": "etcAlarm",
    "oid": "1.3.6.1.4.1.90700.0",
    "class": "notificationtype",
    "objects": [
      {
        "module": "SYMM-SMI",
        "object": "etcAlarmString"
      }
    ]
  },
  "meta": {
    "comments": [
      "ASN.1 source http://mibs.snmplabs.com:80/asn1/SYMM-SMI",
      "Produced by pysmi-0.3.4 at Thu Jul  2 00:28:38 2020",
      "On host rockhopper platform Linux version 4.4.0-19041-Microsoft by user fio",
      "Using Python version 3.8.2 (default, Apr 27 2020, 15:53:34) "
    ],
    "module": "SYMM-SMI"
  }
}

def lookup_symm_mib(l_oid):
  for s in SYMM_MIB:
    #print("lookup_symm_mib(" + l_oid + "): " + s)
    if "oid" in SYMM_MIB[s]:
      name = s
      # returned data always has an ending .0 (value?)
      oid = SYMM_MIB[s]["oid"] + ".0"
      #print("lookup_symm_mib(" + l_oid + "): " + oid + ": " + name)
      if l_oid == oid:
        #print("lookup_symm_mib(" + l_oid + "): " + oid + ": FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return "symm." + name
  return None

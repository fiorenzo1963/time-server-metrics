#!/usr/bin/python3

from influxdb import InfluxDBClient
import os
import sys
import fcntl
import socket
import time
import fcntl
import syslog
import random
import subprocess
import shutil
import json
import logging.handlers

DB_DB = 'metrics_test_00' # make a parameter

def setup_db(host, port):
    print("setup_db: host=" + str(host) + ":" + str(port))
    db = InfluxDBClient(host=host, port=port)
    db.switch_database(DB_DB)
    return db

def insert_db(db, metrics, metrics_stamp):
    print('insert_db() ' + str(db))
    # print("insert_db: db=" + str(db) + ", metrics=" + str(metrics) + ", metrics_stamp=" + metrics_stamp)
    json_e = { }
    json_e['measurement'] = 'symm300_rubidium_ptp.0' # make a param
    json_e['tags'] = { }
    json_e['tags']['host'] = "masterclock-h1.0" # make a param
    # json_e['time'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    json_e['time'] = metrics_stamp
    json_e['fields'] = { }
    for metric in metrics.keys():
        value = metrics[metric]
        print("insert_db: " + metric + ": " + str(value))
        json_e['fields'][metric] = value
        #json_body = [ json_e ]
    json_body = [ json_e ]
    # print('JSON_BODY = ' + str(json_body))
    db.write_points(json_body)
    print('insert_db() ' + str(db) + ': done')

#!/bin/bash
set -x
killall symm_mib_walk.py
sleep 1
killall -9 symm_mib_walk.py
sleep 1
nohup ./symm_mib_walk.py > symm_mib_walk.log 2>&1 &

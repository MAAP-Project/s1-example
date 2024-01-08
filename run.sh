#!/bin/bash

basedir=$( cd "$(dirname "$0")" ; pwd -P )

# change the dest to /output on DPS
python ${basedir}/asf-s1-edc.py --dest 'output'
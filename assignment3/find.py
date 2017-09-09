#!/usr/bin/env python3
import os, sys
import random
import urllib
import subprocess
import re
from collections import Counter

os.system('clear')

extension=sys.argv[1]
dir=sys.argv[2]
#dir="/Users/samiulsaki/Documents//inf4331nsa/INF3331-aschowdh/assignment3"
#dir1="/Users/samiulsaki/Documents/inf4331nsa/UiO-INF3331.github.io/assignments"


def recursive(dir):
  for root,folders,files in os.walk(dir):
    for file in files:
      if file.endswith(extension):
        print(os.path.abspath(root),file,sep="/")


recursive(dir)
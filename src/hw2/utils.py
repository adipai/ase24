"""
gate: guess, assess, try, expand
(c) 2023, Tim Menzies, BSD-2
Learn a little, guess a lot, try the strangest guess, learn a little more, repeat

USAGE:
  python gate.py [OPTIONS]

OPTIONS:
  -c --cohen    small effect size               = .35
  -f --file     csv data file name              = ../data/diabetes.csv
  -h --help     show help                       = False
  -k --k        low class frequency kludge      = 1
  -m --m        low attribute frequency kludge  = 2
  -s --seed     random number seed              = 31210
  -t --todo     start up action                 = help
"""

import math
import re
import sys

def coerce(s1):
    def fun(s2):
        if s2 == "nil":
            return None
        else:
            return s2 == "true" or (s2 != "false" and s2)
    try:
        return float(s1)
    except:
        return fun(re.match(r'^\s*(.*\S)', s1).group(1))

def settings(s):
    t, pat = {}, r"--(\w+)[^=]*=\s*(\S+)"
    for k, s1 in re.findall(pat, s):
        t[k] = coerce(s1)
    t["_help"] = s
    return t

def cells(s):
    return [coerce(s1) for s1 in re.findall("([^,]+)", s)]

def csv(src):
    i, src = 0, src if src == "-" else open(src)
    
    def read_line():
        nonlocal i
        s = src.readline()
        if s:
            i += 1
            return i, cells(s)
        else:
            src.close()

    return read_line

def round(n, ndecs=None):
    if type(n) == str:
        return n
    if math.floor(n) == n:
        return n
    mult = 10**(ndecs or 2)
    return math.floor(n * mult + 0.5) / mult

def cells(s):
    t = []
    for s1 in s.split(","):
        t.append(coerce(s1))
    return t


def cli(t):
    options_dict = {}
    options = sys.argv[1:]
    i=0
    while(i<len(options)):
        options_dict[options[i]] = options[i+1]
        i = i+2
        

    for opt,val in options_dict.items():
        if opt.startswith('--'):
            opt = opt[2:]
        elif opt.startswith('-'):
            opt = opt[1:]
        else:
            continue
        
        t[opt] = coerce(val)

    return t


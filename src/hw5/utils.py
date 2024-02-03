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
  -t --run_tc   run test-cases                  = None
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
    options = re.findall(r'-(\w+)\s+--(\w+)\s+.*=\s*(\S+)', s)
    the = {}
    opt_dir = {}
    for option in options:
        short_form, full_form, default_value = option
        the[full_form] = coerce(default_value)
        opt_dir[short_form] = full_form
    return [the, opt_dir]

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


def cli(the, opt_dir):
    options_dict = {}
    options = sys.argv[1:]
    if("--help" in options or "-h" in options):
        the["help"] = 'True'
        return

    for i in range(0, len(options), 2):
        options_dict[options[i]] = options[i+1]

    for opt,val in options_dict.items():
        if opt.startswith('--'):
            the[opt[2:]] = coerce(val)
        elif opt.startswith('-'):
            the[opt_dir[opt[1:]]] = coerce(val)
    return the

def keys(t):
    u = [k for k in t]
    u.sort()
    return u

def copy(t):
    if type(t) != dict and type(t) != list:
        return t

    u = {}
    for k, v in t.items() if isinstance(t, dict) else enumerate(t):
        u[copy(k)] = copy(v)

    return u

def shuffle(t):
    u = t.copy()
    for i in range(len(u) - 1, 0, -1):
        j = random.randint(0, i)
        u[i], u[j] = u[j], u[i]
    return u

def slice(t, go=None, stop=None, inc=None):
    if go and go < 0:
        go = len(t) + go
    if stop and stop < 0:
        stop = len(t) + stop

    u = [t[j] for j in range((go or 0)//1, (stop or len(t))//1, (inc or 1)//1)]
    return u

""" HW5 addition """

def entropy(t):
    n = sum(t.values())
    e = 0
    for v in t.values():
        e -= (v / n) * math.log2(v / n)
    
    return e, n

def keysort(t, fun):
    u = [{"x": x, "y": fun(x)} for x in t]  # decorate
    u.sort(key=lambda a: a["y"])  # sort
    v = [xy["x"] for xy in u]  # undecorate
    return v
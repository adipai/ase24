import math
import re

def coerce(s1):
    def fun(s2):
        if s2 == "nil":
            return None
        else:
            return s2 == "true" or (s2 != "false" and s2)

    return int(s1) or float(s1) or fun(re.match(r'^\s*(.*\S)', s1).group(1))

def settings(s):
    t, pat = {}, "[-][-]([%S]+)[^=]+= ([%S]+)"
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

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

from test_suite import TestSuite

help_str = __doc__

test_suite = TestSuite()
egs = {
    "coerce":test_suite.test_coerce,
    "settings":test_suite.test_settings,
    "cells":test_suite.test_cells,
    "round":test_suite.test_round,
    "add_num":test_suite.test_add_num,
    "mid_num":test_suite.test_mid_num,
    "div_num":test_suite.test_div_num,
    "add_sym":test_suite.test_add_sym,
    "mid_sym":test_suite.test_mid_sym,
    "div_sym":test_suite.test_div_sym,
    "small_sym":test_suite.test_small_sym
    }

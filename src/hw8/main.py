from utils import settings, cli, round, o
from config import help_str, egs
from test_suite import TestSuite
# from globals import the, my
from learner import print_stats,bayes
from data import DATA
import random
from row import ROW
import csv
from task import far
from datetime import datetime
import math

"""
# Parse command-line arguments
parser = argparse.ArgumentParser(description="gate: guess, assess, try, expand")
parser.add_argument("-c", "--cohen", type=float, default=0.35, help="small effect size")
parser.add_argument("-f", "--file", type=str, default="../data/diabetes.csv", help="csv data file name")
parser.add_argument("-h", "--help", action="store_true", help="show help")
parser.add_argument("-k", "--k", type=int, default=1, help="low class frequency kludge")
parser.add_argument("-m", "--m", type=int, default=2, help="low attribute frequency kludge")
parser.add_argument("-s", "--seed", type=int, default=31210, help="random number seed")
parser.add_argument("-t", "--run_tc", type=str, default="None", help="run test cases")
args = parser.parse_args()

# Access command-line argument values
cohen = args.cohen
file_name = args.file
show_help = args.help
k_value = args.k
m_value = args.m
seed_value = args.seed
run test-cases = args.run_tc
"""
# global my

def hw7_part1(the):
    d = DATA(src = the['file'], the=the)
    mid_whole, div_whole = d.mid_div()
    random_seeds = random.sample(range(100),20)
    smo_output = []
    any50_output = []
    for random_seed in random_seeds:
        
        data_new = DATA(src = the['file'], the=the)
        _,_, a = data_new.gate(random_seed, budget=5)
        smo_output.append(a)
        any50_output.append(data_new.any50(random_seed))
    
    best_whole = data_new.best_whole(random_seed)
    print("date:{}\nfile:{}\nrepeat:{}\nseed:{}\nrows:{}\ncols:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20",the['seed'],len(data_new.rows), len(data_new.rows[0].cells)))
    print(format_row("names", data_new.cols.names,        None))
    print(format_row("Mid"  , list(mid_whole[0].values()),mid_whole[1]))
    print(format_row("Div"  , list(div_whole[0].values()),div_whole[1]))
    print("#")
    smo_output = sorted(smo_output, key=lambda x: x[1])
    any50_output = sorted(any50_output, key=lambda x: x[1])
    for op in smo_output:
        print(format_row("smo9",op[0],op[1]))
    print("#")
    for op in any50_output:
        print(format_row("any50",op[0],op[1]))
    print("#")
    print(format_row("100%",best_whole[0],best_whole[1]))

def format_row(name, row, d2h_val=None):
    return_string = ""
    len_space = [11,11,9,10,11,10,9,9]

    def _format_item(item):
        try:
            float(item)
            return item
        except:
            return f"'{item}'"

    for i, item in enumerate(row):
        start_string = ""
        end_string=""
        if i == 0:
            start_string += "["
        if i == 7:
            end_string += "]"
        item_str = start_string + _format_item(str(item)) + end_string
        return_string +=  item_str + (" " * (len_space[i] - len(item_str)))
    return f"{name}\t\t\t{return_string}\t{'d2h-' if d2h_val is None else str(d2h_val)}"


def distance(the, data_new):
    row_first = ['8','304','193','70','1','4732','18.5','10']
    row_obj = ROW(row_first, the=the)
    sorted_rows = row_obj.neighbors(data=data_new)

    print("Task 1: Get Distance Working:")
    print()
    index = 1
    for row in sorted_rows:
        if(index % 30 == 1):
            print(index, row.cells, round(row.dist(row_obj,data_new)))
        
        index += 1

    print()
    print()

def eg_branch(the={}):
    print("Task2 output: ")
    d = DATA(the['file'], the=the)
    best, rest, evals = d.branch()
    print("centroid of output cluster: ")
    print(o(best.mid().cells), o(rest.mid().cells))
    print("evals: ", evals)
    print()

def eg_doubletap(the={}):
    print("Task3 output: ")
    d = DATA(the['file'], the=the)
    best1, rest, evals1 = d.branch(32)
    best2, _, evals2 = best1.branch(4)
    print("median and best found in that four: ")
    print(o(best2.mid().cells), o(rest.mid().cells))
    print("evals: ",evals1 + evals2)
    print()

def eg_tree(the={}):
    print("Task1 output: ")
    data_instance = DATA(the['file'], the=the)
    t, evals = data_instance.tree(True)
    t.show()
    print("evals: ", evals)
    print()

"""HW7 addition"""
def _ranges1(col, rowss):
    out, nrows = {}, 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in rows:
            x = row.cells[col.at]
            if x != "?":
                bin_ = col.bin(x)
                if bin_ not in out:
                    out[bin_] = Range(col.at, col.txt, x)
                out[bin_].add(x, y)
    out = list(out.values())
    out.sort(key=lambda r: r.x['lo'])
    return _mergeds(out, nrows // the.bins) if col.has else out

def _mergeds(ranges, tooFew):
    t = []
    i = 0
    while i < len(ranges):
        a = ranges[i]
        if i < len(ranges) - 1:
            both = a.merged(ranges[i + 1], tooFew)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1
    if len(t) < len(ranges):
        return _mergeds(t, tooFew)
    for i in range(1, len(t)):
        t[i].x['lo'] = t[i - 1].x['hi']
    t[0].x['lo'] = -math.inf
    t[-1].x['hi'] = math.inf
    return t

def bins():
    d = DATA(the['file'], the=the)
    best, rest, _ = d.branch()
    LIKE = list(best.rows.values())
    # HATE = random.sample(rest.rows, min(3 * len(LIKE), len(rest.rows)))
    HATE = random.sample(list(rest.rows.values()), min(3 * len(LIKE), len(rest.rows)))

    def score(range_):
        return range_.score("LIKE", len(LIKE), len(HATE))

    t = []
    for col in list(d.cols.x.values()):
        print("")
        for range_ in _ranges1(col, {"LIKE": LIKE, "HATE": HATE}):
            print(range_)
            t.append(range_)
   

if __name__ == '__main__':
    the, opt_dir = settings(help_str)
    the = cli(the, opt_dir)

    if(the['help'] == 'True'):
        print("You can use the following help: ")
        print(help_str)
        exit(1)
    
    if(the['run_tc']=="all"):
        print("running all tests!")
        ts = TestSuite()
        ts.run_tests()
    elif(the['run_tc']==""):
        pass
    elif(the['run_tc']!="None"):
        print("running test "+ the['run_tc'])
        ts = TestSuite()
        try:
            egs[the['run_tc']]()
            print(f"Test {the['run_tc']} passed.")
        except AssertionError as e:
            print(f"Test {the['run_tc']} failed: {e}")
        
    hw7_part1(the=the)
    # data_new = DATA(the['file'], the=the)
    # distance(the, data_new)
    # far(the, data_new)
    # eg_tree(the=the)

    # eg_branch(the=the)
    
    # eg_doubletap(the=the)


    

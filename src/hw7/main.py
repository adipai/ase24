from utils import settings, cli, round, o
from config import help_str, egs
from test_suite import TestSuite
# from globals import the, my
from learner import print_stats,bayes
from data import DATA
import random
from row import ROW
import csv
import statistics
from task import far
from datetime import datetime
from stats import SAMPLE, eg0

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
    print("TASK-1:")
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

def hw7_part2(the):
    print("\n")
    print("TASK-2:")
    d = DATA(src = the['file'], the=the)
    print("date:{}\nfile:{}\nrepeat:{}\nseed:{}\nrows:{}\ncols:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20",the['seed'],len(d.rows), len(d.rows[0].cells)))
    sortedRows =  sorted(d.rows, key=lambda x: x.d2h(d))
    print(f"best: {o(sortedRows[0].d2h(d),n=2)}")
    all = base(d)
    print(f"tiny: {o(statistics.stdev(all)*0.35,n=2)}")
    print("#base #bonr9 #rand9 #bonr15 #rand15 #bonr20 #rand20 #rand358 ")
    eg0([
        SAMPLE(randN(d,9, the=the), "rand9"),
        SAMPLE(randN(d,15, the=the), "rand15"),
        SAMPLE(randN(d,20, the=the), "rand20"), 
        SAMPLE(randN(d,358, the=the), "rand358"), 
        SAMPLE(bonrN(d,9, the=the), "bonr9"),
        SAMPLE(bonrN(d,15,the=the), "bonr15"),
        SAMPLE(bonrN(d,20, the=the), "bonr20"),
        SAMPLE(base(d), "base")
    ])

def base(d):
    baseline_output = [row.d2h(d) for row in d.rows]
    return baseline_output

def randN(d, n, the):
    random.seed(the['seed'])
    rand_arr = []
    for _ in range(20):
        rows = d.rows
        random.shuffle(rows)
        rowsN = random.sample(rows,n)
        rowsN.sort(key=lambda row: row.d2h(d))
        rand_arr.append(round(rowsN[0].d2h(d),2))

    return rand_arr

def bonrN(d, n, the):
    bonr_arr = []
    for _ in range(20):
        _,_, best_stats = d.gate(the['seed'], 4, n-4, 0.5)
        bonr_arr.append(best_stats[1])
    
    return bonr_arr

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
    hw7_part2(the=the)
    # data_new = DATA(the['file'], the=the)
    # distance(the, data_new)
    # far(the, data_new)
    # eg_tree(the=the)

    # eg_branch(the=the)
    
    # eg_doubletap(the=the)


    

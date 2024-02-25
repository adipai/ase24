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
    d.mid_div()
    random_seeds = random.sample(range(100),20)
    for random_seed in random_seeds:
        print("========================================================================================================================")
        print("Current random seed: ", random_seed)
        print("Smo9 results: ")
        data_new = DATA(src = the['file'], the=the)
        data_new.gate(random_seed, budget=5)

        # print()
        print("any50 results: ")
        data_new.any50(random_seed)
        print()
        print("========================================================================================================================")

        data_new.best_whole(random_seed)


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
    # data_new = DATA(the['file'], the=the)
    # distance(the, data_new)
    # far(the, data_new)
    # eg_tree(the=the)

    # eg_branch(the=the)
    
    # eg_doubletap(the=the)


    

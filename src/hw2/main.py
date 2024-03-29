from data import DATA
from utils import settings, cli
from config import help_str, egs
from test_suite import TestSuite

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

if __name__ == '__main__':
    t, opt_dir = settings(help_str)
    t = cli(t, opt_dir)
    if(t['help']):
        print("You can use the following help: ")
        print(help_str)
    else:
        if(t['run_tc']=="all"):
            print("running all tests!")
            ts = TestSuite()
            ts.run_tests()
        elif(t['run_tc']==""):
            pass
        elif(t['run_tc']!="None"):
            print("running test "+ t['run_tc'])
            ts = TestSuite()
            try:
                egs[t['run_tc']]()
                print(f"Test {t['run_tc']} passed.")
            except AssertionError as e:
                print(f"Test {t['run_tc']} failed: {e}")

        data_new = DATA(t['file'])
        print(data_new.stats())

from data import DATA
from utils import settings, cli
from config import help_str

"""
# Parse command-line arguments
parser = argparse.ArgumentParser(description="gate: guess, assess, try, expand")
parser.add_argument("-c", "--cohen", type=float, default=0.35, help="small effect size")
parser.add_argument("-f", "--file", type=str, default="../data/diabetes.csv", help="csv data file name")
parser.add_argument("-h", "--help", action="store_true", help="show help")
parser.add_argument("-k", "--k", type=int, default=1, help="low class frequency kludge")
parser.add_argument("-m", "--m", type=int, default=2, help="low attribute frequency kludge")
parser.add_argument("-s", "--seed", type=int, default=31210, help="random number seed")
parser.add_argument("-t", "--todo", type=str, default="help", help="start up action")
args = parser.parse_args()

# Access command-line argument values
cohen = args.cohen
file_name = args.file
show_help = args.help
k_value = args.k
m_value = args.m
seed_value = args.seed
startup_action = args.todo
"""

if __name__ == '__main__':
    t = cli(settings(help_str))
    if(t['help']=='True'):
        print("You can use the following help: ")
        print(help_str)
    else:

        data_new = DATA(t['file'])
        print("Data Stats are as follows: ")
        print(data_new.stats())

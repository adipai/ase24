from data import DATA
from utils import settings, cli
from config import help_str, egs
from test_suite import TestSuite
from globals import opt_dir, the, my


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

def print_stats():
    """
    Function to print data stats
    """
    data_new = DATA()
    data_new.full_data(the['file'])
    # print(data_new.stats())
    return data_new

def learn(data_new):
    rows_obj = data_new.rows_obj
    rows_actual = data_new.rows_actual
    for i in range(len(rows_obj)):
        row_obj = rows_obj[i]
        row_actual = rows_actual[i]
        my['n'] += 1
        kl = row_obj.cells[data_new.cols.klass.at-1]
        if(my['n']>10):
            my['tries'] += 1
            predict_class, _ = row_obj.likes(my['datas'])
            if(predict_class == kl):
                my['acc'] += 1  
        if(i > 0 and kl not in my['datas']):
            my['datas'][kl] = DATA()
            my['datas'][kl].add(rows_actual[0])
            my['datas'][kl].add(row_actual)
        
        elif(i > 0 and kl in my['datas']):
            my['datas'][kl].add(row_actual)

def bayes(data_new):
    learn(data_new)
    print("Accuracy for "+the['file'].split("/")[3] + ": ", (my['acc']/my['tries'])*100)


if __name__ == '__main__':
    settings(help_str)
    cli()

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
    
    data_new = print_stats()
    bayes(data_new)
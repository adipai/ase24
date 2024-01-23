import sys
import io
import math
from num import NUM
from sym import SYM
from utils import coerce, settings, cells,  round
from learner import *

class TestSuite:
    # def __init__(self) -> None:
    #     self.f_tests = {}

    def test_coerce(self):
        assert coerce("42") == 42
        assert coerce("3.14") == 3.14
        assert coerce("true") == True
        assert coerce("false") == False
        assert coerce("nil") == None
        assert coerce("  hello  ") == "hello"
        assert coerce("  42  ") == 42

    def test_settings(self):
        input_str = "-c --cohen = 0.35\n -f --file = data.csv\n -h --help = False"
        result, opt_dir = settings(input_str)

        assert result == {'cohen': 0.35, 'file': 'data.csv', 'help': 'False'}

    def test_cells(self):
        input_str = "1, 2, 3.14, true, false, nil, hello"
        result = cells(input_str)
        assert result == [1, 2, 3.14, True, False, None, "hello"]

    def test_round(self):
        assert round(3.14159, 2) == 3.14
        assert round(42) == 42
        assert round("hello") == "hello"
        assert round(True) == True
        assert round(False) == False

    def test_add_num(self):
        num_obj = NUM()
        num_obj.add(5)
        assert num_obj.n == 1
        assert num_obj.mu == 5
        assert num_obj.m2 == 0
        assert num_obj.lo == 5
        assert num_obj.hi == 5

        num_obj.add(10)
        assert num_obj.n == 2
        assert num_obj.mu == 7.5
        assert num_obj.m2 == 12.5
        assert num_obj.lo == 5
        assert num_obj.hi == 10

    def test_mid_num(self):
        num_obj = NUM()
        num_obj.add(5)
        num_obj.add(10)
        assert num_obj.mid() == 7.5

    def test_div_num(self):
        num_obj = NUM()
        num_obj.add(5)
        num_obj.add(10)
        assert num_obj.div() == (12.5 / 1)**0.5

    def test_add_sym(self):
        sym_obj = SYM()
        sym_obj.add("a")
        assert sym_obj.n == 1
        assert sym_obj.has == {"a": 1}
        assert sym_obj.mode == "a"
        assert sym_obj.most == 1

        sym_obj.add("b")
        sym_obj.add("a")
        assert sym_obj.n == 3
        assert sym_obj.has == {"a": 2, "b": 1}
        assert sym_obj.mode == "a"
        assert sym_obj.most == 2

    def test_mid_sym(self):
        sym_obj = SYM()
        sym_obj.add("a")
        sym_obj.add("b")
        assert sym_obj.mid() == "a"

    def test_div_sym(self):
        sym_obj = SYM()
        sym_obj.add("a")
        sym_obj.add("b")
        sym_obj.add("a")
        sym_obj.add("c")
        assert math.isclose(sym_obj.div(), 1.5)

    def test_small_sym(self):
        sym_obj = SYM()
        assert sym_obj.small() == 0

    def test_print_stats_diabetes(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        result = print_stats(the["file"], the)
        assert isinstance(result, DATA)

    def test_learn_diabetes(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the)
        result = learn(data_new, the)
        assert isinstance(result, dict)
        assert 'n' in result
        assert 'tries' in result
        assert 'acc' in result
        assert 'datas' in result
    
    def test_bayes_diabetes(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the)
        data_new.full_data(the['file'])
        result = bayes(data_new, the)
        assert result > 70

    def test_print_stats_soybean(self):
        the = {'cohen': 0.35, 'file': '../../Data/soybean.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        result = print_stats(the["file"], the)
        assert isinstance(result, DATA)

    def test_learn_soybean(self):
        the = {'cohen': 0.35, 'file': '../../Data/soybean.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the) 
        result = learn(data_new, the)
        assert isinstance(result, dict)
        assert 'n' in result
        assert 'tries' in result
        assert 'acc' in result
        assert 'datas' in result
    
    def test_bayes_soybean(self):
        the = {'cohen': 0.35, 'file': '../../Data/soybean.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the)
        data_new.full_data(the['file'])
        result = bayes(data_new, the)
        assert result > 80
        
    def _run_test(self, test_func, test_name):
        try:
            test_func()
            print(f"Test {test_name} passed.")
        except AssertionError as e:
            # self.f_tests[test_name[5:]] = test_name[5:]  # append to failing test lists
            print(f"Test {test_name} failed: {e}")

    def run_tests(self):
        print("Running tests in TestSuite")
        test_functions = [func for func in dir(self) if func.startswith('test_') and callable(getattr(self, func))]
        for test_func_name in test_functions:
            test_func = getattr(self, test_func_name)
            self._run_test(test_func, test_func_name)        
        
        # append to failing test lists
        # if self.f_tests:
        #     set_environment_variable('TEST_SUITE', ' '.join(self.f_tests.keys()))
        #     self.f_tests.clear()


if __name__ == '__main__':
    test_suite = TestSuite()
    test_suite.run_tests()

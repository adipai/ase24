import sys
import io
import math
from num import NUM
from sym import SYM
from data import DATA
from node import NODE
from utils import coerce, settings, cells, round, entropy, keysort, any_item, many, o
from learner import *
from task import far

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
        assert sym_obj.div() == (1.5, 4)
    
    def test_small_sym(self):
        sym_obj = SYM()
        assert sym_obj.small() == 0

    def test_print_stats_diabetes(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        result = print_stats(the)
        assert isinstance(result, DATA)
    
    def test_bayes_diabetes(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the, src= the['file'])
        result = bayes( the)
        assert result > 70

    def test_print_stats_soybean(self):
        the = {'cohen': 0.35, 'file': '../../Data/soybean.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        result = print_stats(the)
        assert isinstance(result, DATA)
    
    def test_bayes_soybean(self):
        the = {'cohen': 0.35, 'file': '../../Data/soybean.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the, src= the['file'])
        
        result = bayes(the)
        assert result > 80

    def test_datas_type(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the, src= the['file'])
        
        assert isinstance(data_new, DATA)
    
    def test_datas_stats_diabetes(self):
        the = {'cohen': 0.35, 'file': '../../Data/diabetes.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the = the, src= the['file'])
        
        stats = data_new.stats()
        mock_result = {'Preg': 3.85, 'Plas': 120.89, 'Pres': 69.11, 'Skin': 20.54, 'Insu': 79.8, 'Mass': 31.99, 'Pedi': 0.47, 'Age': 33.24, 'class!': 'negative'}
        assert stats == mock_result
    
    def test_datas_stats_soybean(self):
        the = {'cohen': 0.35, 'file': '../../Data/soybean.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data_new = DATA(the=the, src= the['file'])
        
        stats = data_new.stats()
        mock_result = {'date': 'september', 'plant-stand ': 'normal', 'precip': 'gt-norm', 'temp': 'norm', 'hail': 'yes', 'crop-hist': 'same-lst-two-yrs', 'area-damaged': 'low-areas', 'severity': 'pot-severe', 'seed-tmt': 'none', 'germination': '80-89', 'plant-growth': 'norm', 'leaves': 'abnorm', 'leafspots-halo': 'no-yellow-halos', 'leafspots-marg': 'w-s-marg', 'leafspot-size': 'gt-1/8', 'leaf-shread': 'absent', 'leaf-malf': 'absent', 'leaf-mild': 'absent', 'stem': 'abnorm', 'lodging': 'yes', 'stem-cankers': 'absent', 'canker-lesion': 'dna', 'fruiting-bodies': 'absent', 'external-decay': 'absent', 'mycelium': 'absent', 'int-discolor': 'none', 'sclerotia': 'absent', 'fruit-pods': 'norm', 'fruit-spots': 'absent', 'seed': 'norm', 'mold-growth': 'absent', 'seed-discolor': 'absent', 'seed-size': 'norm', 'shriveling': 'absent', 'roots': 'norm', 'class!': 'brown-spot'}
        assert stats == mock_result

    def test_num_heaven_pos(self):
        n = NUM("COL+",1)
        assert n.heaven == 1
    
    def test_num_heaven_neg(self):
        n = NUM("COL-",1)
        assert n.heaven == 0

    def test_entropy(self):
        t_entropy = {'A': 10, 'B': 20, 'C': 30}
        result_entropy, total_count = entropy(t_entropy)
        assert result_entropy == 1.4591479170272448 and total_count == 60

    def test_keysort(self):
        t_keysort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result_keysort = keysort(t_keysort, lambda x: x % 3)
        assert result_keysort == [3, 9, 6, 3, 1, 4, 1, 5, 2, 5, 5]

    def test_any_item(self):
        t_any_item = [10, 20, 30, 40, 50]
        result_any_item = any_item(t_any_item)
        assert result_any_item in t_any_item

    def test_many(self):
        t_many = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result_many_default = many(t_many)
        result_many_custom = many(t_many, n=3)
        assert len(result_many_default) == len(t_many)
        assert len(result_many_custom) == 3

    def test_far(self):
        data_new = DATA('../../Data/auto93.csv', the={})
        _, attempts = far({}, data_new)
        assert attempts == 100
    
    def test_faraway(self):
        data_new = DATA('../../Data/auto93.csv', the={})
        a,b,C,_ = data_new.farapart(data_new.rows[:21])
        assert a.cells[0] == b.cells[0]
        assert C<0.24

    def test_o(self):
        
        assert o(10) == "10"
        assert o(3.14159, 2) == "3.14"
        assert o("hello") == "hello"
        assert o([1, 2, 3]) == "{1, 2, 3}"
        assert o([[1, 2], [3, 4]]) == "{{1, 2}, {3, 4}}"
    

    def test_DATA_half(self):

        # Test case 1: Testing the half method with sorting and before
        the = {'cohen': 0.35, 'file': '../../Data/auto93.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data = DATA(the = the, src= the['file'])
        as_, bs, a, b, C, d_ab, evals = data.half(data.rows, sortp=True, before=None)
        assert len(as_) == 200
        assert len(bs) == 198
        assert C > 0
        assert d_ab > 0
        assert evals > 0
        
        # Test case 2: Testing the half method without sorting and before
        as_, bs, a, b, C, d_ab, evals = data.half(data.rows, sortp=False, before=None)
        assert len(as_) == 200
        assert len(bs) == 198
        assert C > 0
        assert d_ab > 0
        assert evals > 0

    def test_DATA_tree(self):
            
            the = {'cohen': 0.35, 'file': '../../Data/auto93.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
            data = DATA(the = the, src= the['file'])
            tree, evals = data.tree(sortp=True)
            assert isinstance(tree, NODE)
            assert evals > 0
    

    def test_DATA_branch(self):
        
        the = {'cohen': 0.35, 'file': '../../Data/auto93.csv', 'help': 'False', 'k': 1.0, 'm': 2.0, 'seed': 31210.0, 'run_tc': 'all'}
        data = DATA(the = the, src= the['file'])
        left_branch, right_branch, evals = data.branch()
        assert len(left_branch.rows) > 0
        assert len(right_branch.rows) > 0
        assert evals > 0

        
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


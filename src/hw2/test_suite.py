import sys
import io
import math
from num import NUM
from sym import SYM
from data import DATA
from utils import coerce, settings, cells, csv, round, cli


class UtilityTestSuite:

    def test_coerce(self):
        assert coerce("42") == 42
        assert coerce("3.14") == 3.14
        assert coerce("true") == True
        assert coerce("false") == False
        assert coerce("nil") == None
        assert coerce("  hello  ") == "hello"
        assert coerce("  42  ") == 42

    def test_settings(self):
        input_str = "--cohen=0.35 --file=data.csv --help"
        result = settings(input_str)
        assert result == {'cohen': 0.35, 'file': 'data.csv', '_help': input_str}

    def test_cells(self):
        input_str = "1, 2, 3.14, true, false, nil, hello"
        result = cells(input_str)
        assert result == [1, 2, 3.14, True, False, None, "hello"]
    """
    def test_csv(self):
        input_str = "1,2,3\n4,5,6\n"
        read_line = csv(input_str)
        assert read_line() == (1, [1, 2, 3])
        assert read_line() == (2, [4, 5, 6])
        assert read_line() == None
    """

    def test_round(self):
        assert round(3.14159, 2) == 3.14
        assert round(42) == 42
        assert round("hello") == "hello"
        assert round(True) == True
        assert round(False) == False

    """
    def test_cli(self):
        sys.argv = ["test.py", "--cohen", "0.35", "--file", "data.csv", "--help"]
        result = cli({})
        assert result == {'cohen': 0.35, 'file': 'data.csv', '_help': '--cohen=0.35 --file=data.csv --help'}
    """

    def _run_test(self, test_func, test_name):
        try:
            test_func()
            print(f"Test {test_name} passed.")
        except AssertionError as e:
            print(f"Test {test_name} failed: {e}")

    def run_tests(self):
        print("Running tests in UtilityTestSuite")
        test_functions = [func for func in dir(self) if func.startswith('test_') and callable(getattr(self, func))]
        for test_func_name in test_functions:
            test_func = getattr(self, test_func_name)
            self._run_test(test_func, test_func_name)

class SymTestSuite:

    def test_add(self):
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

    def test_mid(self):
        sym_obj = SYM()
        sym_obj.add("a")
        sym_obj.add("b")
        assert sym_obj.mid() == "a"

    def test_div(self):
        sym_obj = SYM()
        sym_obj.add("a")
        sym_obj.add("b")
        sym_obj.add("a")
        sym_obj.add("c")
        assert math.isclose(sym_obj.div(), 1.5)

    def test_small(self):
        sym_obj = SYM()
        assert sym_obj.small() == 0

    def _run_test(self, test_func, test_name):
        try:
            test_func()
            print(f"Test {test_name} passed.")
        except AssertionError as e:
            print(f"Test {test_name} failed: {e}")

    def run_tests(self):
        print("Running tests in SymTestSuite")
        test_functions = [func for func in dir(self) if func.startswith('test_') and callable(getattr(self, func))]
        for test_func_name in test_functions:
            test_func = getattr(self, test_func_name)
            self._run_test(test_func, test_func_name)


if __name__ == '__main__':
    util_test_suite = UtilityTestSuite()
    util_test_suite.run_tests()

    sym_test_suite = SymTestSuite()
    sym_test_suite.run_tests()
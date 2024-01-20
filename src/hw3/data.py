import csv
from sym import SYM
from row import ROW
from cols import COLS
from utils import round

class DATA:
    def __init__(self):
        self.rows = []
        self.rows_obj = []
        self.cols = None
        self.rows_actual = []

    def full_data(self, src, fun=None):
        if isinstance(src, str):
            with open(src, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.rows_actual.append(row)
                    self.add(row, fun)
        else:
            for row in src or []:
                self.add(row, fun)

    def add(self, t=None, fun=None):
        row = ROW(t) if type(t)==list else t
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)
        self.rows_obj.append(row)

    def mid(self, cols=None):
        u = [col.mid() for col in (cols or self.cols.all)]
        return ROW(u)

    def div(self, cols=None):
        u = [col.div() for col in (cols or self.cols.all)]
        return ROW(u)
    
    def stats(self, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                u[col.txt] = col.mid()
            else:
                u[col.txt] = round(col.mid())
        return u
import csv
from sym import SYM
from row import ROW
from cols import COLS

class DATA:
    def __init__(self, src="", fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            with open(src, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
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

    def mid(self, cols=None):
        u = [col.mid() for col in (cols or self.cols.all)]
        return ROW(u)

    def div(self, cols=None):
        u = [col.div() for col in (cols or self.cols.all)]
        return ROW(u)
    
    def stats(self, cols=None, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                u[col.txt] = col.mid()
            else:
                u[col.txt] = col.mid()
        return u

    def small(self):
        u = [col.small() for col in self.cols.all]
        return ROW(u)

    def clone(self, rows=None):
        new = DATA()
        for row in rows or []:
            new.add(row)
        return new
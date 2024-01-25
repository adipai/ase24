import csv
from sym import SYM
from row import ROW
from cols import COLS
from utils import round
import random

class DATA:
    def __init__(self, the={}):
        self.rows = []
        self.rows_obj = []
        self.cols = None
        self.rows_actual = []
        self.the = the

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
        row = ROW(t, self.the) if type(t)==list else t
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row, the=self.the)
        self.rows_obj.append(row)

    def mid(self, cols=None):
        u = [col.mid() for col in (cols or self.cols.all)]
        return ROW(u, self.the)

    def div(self, cols=None):
        u = [col.div() for col in (cols or self.cols.all)]
        return ROW(u, self.the)
    
    def stats(self, fun=None, ndivs=None):
        u = {".N": len(self.rows)}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                u[col.txt] = col.mid()
            else:
                u[col.txt] = round(col.mid())
        return u
    
    """ HW 4 addition starts here, needs refining"""
    
    def gate(self, budget0, budget, some):
        rows = random.sample(self.rows, len(self.rows))
        lite = rows[:budget0]
        dark = rows[budget0:]

        stats, bests = [], []

        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            stats.append(selected.mid())
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))

        return stats, bests

    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols.names)
        max_value = 1E30
        out = 1

        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)

            if b > r:
                selected.add(row)

            tmp = abs(b + r) / abs(b - r + 1E-300)

            if tmp > max_value:
                out, max_value = i, tmp

        return out, selected

    def best_rest(self, rows, want):
        rows.sort(key=lambda row: row.d2h(self))
        best, rest = [self.cols.names], [self.cols.names]

        for i, row in enumerate(rows):
            if i < want:
                best.append(row)
            else:
                rest.append(row)

        return DATA(best), DATA(rest)
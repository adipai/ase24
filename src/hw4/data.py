import csv
from sym import SYM
from row import ROW
from cols import COLS
from utils import round
import random


class DATA:
    def __init__(self, src = [], the={}, fun=None):
        self.the = the
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            with open(src, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.add(row, fun)
        else:
            self.add(src, fun)


    def add(self, t=None, fun=None):
        row = t if isinstance(t, ROW) else ROW(t, self.the)
        if self.cols:
            if fun:
                fun(self, row)
            
            self.cols.add(row)
            self.rows.append(row)
        else:
            self.cols = COLS(row, the=self.the)

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
    
    def gate(self, budget0=4, budget=10, some=0.5):
        random.seed(self.the['seed'])
        rows = random.sample(self.rows, len(self.rows))

        print("1. top6: ", [r.cells[-1] for r in rows[:6]])
        print("2. top50: ", [[r.cells[-1] for r in rows[:50]]])

        # sort rows based on d2h
        rows.sort(key=lambda row: row.d2h(self))
        print("3. most: ", rows[0].cells[-1])

        # shuffle again
        rows = random.sample(self.rows, len(self.rows))

        # divide into train and test
        lite = rows[:budget0] #train-data
        dark = rows[budget0:] #test-data

        stats, bests = [], []

        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark)
            print("4: ")
            print("5: ")
            print("6: ")
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
        best_data, rest_data = DATA(best), DATA(rest)
        for i, row in enumerate(rows):
            if i < want:
                best_data.add(row)
            else:
                rest_data.add(row)
        
        return best_data, rest_data
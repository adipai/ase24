import csv
from sym import SYM
from row import ROW
from cols import COLS
from utils import round, coerce
import random
import numpy as np


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
            for row in src:
                self.add(row, fun)


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
    
    def gate(self, random_seed, budget0=4, budget=10, some=0.5):

        random.seed(random_seed)
        list_1,list_2,list_3, list_4, list_5, list_6 =[],[],[],[],[],[]
        rows = random.sample(self.rows, len(self.rows))

        #print("1. top6: ", [r.cells[len(r.cells)-3:] for r in rows[:6]])
        #print("2. top50: ", [[r.cells[len(r.cells)-3:] for r in rows[:50]]])
        list_1.append(f"1. top6: {[r.cells[len(r.cells)-3:] for r in rows[:6]]}")
        list_2.append(f"2. top50:{[[r.cells[len(r.cells)-3:] for r in rows[:50]]]}")

        # sort rows based on d2h
        rows.sort(key=lambda row: row.d2h(self))
        #print("3. most: ", rows[0].cells[len(rows[0].cells)-3:])
        list_3.append(f"3. most: {rows[0].cells[len(rows[0].cells)-3:]}")

        # shuffle again
        rows = random.sample(self.rows, len(self.rows))

        # divide into train and test
        lite = rows[:budget0] #train-data
        dark = rows[budget0:] #test-data
        # print(len(dark))

        stats, bests = [], []

        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite) ** some)
            # print(best.stats(), rest.stats())
            todo, selected, max_value = self.split(best, rest, lite, dark)
            # print("HIIIIIII: ", todo, max_value, len(dark))

            #print("4: rand:", sum(list(map(coerce, random.sample(dark, budget0+i)[0].cells[-3:])))/3)
            #print("5: mid: ", selected.mid().cells[len(selected.mid().cells)-3:])
            #print("6: top: ", best.rows[0].cells[len(best.rows[0].cells)-3:])
            selected_rows_rand = random.sample(dark, budget0+i)
            y_values_rand = []
            for row in selected_rows_rand:
                y_val = list(map(coerce, row.cells[-3:]))
                y_values_rand.append(y_val)
            # y_values = np.array(row[-3:])
            list_4.append(f"4: rand:{np.mean(np.array(y_values_rand), axis=0)}")
            list_5.append(f"5: mid: {selected.mid().cells[len(selected.mid().cells)-3:]}")
            list_6.append(f"6: top: {best.rows[0].cells[len(best.rows[0].cells)-3:]}")
            stats.append(selected.mid())
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))
            # print(len(lite))
        
        print('\n'.join(map(str, list_1)))
        print('\n'.join(map(str, list_2)))
        print('\n'.join(map(str, list_3)))
        print('\n'.join(map(str, list_4)))
        print('\n'.join(map(str, list_5)))
        print('\n'.join(map(str, list_6)))
        # print(bests[-1].cells)
        return stats, bests

    def split(self, best, rest, lite, dark):
        selected = DATA([self.cols.names], the=self.the)
        max_value = -1E30
        out = 0
        # print(dark)
        for i, row in enumerate(dark):
            # print("DARK row: ",row.cells)
            b = row.like(best, len(lite), 2)
            # print("HI")
            r = row.like(rest, len(lite), 2)
            # print(b,r)
            if b > r:
                selected.add(row)

            tmp = abs(b + r) / abs(b - r + 1E-300)
            # print("TEMP: ", tmp)
            if tmp > max_value:
                out, max_value = i, tmp

        return out, selected, max_value

    def best_rest(self, rows, want):
        # print("Starting sorting in best-rest")
        rows.sort(key=lambda row: row.d2h(self))
        # print("In best-rest: ",rows)
        best, rest = [self.cols.names], [self.cols.names]
        for i, row in enumerate(rows):
            if i < want:
                best.append(row)
            else:
                rest.append(row)
        # print("best", best)
        # print("rest ",rest)
        return DATA(best, the=self.the), DATA(rest, the=self.the)
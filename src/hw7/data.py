import csv
from sym import SYM
from row import ROW
from cols import COLS
from utils import round, coerce, any_item, keysort, many
import random
import numpy as np
from node import NODE


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
        u = {}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                if(col.txt == "origin"):
                    u[col.txt] = int(col.mid())
                else:
                    u[col.txt] = col.mid()
            else:
                u[col.txt] = round(col.mid())
        return u

    def stats_div(self, fun=None, ndivs=None):
        u = {}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                if(col.txt == "origin"):
                    u[col.txt] = round(col.div()[0])
                else:
                    u[col.txt] = col.div()
            else:
                u[col.txt] = round(col.div())
                
        return u

    
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

        stats, bests, stats_data = [], [], []

        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite) ** some)
            todo, selected, max_value = self.split(best, rest, lite, dark)
            selected_rows_rand = random.sample(dark, budget0+i)
            y_values_rand = []
            for row in selected_rows_rand:
                y_val = list(map(coerce, row.cells[-3:]))
                y_values_rand.append(y_val)

            list_4.append(f"4: rand:{np.mean(np.array(y_values_rand), axis=0)}")
            list_5.append(f"5: mid: {selected.mid().cells[len(selected.mid().cells)-3:]}")
            list_6.append(f"6: top: {best.rows[0].cells[len(best.rows[0].cells)-3:]}")
            stats.append(selected.mid())
            bests.append(best.rows[0])
            stats_data.append(selected)
            lite.append(dark.pop(todo))

        return stats, bests, [bests[-1].cells, round(bests[-1].d2h(self))]

    def any50(self, random_seed):
        random.seed(random_seed)
        rows = random.sample(self.rows, 50)
        return [rows[0].cells, round(rows[0].d2h(self))]

    def best_whole(self, random_seed):
        random.seed(random_seed)
        rows = random.sample(self.rows, len(self.rows))
        rows.sort(key=lambda row: row.d2h(self))
        return [rows[0].cells, round(rows[0].d2h(self))]
    
    def mid_div(self):
        d2h_vals = [r.d2h(self) for r in self.rows]
        #mid stats and div stats
        return[[self.stats(), round(np.mean(d2h_vals))],[self.stats_div(), round(np.std(d2h_vals))]]

    def split(self, best, rest, lite, dark):
        selected = DATA([self.cols.names], the=self.the)
        max_value = -1E30
        out = 0
        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r:
                selected.add(row)

            tmp = abs(b + r) / abs(b - r + 1E-300)
            if tmp > max_value:
                out, max_value = i, tmp

        return out, selected, max_value

    def best_rest(self, rows, want):
        rows.sort(key=lambda row: row.d2h(self))
        best, rest = [self.cols.names], [self.cols.names]
        for i, row in enumerate(rows):
            if i < want:
                best.append(row)
            else:
                rest.append(row)
        return DATA(best, the=self.the), DATA(rest, the=self.the)

    def clone(self, rows=None):
        new = DATA()
        for row in rows or []:
            new.add(row)
        return new
    
    def farapart(self, rows, sortp=True, a=None, b=None):
        far = int(len(rows) * 0.95)
        evals = 1 if a else 2
        x = any_item(rows).neighbors(self, rows)
        a = a or any_item(rows).neighbors(self, rows)[far]
        b = a.neighbors(self, rows)[far]

        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a

        return a, b, a.dist(b,self), evals

    def half(self, rows, sortp=None, before=None):
        some = many(rows, min(self.the.Half, len(rows)))
        a, b, C, evals = self.farapart(some, sortp, before)

        def d(row1, row2):
            return row1.dist(row2, self)

        def project(r):
            return (d(r, a) ** 2 + C ** 2 - d(r, b) ** 2) / (2 * C)

        as_, bs = [], []
        sorted_rows = keysort(rows, project)

        for n, row in enumerate(sorted_rows, start=1):
            if n <= len(rows) // 2:
                as_.append(row)
            else:
                bs.append(row)

        return as_, bs, a, b, C, d(a, bs[0]), evals

    def tree(self, sortp):
        evals = [0]

        def _tree(data, above = None):
            nonlocal evals
            node = NODE(data)

            if len(data.rows) > 2 * (len(self.rows) ** 0.5):
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
                evals[0] += evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)

            return node

        return _tree(self), evals[0]

    def branch(self, stop=None, rest=None, _branch=None, evals=None):
        evals, rest = 1, []
        stop = stop or (2 * (len(self.rows) ** 0.5))

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals, rest

            if len(data.rows) > stop:
                lefts, rights, left, _, _, _, _  = self.half(data.rows, True, above)
                evals += 1
                for row1 in rights:
                    rest.append(row1)

                return _branch(self.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals

        return _branch(self)
    
    def clone(self, rows=None, newData=None):
        newData = DATA([self.cols.names])
        for row in rows or []:
            newData.add(row)
        return newData
    
    def half(self, rows, sortp, before):
        the_Half = len(rows) // 2
        some = many(rows, min(the_Half, len(rows)))
        a, b, C, evals = self.farapart(some, sortp, before)

        def d(row1, row2):
            return row1.dist(row2, self)

        def project(r):
            return (d(r, a) ** 2 + C ** 2 - d(r, b) ** 2) / (2 * C)

        as_, bs = [], []

        for n, row in enumerate(sorted(rows, key=project)):
            if n <= (len(rows) // 2):
                as_.append(row)
            else:
                bs.append(row)

        return as_, bs, a, b, C, d(a, bs[0]), evals


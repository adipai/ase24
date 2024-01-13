import math
import csv
import random

class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi =  float("-inf") # or  -1E30
        self.lo = float("inf")  # or 1E30
        self.heaven = 0 if s and s.endswith("-") else 1

    def add(self, x):
        if not x == "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.n < 2 else (self.m2 / (self.n - 1))**0.5

"""
    def small(self):
        return the.cohen * self.div()
    
    
    def same(self, other, pooledSd, n12, correction):
        n12 = self.n + other.n
        pooledSd = ((self.n - 1) * self.div()**2 + (other.n - 1) * other.div()**2) / (n12 - 2)**0.5
        correction = 1 if n12 >= 50 else (n12 - 3) / (n12 - 2.25)
        return abs(self.mu - other.mu) / pooledSd * correction <= the.cohen

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)

    def like(self, x):
        mu, sd = self.mid(), self.div() + 1E-30
        nom = 2.718**(-0.5 * (x - mu)**2 / (sd**2))
        denom = (sd * 2.5 + 1E-30)
        return nom / denom
"""


class SYM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if not x == "?":
            self.n += 1
            self.has[x] = self.has.get(x, 0) + 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for v in self.has.values():
            e -= (v / self.n) * math.log(v / self.n, 2)
        return e

    def small(self):
        return 0
    
class COLS:
    def __init__(self, row):
        self.x, self.y, self.all = {}, {}, []
        self.klass = None
        self.names = row.cells
        for at, txt in enumerate(row.cells, 1):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = col
                (self.y if txt[-1] in "!+-" else self.x)[at] = col

    def add(self, row):

        for cols in [self.x, self.y]:
            for col in cols:
                col.add(row.cells[col.at])


class ROW:
    def __init__(self, t):
        self.cells = t
   

class DATA:
    def __init__(self):
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

    def add(self, t, fun=None, row=None):
        row = t.cells if t.cells else ROW(t)
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
        for col in (self.cols[cols or "y"]):
            u[col.txt] = round(getattr(col, fun or "mid")(), ndivs)
        return u

    def small(self):
        u = [col.small() for col in self.cols.all]
        return ROW(u)

    def clone(self, rows=None):
        new = DATA()
        for row in rows or []:
            new.add(row)
        return new

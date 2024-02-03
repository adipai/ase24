import sys
import math
from utils import coerce, keysort

class ROW:

    def __init__(self, t, the):
        self.cells = t
        self.the = the

    def likes(self, datas):
        n, nHypotheses = 0,0
        # print(datas.items())
        for k, data in datas.items(): #(pairs(datas))
            n += len(data.rows)
            nHypotheses += 1
        
        most, out = None, None

        for k, data in datas.items(): #(pairs(datas))
            tmp = self.like(data, n, nHypotheses)
            # print("MAP: ", tmp)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most

    def like(self, data, n, nHypotheses):
        # print(self.the)
        prior = (len(data.rows) + self.the['k']) / (n + self.the['k'] * nHypotheses)
        # print(data.cols.x.items())
        # print("Prior prob: ", prior)
        out = math.log(prior)
        for _, col in data.cols.x.items(): #(pairs(data.cols.x))
            # print(self.cells)
            # print("HOLA")
            # print(col.at)
            v = self.cells[col.at-1]
            # print(v, col.mid(), col.div())
            v = coerce(v)
            # print(v)
            if v != "?":
                # v = coerce(v)
                inc = col.like(v, prior)
                if(inc>0):
                    out += math.log2(inc) 
                else:
                    out += float('-inf')

        return math.exp(1)**out
    
    """
    def d2h(self, data):
        d, n = 0, 0
        # print(data.cols.y.values())
        for col in data.cols.y.values():
            n += 1
            # print((self.cells[col.at]))
            x = col.norm(coerce(self.cells[col.at - 1]))
            d += abs(col.heaven - x) ** 2
        
        # print((d ** 0.5) / (n ** 0.5))
        return (d ** 0.5) / (n ** 0.5)
    """
    
    def d2h(self, data):
        d, n, p = 0, 0, 2
        for col in data.cols.y.values():
            x = coerce(self.cells[col.at-1])
            if x is None:
                print("?", end="", file=sys.stderr)
            else:
                n += 1
                d += abs(col.heaven - col.norm(self.cells[col.at-1])) ** p
        return (d / n) ** (1 / p)

    def dist(self, other, data):
        d, n, p = 0, 0, 2
        for col in data.cols.x.values():
            n += 1
            d += col.dist(coerce(self.cells[col.at-1]), coerce(other.cells[col.at-1])) ** p
            # print(d)
        
        # print((d / n) ** (1 / p), self.cells, other.cells)
        return (d / n) ** (1 / p)

    def neighbors(self, data, rows=None):
        return keysort(rows or data.rows,
                          fun=lambda row: self.dist(row, data))

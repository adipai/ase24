import math
from config import *

class ROW:

    def __init__(self, t):
        self.cells = t

    def likes(self, datas):
        n, nHypotheses = 0, 0

        for k, data in datas.items(): #(pairs(datas))
            n += len(data.rows)
            nHypotheses += 1

        most, out = None, None

        for k, data in datas.items(): #(pairs(datas))
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most

    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + the.k) / (n + the.k * nHypotheses)
        out = math.log(prior)
        
        for _, col in data.cols.x.items(): #(pairs(data.cols.x))
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)

        return math.exp(1)**out
    
    
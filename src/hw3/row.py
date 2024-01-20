import math
from utils import coerce
from globals import the

class ROW:

    def __init__(self, t):
        self.cells = t

    def likes(self, datas):
        n, nHypotheses = 0, 0

        for k, data in datas.items(): #(pairs(datas))
            # print(data)
            n += len(data.rows)
            nHypotheses += 1

        most, out = None, None

        for k, data in datas.items(): #(pairs(datas))
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most

    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)
        print(data.cols.x.keys())
        for _, col in data.cols.x.items(): #(pairs(data.cols.x))
            # print(col.at)
            v = self.cells[col.at-1]
            if v != "?":
                v = coerce(v)
                inc = col.like(v, prior)
                print(inc)
                out += math.log2(inc) #add a small term to avoid error 

        return math.exp(1)**out
    
    
import math
from utils import coerce

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
        # print("Prior prob: ", prior)
        out = math.log(prior)
        for _, col in data.cols.x.items(): #(pairs(data.cols.x))
            # print(col.at)
            v = self.cells[col.at-1]
            # print(v)
            v = coerce(v)
            # print(v)
            if v != "?":
                # v = coerce(v)
                inc = col.like(v, prior)

                out += math.log2(inc) 

        return math.exp(1)**out
    
    """Addition for HW4"""
    
    def d2h(self, data):
        d, n = 0, 0
        for col in data.cols.y.values():
            n += 1
            # print((self.cells[col.at]))
            x = col.norm(coerce(self.cells[col.at - 1]))
            d += abs(col.heaven - x) ** 2

        return (d ** 0.5) / (n ** 0.5)

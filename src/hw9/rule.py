
from utils import coerce, copy
class RULE:
    def __init__(self, ranges):
        self.parts = {}
        self.scored = 0
        for range in ranges:
            if range.txt not in self.parts:
                self.parts[range.txt] = []
            self.parts[range.txt].append(range)

    def _or(self, ranges, row):
        # print(ranges[0].at)
        x = row.cells[ranges[0].at-1]
        if x == "?":
            return True
        for range in ranges:
            # print(range.x, range.txt, x)
            lo, hi = range.x['lo'], range.x['hi']
            x, lo, hi = coerce(x), coerce(lo), coerce(hi)
            if (lo == hi and lo == x) or (lo <= x < hi):
                return True
        return False

    def _and(self, row):
        for ranges in self.parts.values():
            if not self._or(ranges, row):
                return False
        return True

    def selects(self, rows):
        selected = []
        for r in rows:
            if self._and(r):
                # print("Hi")
                selected.append(r)
        return selected

    def selectss(self, rowss):
        result = {}
        for y, rows in rowss.items():
            result[y] = len(self.selects(rows))
        return result

    def show(self):
        ands = []
        # print(self.parts)
        # print(list(self.parts.values()))
        for ranges in self.parts.values():
            # print(ranges)
            ors = _showLess(ranges)
            at = None
            # print("ors: ", ors)
            for i, range in enumerate(ors):
                # print(type(range))
                at = range.at
                ors[i] = range.show()
                # print(ors)
            ands.append(" or ".join(ors))
        return " and ".join(ands)
      
"""
Note : this function is not a part of the class, it is called in show()
"""

def _showLess(t, ready=False):
    if not ready:
        t = t[:]
        # print(t)
        t = sorted(t, key=lambda x: x.x['lo'])
    u = []
    i = 0
    # print(len(t))
    while i < len(t):
        a = t[i]
        if i < len(t) - 1:
            if a.x['hi'] == t[i + 1].x['lo']:
                a = a.merge(t[i + 1])
                i += 1
        u.append(a)
        i += 1
    
    if(len(u)==len(t)):
        # print("Showless:", t)
        return t
    else:
        return _showLess(u, ready=True)

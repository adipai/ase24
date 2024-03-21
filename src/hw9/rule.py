

class RULE:
    def __init__(self, ranges):
        self.parts = {}
        self.scored = 0
        for range in ranges:
            if range.txt not in self.parts:
                self.parts[range.txt] = []
            self.parts[range.txt].append(range)

    def _or(self, ranges, row):
        x = row.cells[ranges[0].at]
        if x == "?":
            return True
        for range in ranges:
            lo, hi = range.x.lo, range.x.hi
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
                selected.append(r)
        return selected

    def selectss(self, rowss):
        result = {}
        for y, rows in rowss.items():
            result[y] = len(self.selects(rows))
        return result

    def show(self):
        ands = []
        for ranges in self.parts.values():
            ors = _showLess(ranges)
            at = None
            for range in ors:
                at = range.at
                ors.append(range.show())
            ands.append(" or ".join(ors))
        return " and ".join(ands)
      
"""
Note : this function is not a part of the class, it is called in show()
"""

def _showLess(t, ready=False):
    if not ready:
        t = sorted(t, key=lambda x: x.x.lo)
    u = []
    i = 0
    while i < len(t):
        a = t[i]
        if i < len(t) - 1:
            if a.x.hi == t[i + 1].x.lo:
                a = a.merge(t[i + 1])
                i += 1
        u.append(a)
        i += 1
    return t if len(u) == len(t) else _showLess(u, ready=True)

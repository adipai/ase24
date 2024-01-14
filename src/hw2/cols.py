from num import NUM
from sym import SYM


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
            for col in list(cols.values()):
                col.add(row.cells[col.at-1])


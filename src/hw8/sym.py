from utils import entropy

class SYM:
    def __init__(self, s=None, n=None, the = {}):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0
        self.the = the

    def add(self, x):
        if not x == "?":
            self.n += 1
            self.has[x] = self.has.get(x, 0) + 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        """
            e = 0
            for v in self.has.values():
                e -= (v / self.n) * math.log(v / self.n, 2)
            return e
        """
        return entropy(self.has)

    def small(self):
        return 0
    
    def like(self, x, prior):
        # print("Likelihood stuff: ",(x, self.has.get(x,0),self.n))
        return ((self.has.get(x, 0) or 0) + self.the['m'] * prior) / (self.n + self.the['m'])
    
    def norm(self, x):
        return x

    def dist(self, x, y):
        if(x==y):
            return 0
    
        return 1

    def bin(self, x, the):
        return x

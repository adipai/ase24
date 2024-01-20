import math
from utils import coerce

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
            x = coerce(x)
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
    
    def like(self, x, prior=None):
        mu, sd = self.mid(), (self.div() + 1E-30)
        print(x, mu)
        nom = math.exp(-0.5 * (x - mu) ** 2 / (sd ** 2))
        denom = (sd * 2.5 + 1E-30)
        print(nom, denom, nom/denom)
        return nom / denom
from utils import powerset
from utils import score as utils_score
from rule import RULE

class RULES:
    def __init__(self, ranges, goal, rowss, the):
        self.sorted = []
        self.goal = goal
        self.rowss = rowss
        self.LIKE = 0
        self.HATE = 0
        self.likeHate()
        self.the = the

        for range in ranges:
            range.scored = self.score(range.y)
        self.sorted = self.top(self._try(self.top(ranges, self.the)), self.the)

    def likeHate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE += len(rows)

    def score(self, t):
        return utils_score(t, self.goal, self.LIKE, self.HATE, self.the)

    def _try(self, ranges):
        u = []
        for subset in powerset(ranges):
            if len(subset) > 0:
                rule = RULE(subset)
                # print(rule.items())
                # print(rule.parts)
                y_preds = rule.selectss(self.rowss)
                if(y_preds["LIKE"]==0 and y_preds["HATE"]==0):
                    rule.scored = 0
                else:
                    rule.scored = self.score(y_preds)
                if rule.scored > 0.01:
                    u.append(rule)
        return u

    def top(self, t, the):
        t.sort(key=lambda x: x.scored, reverse=True)
        u = []
        for x in t:
            if x.scored >= t[0].scored * the['Cut']:
                u.append(x)
        return u[:int(the['Beam'])]

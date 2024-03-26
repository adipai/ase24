from utils import round, coerce
from ranges import Range
from data import DATA
import math 
import random 

def ranges(cols, rowss, the):
    # print(cols)
    t = []
    for col in cols:
        if(col==3):
            continue
        for range in _ranges1(cols[col], rowss, the):
            t.append(range)
    return t

def _ranges1(col, rowss, the):
    # print(col.at)
    out, nrows = {}, 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in list(rows):
            x = row.cells[col.at-1]
            if x != "?":
                bin = col.bin(coerce(x), the=the)
                if bin not in out:
                    out[bin] = Range(col.at, col.txt, coerce(x))
                out[bin].add(coerce(x), y)
    out = list(out.values())
    # print(out)
    out.sort(key=lambda r: r.x['lo'])
    return out if hasattr(col, 'has') else mergeds(out, nrows / the['bins'])

def mergeds(ranges, tooFew):
    t = []
    i = 1
    while i <= len(ranges):
        a = ranges[i-1]
        if i < len(ranges):
            both = a.merged(ranges[i], tooFew)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1
    if len(t) < len(ranges):
        return mergeds(t, tooFew)
    for i in range(1, len(t)):
        t[i].x['lo'] = t[i - 1].x['hi']
    t[0].x['lo'] = -math.inf
    t[-1].x['hi'] = math.inf
    return t

def bins(the):
    d = DATA(the['file'], the=the)
    best, rest, _ = d.branch()
    LIKE = best.rows
    HATE = random.sample(rest.rows, min(3 * len(LIKE), len(rest.rows)))

    def score(range_, the):
        return range_.score("LIKE", len(LIKE), len(HATE), the=the)
    print()
    print("PART - 1")
    t = []
    # print(d.cols.x.values())
    for col in list(d.cols.x.values()):
        if(col.at==3):
            continue
        print("")
        for range_ in _ranges1(col, {"LIKE": LIKE, "HATE": HATE}, the=the):
            temp_x = {'hi':range_.x['hi'], 'lo':range_.x['lo']}
            temp_y = {}
            if 'HATE' in range_.y:
                temp_y['HATE'] = range_.y['HATE']
            if 'LIKE' in range_.y:
                temp_y['LIKE'] = range_.y['LIKE']
            d = {'at':range_.at, 'scored':range_.scored, 'txt':range_.txt, 'x':temp_x, 'y':temp_y}
            print(d)
            t.append(range_)
    t.sort(key=lambda a: score(a, the), reverse=True)
    max_score = score(t[0], the=the)
    print("\n\nPART - 2")
    print("\n#scores:\n")
    # print(t, the['Beam'])
    for v in t[:int(the['Beam'])]:
        if score(v, the) > max_score * 0.1:
            temp_x = {'hi':v.x['hi'], 'lo':v.x['lo']}
            temp_y = {}
            if 'HATE' in v.y:
                temp_y['HATE'] = v.y['HATE']
            if 'LIKE' in v.y:
                temp_y['LIKE'] = v.y['LIKE']
            d_v = {'at':v.at, 'scored':v.scored, 'txt':v.txt, 'x':temp_x, 'y':temp_y}
            print("{:.2f}".format(round(score(v,the), 2)), d_v)
    print({"HATE": len(HATE),"LIKE": len(LIKE),})
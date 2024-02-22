# constructor
# walk
# show
from utils import round, o

class NODE:
    def __init__(self, data):
        self.here = data
        self.lefts = None
        self.left = None
        self.rights = None
        self.right = None
        self.C = None
        self.cut = None

        

    def walk(self, fun, depth=0):
        fun(self, depth, not (self.lefts or self.rights))
        if self.lefts:
            self.lefts.walk(fun, depth + 1)
        if self.rights:
            self.rights.walk(fun, depth + 1)

    def show(self, maxDepth=0):
        def d2h(data):
            return round(data.mid().d2h(self.here))

        maxDepth = 0

        def _show(node, depth, leafp):
            nonlocal maxDepth
            # print('-->')
            # print(d2h(node.here), type(d2h(node.here)))
            # print('---->')
            # print(o(node.here.mid().cells), type(o(node.here.mid().cells)))
            # print('------>')
            # print(leafp)
            post =  "\t\t" + o(node.here.mid().cells) if leafp else ""
            maxDepth = max(maxDepth, depth)
            print(('|.. ' * depth) + post)

        self.walk(_show)
        print("")
        print(("    " * maxDepth) + "\t\t" + o(self.here.mid().cells))
        print(("    " * maxDepth) + "\t" + o(self.here.cols.names))
        # print("evals")


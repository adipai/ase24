from data import DATA

def print_stats(the={}):
    """
    Function to print data stats
    """
    data_new = DATA(src=the['file'], the=the)
    # print(data_new.stats())
    return data_new

def learn(data, row, my, the):
    my['n'] += 1
    kl = row.cells[data.cols.klass.at-1]
    if my['n'] > 10:
        my['tries'] += 1
        my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0
    
    if kl not in my['datas']:
        my['datas'][kl] =  DATA(src = [data.cols.names], the = the)
    my['datas'][kl].add(row)
    
def bayes(the={}):
    my = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
    DATA(src = the['file'], fun=lambda data, t: learn(data, t, my, the), the=the)
    return round((my['acc']/my['tries'])*100, 2)

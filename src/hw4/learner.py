from data import DATA

def print_stats(file_name, the= {}):
    """
    Function to print data stats
    """
    data_new = DATA(the=the)
    data_new.full_data(file_name)
    # print(data_new.stats())
    return data_new

def learn(data_new, the = {}):
    rows_obj = data_new.rows_obj
    rows_actual = data_new.rows_actual
    my = {"n":0, "tries":0, "acc":0, "datas":{}}
    for i in range(len(rows_obj)):
        row_obj = rows_obj[i]
        row_actual = rows_actual[i]
        my['n'] += 1
        kl = row_obj.cells[data_new.cols.klass.at-1]
        if(my['n']>10):
            my['tries'] += 1
            predict_class, _ = row_obj.likes(my['datas'])
            if(predict_class == kl):
                my['acc'] += 1  
        if(i > 0 and kl not in my['datas']):
            my['datas'][kl] = DATA(the=the)
            my['datas'][kl].add(rows_actual[0])
            my['datas'][kl].add(row_actual)
        
        elif(i > 0 and kl in my['datas']):
            my['datas'][kl].add(row_actual)
    return my

def bayes(data_new, the={}):
    my = learn(data_new, the)
    return round((my['acc']/my['tries'])*100, 2)


from data import DATA
from globals import the, my

def print_stats():
    """
    Function to print data stats
    """
    data_new = DATA()
    data_new.full_data(the['file'])
    # print(data_new.stats())
    return data_new

def learn(data_new):
    rows_obj = data_new.rows_obj
    rows_actual = data_new.rows_actual
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
            my['datas'][kl] = DATA()
            my['datas'][kl].add(rows_actual[0])
            my['datas'][kl].add(row_actual)
        
        elif(i > 0 and kl in my['datas']):
            my['datas'][kl].add(row_actual)

def bayes(data_new):
    learn(data_new)
    print("Accuracy for "+the['file'].split("/")[3] + ": ", (my['acc']/my['tries'])*100)

import random
import pandas as pd

def MyGetDummies(data):
    names = AllNames(data)
    head = ''
    for i in range(0, len(names)):
        head += '\t' + names[i]
    print(head)

    for i in range(0, len(data)):
        row = str(i)
        for j in range(0, len(names)):
            x = '\t' + str(data[i] == names[j])
            row += x
        print(row)

def AllNames(data):
    res = [data[0]]
    for i in range(1, len(data)):
        if data[i] not in res:
            res += [data[i]]
    return res

lst = ['robot'] * 10
lst += ['human'] * 10
#lst += ['triss'] * 5
#lst += ['neo'] * 5

random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

#print(pd.get_dummies(data['whoAmI']))
MyGetDummies(data['whoAmI'])
#MyGetDummies(lst)
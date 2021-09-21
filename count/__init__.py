import pandas as pd
import matplotlib.pyplot as plt
import collections
import re

#字母统计
def count_letters(path):
    with open(path, "r") as f:
        data = f.read()
        dic = collections.Counter(data)#使用Counter进行计数
        del dic[' ']
        del dic['\n']
        dic = dic.items()
        pds = pd.DataFrame(dic, columns=['letter', 'counts'])
        pds.sort_values(by='counts', inplace=True, ascending=False)
        pds.reset_index(drop=True, inplace=True)
        pds.plot.bar(x='letter', y='counts')
        plt.xticks(rotation=360)
        plt.show()
        pds.value_counts(normalize = True )
        f.close()
    return dic

#统计词频
def count_words(path):
    with open(path, "r") as f:
        data = f.read()
        dic = collections.Counter(re.split(r"\W+", data))
        dic = dic.items()
        pds = pd.DataFrame(dic, columns=['word', 'counts'])
        pds.sort_values(by='counts', inplace=True, ascending=False)
        pds.reset_index(drop=True, inplace=True)
        pds=pds.head(20)
        IC(pds)
        pds.plot.bar(x='word', y='counts')
        plt.xticks(rotation=360)
        plt.show()
        f.close()

#计算IC值
def IC(pds):
    total = pds['counts'].sum()
    pds['pinlv'] = pds.apply(lambda x: function(total, x["counts"]), axis=1)
    pds['result'] = pds['pinlv'].pow(2)
    IC_R = pds['result'].sum() - 0.0385
    print(IC_R)

# 计算频率
def function(total, x):
    x=x/total
    return x
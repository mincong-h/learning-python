# -*- coding: utf-8 -*-
"""
来个小小的小实践项目吧（此处不计分，但是其实在其他地方有计分哟）。
计算MovieLens 100k数据集中男性女性用户评分的标准差并输出。

数据集下载http://files.grouplens.org/datasets/movielens/ml-100k.zip

其中u.data 表示100k条评分记录，每一列的数值含义是：
user id | item id | rating | timestamp

u.user表示用户的信息，每一列的数值含义是：
user id | age | gender | occupation | zip code

u.item文件表示电影的相关信息，每一列的数值含义是：
movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation | Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |

可能会用到的相关函数：
pandas.read_table(filepath_or_buffer, sep='\t', names=None)
pandas.pivot_table(data, values=None, columns=None, aggfunc='mean')
pandas.merge(left, right, how='inner')

更详尽的API文档请参考http://pandas.pydata.org/pandas-docs/stable/ 。
"""
import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
# ratings
r_names = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_table('ml-100k/u.data', sep='\t', names=r_names)
# users
u_names = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_table('ml-100k/u.user', sep='|', names=u_names)
df = pd.merge(ratings, users, how='inner', on='user id')
print df['rating'].sum() / df['rating'].count()

from math import *
from jieba import *
from time import *

txt=open("红楼梦.txt","r",encoding='utf-8').read()
words=lcut(txt)
counts={}
excludes={"什么","一个","我们","那里","你们","如今","知道","姑娘","这里","说道","起来","出来","他们","太太","众人","自己","一面","奶奶","只见","怎么","没有","两个","不是","这个","听见","不知","这样","近来","告诉","进来","东西","就是","咱们","回来","老爷","大家","只是","只得","不敢","这些","丫头","出去","所以","的话","姐姐","不过"}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del(counts[word])

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print ("{:<10}{:>5}".format(word,count))
   
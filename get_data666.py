from random import randint
      #筛选：在列表、字典、集合中根据条件筛选数据
# data=[randint(-10,10) for _ in  range(10)]
# print(data)
#法一：使用filter函数
# filter = filter(lambda x: x >= 0, data)
# print(list(filter))
#法二：使用列表解析,速度较快
# print([x for x in data if x >= 0] )


#在字典中根据条件筛选数据
# data = {x: randint(60,100) for x in range(1,21)}
# print(data)
# item = {k:v for k,v in x.iteritems()if v>90}
# print(item)

#在集合中根据条件筛选数据
# data=[randint(-10,10) for _ in  range(10)]
# s=set(data)
# set = {x for x in s if x%3==0}
# print(set)

    #如何为元组中的每个元素命名，提高程序可读性，定义一些数值常量
# NAME=0
# AGE=1
# NAME,AGE = range(2)
# student = ('jim',19)
# print(student[NAME])
#法二:使用 namedtuple函数
# from collections import namedtuple
# student=namedtuple('student', ['name', 'age'])
# s1=student('jim',19)
# s2=student('shilry',19)
# print(s1.name)


    #如何统计序列中元素的出现频率
#法一：根据字典查找键
# from random import randint
# data = [randint(0,20) for _ in range(30)]
# print(data)
# c = dict.fromkeys(data, 0)
# print(c)
# for x in data:
#     c[x]+=1
# print(c)

#法二：使用collection下的counter对象
# from collections import Counter
# data = [randint(0,20) for _ in range(30)]
# c2 = Counter(data)
# print(c2[14])

    #根据字典中值的大小，对字典中的项排序
#使用zip函数将字典数据转化为元组
# from random import randint
# data={x:randint(60,100) for x in 'abcdefg'}
# sorted(data)
# print(data.keys())
# print(data.values())
# zip = zip(data.values(),data.keys())
# zipsorted = sorted(zip)
# print(list(zipsorted))


# #如何快速找到多个字典中的公共键
# from random import randint,sample
# sample = sample('abcdefg',randint(3,6))
# print(sample)


#如何让字典保持有序
# d={}
# d['jim']=(1,35)
# d['shirley']=(2,38)
# d['query']=(3,45)
# for k in d :
#     print(k)

l= [1,34,56,2]
for x in l:
    print(x)

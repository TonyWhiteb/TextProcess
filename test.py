import os 
from itertools import chain, islice
import itertools
# def chunks(iterable, n):

#     iterable = iter(iterable)
    
#     while True:
#         yield chain([next(iterable)],islice(iterable, ))

# def chunks(iterable, n):
#     iterable = iter(iterable)
#     while True:
#         delimiter = iter(n)
#         for i in delimiter:
#             print (i, next(delimiter))
#             yield  chain([next(iterable)],islice(iterable,i,next(delimiter)))
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
def chunks(iterable, n):
    iterable = iter(iterable)
    while True:
        for it_start, it_end in pairwise(n):
            print(it_start,it_end)
            return  islice(iterable,it_start-1,it_end-1)
delimiter = [4, 60, 116, 177,229]
a = [4,60]
with open('XSS1-EOS-2018FA.TXT') as f:
    # for line in itertools.islice(f, 4, 60):
    #     print(line)
    # print(itertools.islice(f, 4, 60))
    # for i,lines in enumerate(islice(f, 60, 116)):
    #     print(i,lines)
    # item = iter(delimiter)
    # for x in item:
    #     n = x
    #     m = next(item)
    #     for a in islice(f,n,m):
    #         print(a)
    # for a in islice(f,item,next(item)):
    #     print(a)
    # for i, lines in enumerate(chunks(f,delimiter)):
    #     file_split = '{}.{}'.format(f,i)
    #     with open(file_split,'w') as fi:
    #         fi.writelines(lines)
    # for i in enumerate(chunks(f,delimiter)):
    #     print(i)
    for i, lines in enumerate(chunks(f,a)):
        print(i,lines)





import os 
from itertools import chain, islice
# def chunks(iterable, n):

#     iterable = iter(iterable)
    
#     while True:
#         yield chain([next(iterable)],islice(iterable, ))

def chunks(iterable, n):
    iterable = iter(iterable)
    while True:
        delimiter = iter(n)
        for i in delimiter:
            yield  chain([next(iterable)],islice(iterable,i,next(delimiter)))

delimiter = [4, 60, 116, 177]
with open('XSS1-EOS-2018FA.TXT') as f:
    # for line in itertools.islice(f, 4, 60):
    #     print(line)
    # print(type(itertools.islice(f, 4, 60)))
    # item = iter(delimiter)
    # for x in item:
    #     n = x
    #     m = next(item)
    #     for a in islice(f,n,m):
    #         print(a)
    # for a in islice(f,item,next(item)):
    #     print(a)
    for i, lines in enumerate(chunks(f,delimiter)):
        file_split = '{}.{}'.format(f,i)
        with open(file_split,'w') as fi:
            fi.writelines(lines)
    # for i in enumerate(chunks(f,delimiter)):
    #     print(i)





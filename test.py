import os 
import itertools
def chunks(iterable, n):
    iterable = iter(iterable)
    num = len(n)
    
    while True:
        yield chain([next(iterable)],islice(iterable, ))
with open('XSS1-EOS-2018FA.TXT') as f:
    # for line in itertools.islice(f, 4, 60):
    #     print(line)
    # print(type(itertools.islice(f, 4, 60)))
    for i, lines in enumerate(chunks(f,4,60))
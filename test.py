import os 
import itertools

with open('XSS1-EOS-2018FA.TXT') as f:
    # for line in itertools.islice(f, 4, 60):
    #     print(line)
    print(type(itertools.islice(f, 4, 60)))
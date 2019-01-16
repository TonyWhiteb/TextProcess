import os 

with open('XSS1-EOS-2018FA.TXT') as f:
    i = 0
    delimiter = []
    num_lines = sum(1 for line in open('XSS1-EOS-2018FA.TXT'))
    for line in f:
        rm_space = " ".join(line.split())
        line_list = rm_space.split()
        if 'Page' in line_list:
            delimiter.append(i)
        i = i + 1
    delimiter.append(num_lines)
print(delimiter)

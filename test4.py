delimiter = [4, 60, 116, 177]
import itertools
# def pairwise(iterable):
#     it = iter(iterable)
#     a = next(it, None)

#     for b in it:
#         yield (a, b)
#         a = b 
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    yield zip(a, b)
print(pairwise(delimiter))
for  m, n in pairwise(delimiter):
    print(m+n)
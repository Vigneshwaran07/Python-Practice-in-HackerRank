n = int(input())
s = input().split()
c = int(input())
import itertools as it
com = list(it.combinations(s,c))
alist = [i for i in com if 'a' in i]
print("{0:.3}".format(len(alist)/len(com)))

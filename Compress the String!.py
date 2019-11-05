from itertools import groupby
inp = input()
print(*[(len(list(c)), int(k))for k,c in groupby(inp)])

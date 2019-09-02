n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    list_one = input().split()
    if(len(list_one)==2):
        key, ele = str(list_one[0]), int(list_one[1])
        eval("s.{}({})".format(key,ele))
    else:
        eval("s.{}()".format(list_one[0]))
print(sum(s))


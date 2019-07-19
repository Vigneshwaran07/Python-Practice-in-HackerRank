a = list(map(int, raw_input().split()))
m = min([a[i+1]-a[i] for i in xrange(len(a)-1)])
t = a[0]
i = 0
while(True):
    if(a[i]!=t):
        print(t)
        break
    t += m
    i += 1

n = int(input())
a = list(map(int, input().split()))
s = 0
c = 0
for i in a:
    s += i
    if(s%2==1):
        c+= 2
print(c if s%2==0 else "NO")

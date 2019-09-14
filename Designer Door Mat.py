# Enter your code here. Read input from STDIN. Print output to STDOUT
n, ch = map(int, input().split())
for i in range(1, (n//2)+1):
    t = (2*i)-1
    print((".|."*t).center(ch, '-'))
print("WELCOME".center(ch, '-'))
for i in range((n//2),0,-1):
    t = (2*i)-1
    print((".|."*t).center(ch, '-'))

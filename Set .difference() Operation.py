# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_one = set(list(map(int, input().split())))
n = int(input())
set_two = set(list(map(int, input().split())))
print(len(set_one-(set_two)))

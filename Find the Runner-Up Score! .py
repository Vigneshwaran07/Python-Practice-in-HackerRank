_ = int(input())
a = list(map(int, input().split()))
a = list(filter(lambda x: x!=max(a), a))
print(max(a))


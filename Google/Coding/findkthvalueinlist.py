l = list(map(int,input().split(' ')))
k = int(input())
counter = 0
for i in l:
    if k - i in l:
        counter += 1
print(True if counter // 2 == 1 else 'false')
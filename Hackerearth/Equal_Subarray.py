for _ in range(int(input())):
    n , k = input().split(' ')
    c = int(n) // int(k) - 1
    count = 0
    for i in range(0, int(k)):
        m = c + i
        count += m
    if count < int(n):
        print(int(n)-count)
    else:
        print(int(n))
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split(' ')))
    B = list(map(int,input().split(' ')))
    m1 = max(A)
    mi = min(A)
    m2 = max(B)
    print((m1+mi)//2+m2)
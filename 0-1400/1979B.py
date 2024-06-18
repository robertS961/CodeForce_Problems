

for _ in range(int(input())):
    x,y = map(int, input().split())

    ans = 0
    for i in range(32):
        if (x>>i & 1) == (y>>i & 1):
            ans += 1
        else: break
    print(pow(2, ans))

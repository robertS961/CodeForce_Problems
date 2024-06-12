from math import lcm
for i in range(int(input())):
    n = int(input())
    mult = list(map(int, input().split()))
    tot = 0
    l = lcm(*mult)
    for num in mult:
        tot += l // num
    if tot >= l or l > 10**9:
        print(-1)
    else:
        print(*[l // num for num in mult])

#Think with math on each problem and maybe greedy
# Use built in libraries for lcm, gcd, gcf
# Think to use lcm, gcf, gcd
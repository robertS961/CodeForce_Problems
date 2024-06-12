for _ in range(int(input())):
    arr = list(map(int, input().split()))
    n, m = arr[0], arr[1]
    p, t = n, m
    prog = list(map(int, input().split()))
    test = list(map(int, input().split()))

    choice, res, tot = [], [], 0
    for i in range(1, len(prog)):
        if (prog[i] > test[i] and n > 0) or (m == 0):
            choice.append('p')
            n-= 1
            tot += prog[i]
        else:
            choice.append('t')
            m -= 1
            tot+= test[i]
    res.append(tot)
    for i in range(len(prog) - 1):
        if (prog[i] > test[i] and p >0) or (t == 0):
            p -= 1
            if choice[i] == 'p':
                tot += (prog[i] - prog[i+1])
            else:
                idx = ''.join(choice).rfind('p')
                choice[idx] = 't'
                tot += (prog[i] - test[i+1] + test[idx + 1] - prog[idx + 1])
        else:
            t-= 1
            if choice[i] == 't':
                tot += (test[i] - test[i+1])
            else:
                idx = ''.join(choice).rfind('t')
                choice[idx] = 'p'
                tot += (test[i] - prog[i+1] + prog[idx + 1] - test[idx + 1])
        res.append(tot)
    print(*res)
#Incorrectly prepared an alysis for the problem.
#I need to spend more time with pen and paper to make sure i understand it full

for _ in range(int(input())):
    n, m = map(int, input().split())
    bounds = [n, m]
    a = []
    a.append(list(map(int, input().split())))
    a.append(list(map(int, input().split())))

    bad = -1
    badType = -1
    cur = [0, 0]
    ans = 0
    types = [0 for i in range(n + m + 1)]
    for i in range(n + m):
        curType = 0
        if a[0][i] < a[1][i]:
            curType = 1
        if cur[curType] == bounds[curType]:
            curType = 1 - curType
            if bad == -1:
                bad = i
                badType = 1 - curType
        types[i] = curType
        ans += a[types[i]][i]
        cur[types[i]] += 1

    res = []
    for i in range(n + m):
        val = ans - a[types[i]][i]
        if bad != -1 and i < bad and types[i] == badType:
            val = val + a[badType][bad] - a[1 - badType][bad] + a[1 - badType][n + m]
        else:
            val = val + a[types[i]][n + m]
        res.append(val)
    res.append(ans)
    print(*res)

    #Actual solution










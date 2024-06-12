
from math import gcd

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    gcd_a = []
    if n == 2: print('Yes')

    def checkArray(idx):
        n1 = nums[:idx] + nums[idx +1:]
        tmp = [gcd(n1[i], n1[i+1]) for i in range(len(n1) - 1)]
        return tmp == sorted(tmp)

    g = [gcd(nums[i],nums[i+1]) for i in range(n -1)]
    op1 = op2 = op3 = 0
    for i in range(n -2):
        if g[i +1] < g[i]:
            op1 = i
            op2 = i + 1
            op3 = min(n - 1, i + 2)
            break
    print('Yes') if any([checkArray(op1), checkArray(op2), checkArray(op3)]) else print('No')

# I learned that our edge cases bonned us. We need to consider them before submitting the problem
# This one was when n == 1.
#Check the bounds on alll the variables and make sure they work





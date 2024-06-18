
from itertools import pairwise
for _ in range(int(input())):
    n = int(input())
    nums = map(int, input().split())

    max_num = 10**10

    for a,b in pairwise(nums):
        max_num = min(max(a, b), max_num)
    print(max_num - 1)

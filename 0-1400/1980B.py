
for _ in range(int(input())):
    vars = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    fav = nums[vars[1] - 1]
    remove = vars[2]

    nums = sorted(nums, reverse = True)
    if remove == vars[0]: print('Yes')
    elif nums[remove -1] < fav: print('Yes')
    elif nums[remove - 1] > fav: print('No')
    else:
        if nums[remove] == nums[remove -1]: print('Maybe')
        else: print('Yes')

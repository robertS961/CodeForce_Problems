for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    nSet = set(nums)
    if len(nSet) == 1:
        print('No')
        continue
    seen = set()
    blue = False
    ans = ""

    for i in range(len(nums)):
        if (nums[i] in seen and not blue) or (i == len(nums) - 1 and not blue):
            ans+= "B"
            blue = True
        else:
            seen.add(nums[i])
            ans += "R"
    print('Yes')
    print(ans)


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = min(nums)
    for i in range(n -2):
        ans = max(ans, sorted(nums[i:i+3])[1])
    print(ans)

# Learned we can't sort the input array.
# Check in the problem if it wants you to take the array as it
# or sort it and move it around
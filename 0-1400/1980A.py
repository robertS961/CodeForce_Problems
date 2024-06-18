from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    letters = input()

    cnt = Counter(letters)
    ans = 0

    for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        ans += max(m - cnt[char], 0)

    print(ans)

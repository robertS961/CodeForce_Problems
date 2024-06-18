
import math
for _ in range(int(input())):
    num = int(input())
    turns = int(math.log10(num))
    bit = 0
    flag = True

    for i in range(turns):
        curr = ((num % 10) - bit) + 10
        num //= 10
        bit = 0

        for j in range(5, 10):
            if 5<=  curr - j <= 9:
                bit = 1
                break
        flag &= bit

    print('Yes') if flag and num == 1 else print('No')

#Careful with hidden test cases that will sometimes
#test for issues outside the range

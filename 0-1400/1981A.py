

for _ in range(int(input())):
    range = list(map(int, input().split()))
    print(range[1].bit_length() - 1)
#log is just division everytime
#log10 is num//10 everytime

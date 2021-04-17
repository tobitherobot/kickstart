# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3

def solve():
    n, k = map(int, input().split())
    s = input()
    c = 0

    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            c += 1
    
    return abs(k-c)

t = int(input())
for i in range(t):
    s = solve()
    print("Case #{}: {}".format(i+1, s))
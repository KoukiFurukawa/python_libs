n = int(input())
ans = []

while n > 0:
    for i in range(10,-1,-1):
        if 3**i <= n:
            ans.append(i)
            n -= 3**i
            break

print(len(ans))
print(*ans, sep=" ")
n = int(input("Number of items: "))
v = list(map(int, input("Values: ").split()))
w = list(map(int, input("Weights: ").split()))
W = int(input("Capacity: "))

dp = [0] * (W + 1)

for i in range(n):
    for c in range(W, w[i] - 1, -1):
        dp[c] = max(dp[c], dp[c - w[i]] + v[i])

print("Maximum value:", dp[W])
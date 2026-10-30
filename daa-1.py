
n = int(input("Number of items: "))
p = list(map(int, input("Profits: ").split()))
w = list(map(int, input("Weights: ").split()))
cap = int(input("Capacity: "))

items = sorted(zip(p, w), key=lambda x: x[0] / x[1], reverse=True)
ans = 0

for profit, weight in items:
    ratio = profit / weight
    take = min(cap, weight)
    ans += take * ratio
    cap -= take
    if cap == 0:
        break
    
print("Maximum Profit:", ans)

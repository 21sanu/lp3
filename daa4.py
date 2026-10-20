
# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    p = int(input(f"Enter profit of item {i + 1}: "))
    weights.append(w)
    profits.append(p)

W = int(input("Enter knapsack capacity: "))

if n <= 0 or W < 0 or any(w <= 0 for w in weights):
    print("Enter a positive number of items, positive weights, "
          "and non-negative capacity.")
else:
    # Create DP table
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected = []
    w = W

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()

    print("Maximum profit:", dp[n][W])
    print("Selected items:", selected)


n = int(input("Enter number of items: "))

wgt = []
pft = []

for i in range(n):
    wgt.append(int(input("Enter weight: ")))
    pft.append(int(input("Enter profit: ")))

cap = int(input("Enter knapsack capacity: "))

if n <= 0 or cap < 0 or any(w <= 0 for w in wgt):
    print("Enter valid values")

else:
    # Create DP table
    dp = [[0] * (cap+1) for _ in range(n+1)]

    # Fill DP table
    for i in range(1, n+1):
        for c in range(cap+1):

            if wgt[i-1] <= c:
                dp[i][c] = max(
                    pft[i-1] + dp[i-1][c-wgt[i-1]],
                    dp[i-1][c]
                )
            else:
                dp[i][c] = dp[i-1][c]

    # Find selected items
    selected = []
    c = cap

    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            selected.append(i)
            c = c - wgt[i-1]

    selected.reverse()

    print("Maximum profit:", dp[n][cap])
    print("Selected items:", selected)

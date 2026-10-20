
# Fractional Knapsack using Greedy Method

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = float(input(f"Enter weight of item {i + 1}: "))
    p = float(input(f"Enter profit of item {i + 1}: "))
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter knapsack capacity: "))

if n <= 0 or capacity < 0 or any(w <= 0 for w in weights):
    print("Enter a positive number of items, positive weights, "
          "and non-negative capacity.")
else:
    # Calculate profit-to-weight ratio
    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i + 1))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_profit = 0.0
    remaining_capacity = capacity

    for ratio, weight, profit, item_no in items:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            total_profit += profit
            remaining_capacity -= weight
            print(f"Item {item_no}: Taken completely")
        else:
            fraction = remaining_capacity / weight
            total_profit += profit * fraction
            print(f"Item {item_no}: Taken {fraction:.2f} fraction")
            remaining_capacity = 0

    print(f"Maximum profit: {total_profit:.2f}")

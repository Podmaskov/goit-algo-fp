def greedy_algorithm(items, budget):
    """
    Greedy algorithm that selects items based on the best calories/cost ratio.
    """
    items_sorted = sorted(
        items.items(),
        key=lambda item: item[1]['calories'] / item[1]['cost'],
        reverse=True
    )
    total_calories = 0
    total_cost = 0
    selected_items = []

    for name, data in items_sorted:
        if total_cost + data['cost'] <= budget:
            selected_items.append(name)
            total_cost += data['cost']
            total_calories += data['calories']
    
    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    """
    Dynamic programming approach (0-1 knapsack) to find the optimal set of items.
    """
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(items.items())

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name, item_data = item_list[i - 1]
            cost = item_data['cost']
            calories = item_data['calories']

            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, _ = item_list[i - 1]
            selected_items.append(item_name)
            w -= items[item_name]['cost']

    selected_items.reverse()
    total_calories = dp[n][budget]
    total_cost = sum(items[item]['cost'] for item in selected_items)
    return selected_items, total_calories, total_cost

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    selected_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
    print(f"Greedy Algorithm => Items: {selected_items_greedy}, Calories: {total_calories_greedy}, Cost: {total_cost_greedy}")

    selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
    print(f"Dynamic Programming => Items: {selected_items_dp}, Calories: {total_calories_dp}, Cost: {total_cost_dp}")
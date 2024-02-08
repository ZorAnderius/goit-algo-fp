def greedy_algorithm(items: dict, budget: int) -> dict:
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    total_cost = 0
    selected_items = []

    for item_name, item_info in items_sorted:
        if total_cost + item_info['cost'] <= budget:
            selected_items.append(item_name)
            total_calories += item_info['calories']
            total_cost += item_info['cost']

    return {'selected_items': selected_items, 
            'total_calories': total_calories, 
            'total_cost': total_cost}

def dynamic_programming(items: dict, budget: int) -> dict:
    table = [[0 for x in range(budget + 1)] for x in range(len(items) + 1)] 
    
    for i in range(1, len(items) + 1):
        item_name = list(items.keys())[i-1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']

        for b in range(1, budget + 1):
            if item_cost > b:
                table[i][b] = table[i-1][b]
        
            else:
                table[i][b] = max(table[i-1][b], 
                table[i-1][b-item_cost] + item_calories)

    b = budget
    selected_items = []
    total_cost = 0
    total_calories = 0
    for i in range(len(items), 0, -1):
        if table[i][b] != table[i-1][b]:
            key = list(items.keys())[i-1]
            selected_items.append(list(items.keys())[i-1])
            total_calories += items[key]['calories']
            total_cost += items[key]['cost']
            b -= items[selected_items[-1]]['cost']

    return {'selected_items': selected_items, 
            'total_calories': total_calories, 
            'total_cost': total_cost}

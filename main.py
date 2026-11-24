class Item:
    def __init__(self, symbol, weight, value):
        self.symbol = symbol
        self.weight = weight
        self.value = value


def knapsack(items, capacity):
    items = sorted(items, key=lambda item: item.value / item.weight, reverse=True)

    max_value = 0
    best_items = []

    def node_count(i, weight, value):
        if weight > capacity:
            return 0

        node_value = value
        node_weight = weight
        j = i

        while j < len(items) and node_weight + items[j].weight <= capacity:
            node_value += items[j].value
            node_weight += items[j].weight
            j += 1

        if j < len(items):
            node_value += (capacity - node_weight) * (
                items[j].value / items[j].weight
            )

        return node_value

    def branch_bound(i, weight, value, chosen):
        nonlocal max_value, best_items

        if weight > capacity:
            return

        if value > max_value:
            max_value = value
            best_items = chosen

        if i == len(items):
            return

        if node_count(i, weight, value) <= max_value:
            return

        branch_bound(
            i + 1,
            weight + items[i].weight,
            value + items[i].value,
            chosen + [items[i]]
        )

        branch_bound(i + 1, weight, value, chosen)

    branch_bound(0, 0, 0, [])
    return max_value, best_items
    
items = [
    Item("r", 3, 25),
    Item("p", 2, 15),
    Item("a", 2, 15),
    Item("m", 2, 20),
    Item("i", 1, 5),
    Item("k", 1, 15),
    Item("x", 3, 20),
    Item("t", 1, 25),
    Item("f", 1, 15),
    Item("d", 1, 10),
    Item("s", 2, 20),
    Item("c", 2, 20)
]

capacity = 9
start_points = 15

total_points = 0

for item in items:
    total_points = total_points + item.value

inhaler = items[4]
items.remove(inhaler)

capacity = capacity - inhaler.weight

best_value, best_items = knapsack(items, capacity)

best_items.append(inhaler)

selected_points = best_value + inhaler.value
left_points = total_points - selected_points
final_points = start_points + selected_points - left_points

print("Очки выбранных предметов:", selected_points)
print("Итоговые очки выживания:", final_points)

if final_points > 0:
    print("Решение найдено")
else:
    print("Нет подходящего решения")

if final_points > 0:
    inventory = []

    for item in best_items:
        for j in range(item.weight):
            inventory.append(item.symbol)

    while len(inventory) < 9:
        inventory.append("-")

    print("Инвентарь:")

    print(inventory[0:3])
    print(inventory[3:6])
    print(inventory[6:9])
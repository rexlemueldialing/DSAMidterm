max_bagCap = 5
itemWeight = {'A': 1, 'B': 2, 'C': 3}
itemValue = {'A': 10, 'B': 15, 'C': 40}

def bestItemCombinations():
    best_combinations = []

    for a in range(max_bagCap // itemWeight['A'] + 1):
        for b in range(max_bagCap // itemWeight['B'] + 1):
            for c in range(max_bagCap // itemWeight['C'] + 1):
                total = a * itemWeight['A'] + b * itemWeight['B'] + c * itemWeight['C']
                if total == max_bagCap:
                    best_combinations.append({'A': a, 'B': b, 'C': c})
                    print(f"Item Combos: A={a}, B={b}, C={c}, Total weight of the Items={total} kg")
    return best_combinations

print("Item Combinations That Maximzes Bag Capacity (5kg): ")
all_combos = bestItemCombinations()

def highestValueCombination(combinations, itemValue):
    max_value = 0
    best_combo = None

    for combo in combinations:
        total_value = combo['A'] * itemValue['A'] + combo['B'] * itemValue['B'] + combo['C'] * itemValue['C']
        print(f"Combination {combo} → Total value = {total_value} pesos")

        if total_value > max_value:
            max_value = total_value
            best_combo = combo

    return max_value, best_combo


max_value, best_value_combo = highestValueCombination(all_combos, itemValue)
print(f"\nCombination with highest value: {best_value_combo}, Total value = {max_value} pesos")

def itemName():
    best_value_combo['Bucket'] = best_value_combo['A']
    del best_value_combo['A']
    best_value_combo['PM1'] = best_value_combo['B'] 
    del best_value_combo['B']
    best_value_combo['Brick'] = best_value_combo['C']
    del best_value_combo['C']
    print(f"\nYOU STEAL THESE ITEMS {best_value_combo} TO MAKE A TOTAL OF {max_value} PESOS!!!")
    return best_value_combo

itemName()
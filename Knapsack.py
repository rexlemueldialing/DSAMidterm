# Say you are trying to build muscles. So, you're gonna need to eat 
# a lot of protein. However, in every meal you can only eat up to
# 100 calories. How would you make a meal with the most amount of 
# protein but does not exceed your maximum calaorie intake per meal?

# There are three foods available: (A)Egg --- 10 calories with 15g of protein,
# (B) Chicken --- 35 calories with 75g of protein, and (C) Fish --- 25 calories
# with 40g of protein.

MAX_CAL_INTAKE = 100
foodCalories = {'A': 10, 'B': 35, 'C': 25}
foodProtein = {'A': 15, 'B': 75, 'C': 40}

def bestMealCombinations():
    best_combinations = []

    for a in range(MAX_CAL_INTAKE // foodCalories['A'] + 1):
        for b in range(MAX_CAL_INTAKE // foodCalories['B'] + 1):
            for c in range(MAX_CAL_INTAKE // foodCalories['C'] + 1):
                total = a * foodCalories['A'] + b * foodCalories['B'] + c * foodCalories['C']
                if total == MAX_CAL_INTAKE:
                    best_combinations.append({'A': a, 'B': b, 'C': c})
                    print(f"Food Combos: A={a}, B={b}, C={c} > Total Calorie={total}")
    return best_combinations

print("FOOD COMBOS THAT DOES NOT EXCEED YOUR CALORIE PER MEAL INTAKE: ")
foodCombos = bestMealCombinations()

def highestProteinFoodCombo(combinations, foodProtein):
    max_protein = 0
    best_combo = None

    for combo in combinations:
        total_protein = combo['A'] * foodProtein['A'] + combo['B'] * foodProtein['B'] + combo['C'] * foodProtein['C']
        print(f"Food Combo {combo} > Total Protein = {total_protein}")

        if total_protein > max_protein:
            max_protein = total_protein
            best_combo = combo
    return max_protein, best_combo


max_protein, best_combo = highestProteinFoodCombo(foodCombos, foodProtein)
print(f"\nFood Combination with the highest protein: {best_combo}, Total protein = {max_protein}")

def FoodName():
    best_combo['Egg'] = best_combo['A']
    del best_combo['A']
    best_combo['Chicken'] = best_combo['B'] 
    del best_combo['B']
    best_combo['Fish'] = best_combo['C']
    del best_combo['C']
    print(f"\nYOUR MEAL SHOULD CONSIST OF {best_combo} WHICH TOTALS TO {max_protein} PROTEIN!!!")
    return best_combo

FoodName()
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"] for food in spicy_foods]
names = get_names(spicy_foods)
print(names)

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
cuisine = "American"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine)
print(spicy_food)


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_emojis = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  

    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

result = get_average_heat_level(spicy_foods)
print(result)

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods_copy = spicy_foods.copy()
     spicy_foods_copy.append(spicy_food)
     return spicy_foods_copy
print(spicy_foods)

import json
import random

class Recipes:
    def __init__(self, recipes_dict=None):
        self.recipes_file = "my_recipes.txt"
        self.recipes = {}

        if recipes_dict is not None:
            self.recipes = recipes_dict
            self._update_recipes_file()

    def add_recipe(self, recipe):
        if self._is_valid_recipe(recipe):
            code = self._generate_code(recipe['name'])
            self.recipes[code] = recipe
            self._update_recipes_file()

    def remove_recipe(self, code):
        if code in self.recipes:
            del self.recipes[code]
            self._update_recipes_file()

    def _is_valid_recipe(self, recipe):
        required_keys = {'name', 'ingredients', 'time'}
        return set(recipe.keys()).issuperset(required_keys)

    def _generate_code(self, name):
        words = name.split()
        code = ''.join(word[0].upper() for word in words)
        return code

    def _update_recipes_file(self):
        with open(self.recipes_file, 'w') as file:
            file.write(json.dumps(self.recipes))

    def __str__(self):
        recipe_str = ''
        for code, recipe in self.recipes.items():
            recipe_str += f"Name: {recipe['name']}\n"
            recipe_str += f"Time: {recipe['time']} minutes\n"
            recipe_str += f"Ingredients: {', '.join(recipe['ingredients'])}\n\n"
        return recipe_str

    def load_recipes_from_file(self):
        try:
            with open(self.recipes_file, 'r') as file:
                self.recipes = json.load(file)
        except FileNotFoundError:
            self.recipes = {}

    def save_recipes_to_file(self):
        self._update_recipes_file()

    def get_random_recipe_with_enough_ingredients(self, ingredient_list):
        eligible_recipes = []
        for recipe in self.recipes.values():
            if all(ingredient in ingredient_list for ingredient in recipe['ingredients']):
                eligible_recipes.append(recipe)
        
        if eligible_recipes:
            random_recipe = random.choice(eligible_recipes)
            return random_recipe
        else:
            return None

    def get_all_recipes_with_enough_ingredients(self, ingredient_list):
        eligible_recipes = []
        for recipe in self.recipes.values():
            if all(ingredient in ingredient_list for ingredient in recipe['ingredients']):
                eligible_recipes.append(recipe)

        return eligible_recipes

    def get_recipe_details(self, recipe_id):
        if recipe_id in self.recipes:
            recipe = self.recipes[recipe_id]
            details = {
                "name": recipe["name"],
                "ingredients": recipe["ingredients"],
                "time": recipe["time"]
            }
            return details
        else:
            print(f"Recipe {recipe_id} was not found")
            return None


# recipes_dict = {
#     'SPO': {
#         'name': 'Spaghetti Bolognese',
#         'ingredients': ['Pasta', 'Ground beef', 'Tomato', 'Onion', 'Garlic', 'Olive oil'],
#         'time': '45',
#     },
#     'OML': {
#         'name': 'Omelette',
#         'ingredients': ['Eggs', 'Butter', 'Salt', 'Pepper'],
#         'time': '15',
#     },
#     'CTP': {
#         'name': 'Chicken Tacos',
#         'ingredients': ['Chicken', 'Tortillas', 'Lettuce', 'Tomato', 'Onion', 'Cilantro'],
#         'time': '30',
#     },
#     'PBR': {
#         'name': 'Potato Salad',
#         'ingredients': ['Potato', 'Mayonnaise', 'Mustard', 'Onion', 'Celery', 'Salt', 'Pepper'],
#         'time': '20',
#     },
#     'CTM': {
#         'name': 'Chicken Tikka Masala',
#         'ingredients': ['Chicken', 'Tomato', 'Onion', 'Garlic', 'Ginger', 'Cream', 'Spices'],
#         'time': '60',
#     },
#     'BFC': {
#         'name': 'Beef Stroganoff',
#         'ingredients': ['Beef', 'Mushroom', 'Onion', 'Sour cream', 'Flour', 'Butter'],
#         'time': '45',
#     },
#     'SCS': {
#         'name': 'Scrambled Eggs',
#         'ingredients': ['Eggs', 'Milk', 'Salt', 'Pepper'],
#         'time': '10',
#     },
#     'GCR': {
#         'name': 'Grilled Cheese Sandwich',
#         'ingredients': ['Bread', 'Cheese', 'Butter'],
#         'time': '10',
#     },
#     'FGS': {
#         'name': 'French Toast',
#         'ingredients': ['Bread', 'Eggs', 'Milk', 'Cinnamon'],
#         'time': '15',
#     },
#     'CCH': {
#         'name': 'Classic Caesar Salad',
#         'ingredients': ['Romaine lettuce', 'Caesar dressing', 'Parmesan cheese', 'Croutons'],
#         'time': '10',
#     },
# }

# my_recipes = Recipes(recipes_dict)

# # Adding a new recipe
# new_recipe = {
#     'name': 'Tomato Soup',
#     'ingredients': ['Tomato', 'Onion', 'Garlic', 'Olive oil'],
#     'time': '30',
# }
# my_recipes.add_recipe(new_recipe)

# # Removing a recipe
# my_recipes.remove_recipe('OML')

# # Printing the recipes
# print(my_recipes)
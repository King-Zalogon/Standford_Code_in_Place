"""
This files handles the class that keeps track of the recipes. Stores them in a txt.
Each recipe is a dictionary on itself with a "name", "time", and a "ingredients" list.
The main will interact with this class so as to check the requiered ingredients and compare with those stored in the Ingredients object
The main will also reques for a random recipe, a list of thouse for with the ingredients are present.
For each recipe it should also be able the request any or all recipes keys and/values.
This class will contain methods to review current recipes, add or remove them.
"""

import json
import random


class Recipes:
    def __init__(self, recipes_dict=None):
        self.recipes_file = "my_recipes.txt"
        self.recipes = {}

        if recipes_dict is not None:
            self.recipes = recipes_dict
            self._update_recipes_file()

    # def add_recipe(self, recipe):
    #     if self._is_valid_recipe(recipe):
    #         code = self._generate_code(recipe['name'])
    #         if code not in self.recipes:
    #             self.recipes[code] = recipe
    #             self._update_recipes_file()
    #         else:
    #             print("Recipe already exists")

    def add_recipe(self, recipe):
        if self._is_valid_recipe(recipe):
            code = self._generate_code(recipe['name'])
            if code not in self.recipes:
                self.recipes[code] = {
                    'name': recipe['name'],
                    'time': recipe['time'],
                    'ingredients': recipe['ingredients']
                }
                self._update_recipes_file()
            else:
                print("Recipe already exists")

        print("Recipe added successfully!")

    def remove_recipe(self, code):
        if code in self.recipes:
            del self.recipes[code]
            self._update_recipes_file()
        else:
            print(f"Recipe {code} was not found")

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
        try:
            recipe = self.recipes[recipe_id]
            details = {
                "name": recipe["name"],
                "ingredients": recipe["ingredients"],
                "time": recipe["time"]
            }
            return details
        except KeyError:
            raise KeyError(f"Recipe {recipe_id} was not found")
        
    def get_recipes_using_ingredient(self, ingredient):
        matching_recipes = []
        for recipe in self.recipes.values():
            if ingredient in recipe['ingredients']:
                matching_recipes.append(recipe)
        return matching_recipes
    
    def get_all_recipes(self):
        return list(self.recipes.values())
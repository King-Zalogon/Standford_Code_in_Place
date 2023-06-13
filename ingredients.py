"""
This file handles the class created to keep record of the users current ingredients.
Allow to print, add and remove ingredients (as a str or list of str).
Should also be iterable by the function/class that checks available ingredients agains those needed by any given recipe.
"""

import json

class Ingredients:
    def __init__(self, ingredients_list=None):
        self.ingredients_file = "my_ingredients.txt"
        self.ingredients = []

        if ingredients_list is not None:
            self.ingredients = ingredients_list
            self._update_ingredients_file()
        else:
            self.ingredients = self.load_ingredients()
    
    def __str__(self):
        return ", ".join(self.ingredients)

    def _update_ingredients_file(self):
        with open(self.ingredients_file, 'w') as file:
            file.write(json.dumps(self.ingredients))

    def load_ingredients(self):
        try:
            with open(self.ingredients_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_ingredients(self):
        with open(self.ingredients_file, "w") as file:
            json.dump(self.ingredients, file)

        
    def add_ingredient(self, new_ingredient):
        if isinstance(new_ingredient, str):
            new_ingredient = new_ingredient.capitalize()
            if new_ingredient not in self.ingredients:
                self.ingredients.append(new_ingredient)
                self.save_ingredients()
        elif isinstance(new_ingredient, list):
            new_ingredients = [ingredient.capitalize() for ingredient in new_ingredient]
            for ingredient in new_ingredients:
                if ingredient not in self.ingredients:
                    self.ingredients.append(ingredient)
            self.save_ingredients()
        else:
            print("Can only add one item as a string or several ingredients as a list of strings")

    def remove_ingredient(self, ingredient_to_remove):
        if isinstance(ingredient_to_remove, str):
            ingredient_to_remove = ingredient_to_remove.capitalize()
            if ingredient_to_remove in self.ingredients:
                self.ingredients.remove(ingredient_to_remove)
                self.save_ingredients()
                print(f"{ingredient_to_remove} was removed")
            else:
                print(f"{ingredient_to_remove} was not found in current ingredients")
        elif isinstance(ingredient_to_remove, list):
            removed_ingredients = []
            for ingredient in ingredient_to_remove:
                ingredient = ingredient.capitalize()
                if ingredient in self.ingredients:
                    self.ingredients.remove(ingredient)
                    removed_ingredients.append(ingredient)
            if removed_ingredients:
                self.save_ingredients()
                print(f"{', '.join(removed_ingredients)} were removed")
            else:
                print("No ingredients were found in current ingredients")
        else:
            print("Can only remove one item as a string or several ingredients as a list of strings")

            

"""
This file handles the class created to keep record of the users current ingredients.
Allow to print, add and remove ingredients (as a str or list of str).
Should also be iterable by the function/class that checks available ingredients agains those needed by any given recipe.
"""

class my_ingredients:
    
    def __init__(self):
        self.cooking_ingredients = [
        'Salt',
        'Pepper',
        'Olive oil',
        'Butter',
        'Garlic',
        'Onion',
        'Tomato',
        'Chicken',
        'Beef',
        'Pork',
        'Eggs',
        'Milk',
        'Flour',
        'Sugar',
        'Bread',
        'Potato',
        'Rice',
        'Pasta',
        'Cheese',
        'Yogurt',
        'Lemon',
        'Honey',
        'Vinegar',
        'Mayonnaise',
        'Mustard',
        'Ketchup',
        'Soy sauce',
        'Worcestershire sauce',
        'Lettuce',
        'Cucumber',
        'Carrot',
        'Celery',
        'Bell pepper',
        'Mushroom',
        'Green beans',
        'Broccoli',
        'Cauliflower',
        'Zucchini',
        'Spinach',
        'Parsley',
        'Basil',
        'Thyme',
        'Rosemary',
        'Oregano',
        'Bay leaves',
        'Cinnamon',
        'Nutmeg',
        'Vanilla extract',
        'Lime',
        'Ginger',
        'Coconut milk',
        'Cilantro',
        'Curry powder',
        'Paprika',
        'Chili powder',
        'Cumin',
        'Coriander',
        ]
    
    def __str__(self):
        self.my_list = ""
        for i in self.cooking_ingredients:
            self.my_list += f"{i}, "
        return self.my_list
        
    def add_ingredient(self, new_ingredient):
        if type(new_ingredient) == str:
            if new_ingredient not in self.cooking_ingredients:
                self.cooking_ingredients.append(new_ingredient.capitalize())
        elif type(new_ingredient) == list:
            for ingredient in new_ingredient:
                if ingredient not in self.cooking_ingredients:
                    self.cooking_ingredients.append(ingredient.capitalize())
        else:
            print("Can only add on item as a string or seveal ingredients as a list of strings")


    def remove_ingredient(self, new_ingredient):
        if type(new_ingredient) == str:
            if new_ingredient.capitalize() in self.cooking_ingredients:
                self.cooking_ingredients.remove(new_ingredient.capitalize())
                print(f"{new_ingredient.capitalize()} was removed")
            else:
                print(f"{new_ingredient.capitalize()} was not found in current ingredients")
        elif type(new_ingredient) == list:
            for ingredient in new_ingredient:
                if ingredient.capitalize() in self.cooking_ingredients:
                    self.cooking_ingredients.remove(ingredient.capitalize())
                    print(f"{ingredient.capitalize()} was removed")
                else:
                    print(f"{ingredient.capitalize()} was not found in current ingredients") 
        else:
            print("Can only add on item as a string or seveal ingredients as a list of strings")


"""
This file handles the main function.
The main() allows the user to interact with the Ingredients and Recipes objects created from such classes.
It will give the user several options in its menu:
-Get a random recipe for which there are enough ingredients
    -- Get another random recipe
    -- Get full details of the recipe
-Get the list recipes for which there are enough ingredients
    -- Get full details of the recipe
-List, add or remove the ingredients or the recipes
    -- Get full details for a recipe
    -- List missing ingredientes for a recipe
    -- List ingredients not used in any recipe
-Return to the previous menu
-Exit Program (should be available in each menu and sub menu)
"""

from ingredients import Ingredients
from recipes import Recipes
import samples


def main():
    ing_ex = samples.ingredients_examples
    rec_ex = samples.recipes_examples

    ingredients = Ingredients(ing_ex)
    recipes = Recipes(rec_ex)

    print("Welcome to the Recipe Manager!")
    print("-------------------------------")

    while True:
        print("\nCurrent Statistics:")
        print("-------------------")
        print(f"Number of Ingredients: {len(ingredients.ingredients)}")
        print(f"Number of Recipes: {len(recipes.recipes)}")

        print("\nOptions:")
        print("--------")
        print("1. Get a random recipe with enough ingredients")
        print("2. Get a list of all current possible recipes")
        print("3. Get the complete list of recipes")
        print("4. Get the complete list of ingredients")
        print("5. Add or remove ingredients or recipes")
        print("6. Exit program")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            get_random_recipe(ingredients, recipes)

        elif choice == "2":
            get_all_possible_recipes(ingredients, recipes)

        elif choice == "3":
            get_all_recipes(recipes)

        elif choice == "4":
            get_all_ingredients(ingredients, recipes)

        elif choice == "5":
            add_or_remove(ingredients, recipes)

        elif choice == "6":
            exit_program()

        else:
            print("Invalid choice. Please try again.")


def get_random_recipe(ingredients, recipes):
    print("\n-- Get a random recipe with enough ingredients --")
    random_recipe = recipes.get_random_recipe_with_enough_ingredients(ingredients.ingredients)
    if random_recipe is not None:
        print("Title:", random_recipe['name'])
        print("Preparation Time:", random_recipe['time'], "minutes")
        print("Ingredients Required:", len(random_recipe['ingredients']))

        while True:
            print("\n*** Sub-Options ***")
            print("1. Get complete details of the recipe")
            print("2. Get another random recipe")
            print("3. Go back to the main menu")
            print("4. Exit program")

            sub_choice = input("Enter your choice (1-4): ")

            if sub_choice == "1":
                print("\n-- Complete Details of the Recipe --")
                recipe_code = input("Enter the recipe code: ")
                try:
                    recipes.get_recipe_details(recipe_code)
                except KeyError as e:
                    print(e)

            elif sub_choice == "2":
                random_recipe = recipes.get_random_recipe_with_enough_ingredients()
                if random_recipe is not None:
                    print("Title:", random_recipe['name'])
                    print("Preparation Time:", random_recipe['time'], "minutes")
                    print("Ingredients Required:", len(random_recipe['ingredients']))
                else:
                    print("No more random recipes available.")

            elif sub_choice == "3":
                break

            elif sub_choice == "4":
                exit_program()

            else:
                print("Invalid choice. Please try again.")

    else:
        print("No recipes available with enough ingredients.")


def get_all_possible_recipes(ingredients, recipes):
    print("\n-- Get a list of all current possible recipes --")
    all_recipes = recipes.get_all_recipes_with_enough_ingredients(ingredients.ingredients)
    for recipe in all_recipes:
        print("Title:", recipe['name'])
        print("Preparation Time:", recipe['time'], "minutes")
        print("Ingredients Required:", len(recipe['ingredients']))

    while True:
        print("\n*** Sub-Options ***")
        print("1. Select one recipe and get the full details")
        print("2. Go back to the list of all current possible recipes")
        print("3. Go back to the main menu")
        print("4. Exit program")

        sub_choice = input("Enter your choice (1-4): ")

        if sub_choice == "1":
            print("\n-- Full Details of the Recipe --")
            recipe_code = input("Enter the recipe code: ")
            try:
                recipes.get_recipe_details(recipe_code)
            except KeyError as e:
                print(e)

        elif sub_choice == "2":
            break

        elif sub_choice == "3":
            break

        elif sub_choice == "4":
            exit_program()

        else:
            print("Invalid choice. Please try again.")


def get_all_recipes(recipes):
    print("\n-- Get the complete list of recipes --")
    all_recipes = recipes.get_all_recipes()
    for recipe in all_recipes:
        print("Title:", recipe['name'])
        print("Preparation Time:", recipe['time'], "minutes")
        print("Ingredients Required:", len(recipe['ingredients']))

    while True:
        print("\n*** Sub-Options ***")
        print("1. Select one recipe and get the full details")
        print("2. Go back to the list of all recipes")
        print("3. Go back to the main menu")
        print("4. Exit program")

        sub_choice = input("Enter your choice (1-4): ")

        if sub_choice == "1":
            print("\n-- Full Details of the Recipe --")
            recipe_code = input("Enter the recipe code: ")
            try:
                # recipes.get_recipe_details(recipe_code, include_missing_ingredients=True)
                recipes.get_recipe_details(recipe_code)
            except KeyError as e:
                print(e)

        elif sub_choice == "2":
            break

        elif sub_choice == "3":
            break

        elif sub_choice == "4":
            exit_program()

        else:
            print("Invalid choice. Please try again.")


def get_all_ingredients(ingredients, recipes):
    print("\n-- Get the complete list of ingredients --")
    all_ingredients = ingredients.get_all_ingredients()
    for ingredient in all_ingredients:
        print("Ingredient:", ingredient)
        recipes_using_ingredient = recipes.get_recipes_using_ingredient(ingredient)
        if recipes_using_ingredient:
            print("Recipes using it:")
            for recipe in recipes_using_ingredient:
                print("- Title:", recipe['name'])
                print("  Preparation Time:", recipe['time'], "minutes")
                print("  Ingredients Required:", len(recipe['ingredients']))
        else:
            print("No recipes using this ingredient.")

    while True:
        print("\n*** Sub-Options ***")
        print("1. Select one ingredient and list which recipes use it")
        print("2. Go back to the list of all ingredients")
        print("3. Go back to the main menu")
        print("4. Exit program")

        sub_choice = input("Enter your choice (1-4): ")

        if sub_choice == "1":
            print("\n-- List of Recipes Using the Ingredient --")
            ingredient_name = input("Enter the ingredient name: ")
            recipes_using_ingredient = recipes.get_recipes_using_ingredient(ingredient_name)
            if recipes_using_ingredient:
                print(f"Recipes using {ingredient_name}:")
                for recipe in recipes_using_ingredient:
                    print("- Title:", recipe['name'])
                    print("  Preparation Time:", recipe['time'], "minutes")
                    print("  Ingredients Required:", len(recipe['ingredients']))
            else:
                print(f"No recipes using {ingredient_name}.")

        elif sub_choice == "2":
            break

        elif sub_choice == "3":
            break

        elif sub_choice == "4":
            exit_program()

        else:
            print("Invalid choice. Please try again.")


def add_or_remove(ingredients, recipes):
    print("\n-- Add or Remove Ingredients/Recipes --")

    while True:
        print("\n*** Options ***")
        print("1. Add an ingredient")
        print("2. Remove an ingredient")
        print("3. Add a recipe")
        print("4. Remove a recipe")
        print("5. Go back to the main menu")
        print("6. Exit program")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            ingredient_name = input("Enter the name of the ingredient to add: ")
            ingredients.add_ingredient(ingredient_name)
            print(f"Ingredient '{ingredient_name}' has been added.")

        elif choice == "2":
            ingredient_name = input("Enter the name of the ingredient to remove: ")
            ingredients.remove_ingredient(ingredient_name)
            print(f"Ingredient '{ingredient_name}' has been removed.")

        elif choice == "3":
            recipe_name = input("Enter the name of the recipe to add: ")
            recipe_time = int(input("Enter the preparation time (in minutes): "))
            recipe_ingredients = input("Enter the ingredients (comma-separated): ").split(",")
            words = recipe_name.split()
            code = ''.join(word[0].upper() for word in words)
            new_recipe = {code:{'name':recipe_name, 'time':recipe_time, 'ingredients':recipe_ingredients}}
            recipes.add_recipe(new_recipe)
            print(f"Recipe '{recipe_name}' has been added.")

        elif choice == "4":
            recipe_code = input("Enter the code of the recipe to remove: ")
            recipes.remove_recipe(recipe_code)
            print(f"Recipe with code '{recipe_code}' has been removed.")

        elif choice == "5":
            break

        elif choice == "6":
            exit_program()

        else:
            print("Invalid choice. Please try again.")


def exit_program():
    print("\nGoodbye!")
    exit()


if __name__ == '__main__':
    main()


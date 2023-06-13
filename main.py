from ingredients import Ingredients
from recipes import Recipes
import samples

ing_ex = samples.ingredients_examples
rec_ex = samples.recipes_examples

def main():
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
            print("\n-- Get a random recipe --")
            random_recipe = recipes.get_random_recipe_with_enough_ingredients(ingredients.ingredients)
            if random_recipe is not None:
                print("Title:", random_recipe['name'])
                print("Preparation Time:", random_recipe['time'], "minutes")
                print("Ingredients Required:", len(random_recipe['ingredients']))
                sub_choice = ""
                while sub_choice != "4":
                    print("\n*** Sub-Options ***")
                    print("1. Get complete details of the recipe")
                    print("2. Get another random recipe")
                    print("3. Go back to the main menu")
                    print("4. Exit program")

                    sub_choice = input("Enter your choice (1-4): ")

                    if sub_choice == "1":
                        print("\n-- Complete Details of the Recipe --")
                        recipes.get_recipe_details(random_recipe['code'])
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

        elif choice == "2":
            print("\n-- Get a list of all current possible recipes --")
            all_recipes = recipes.get_all_recipes_with_enough_ingredients(ingredients.ingredients)
            for recipe in all_recipes:
                print("Title:", recipe['name'])
                print("Preparation Time:", recipe['time'], "minutes")
                print("Ingredients Required:", len(recipe['ingredients']))

            sub_choice = ""
            while sub_choice != "4":
                print("\n*** Sub-Options ***")
                print("1. Select one recipe and get the full details")
                print("2. Go back to the list of all current possible recipes")
                print("3. Go back to the main menu")
                print("4. Exit program")

                sub_choice = input("Enter your choice (1-4): ")

                if sub_choice == "1":
                    print("\n-- Full Details of the Recipe --")
                    recipe_code = input("Enter the recipe code: ")
                    recipes.get_recipe_details(recipe_code)
                elif sub_choice == "2":
                    break
                elif sub_choice == "3":
                    break
                elif sub_choice == "4":
                    exit_program()

        elif choice == "3":
            print("\n-- Get the complete list of recipes --")
            all_recipes = recipes.get_all_recipes()
            for recipe in all_recipes:
                print("Title:", recipe['name'])
                print("Preparation Time:", recipe['time'], "minutes")
                print("Ingredients Required:", len(recipe['ingredients']))

            sub_choice = ""
            while sub_choice != "4":
                print("\n*** Sub-Options ***")
                print("1. Select one recipe and get the full details")
                print("2. Go back to the list of all recipes")
                print("3. Go back to the main menu")
                print("4. Exit program")

                sub_choice = input("Enter your choice (1-4): ")

                if sub_choice == "1":
                    print("\n-- Full Details of the Recipe --")
                    recipe_code = input("Enter the recipe code: ")
                    recipes.get_recipe_details(recipe_code, include_missing_ingredients=True)
                elif sub_choice == "2":
                    break
                elif sub_choice == "3":
                    break
                elif sub_choice == "4":
                    exit_program()

        elif choice == "4":
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

            sub_choice = ""
            while sub_choice != "3":
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

        elif choice == "5":
            print("\n-- Add or Remove Ingredients or Recipes --")
            print("1. Add an ingredient")
            print("2. Remove an ingredient")
            print("3. Add a recipe")
            print("4. Remove a recipe")
            print("5. Go back to the main menu")
            print("6. Exit program")

            sub_choice = input("Enter your choice (1-6): ")

            if sub_choice == "1":
                ingredient_name = input("Enter the name of the ingredient to add: ")
                ingredients.add_ingredient(ingredient_name)
            elif sub_choice == "2":
                ingredient_name = input("Enter the name of the ingredient to remove: ")
                ingredients.remove_ingredient(ingredient_name)
            elif sub_choice == "3":
                recipe_name = input("Enter the name of the recipe to add: ")
                preparation_time = input("Enter the preparation time (in minutes): ")
                recipe_ingredients = input("Enter the ingredients (comma-separated): ").split(",")
                recipe = {
                    'name': recipe_name,
                    'ingredients': recipe_ingredients,
                    'time': preparation_time
                }
                recipes.add_recipe(recipe)
            elif sub_choice == "4":
                recipe_code = input("Enter the code of the recipe to remove: ")
                recipes.remove_recipe(recipe_code)
            elif sub_choice == "5":
                continue
            elif sub_choice == "6":
                exit_program()

        elif choice == "6":
            exit_program()

        else:
            print("Invalid choice. Please try again.")


def exit_program():
    print("Exiting the program. Goodbye!")
    exit()


if __name__ == "__main__":
    main()

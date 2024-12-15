from ingredients import generate_ingredients, IngredientGeneration
from country import get_country


def main():
    # get_ingredients()
    default_toppings = IngredientGeneration(cheeses=2, sauces=1)
    generated_ingredients = generate_ingredients(default_toppings)
    country = get_country()
    print(generated_ingredients)
    final_query = {**generated_ingredients, country: country}

if __name__ == "__main__":
    main()

from ingredients import generate_ingredients, IngredientGeneration, Category
from country import get_country


def main():
    # get_ingredients()
    # default_toppings = IngredientGeneration(cheeses=2, sauces=1)
    default_toppings = IngredientGeneration(
        quantities={
            Category.CHEESES.name: 2,
            Category.SAUCES.name: 1,
            Category.MEATS.name: 2,
            Category.VEGETABLES.name: 2,
            Category.HERBS_AND_SPICES.name: 1,
            Category.EXTRAS.name: 1,
        }
    )
    generated_ingredients = generate_ingredients(default_toppings)
    country = get_country()
    final_query = {**generated_ingredients, 'country': country}
    print(final_query)


if __name__ == "__main__":
    main()

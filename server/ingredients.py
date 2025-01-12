from dataclasses import asdict
from models.ingredient_model import PizzaIngredients, IngredientGeneration, pizza_ingredients
import random


def generate_ingredients(topping_input: IngredientGeneration) -> dict[str, int]:
    final_toppings = PizzaIngredients()

    # Iterate through the topping input to generate the pizza toppings
    for category_name, number in topping_input.quantities.items():
        # Get the number of available options for the category
        topping_category_length = len(pizza_ingredients[category_name])

        # Ensure the number of requested ingredients does not exceed available options
        if number > topping_category_length:
            raise ValueError(
                f"Cannot select {number} toppings from {category_name}, only {topping_category_length} available."
            )

        # Randomly select toppings from the available options
        random_ingredients = random.sample(pizza_ingredients[category_name], number)

        # Add the randomly selected ingredients to the final toppings list
        final_toppings.ingredients[category_name].extend(random_ingredients)

    # Convert the final toppings dataclass into a dictionary
    topping_dict = asdict(final_toppings)
    return topping_dict

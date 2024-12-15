from typing import List, Optional, Dict
from dataclasses import asdict, dataclass, field, fields
from enum import Enum, auto
import random, json


# Enum for ingredient categories
class Category(Enum):
    CHEESES = auto()
    SAUCES = auto()
    MEATS = auto()
    VEGETABLES = auto()
    HERBS_AND_SPICES = auto()
    EXTRAS = auto()


# PizzaIngredients class using a dictionary for ingredients
@dataclass(slots=True)
class PizzaIngredients:
    ingredients: Dict[str, List[str]] = field(
        default_factory=lambda: {
            Category.CHEESES.name: [],
            Category.SAUCES.name: [],
            Category.MEATS.name: [],
            Category.VEGETABLES.name: [],
            Category.HERBS_AND_SPICES.name: [],
            Category.EXTRAS.name: [],
        }
    )


# IngredientGeneration class using a dictionary for quantities
@dataclass(slots=True)
class IngredientGeneration:
    quantities: Dict[str, int] = field(
        default_factory=lambda: {
            Category.CHEESES.name: 0,
            Category.SAUCES.name: 0,
            Category.MEATS.name: 0,
            Category.VEGETABLES.name: 0,
            Category.HERBS_AND_SPICES.name: 0,
            Category.EXTRAS.name: 0,
        }
    )


# Pizza ingredients dictionary
pizza_ingredients = {
    Category.CHEESES.name: [
        "mozzarella cheese",
        "parmesan cheese",
        "cheddar cheese",
        "provolone cheese",
        "ricotta cheese",
        "goat cheese",
        "blue cheese",
        "feta cheese",
        "pecorino cheese",
        "gorgonzola cheese",
    ],
    Category.SAUCES.name: [
        "tomato sauce",
        "pesto sauce",
    ],
    Category.MEATS.name: [
        "pepperoni",
        "sausage",
        "ham",
        "bacon",
        "chicken",
        "ground beef",
        "salami",
        "prosciutto",
        "anchovies",
    ],
    Category.VEGETABLES.name: [
        "mushrooms",
        "onions",
        "bell peppers",
        "black olives",
        "green olives",
        "spinach",
        "artichokes",
        "tomatoes",
        "sun-dried tomatoes",
        "jalapeños",
        "pineapple",
        "broccoli",
        "arugula",
        "zucchini",
        "eggplant",
        "corn",
        "pineapple",
    ],
    Category.HERBS_AND_SPICES.name: [
        "fresh basil",
        "oregano",
        "thyme",
        "rosemary",
        "garlic",
        "red pepper flakes",
        "black pepper",
    ],
    Category.EXTRAS.name: [
        "barbecue sauce",
        "ranch dressing",
        "balsamic glaze",
        "truffle oil",
        "hot sauce",
        "hot honey",
    ],
}


# Generate ingredients based on the IngredientGeneration input
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

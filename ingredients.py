from typing import List, Optional
from dataclasses import asdict, dataclass, field, fields
from enum import Enum, auto
import random, json


class Category(Enum):
    CHEESES = auto()
    SAUCES = auto()
    MEATS = auto()
    VEGETABLES = auto()
    HERBS_AND_SPICES = auto()
    EXTRAS = auto()

@dataclass(slots=True)
class PizzaIngredients:
    cheeses: List[str]
    sauces: List[str]
    meats: Optional[List[str]] = field(default_factory=list)
    vegetables: Optional[List[str]] = field(default_factory=list)
    herbs_and_spices: Optional[List[str]] = field(default_factory=list)
    extras: Optional[List[str]] = field(default_factory=list)


@dataclass(slots=True)
class IngredientGeneration:
    cheeses: int
    sauces: int
    meats: Optional[int] = 0
    vegetables: Optional[int] = 0
    herbs_and_spices: Optional[int] = 0
    extras: Optional[int] = 0


pizza_ingredients = {
    Category.CHEESES: [
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
    Category.SAUCES: [
        "tomato sauce",
        "pesto sauce",
    ],
    Category.MEATS: [
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
    Category.VEGETABLES: [
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
    Category.HERBS_AND_SPICES: [
        "fresh basil",
        "oregano",
        "thyme",
        "rosemary",
        "garlic",
        "red pepper flakes",
        "black pepper",
    ],
    Category.EXTRAS: [
        "barbecue sauce",
        "ranch dressing",
        "balsamic glaze",
        "truffle oil",
        "hot sauce",
        "hot honey",
    ],
}

# default_topping_example = IngredientGeneration(cheeses=2, sauces=1)


# Returns a JSON version of PizzaIngredients
def generate_ingredients(topping_input: IngredientGeneration) -> str:
    final_toppings = PizzaIngredients(
        cheeses=[], sauces=[], meats=[], vegetables=[], herbs_and_spices=[], extras=[],
    )

    for entry in fields(topping_input):
        key = entry.name
        number = getattr(topping_input, key)
        category = Category[key.upper()]

        if category not in pizza_ingredients:
            raise ValueError(f"Invalid topping category: {category}")

        number = int(number) if number is not None else 0
        topping_category_length = len(pizza_ingredients[category])

        if number > topping_category_length:
            raise ValueError(
                f"Cannot select {number} toppings from {category}, only {topping_category_length} available."
            )
        random_ingredients = random.sample(pizza_ingredients[category], number)
        getattr(final_toppings, key).extend(random_ingredients)
    topping_dict = asdict(final_toppings)
    topping_json = json.dumps(topping_dict)

    print(topping_json)
    return topping_json


# generated_toppings = generate_ingredients(default_topping_example)
# print(generated_toppings)

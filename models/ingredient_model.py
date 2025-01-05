from typing import List, Dict
from dataclasses import dataclass, field
from enum import Enum
from pydantic import BaseModel, field_validator


# Enum for ingredient categories
class Category(Enum):
    CHEESES = "CHEESES"
    SAUCES = "SAUCES"
    MEATS = "MEATS"
    VEGETABLES = "VEGETABLES"
    HERBS_AND_SPICES = "HERBS_AND_SPICES"
    EXTRAS = "EXTRAS"


class ToppingInputModel(BaseModel):
    ingredients: Dict[Category, int]

    @field_validator("ingredients", mode="before")
    def validate_ingredients(cls, value):
        """
        Convert dictionary keys from strings to Enum instances.
        """
        if isinstance(value, dict):
            try:
                return {Category(key): val for key, val in value.items()}
            except ValueError as e:
                raise ValueError(f"Invalid key in ingredients: {e}")
        raise TypeError("ingredients must be a dictionary")

    class Config:
        use_enum_values = True


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

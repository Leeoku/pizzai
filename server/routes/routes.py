from fastapi import APIRouter
from models.ingredient_model import ToppingInputModel
from utils import assemble_data

from typing import Dict

router = APIRouter()


@router.post("/suggest/", tags=["suggestion"])
def suggest_toppings(data: ToppingInputModel):
    print("ingredientsINPUTNOW", data)
    suggestions = assemble_data(data)
    return suggestions


"""
Sample Input
{
    "ingredients": {
        "CHEESES": 3,
        "SAUCES": 2,
        "MEATS": 1,
        "VEGETABLES": 1,
        "HERBS_AND_SPICES": 1,
        "EXTRAS": 2,
    }
}
"""

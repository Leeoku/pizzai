from ingredients import generate_ingredients
from models.ingredient_model import IngredientGeneration
from country import get_country
from prompt import get_chat_conversation
import uuid


def assemble_data(data):
    toppings = IngredientGeneration(data.ingredients)
    generated_ingredients = generate_ingredients(toppings)
    country = get_country()
    generated_uuid = uuid.uuid4()
    final_query = {**generated_ingredients, "country": country, "id": generated_uuid}
    return final_query
    # get_chat_conversation()

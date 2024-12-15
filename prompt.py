# Import the openai key

# Create the general prompt. Goal is to input the ingredients and regenerate new ones based on a culture

# Start a conversation with OpenAI that feeds the prompt and returns the culture with new ingredients
from pydantic import BaseModel
from openai import OpenAI
from openai.types import (
    ErrorObject,
    FunctionDefinition,
    FunctionParameters,
    ResponseFormatJSONObject,
    ResponseFormatJSONSchema,
    ResponseFormatText,
)
from ingredients import PizzaIngredients


client = OpenAI()
sample_input = {
    "cheeses": ["mozzarella", "parmesan"],
    "sauces": ["tomato"],
    "meats": ["pepperoni"],
    "vegetables": ["bell peppers", "onions"],
    "country": "korean"
}


def get_chat_conversation():
    system_prompt = "You are an assistant specializing in culinary. You are to recommend ingredients to the user based on a provided nationality. When recommending, keep the same number of ingredients. You may choose to recommend none or all of the ingredients. "
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": sample_input},
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    chat_response_message = response.choices[0].message.content
    print(f"BOT:{chat_response_message}")

    print(response.choices)

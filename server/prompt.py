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
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI()
sample_input = {
    "cheeses": ["mozzarella", "parmesan"],
    "sauces": ["tomato"],
    "meats": ["pepperoni"],
    "vegetables": ["bell peppers", "onions"],
    "country": "korean",
}


def get_chat_conversation():
    system_prompt = "You are an assistant specializing in culinary. You are to recommend ingredients to the user based on a provided nationality. When recommending, keep the same number of ingredients. You may choose to recommend none, some or all of the ingredients. Return the output in the same json object format. If a category entry does not have a good recommendation, keep the original value."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"{sample_input}"},
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    print(response)
    chat_response_message = response.choices[0].message.content
    print(f"BOT:{chat_response_message}")
    if chat_response_message is None:
        chat_response_message = ""
    try:
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(chat_response_message)
    except Exception as e:
        print(f"Error writing to file: {e}")

    print(response.choices)

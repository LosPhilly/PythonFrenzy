import requests
import json


def get_recipes(ingredients):
    api_key = "YOUR_API_KEY"
    ingredients = "+".join(ingredients)
    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query={ingredients}"

    response = requests.get(url)
    data = response.json()
    return data
def main():
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    data = get_recipes(ingredients)
    for recipe in data["results"]:
        print(recipe["title"])


if __name__ == "__main__":
    main()

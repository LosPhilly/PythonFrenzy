import requests
import json

def translate(text, target_language):
    # Your API key
    api_key = "AIzaSyCzBJkNYjFpWEyTT3IBCKy3k-cQONaOLKY"
    
    # API URL
    url = f"https://translation.googleapis.com/language/translate/v2?q={text}&target={target_language}&key={api_key}"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = json.loads(response.text)
        
        # Get the translated text
        translated_text = data["data"]["translations"][0]["translatedText"]
        
        return translated_text
    else:
        return "Oops, something went wrong."

# Test the function
print(translate("Hello, world!", "fr"))


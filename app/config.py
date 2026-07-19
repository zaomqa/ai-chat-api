# config.py
import os
import json
from dotenv import load_dotenv

load_dotenv()



ai_api_key_config = os.getenv("AI_API_KEY")
name_config = os.getenv("NAME")

def get_ai_menu_context():
    # 1. Load the raw string from .env
    raw_menu = os.getenv("MENU", "{}")
    
    try:
        # 2. Safely parse string into a dictionary
        menu_dict = json.loads(raw_menu)
        
        # 3. Format it into an ultra-clear list for the AI prompt
        menu_lines = [f"- {item.title()}: ${price}" for item, price in menu_dict.items()]
        menu_text = "\n".join(menu_lines)
        
        return menu_text
    
    except json.JSONDecodeError:
        return "Error loading menu details."

# Generate the readable text
menu_config = get_ai_menu_context()

phone_config = os.getenv("PHONE")
hours_config = os.getenv("HOURS")
location_config = os.getenv("LOCATION")





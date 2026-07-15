# config.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()



ai_api_key_config = os.getenv("AI_API_KEY")
name_config = os.getenv("NAME")
menu_config = os.getenv("MENU")
phone_config = os.getenv("PHONE")
hours_config = os.getenv("HOURS")
location_config = os.getenv("LOCATION")
client = OpenAI(
    base_url= "https://openrouter.ai/api/v1" ,
    api_key = ai_api_key_config 
)



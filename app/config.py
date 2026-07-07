# config.py
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key_config = os.getenv("API_KEY")
name_config = os.getenv("NAME")
menu_config = os.getenv("MENU")
phone_config = os.getenv("PHONE")
hours_config = os.getenv("HOURS")
location_config = os.getenv("LOCATION")
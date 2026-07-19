# ai_service
from openai import OpenAI
import config as cfg
from services.prompts import SYSTEM_PROMPTS


client = OpenAI(
    base_url= "https://openrouter.ai/api/v1" ,
    api_key = cfg.ai_api_key_config 
)



restaurant_context = f"""
Restaurant name:
{cfg.name_config}

Location:
{cfg.location_config}

Phone:
{cfg.phone_config}

Hours:
{cfg.hours_config}

Menu:
{cfg.menu_config}
"""

# post
hours = {"opening","hours","open","close","closing"}
location = {"location","address","where"}
phone = {"phone","call","number","contact"}
pizza = {"pizzas","pizza"}
"""def generate_response(question: str):
    lower_question = question.lower()
    if any(word in lower_question for word in hours):
        return "our hours are from 10 am to 22 pm everyday"
    elif any(word in lower_question for word in location):
        return "we are located at in amman- jordan"
    elif any(word in lower_question for word in phone):
        return "our phone number is 0799999999"
    elif any(word in lower_question for word in pizza):
        return {"our pizza cost 8$"}
    else :
        return "I'm sorry, I don't have information on that. Please contact us directly for assistance."
"""
    

def generate_response(question: str):
    try:
        response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",  
        messages = [
            {"role": "system",
            "content": f"{SYSTEM_PROMPTS}\n\n{restaurant_context}"
            },
            { "role" : "user" ,
            "content" : question 
            }
        ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return {
            f"error : {str(e)}" 
        }



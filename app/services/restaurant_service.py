# restaurant_service.py
from restaurant_data import restaurant_info



def get_restaurant():
        return restaurant_info

def get_menu(item : str | None = None):
    if item is not None:
        price = restaurant_info["menu"].get(item)
        if price is not None:
            return {
                "item": item,
                "price": price
            }
        else:
            return {
                "error": "404 Not Found",
                "message": f"Item '{item}' not found in the menu."
            }
    return restaurant_info["menu"]

def get_hours():
    return {
        "hours": restaurant_info["hours"]
    }


def get_location():
    return {
        "location": restaurant_info["location"]
    }
       

def search_menu(item : str):
     price = restaurant_info["menu"].get(item)
     if item in restaurant_info["menu"]:
         return {
             "item": item,
             "price": price
         }  
     return {
            "error": "404 Not Found",
            "message": f"Item '{item}' not found in the menu."
     }

def get_phone():
     return {
          "phone": restaurant_info["phone"]
     }

def answer_question(question: str):
    question_lower = question.lower()
    if "hours" in question_lower:
        return get_hours()
    elif "location" in question_lower:
        return get_location()
    elif "phone" in question_lower:
        return get_phone()
    elif "menu" in question_lower:
        item = question_lower.replace("menu", "").strip()
        if item:
            return search_menu(item)
        else:
            return get_menu()
    else:
        return {
            "message": "i dont know the answer to that question."
        }
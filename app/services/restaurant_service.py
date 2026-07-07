# restaurant_service.py
import restaurant_data as data



def get_restaurant():
        return data.restaurant_info

def get_menu(item : str | None = None):
    if item is not None:
        price = data.menu.get(item)
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
    return data.menu

def get_hours():
    return {
        "hours": data.hours
    }


def get_location():
    return {
        "location": data.location
    }
       

def search_menu(item : str):
     price = data.menu.get(item)
     if item in data.menu:
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
          "phone": data.phone
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
    
def get_config():
    return {
        "phone": data.phone,
        "hours": data.hours,
        "location": data.location
    }
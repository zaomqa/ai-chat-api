# ai_service
import config as cfg

# post
hours = {"opening","hours","open","close","closing"}
location = {"location","address","where"}
phone = {"phone","call","number","contact"}
pizza = {"pizzas","pizza"}
def generate_response(question: str):
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
    
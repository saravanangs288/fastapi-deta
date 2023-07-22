def individual_serial(todo) -> dict:
    return{
        "id":str(todo["_id"]),
        "heading": todo["heading"],
        "description": todo["description"]
    }
def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
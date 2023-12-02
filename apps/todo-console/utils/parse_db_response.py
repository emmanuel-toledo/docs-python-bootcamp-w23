def parse_todo_to_json_array(todos):
    json_array = []
    for todo in todos:
        json_array.append({
            "id": todo[0],
            "name": todo[1],
            "description": todo[2],
            "status": todo[3],
            "created_on": todo[4],
            "completed_on": todo[5]
        })
    return json_array

def parse_todo_to_json(todo):
    json_object = {
        "id": todo[0],
        "name": todo[1],
        "description": todo[2],
        "status": todo[3],
        "created_on": todo[4],
        "completed_on": todo[5]
    }
    return json_object
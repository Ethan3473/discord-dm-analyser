import json

def load_json(file_path):
    """" Loads JSON data from a file. """

    with open(file_path, 'r', encoding = "utf-8") as file:
        raw_data = json.load(file)

    data = raw_data.get("messages")

    return data


def extract_processing_info(data, limit = -1):
    """ Extracts relevant information from the data and saves it to a new JSON file. """

    processed_data = []
    counter = 0

    for entry in data:
        if limit != -1 and counter >= limit:
            break

        if entry.get("content") != "":
            processed_data.append({
                "sender": (entry.get("author")).get("nickname"),
                "timestamp": entry.get("timestamp"),
                "message": entry.get("content")
            })
            counter += 1
    
    return processed_data



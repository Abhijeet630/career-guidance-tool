import json

def load_career_data(filepath='careers.json'):
    with open(filepath, 'r') as file:
        careers = json.load(file)
    return careers

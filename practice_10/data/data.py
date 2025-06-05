import json

def get_data(file_path):
    with open(file_path, 'r+') as f:
        content = json.load(f)
    return content 

def load_data(data, file_path):
    with open(file_path, 'r+') as f:
        content = json.dump(data, f)


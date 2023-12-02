import os

def filepath(file_name: str):
    current_path = os.path.dirname(__file__)
    return f'{current_path}/inputs/{file_name}'

    
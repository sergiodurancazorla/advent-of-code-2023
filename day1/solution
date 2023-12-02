import os

def calculate_number(string : str)-> int:
    string_reversed = string[::-1]
    
    first_number = _extract_number(string)
    last_number = _extract_number(string_reversed)
    
    number = int(first_number + last_number)
    return number

def _extract_number(string: str):
    for char in string:
        if char.isdigit():
            last_number = char
            break
    return last_number
    
def calibrate_trebuchet(file_name):
    current_path = os.path.dirname(__file__)
    file_path = f'{current_path}/{file_name}'
    
    result = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            result += calculate_number(line)
    
    return result
    

print(calibrate_trebuchet('input1.txt'))

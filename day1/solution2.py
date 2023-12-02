import os
from string import digits

RESULT = '52840'

NUMBERS_MAPPING = {'one': '1',
                   'two': '2', 
                   'three': '3', 
                   'four': '4', 
                   'five': '5', 
                   'six': '6', 
                   'seven': '7', 
                   'eight': '8', 
                   'nine': '9'}
    
def calibrate_trebuchet(file_name):
    current_path = os.path.dirname(__file__)
    file_path = f'{current_path}/{file_name}'

    result = 0
    with open(file_path, 'r', encoding='utf-8') as file:        
        lines = file.read().splitlines()
        for line in lines:
            numbers = []
            calculate_numbers(line, numbers)
            calculate_text_numbers(line, numbers)

            numbers.sort()
            
            result += int(f"{numbers[0][1]}{numbers[-1][1]}")

    return result

def calculate_text_numbers(line: str, numbers: list):
    for key, value in NUMBERS_MAPPING.items():
        match = line.find(key)
        if match != -1:
            numbers.append((match, value))
            
        match = line.rfind(key)
        if match != -1:
            numbers.append((match, value))

def calculate_numbers(line: str, numbers: list):
    for value in digits:
        match = line.find(value)
        if match != -1:
            numbers.append((match, value))
        match = line.rfind(value)
        if match != -1:
            numbers.append((match, value))


print(calibrate_trebuchet('input.txt'))

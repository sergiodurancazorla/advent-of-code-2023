import os
import re

def calculate_number(string : str)-> int:    
    numbers = ''.join(re.findall(r'\d', string))
    return int(numbers[0] + numbers[-1])

    
def calibrate_trebuchet(file_name):
    current_path = os.path.dirname(__file__)
    file_path = f'{current_path}/{file_name}'
    
    result = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            result += calculate_number(line)
    
    return result
    

print(calibrate_trebuchet('input.txt'))

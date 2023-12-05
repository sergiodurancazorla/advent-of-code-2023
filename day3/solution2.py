from utils import filepath
from typing import List
from functools import reduce
from operator import mul

ALL_DIRECTIONS = [
    (-1, -1),  # Top-left
    (-1, 0),  # Up
    (-1, 1),  # Top-right
    (0, -1),  # Left
    (0, 1),   # Right
    (1, -1),  # Bottom-left
    (1, 0),   # Down
    (1, 1)    # Bottom-right
]

GEAR_RATIO = '*'


def is_valid_symbol(char):
    return not (char == '.' or char.isdigit())


def search_in_all_directions(line, index, special_chars):
    for dx, dy in ALL_DIRECTIONS:
        if f'{line+dx}-{index+dy}' in special_chars:
            return True, f'{line+dx}-{index+dy}'
    return False, ''


def calculate_adjacents(matrix: List[List]):
    special_chars_index = []
    numbers_to_check = []  # file - number - index
    for line, line_value in enumerate(matrix):
        temp_number = ''
        index_temp_number = []
        for column, column_value in enumerate(line_value):
            if is_valid_symbol(column_value) and column_value == GEAR_RATIO:
                special_chars_index.append(f'{line}-{column}')
            if column_value.isdigit():
                temp_number += column_value
                index_temp_number.append(column)
            elif temp_number:
                numbers_to_check.append([line, temp_number, index_temp_number])
                temp_number = ''
                index_temp_number = []

            if temp_number and column == len(line_value)-1:
                numbers_to_check.append([line, temp_number, index_temp_number])
                temp_number = ''
                index_temp_number = []

    matches = {}
    for value in numbers_to_check:
        line = value[0]
        number = value[1]
        indexes = value[2]
        for index in indexes:
            to_append, match = search_in_all_directions(
                line, index, special_chars_index)
            if to_append:
                if matches.get(match):
                    matches[match].append(int(number))
                else:
                    matches[match] = [int(number)]
                break
    total_sum = 0
    for _, value in matches.items():
        if len(value) > 1:
            total_sum += reduce(mul, value)
    return total_sum


def locate_part(file_name):
    matrix = []
    with open(filepath.filepath(file_name), 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            matrix.append(list(line))

    return calculate_adjacents(matrix)


print(locate_part('input_day_3.txt'))

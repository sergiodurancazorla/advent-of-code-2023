from utils import filepath
from typing import List


def remove_emptys(numbers: List):
    return [number for number in numbers if number != ""]


def calculate_card_point(game: str):
    points = 0
    winning_numbers, numbers = game.split(':')[1].split('|')
    winning_numbers = winning_numbers.strip().split(' ')
    numbers = numbers.strip().split(' ')

    numbers = remove_emptys(numbers)
    winning_numbers = remove_emptys(winning_numbers)

    for number in numbers:
        if number in winning_numbers:
            points = points*2 if points else 1

    return points


def calculate_game_points(file_name):
    total_points = 0
    with open(filepath.filepath(file_name), 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            total_points += calculate_card_point(line)

    return total_points


print(calculate_game_points('input_day_4.txt'))

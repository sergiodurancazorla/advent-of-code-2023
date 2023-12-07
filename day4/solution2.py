from utils import filepath
from typing import List
import re


def remove_emptys(numbers: List):
    return [number for number in numbers if number != ""]


def calculate_card_point(card_number, game: str, scratchcards: dict):
    points = 0
    winning_numbers, numbers = game.split(':')[1].split('|')
    winning_numbers = winning_numbers.strip().split(' ')
    numbers = numbers.strip().split(' ')

    numbers = remove_emptys(numbers)
    winning_numbers = remove_emptys(winning_numbers)

    iterations = scratchcards.get(card_number)

    for number in numbers:
        if number in winning_numbers:
            points += 1

    if points:
        for index in range(points):
            index += 1
            if scratchcards.get(card_number+index):
                scratchcards[card_number+index] += iterations


def calculate_game_points(file_name):

    with open(filepath.filepath(file_name), 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        scratchcards = {index + 1: 1 for index in range(len(lines))}
        for line in lines:
            card_number = int(''.join(re.findall(r'\d', line.split(':')[0])))
            calculate_card_point(card_number, line, scratchcards)

    return sum(scratchcards.values())


print(calculate_game_points('input_day_4.txt'))

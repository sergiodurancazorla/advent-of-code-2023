
import re

from functools import reduce
from operator import mul
from utils import filepath


def _clean_game_line(game_line: str) -> list:
    game_line = game_line.split(':')
    game_line_list = game_line[1].split(';')

    return game_line_list


def biggest_color(color_dict: dict, to_check: dict):
    for color, value in color_dict.items():
        if value < to_check.get(color):
            color_dict[color] = to_check.get(color)


def check_game(game_line: str):
    game_line_list = _clean_game_line(game_line)
    final_colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in game_line_list:
        round_colors = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        values = round.split(',')
        for value in values:
            number = int(''.join(re.findall(r'\d', value)))
            value = ''.join(re.findall(r'[a-z]', value))
            round_colors[value] += number
        biggest_color(final_colors, round_colors)

    return reduce(mul, final_colors.values())


def calculate_games(file_name):
    result = 0

    with open(filepath.filepath(file_name), 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            result += check_game(line)

    return result


print(calculate_games('input_day_2.txt'))

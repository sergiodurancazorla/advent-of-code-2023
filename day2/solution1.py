
from utils import filepath
import re

MAX_VALUES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def _clean_game_line(game_line: str) -> tuple[list, int]:
    game_line = game_line.split(':')
    game_line_list = game_line[1].split(';')
    game_number = int(''.join(re.findall(r'\d', game_line[0])))

    return game_line_list, game_number


def possible_game(result: dict):
    for color, value in result.items():
        if value > MAX_VALUES.get(color):
            return False
    return True


def check_game(game_line: str):
    game_line_list, game_number = _clean_game_line(game_line)

    for round in game_line_list:
        colors = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        values = round.split(',')
        for value in values:
            number = int(''.join(re.findall(r'\d', value)))
            value = ''.join(re.findall(r'[a-z]', value))
            colors[value] += number

        if not possible_game(colors):
            return 0

    return game_number


def calculate_games(file_name):
    result = 0

    with open(filepath.filepath(file_name), 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        for line in lines:
            result += check_game(line)

    return result


print(calculate_games('input_day_2.txt'))

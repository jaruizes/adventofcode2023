import re


#
# NUMBERS = {
#     'zero': '0',
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9'
# }
#
#
# def find_digit(current_character: str, characters_read: str, include_words: bool) -> str:
#     if current_character.isdigit():
#         return current_character
#
#     if include_words:
#         text = characters_read.lower() + current_character.lower()
#         matches = re.findall('zero|one|two|three|four|five|six|seven|eight|nine', text)
#         if matches:
#             return NUMBERS[matches[0]]
#
#     return ""
#
#
# def combine_first_and_last_digits(line: str, include_words: bool) -> int:
#     digits_found = []
#     characters_read = ""
#     for current_character in line.strip():
#         digit_found = find_digit(current_character, characters_read, include_words)
#
#         if digit_found:
#             digits_found.append(digit_found)
#             characters_read = current_character
#         else:
#             characters_read += current_character
#
#     if len(digits_found) > 0:
#         return int(digits_found[0] + digits_found[-1])
#
#     return 0
from typing import Tuple


def get_game_id(record: str) -> int:
    match = re.match(r"Game (\d+):", record)
    if match:
        return int(match.group(1))
    else:
        return None


def is_valid_game(game: str) -> bool:
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    color_values = [0, 0, 0]
    for amount, color in re.findall(r"(\d+) (blue|red|green)", game):
        if color == "blue" and int(amount) > 14:
            return False
        elif color == "red" and int(amount) > 12:
            return False
        elif color == "green" and int(amount) > 13:
            return False

    return True


def check_record_part_1(record: str) -> int:
    game_id = get_game_id(record)
    if game_id:
        games_info = record.split(":")[1] ## 1 blue, 2 green

        for game in games_info.split(";"):
            if not is_valid_game(game):
                return 0

        return game_id


def check_record_part_2(record: str) -> int:
    game_id = get_game_id(record)
    if game_id:
        games_info = record.split(":")[1] ## 1 blue, 2 green
        color_values = [0, 0, 0]
        for game in games_info.split(";"):
            for amount, color in re.findall(r"(\d+) (blue|red|green)", game):
                if color == "blue" and int(amount) > color_values[0]:
                    color_values[0] = int(amount)
                elif color == "red" and int(amount) > color_values[1]:
                    color_values[1] = int(amount)
                elif color == "green" and int(amount) > color_values[2]:
                    color_values[2] = int(amount)

        return color_values[0] * color_values[1] * color_values[2]


def read_record_games(records_file: str) -> tuple[int, int]:
    records = [line.strip() for line in open(records_file, "r", encoding="utf-8")]
    total1 = 0
    total2 = 0
    for record in records:
        total1 += check_record_part_1(record)
        total2 += check_record_part_2(record)

    return total1, total2


## Asserts
#assert read_record_games("../../inputs/example.txt")[0] == 8
total_example1, total_example2 = read_record_games("../../inputs/example.txt")
assert total_example1 == 8
assert total_example2 == 2286

total_input1, total_input2 = read_record_games("../../inputs/input.txt")
print("- Part one: " + str(total_input1))
print("- Part two: " + str(total_input2))

# print("- Part two (with letters): " + str(read_calibration_document("../../inputs/input.txt", True)))

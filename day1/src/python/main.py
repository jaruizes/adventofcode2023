import re

NUMBERS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def find_digit(current_character: str, characters_read: str, include_words: bool) -> str:
    if current_character.isdigit():
        return current_character

    if include_words:
        text = characters_read.lower() + current_character.lower()
        matches = re.findall('zero|one|two|three|four|five|six|seven|eight|nine', text)
        if matches:
            return NUMBERS[matches[0]]

    return ""


def combine_first_and_last_digits(line: str, include_words: bool) -> int:
    digits_found = []
    characters_read = ""
    for current_character in line.strip():
        digit_found = find_digit(current_character, characters_read, include_words)

        if digit_found:
            digits_found.append(digit_found)
            characters_read = current_character
        else:
            characters_read += current_character

    if len(digits_found) > 0:
        return int(digits_found[0] + digits_found[-1])

    return 0


def read_calibration_document(calibration_file: str, include_words: bool) -> int:
    total = 0
    calibration_lines = [line.strip() for line in open(calibration_file, "r", encoding="utf-8")]
    for calibration_line in calibration_lines:
        total += combine_first_and_last_digits(calibration_line, include_words)

    return total


## Asserts
assert read_calibration_document("../../inputs/example.txt", False) == 142
assert read_calibration_document("../../inputs/example2.txt", True) == 281

print("- Part one: " + str(read_calibration_document("../../inputs/input.txt", False)))
print("- Part two (with letters): " + str(read_calibration_document("../../inputs/input.txt", True)))

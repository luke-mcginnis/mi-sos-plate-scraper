import itertools
import string
import re
from pathlib import Path

substitutions = {'A': ['4'],
                 'B': ['8'],
                 'E': ['3'],
                 'G': ['6'],
                 'I': ['1'],
                 'S': ['5'],
                 'Z': ['2']
                 }

input_words_path = Path('output/syllable_combinations_words.txt')
output_path = Path('output/character_subsitutions_words.txt')


def substitutions_from_word(word: str) -> list[str]:
    word = word.upper()
    combinations = []
    for char in word:
        character_alternatives = [char]
        character_alternatives.extend(substitutions.get(char, list()))
        combinations.append(character_alternatives)
    return [''.join(word) for word in itertools.product(*combinations)]


def validate_license_plate(text: str) -> bool:
    regex = (r'.*\w{2}\d{2}\w|'  # Two letters followed by two numbers and one letter is not allowed
             r'.*O')  # 'O' is not allowed
    if re.match(regex, text):
        return False
    return True


def main():
    with open(input_words_path) as f:
        input_words = f.read().splitlines()

    output_words = []
    for word in input_words:
        output_words.extend([substitution for substitution in substitutions_from_word(word)
                             if validate_license_plate(substitution)])

    output_words.sort(key=lambda s: sum([s.count(digit) for digit in string.digits]))

    print(output_words)

    with open(output_path, 'w') as f:
        f.write('\n'.join(output_words))
    print(f'Wrote to "{output_path}"')


if __name__ == '__main__':
    main()

from pathlib import Path
import itertools

first_syllable_path = Path('input/first_syllable.txt')
second_syllable_path = Path('input/second_syllable.txt')

output_path = Path('output/syllable_combinations_words.txt')

with open(first_syllable_path) as f:
    first_syllables = f.read().splitlines()

with open(second_syllable_path) as f:
    second_syllables = f.read().splitlines()

sassy_words = [''.join(word) for word in itertools.product(first_syllables, second_syllables)]

print(sassy_words)

with open(output_path, 'w') as f:
    f.write('\n'.join(sassy_words))
    print(f'Wrote to: "{output_path}"')

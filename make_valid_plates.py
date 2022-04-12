from pathlib import Path
import json

responses_path = Path('output/webscraper_responses.json')
output_path = Path('output/avaliable_plates.txt')

with open(responses_path, 'r') as f:
    responses = json.load(f)

avaliable_plates = [plate for plate, status in responses.items()
                    if status == 'This plate number is currently available']

with open(output_path, 'w') as f:
    f.write('\n'.join(avaliable_plates))
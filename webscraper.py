import selenium.common.exceptions
from selenium import webdriver
from pathlib import Path
import time
import json

license_plates_path = Path('output/character_subsitutions_words.txt')
json_output_path = Path('output/webscraper_responses.json')


browser = webdriver.Chrome(Path('chromedriver.exe'))
browser.get('https://dsvsesvc.sos.state.mi.us/TAP/_/#13')


# Setup:

time.sleep(2)
check_plate_availability = browser.find_element_by_xpath('//*[@id="l_Df-9-13"]/span/span[2]')

check_plate_availability.click()

while True:
    if elements := browser.find_elements_by_xpath('//*[@id="Dc-b"]/span/span'):
        elements[0].click()
        break

time.sleep(1)

not_motorcycle = browser.find_element_by_xpath('//*[@id="Dn-b"]/div/label[2]/span')
not_motorcycle.click()

not_disability = browser.find_element_by_xpath('//*[@id="Dn-c"]/div/label[2]/span')
not_disability.click()

next_page = browser.find_element_by_xpath('//*[@id="action_7"]')
next_page.click()
time.sleep(1)

standard_plate = browser.find_element_by_xpath('//*[@id="Dp-g-2"]')
standard_plate.click()

next_page = browser.find_element_by_xpath('//*[@id="action_7"]')
next_page.click()
time.sleep(1)

white_plate = browser.find_element_by_xpath('//*[@id="Dq-g-2"]')
white_plate.click()


while True:
    try:
        next_page = browser.find_element_by_xpath(
                '/html/body/div[2]/div/div[1]/div/div/main/div/div/div[2]/button[3]/span/span')
        next_page.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        time.sleep(1)
        continue
    else:
        break

time.sleep(1)


# Tests:

with open(license_plates_path) as f:
    license_plates = f.read().splitlines()

with open(json_output_path, 'r') as f:
    responses = json.load(f)

for license_plate in license_plates:
    if license_plate in responses:
        continue

    search_box = browser.find_element_by_xpath('//*[@id="Dr-j"]')
    print(f'\n Testing plate "{license_plate}"...')
    search_box.send_keys(license_plate)

    enter_button = browser.find_element_by_xpath('//*[@id="Dr-k"]/span/span')
    enter_button.location_once_scrolled_into_view
    enter_button.click()

    time.sleep(1)
    result = browser.find_element_by_xpath('//*[@id="caption2_Dr-p"]/span[2]')
    responses.update({license_plate: result.text})
    print(result.text)

    try:
        ok_button = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/button')
    except selenium.common.exceptions.NoSuchElementException:
        pass
    else:
        ok_button.click()

    time.sleep(1)
    submit_again = browser.find_element_by_xpath('//*[@id="Dr-l"]/span/span')
    submit_again.click()
    time.sleep(1)

    with open('output/webscraper_responses.json', 'w') as f:
        json.dump(responses, f, indent=4)


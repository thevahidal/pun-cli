import random
import requests

PUN_REPOSITORY = 'https://raw.githubusercontent.com/thevahidal/pun-cli/main/pun_repository.txt'

def get_puns():
    try:
        response = requests.get(PUN_REPOSITORY)
        puns = response.text.split('\n')
        puns = [pun.strip() for pun in puns if pun.strip() != '']
        return puns
    except requests.exceptions.RequestException as e:
        print('Error fetching puns:', e)
        return []

def generate_pun(keyword: str):
    puns = get_puns()
    if len(puns) == 0:
        print('No puns found in repository.')
        return ''

    if keyword:
        puns = [pun for pun in puns if keyword in pun]
        if len(puns) == 0:
            print('No puns found for keyword:', keyword)
            return ''

    return random.choice(puns)

import random
import argparse
import requests
import cowsay

PUN_REPOSITORY = 'https://raw.githubusercontent.com/thevahidal/pun-cli/main/pun_repository.txt'
VERSION = 'v' + '0.1.2'

def get_puns():
    try:
        response = requests.get(PUN_REPOSITORY)
        puns = response.text.split('\n')
        puns = [pun.strip() for pun in puns if pun.strip() != '']
        return puns
    except requests.exceptions.RequestException as e:
        print('Error fetching puns:', e)
        return []

def generate_pun(keyword):
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

def main():
    parser = argparse.ArgumentParser(description='Unleash hilarious wordplay with a single command.')
    parser.add_argument('--keyword', '-k', help='Keyword to search for puns.')
    parser.add_argument('--character', '-c', help='Character to use for the pun. One of: ' + ', '.join(cowsay.char_names))
    parser.add_argument('--add', '-a', help='Add a pun to the repository.', action='store_true')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + VERSION, help='Print version and exit.')

    args = parser.parse_args()

    if args.add:
        print("Thanks for your contribution!")
        print("Please create a pull request to add your pun to the repository.")
        print("https://github.com/thevahidal/pun-cli")

    else:
      pun = generate_pun(args.keyword)
      if args.character and args.character in cowsay.char_names:
          character = args.character
      else:
        character = random.choice(cowsay.char_names)

      print(cowsay.get_output_string(character, pun))


if __name__ == '__main__':
    main()

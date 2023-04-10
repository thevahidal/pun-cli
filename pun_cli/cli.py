import argparse
import cowsay
import random
from pun_cli.pun_generator import generate_pun

VERSION = 'v' + '0.1.4'

def cli():
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

# Pun CLI

`pun-cli` is a Python-based command-line tool that generates a random pun based on a given keyword.


## Installation

You can install pun-cli via pip:

```bash
pip install pun-cli
```

## Usage
```bash
pun-cli [-h] [--keyword KEYWORD] [--version] [--add]

Optional Arguments

  --keyword (-k): A keyword to search for puns. By default, pun-cli generates a random pun.
  --version (-v): Show the version number and exit.
  --add (-a): Add a pun to the repository.
```

## Examples
```bash
$ pun-cli
  _________________________________________________
 /                                                 \
| Why did the chicken cross the road? To get to the |
|  other side.                                      |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                              _------~~-,
                                                           ,'            ,
                                                           /               \\
                                                          /                :
                                                         |                  '
                                                         |                  |
                                                         |                  |
                                                          |   _--           |
                                                          _| =-.     .-.   ||
                                                          o|/o/       _.   |
                                                          /  ~          \\ |
                                                        (____\@)  ___~    |
                                                           |_===~~~.`    |
                                                        _______.--~     |
                                                        \\________       |
                                                                 \\      |
                                                               __/-___-- -__
                                                              /            _ \\

$ pun-cli -k restaurant  
  _________________________________________________
 /                                                 \
| The man who invented auto-correct has died. Resta |
| urant in peace.                                   |
 \                                                 /
  =================================================
                                                 \
                                                  \
                                                   \
                                                    \
                                                              ,.
                                                             (_|,.
                                                             ,' /, )_______   _
                                                         __j o``-'        `.'-)'
                                                         (")                 \'
                                                         `-j                |
                                                           `-._(           /
                                                              |_\  |--^.  /
                                                             /_]'|_| /_)_/
                                                                 /_]'  /_]'

$ pun-cli -c cow
  _________________________________________________
 /                                                 \
| Why do melons have weddings? Because they cantalo |
| upe.                                              |
 \                                                 /
  =================================================
                                                 \
                                                  \
                                                    ^__^
                                                    (oo)\_______
                                                    (__)\       )\/\
                                                        ||----w |
                                                        ||     ||

```

## Adding a Pun

To add a pun to the repository, follow these steps:

1. Fork the [pun-cli repository](https://github.com/thevahidal/pun-cli).
2. Clone your fork to your local machine.
3. Add your pun to pun_repository.txt file.
4. Commit your changes and push to your fork.
5. Create a pull request to merge your changes into the main pun-cli repository.

## Contributing

If you'd like to contribute to `pun-cli`, please open an issue or a pull request on the GitHub repository.

## License

`pun-cli` is licensed under the MIT License.

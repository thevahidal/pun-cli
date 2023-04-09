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
Why was the math book sad? Because it had too many problems.

$ pun-cli -k cheese
I’m reading a book about anti-gravity. It’s impossible to put down.
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

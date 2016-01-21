# KeePass/MacPass XML to 1Password CSV converter

Migrate your KeePass(X)/MacPass data to 1Password 6: Export your KeePass(X)/MacPass data to XML,
use this script to convert it to a CSV, and then import the CSV into
1Password 6.

## Prerequisites

Install dependencies:

- `pip install -r requirements.txt`

## Usage

- Export your KeePassX/MacPass passwords to `./input/passwords.xml`.
- Run `keepass or macpass script`.
- Open *1Password* and go to *File > Import > Comma Delimited Text (.csv)* and
  pick `./output/passwords.csv`.
- Enjoy!

## Documentation

- [1Password 6.x CSV Documentation](https://learn2.agilebits.com/1Password4/Mac/en/KB/import.html#csv--comma-separated-values)

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

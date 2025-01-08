# gdrive

A command line tool for interacting with Google Drive.

## Installation

### Install asdf

https://asdf-vm.com/guide/getting-started.html#getting-started

#### Install asdf python plugin

```bash
asdf plugin-add python
```

install poetry asdf plugin

```bash
asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
```

#### Install python & poetry

```bash
asdf install
```

### Install dependencies

```bash
poetry install
```

## Usage

### start poetry shell

```bash
poetry shell
```

### run command

NOTE: you need the credentials.json file before running commands

```bash
python gdrive.py list-files 

# define fields
python gdrive.py list-files --fields='files(id,name)' --page-size=10

# with query

python gdrive.py list-files --q "name CONTAINS 'Ruvixx'"
python gdrive.py list-files --q "name = 'Ruvixx File'"
```


### Google Drive API docs

https://developers.google.com/drive/api/guides/about-files

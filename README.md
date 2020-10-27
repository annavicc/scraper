# Web Crawler

## Requirements:
* Python3
* Virtualenv

## Installing requirements
```bash
sudo apt install virtualenv
sudo apt install python3
```

## Installing virtual enviroment
```bash
python -m venv kolonial-env
```

## Initializing virtual enviroment (before every run)
```bash
source kolonial-env/bin/activate
```

## Preparing the environment (install requirements using pip)
```bash
# install requirements
make install
```

## Running the application
```bash
make run
```

## All make commands:

```bash
make help

Usage: make <command>

options:
	help                 List all available commands
	install              Install all requirements
	run                  Run aplication
```

## Results:
Results are stored in /results/products-{{today's date}}.csv

.PHONY: dev build upgrade push

include .env
export $(shell sed 's/=.*//' .env)
PYTHON=./venv/Scripts/python.exe

dev:
	${PYTHON} start_dev_server.py --dev

build:
	${PYTHON} start_dev_server.py --build

upgrade:
	choco upgrade hugo-extended -confirm

push:
	git add .
	git commit -a -m "change"
	git push

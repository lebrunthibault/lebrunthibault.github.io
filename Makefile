.PHONY: dev build algolia upgrade push

include .env
export $(shell sed 's/=.*//' .env)
PYTHON=./venv/Scripts/python.exe

dev:
	${PYTHON} start_dev_server.py --dev

build:
	${PYTHON} start_dev_server.py --build

algolia:
	${PYTHON} algolia/index_documents.py

upgrade:
	choco upgrade hugo-extended -confirm

push:
	git add .
	git commit -a -m "change"
	git push

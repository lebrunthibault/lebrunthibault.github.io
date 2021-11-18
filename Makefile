.PHONY: dev build algolia

include .env
export $(shell sed 's/=.*//' .env)
PYTHON=./venv/Scripts/python.exe

dev:
	${PYTHON} start_dev_server.py --dev --no-watch

build:
	${PYTHON} start_dev_server.py --build

algolia:
	${PYTHON} algolia/index_documents.py


push:
	git add .
	git commit -a -m "change"
	git push

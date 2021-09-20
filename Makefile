.PHONY: dev build algolia

include .env
export $(shell sed 's/=.*//' .env)

dev:
	${PYTHON} start_dev_server.py dev

build:
	${PYTHON} start_dev_server.py build

algolia:
	${PYTHON} algolia/index_documents.py


push:
	git add .
	git commit -a -m "change"
	git push

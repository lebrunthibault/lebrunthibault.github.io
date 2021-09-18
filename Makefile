.PHONY: dev build algolia

dev:
	venv/Scripts/python start_dev_server.py dev

build:
	venv/Scripts/python start_dev_server.py build

algolia:
	venv/Scripts/python algolia/index_documents.py


push:
	git add .
	git commit -a -m "change"
	git push

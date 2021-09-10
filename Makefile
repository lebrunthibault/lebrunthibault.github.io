.PHONY: dev build algolia

dev:
	python start_dev_server.py dev

build:
	python start_dev_server.py build

algolia:
	python algolia/index_documents.py


push:
	git add .
	git commit -a -m "change"
	git push

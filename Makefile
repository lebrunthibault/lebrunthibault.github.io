.PHONY: dev build algolia

dev:
	make algolia
	python start_dev_server.py dev

build:
	python start_dev_server.py build

algolia:
	python algolia/index_documents.py


push:
	git commit -a -m "change"
	git push

.PHONY: dev build algolia

dev:
	cls
	make algolia
	py start_dev_server.py dev

build:
	cls
	py start_dev_server.py build

algolia:
	cls
	py algolia/index_documents.py



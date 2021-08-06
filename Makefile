.PHONY: dev build algolia algolia_settings

dev:
	cls
	py build_algolia.py
	py start_dev_server.py dev

build:
	cls
	py start_dev_server.py build

algolia:
	cls
	py algolia/index_documents.py

algolia_settings:
	cls
	py build_algolia.py


.PHONY: dev build

dev:
	cls
	py build_algolia.py
	py start_dev_server.py dev

build:
	cls
	py start_dev_server.py build

algolia:
	cls
	py build_algolia.py


.PHONY: dev build

dev:
	cls
	python start_dev_server.py dev

build:
	cls
	python start_dev_server.py build


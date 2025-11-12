.PHONY: dev build update-theme

dev:
	hugo server -D

build:
	hugo -D

update-theme:
	cd themes/even && git pull origin master

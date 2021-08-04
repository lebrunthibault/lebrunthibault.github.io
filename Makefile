.PHONY: dev build

dev:
	cls
	hugo server -D
	#cd public; python -m http.server 8000

build:
	cls
	hugo

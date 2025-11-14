.PHONY: dev build css

dev:
	hugo server -D

css:
	npx tailwindcss -i ./assets/css/main.css -o ./assets/css/output.css --watch

build:
	hugo -D

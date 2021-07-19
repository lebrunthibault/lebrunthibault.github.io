.PHONY: dev build

dev:
	cls
	hugo server -D
	#cd public; python -m http.server 8000

build:
	cls
	sass source/stylesheets/index.scss build/stylesheets/index.css
	#hugo -D

none:
  echo ""


python:
  python2 main.py

docker: run
  echo Finished

run: build
	docker run dockp
build:
	docker build -t dockp .
	clear

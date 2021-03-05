build:
	docker build -t routes_finder .

run:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder 

test:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m tests

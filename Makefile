build:
	docker build -t routes_finder .
	mkdir -p tests/output

help:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m routes_finder -h

run:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m routes_finder --input=tests/input/input1.txt --output=tests/output/output1.txt
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m routes_finder --input=tests/input/input2.txt --output=tests/output/output2.txt
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m routes_finder --input=tests/input/input3.txt --output=tests/output/output3.txt
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m routes_finder --input=tests/input/input4.txt --output=tests/output/output4.txt

test:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder python -m tests

coverage:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder coverage run -m tests	

coverage-report:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder coverage report

coverage-html:
	docker run -it --rm --name routes_finder -v ${PWD}:/usr/src/app -w /usr/src/app routes_finder coverage html
	wslview htmlcov/index.html
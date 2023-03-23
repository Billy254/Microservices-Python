install:
	# install commands
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	# format code
	black *.py mylib/*.py
lint:
	#pylint 
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib test_logic.py
build:
	# build container
	docker build -t deploy-fastapi .
run:
	# run docker image
	docker run -p 127.0.0.1:8080:8080 f33d188e0461
deploy:
	#deploy
all: install lint test deploy
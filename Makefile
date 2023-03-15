install:
	pip install -r requirements.txt

format:
	# format code

lint:
	#pylint 

test:
	#test

deploy:
	#deploy
all: install lint test deploy
install:
	python -m pip install --upgrade pip && python -m pip install -r requirements.txt

test:
	python -m pytest -vv test_my_code.py

format:
	python -m black *.py

lint:
	python -m pylint --disable=R,C my_code.py

all: install lint test
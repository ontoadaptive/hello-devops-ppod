.PHONY: env help all install clean clean-pyc clean-pyo
SRC_ROOT=src
SRC= $(SRC_ROOT)/leet/problem9/solution.py \
	$(SRC_ROOT)/gs2/problem1/solution.py
PYTHONPATH=$(SRC_ROOT)
TEST_ROOT=tests

help:
	@echo "make env"
	@echo "make install"
	@echo ""
	@echo "make build"
	@echo ""
	@echo "make lint"
	@echo "make format"
	@echo ""
	@echo "make run"
	@echo ""
	@echo "make test"

env:
	pipenv shell

install:
	pipenv install -r requirements.txt

build: clean
	pipenv install -e $(SRC_ROOT)

clean-pyc:
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean: clean-pyc clean-build

lint:
	flake8 $(SRC)

format:
	black $(SRC)

test: clean build
	@echo $(PYTHONPATH); pytest	

run: run_leet_prob9 run_gs2_prob1

run_leet_prob9:
	python $(TEST_ROOT)/leet/problem9/solution.py

run_gs2_prob1:
	python $(TEST_ROOT)/gs2/problem1/solution.py
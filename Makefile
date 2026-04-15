
ROOT=$(shell pwd)
SRC=$(ROOT)/uranus
MAIN=$(ROOT)/uranus/main.py

all:
	python3 $(MAIN)

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
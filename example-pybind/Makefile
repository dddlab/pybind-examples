CC=g++
CFLAGS=-Wall

default:
	python setup.py build_ext -i
	python test_funcs.py

clean:
	python setup.py clean --all
	rm -f *.so

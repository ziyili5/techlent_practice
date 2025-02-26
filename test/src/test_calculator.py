import sys
import os

# Add the absolute path of the parent directory to sys.path
sys.path.insert(0, "/Users/aaronli/Documents/Others/Machine_learning_bootcamp/python_practice")

from app.src.calculate import Calculator

cal = Calculator()


def test_add():
	assert cal.add(1,1)==2
	assert cal.add(1,2,)==3


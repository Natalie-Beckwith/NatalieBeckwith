import sys
sys.path.insert(1, 'week2')

import pytest
from factorial import factorial
from factors2 import factors2

f = factorial()

def test_factorial_1():
  assert f(1) is 1

def test_factorial_2():
  assert f(2) == 2

def test_factorial_0():
  assert f(0) == 1

def test_factorial_not_0():
  assert f(0) != 0

def test_factorial_4():
  assert f(4) == 24
  
def test_factorial_5():
  r = f(5)
  assert r == 120

  def test_factorial_7():
    r = f(7)
    assert r == 5080
  
factorsObj = factors2()

def test_factors_0():
  assert factorsObj(0) == []
  
def test_factors_1():
  assert factorsObj(1) == [1]
  
def test_factors_6():
  assert factorsObj(6) == [1, 2, 3, 6]

def test_factors_16():
  assert factorsObj(16) == [1, 2, 4, 8, 16]

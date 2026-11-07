import pytest
from min_stack import Stack

def test_get_min_single_element(capsys):
    s = Stack()
    s.push(42)
    s.push(0)
    assert s.get_min() == "42"

def test_push_top():
    s = Stack()
    s.push(5)
    s.push(67)
    assert s.top() == 67

def test_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_get_min_empty():
    with pytest.raises(IndexError):
        Stack().get_min()


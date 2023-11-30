import pytest 
from directory import Directory

@pytest.fixture
def directory():
    dir = Directory('test')
    return dir

@pytest.fixture
def directory_with_children():
    dir = Directory('/')

    child = Directory('test')
    child1 = Directory('test1')
    dir.add_directory(child)
    dir.add_directory(child1)

    grandChild = Directory('test-child')
    child.add_directory(grandChild)
    return dir
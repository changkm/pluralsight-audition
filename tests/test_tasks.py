from unittest.mock import MagicMock, patch, mock_open
import pytest
from src import solution
from .utils import get_calls, get_assignments, sublist_contains


@pytest.mark.task1
def test_function_defined():
    """Test if a function called `get_stock_price()` is defined."""
    assert 'get_stock_price' in dir(solution), (
        'Make sure to define the function called get_stock_price.\n')  


@pytest.mark.task1
def test_function_one_arg():
    """Test if get_stock_price takes one argument, `name`."""
    # If function does not accept 'name' arg, will raise TypeError
    solution.get_stock_price(name='test')


@pytest.mark.task2
def test_import_beautiful_soup():
    message = 'Have you imported the BeautifulSoup class from the bs4 library?\nHint: from bs4 import BeautifulSoup'
    assert 'BeautifulSoup' in dir(solution), message


@pytest.mark.task3
def test_open_file():
    """Test that open('data/stocks.html') is called."""
    calls = get_calls(solution.get_stock_price)
    message = 'Make sure to call the `open` function, and that you open the file `data/stocks.html`'
    assert 'open:data/stocks.html' in calls, message


@pytest.mark.task4
def test_beautiful_soup_object():
    """Test that a BeautifulSoup object called `doc` is created."""
    assignments = get_assignments(solution.get_stock_price)
    message = 'Did you initialize a BeautifulSoup object, assign it to a variable `doc`, and the file object?'
    assert 'doc:BeautifulSoup:f:html.parser' in assignments, message

@pytest.mark.task5
def test_find_table():
    """Test that the document's table is assigned to the variable `price_table`"""
    assignments = get_assignments(solution.get_stock_price)
    message = 'Did you use find the table using doc.table and assign it to a variable called `price_table`?'
    assert 'price_table:doc:table' in assignments, message

@pytest.mark.task6
def test_find_td():
    """Test that we find the td w/ name."""
    assignments = get_assignments(solution.get_stock_price)
    message = 'Did you use price_table.find() to find the td that contains the string `name`?'
    assert 'td:price_table:find:td:string:name' in assignments, message

@pytest.mark.task7
def test_invalid_name():
    """Test that the function returns `None` if a name is given that is not in the page."""
    message = 'Did you check whether `td is None` and, if so, return -1?'
    assert solution.get_stock_price('ThisNameDoesNotExist') == -1, message

@pytest.mark.task8
def test_find_parent():
    """Test that the parent is found."""
    assignments = get_assignments(solution.get_stock_price)
    message = 'Did you use td.parent to find the parent?'
    assert 'parent:td:parent' in assignments, message

@pytest.mark.task9
def test_find_price_td():
    """Test that the price td is found."""
    assignments = get_assignments(solution.get_stock_price)
    message = 'Did you find the td with class="price" within the parent?'
    assert 'price_elt:parent:find:td:class_:price'in assignments, message

@pytest.mark.task10
def test_full_function():
    """Test that the correct price is returned."""
    message = 'Did you remember to return the value?'
    assert solution.get_stock_price('PS') == '19.83', message

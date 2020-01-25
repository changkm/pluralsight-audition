# Purpose of the project
This project is a step-by-step guide to the basic usage of Python's Beautiful Soup library. We will use this to find stock prices from a sample website.

# Setup

## Installation

In a terminal, navigate to the root folder of this project and create a Python3 virtual environment.
```
$ virtualenv -p python3 venv
```

Once that completes, enter your virtual environment.

Windows
```
$ venv\Scripts\activate.bat
```

macOS & Linux
```
$ source venv/bin/activate
```

Install the project's dependancies with the Python package manager, Pip.
```
$ pip install -r requirements.txt
```

## Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you a list of failing tests. This is good! Each of these tests corresponds to something we'll be working on in this project. By the end, all of the tests will pass.

```
$ pytest
```

If you'd like to only run the tests for your current task, you can run tests only associated with a certain task.

```
$ pytest -m task1
```

# Tasks

## Introduction
We will be using the Beautiful Soup library to find information about stock prices from a sample webpage, `data/stocks.html`.

## Task 1:
In the `src/solution.py` file, create a function called `get_stock_price()` that takes one argument, `name`.
For now, just put `pass` (Python's noop keyword) inside the function. This will allow the program to run without a syntax error.

## Task 2: 
We will be using the `BeautifulSoup` class from the Beautiful Soup library (`bs4`). Import this class at the top of your `src/solution.py` file.

## Task 3:
Load the file that contains the sample webpage (`data/stocks.html`) into your function. Name the file object `f`. Since we want to make sure to close the file when we're done with it, the easiest way is to use `open` as a context manager (also known as a `with` block) See https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files for more information.

## Task 4:
Create a BeautifulSoup object from the html doc. Name the variable `doc`. Initializing a BeautifulSoup object takes two arguments: the file and parser name. Use `'html.parser'` for the document name.
```
doc = BeautifulSoup([file name], 'html.parser')
```

## Task 5:
In our html document, the stock prices are all in a table. Find the table in the document using `doc.table`. Assign the table to the variable `price_table`.

## Task 6: 
In the table, we need to find the row that contains the stock we're looking for. We can do this by using beautiful soup's `find` method. `find` takes a tag type and an optional `string` method as its arguments.
```
find([tag], string=[string])
```
e.g.
```
price_table.find('th', string='Symbol')
```
returns the bs4 element
```
<th>Symbol</th>
```
Find the `<td>` that contains `name` and assign it to a variable called `td`.


## Task 7:
If there is nothing that matches in the document, `find` will return `None`.
Using an `if` statement, check to see whether `td` is `None` and if it is, have your function return -1.

## Task 8: Find the parent
The table row (`<tr>`) we are looking for is the parent of the td we found. Find the correct `<tr>` using the attribute `.parent` and assign it to a variable called `parent`.
Note: because `.parent` is an attribute (a value) instead of a method (a function), do not use parenthesis.

## Task 9: Find the price
This row has several `<td>`s, each with a different type of data, but fortunately each is identified with a class name. Use `find` again, with the optional argument `class_`, to find the `<td>` with `class_="price"` and assign to a variable called `price_elt`.

## Task 10: Return the price
Now, find the text inside the `<td>` with the `.string` attribute. Return this value!
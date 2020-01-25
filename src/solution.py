# Task 2:
# Import BeautifulSoup class from bs4 library.
from bs4 import BeautifulSoup

# Task 1:
# Create function called get_stock_price():
def get_stock_price(name):
    # Task 3: Open file
    with open('data/stocks.html') as f:
        # Task 4: Create Beautiful Soup
        doc = BeautifulSoup(f, 'html.parser')

    # Task 5: find table
    price_table = doc.table

    # Task 6: find correct td 
    td = price_table.find('td', string=name)

    # Task 7: Return None if not found
    if td is None:
        return -1

    # Task 8: Find the parent
    parent = td.parent

    # Task 9: Find the price
    price_elt = parent.find('td', class_="price")


    # Task 10: Return the price
    return price_elt.string

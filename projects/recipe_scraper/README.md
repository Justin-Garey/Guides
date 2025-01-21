# A Python Recipe Scraper

This is a fun little project for collecting recipes. It has only been tested with the one website that is hardcoded in the example and would need further validation and refactoring.

## Steps

1. To get the webpage of a recipe with a provided link
2. Scrape the ingredients and instructions from the recipe
3. Add the ingredients and instructions to a custom data structure and/or a database

## Building the App

### Getting the webpage

Pulling the contents of a webpage in Python is usually done with importing either `urllib.request` or `requests`. For this app, I'll be using `urllib.request`. The example recipe is of some chocolate chip cookies I often make. 

```python
from urllib.request import Request, urlopen

req = Request("https://www.noracooks.com/vegan-chocolate-chip-cookies/", headers={'User-Agent': 'Mozilla/5.0'})

print(urlopen(req).read())
```
- We start by importing the class and function we will need to pull the webpage content.
- Then we create an object of the `Request` class which contains the URL to the webpage and some headers to prevent a 403 error message. Scraping often comes across as a bot (obviously) or web crawler, so passing the headers tells the web server that we are a real client.
- Lastly, the webpage contents are printed out by reading the opened URL.

### Scraping the Ingredients and Instructions

This is the most complicated part of the application as it requires some regular expression usage and HTML parsing with beautiful soup. The process boils down to creating the regular expression, finding all occurrences of a match in the HTML, filtering it to find the one you are looking for, then extracting the list of ingredients or instructions.

The imports and setup includes a bit more than the simple request from before. 
```python
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import string

# This is a set of printable ascii characters to help filter 
# out non-ascii characters from the lists
printable = set(string.printable)

# Make a request to the recipe URL with a user-agent header 
# to avoid a 403 forbidden error
req = Request(
    "https://www.noracooks.com/vegan-chocolate-chip-cookies/",
    headers={"User-Agent": "Mozilla/5.0"},
)
contents = urlopen(req).read()

# Turn the HTML content into a BeautifulSoup object "soup"
soup = BeautifulSoup(contents, "html.parser")
```
- The `BeautifulSoup` import is the only new and required import, the other two, `re` and `string`, are used for convenience.
- The `string` import helps to create a set of printable characters. This is used later to filter out checkboxes or other characters we do not want from the ingredients and instructions lists.

To get the ingredients or instructions list, we match the text to our regular expression, filter out what we don't want, and get the individual list elements put into our own list.
```python
pattern = re.compile(r"Ingredients")
matches = soup.findAll(string=pattern)
matches = [
    match for match in matches if match.text.strip() in ["Ingredients", "ingredients"]
]
if len(matches) == 1:
    in_list = matches[0].find_next("ul")
    elems = in_list.find_all("li")
    elems = [
        "".join(filter(lambda c: c in printable, elem.text)).strip() for elem in elems
    ]
    print("Ingredients:")
    for elem in elems:
        print("    - " + elem)
```

### Storing the Recipe in an SQLite Database

SQLite is a great database for small applications such as this recipe scraper. It is faster and more efficient than storing everything in a JSON file. Only the `sqlite3` import is needed.
```python
import sqlite3
```

After the recipe information has been acquired, the database can be used. Good practice involves strong error handling (I only set up a single try and except block) and making sure to close the database connection. Once a connection with the database is established, the tables can be created if they are not yet, and the recipe data can be added. Here we have three tables, one for recipe metadata such as name, servings, website, etc.. One table is for the ingredients and the other is for the instructions. The ingredients and instruction tables have a reference ID for which recipe they belong to.
```python
# Connect to the database and add the data
try:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS recipes (recipe_name TEXT)"
    )
    cursor.execute("INSERT INTO recipes (recipe_name) VALUES (?)", (recipe_name,))
    recipe_id = cursor.lastrowid
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ingredients (id INTEGER PRIMARY KEY, ingredient TEXT, recipe_id INTEGER, FOREIGN KEY(recipe_id) REFERENCES recipes(id))"
    )
    for item in ingredients:
        cursor.execute("INSERT INTO ingredients (ingredient, recipe_id) VALUES (?, ?)", (item, recipe_id))
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS instructions (id INTEGER PRIMARY KEY, instruction TEXT, recipe_id INTEGER, FOREIGN KEY(recipe_id) REFERENCES recipes(id))"
    )
    for item in instructions:
        cursor.execute("INSERT INTO instructions (instruction, recipe_id) VALUES (?, ?)", (item, recipe_id))
    conn.commit()
    conn.close()
except:
    print("Error connecting to, or using the database")
```

## Immediate Improvements

- Collecting the name, serving size, author, URL, cook/bake time, and more as metadata
- Splitting the ingredients into amount and item
- Better error handling for creation of and insertion to the database tables
- Testing with more than one website to generalize the scraping tools capability

## Ideas for the Future

- Allergen table
- Replacers table
  - e.g. 1 tbsp of ground flax seed with 3 tbsp water sitting for about 5 - 10 minutes replaces 1 egg
- Web interface
  - Able to paste in link
  - View the recipe entry before committing
    - Manual changes allowed
  - Scroll through recipes
  - Add in custom recipes
  - Duplicate and modify recipes
- Tagged recipes
  - Sweet, savory, dessert, etc.
- What can I make with what I have lookup functionality
- Grocery list generator
- Meal cost scraper
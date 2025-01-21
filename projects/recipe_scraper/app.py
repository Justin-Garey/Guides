from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import string
import sqlite3

DEBUG = False
DATABASE = "recipes.db"

# Ingredients and instructions lists
ingredients = []
instructions = []

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

# Collect the ingredients
pattern = re.compile(r"Ingredients")
matches = soup.findAll(string=pattern)
matches = [
    match for match in matches if match.text.strip() in ["Ingredients", "ingredients"]
]
if len(matches) == 1:
    in_list = matches[0].find_next("ul")
    elems = in_list.find_all("li")
    ingredients = [
        "".join(filter(lambda c: c in printable, elem.text)).strip() for elem in elems
    ]

# Collect the instructions
pattern = re.compile(r"Instructions")
matches = soup.findAll(string=pattern)
matches = [
    match for match in matches if match.text.strip() in ["Instructions", "instructions"]
]
if len(matches) == 1:
    in_list = matches[0].find_next("ul")
    elems = in_list.find_all("li")
    instructions = [
        "".join(filter(lambda c: c in printable, elem.text)).strip() for elem in elems
    ]

# Figure out the recipe name
recipe_name = "Vegan Chocolate Chip Cookies"

if DEBUG:
    # Print the ingredients and instructions
    print("Ingredients:")
    for item in ingredients:
        print("    - " + item)
    print("Instructions:")
    for item in instructions:
        print("    - " + item)

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

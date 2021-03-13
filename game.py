from csv import DictReader
from random import choice
from bs4 import BeautifulSoup
import requests

base_url = "http://quotes.toscrape.com"
all_quote = []

# Retrive all quotes from quotes.csv
with open("quotes.csv") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        all_quote.append(row)


# Game logic
quote = choice(all_quote)
remaining_guesses = 4
guess = ""

print("***GAME STARTED***")
print("Here's a quote:")
print(f"- {quote['text']}")
while guess.lower() != quote["author"].lower() and remaining_guesses != 0:
    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
    remaining_guesses -= 1
    if guess.lower() == quote["author"].lower():
        print("Congrads! You nailed it!")
        break
    if remaining_guesses == 3:
        print(f"\nHere's a hint: Author was born on {quote['author_born_date']}.")
    elif remaining_guesses == 2:
        print(f"\nHere's a hint: Author's first name starts with {quote['author'][0]}.")
    elif remaining_guesses == 1:
        print(
            f"\nHere's a hint: Author's last name starts with {quote['author'].split()[1][0]}."
        )
    else:
        print(f"Sorry... You ran out of guesses. The answer was {quote['author']}")

print("***GAME ENDED***")
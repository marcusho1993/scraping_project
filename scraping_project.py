import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import writer

all_quotes = []

base_url = "http://quotes.toscrape.com"
url = "/page/1"

while url:
    # GET request to URL
    res = requests.get(f"{base_url}{url}")
    print(f"Now Scraping {base_url}{url}")

    # Scraping
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    # append quote to all_quote as dicts
    for quote in quotes:
        all_quotes.append(
            {
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio_link": quote.find("a")["href"],
            }
        )
    # get next page url
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    # stop scraping for every 2 seconds
    sleep(2)
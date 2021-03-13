# Scraping Project

Run `scraping_project.py`, which grabs data on every quote from the website <http://quotes.toscrape.com> to update the quotes.

Run `game.py` to start the game.

This project uses **BeautifualSoup** to scrap the data.

This **cli program** displays the **quote** to the user and ask who said it. The player will have **four** guesses remaining.

After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!

After every incorrect guess, the player receives a hint about the author.

When the game is over, the program asks the player if they want to play again. If yes, it restarts the game with a new quote. If no, the program is complete.

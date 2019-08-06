from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.google.com/search?q=daredevil+quotes")


# add if (status_code == 200) to actual code
soup = BeautifulSoup(r.text,"lxml")

#print(soup.prettify())

for quote in soup.find_all("a"):
  #  if quote.text[0] == "“" or quote.text[0] == "\"":
        print(quote.get("href"))

        # use re to find all quotes that begin with http: and are not google.com links

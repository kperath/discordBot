from bs4 import BeautifulSoup
import requests
import re
# module that will retrieve quotes

def get_quotes(show):
    r = requests.get(f"https://www.google.com/search?q=best+{show}+quotes")

    if r.ok:
        soup = BeautifulSoup(r.text,"lxml")

        anchors = soup.find_all("a")

        links = ""

        for l in anchors:
            links += l.get("href") + "\n"

        sites = re.compile(r"http.*").finditer(links)

        for s in sites:
            print(s)

get_quotes("daredevil")

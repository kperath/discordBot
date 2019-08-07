from bs4 import BeautifulSoup
import requests
import re
# module that will retrieve quotes

def get_quotes(show):
    r = requests.get(f"https://www.google.com/search?q=best+{show}+quotes")

    if r.ok:
        soup = BeautifulSoup(r.text,"lxml")

        anchors = soup.find_all("a") # find all anchor tags (links for sites)

        links = ""

        for l in anchors:
            links += l.get("href") + "\n"
        
        # remove all links for stuff that won't have quotes (image sites, video sites, google services)
        sites = re.findall(r"https?://(?!.*google)(?!.*youtube)(?!.*pinterest)(?!.*img.*).+\..+",links)

        quotes = []

        print("QUOTE SITES")
        for s in sites:
            r = requests.get(s)
            print(s)
            if r.ok:
                quotes = re.findall(r"“.*”",r.text) # look for sites with quotation marks

                if (quotes == []): # if no quotes can be found, look at the next site
                    continue
                else:
                   break    # quotes found, end loop

        if (quotes == []):
            # if after entire loop of sites no quotes were found
            return [] 

        return quotes

    else:
        # if google doesn't allow us to use the search function
        return []

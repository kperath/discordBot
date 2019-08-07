from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# UNFINISHED CODE
# originally was going to use selenium but then realized that is was not necessary
# still here to show that I do know how to use selenium

# turn into big function and import it into quoteboy.py

media = "godfather" # tv show, movie, book etc.

# open googlechrome and go to google.com
browser = webdriver.Chrome()
browser.get("http://google.com/")

# search for quotes for the given media in the search bar
searchbar = browser.find_element_by_name("q")
searchbar.send_keys(f"best {media} quotes") # google dorking!!!

# click the search button
searchbutton = browser.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.VlcLAe > center > input.gNO89b")
searchbutton.click()

# find the first link from the google search
firstlink = browser.find_element_by_css_selector("#rso > div:nth-child(1) > div > div.kp-blk.c2xzTb.Wnoohf.OJXvsb > div > div.ifM9O > div:nth-child(3) > div.g > div > div > div.r > a")

# checking if the clicking will be a success
r = requests.get(firstlink.get_attribute('href'))

# if success (status_code < 400)
if (r.ok):
    firstlink.click()
else:
    print("Quote could not be found") # change to return null!!!!!!!!!!!!!!

# Can remove selenium and use just bs4 on google search to get first link and go to that link and use bs4 again (while checking with requests)

# can also use google dorking to find sites with “

# use re to find text that start with “ and end with ”

#and no img file links

# find not need bs4

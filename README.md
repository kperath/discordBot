<img src="/quotebot.png" width="150">

# Quotebot
### A discord bot that will find quotes for your favourite things!
#### Using discordpy framework

About:
Quotebot is a bot on discord that when given a piece of media (books, tv shows, movies or even people) it will search for quotes from said media along with that it has other general features a bot should have in a server.

```
COMMANDS:

!quote [media]		gives 1 quote from media chosen

!quotelist [media]	gives a list of quotes from media chosen

!membercount		gives numbers of members in server

!memberlist		lists members in server

!statusreport		gives report of everyones status in server

!banlist		list of members banned and reason they were banned

!logout or !bye		bots goes offline

!fly me to the moon	links to video of fly me to the moon song

```

By working on this side project I learned:
- How to work with asyncrhonous processes better
- How to use python requests and the beautifulsoap4 library
- How to work with bots in general
	- I feel I am ready to tackle other bots like ones from twitter and slack

Reason for project:
- Being an active user of discord myself, I was always curious how bots from other servers worked and decided built one for myself

Notes:
- I want to make one thing very clear, this project is not a success but that was never the point. I took on this project knowing that the task of creating a bot that would be able to search the entire internet for a quote without flaw was ridiculously ambitious.
- To make a proper quotebot a better idea would be to rely on a API from a series of sites, again this was not my plan, I wanted to see what I could do based off just using google.
- The technique I use to find quotes is: google search "best quotes [media]" and then take links as a collection (using bs4 and re) and look for the quotation marks in a site, this is indeed very inefficient

**DISCLAIMER:**
Since this bot does not not use any APIs to collect quotes from sites, it is scraping and that means that using this bot too much could result in an IP ban, this is why I refrain from using it myself and why I consider it to be an ambitious project.

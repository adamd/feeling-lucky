# Feeling Lucky: Google Search from CSVs

Usage: `python feeling-lucky.py filename.csv`

Given a CSV containing search terms:
```
Search Term,First Web Result
automation,
boteconomy,
coffee,
house of cards,
```

Script will overwrite the file to include top search term in the CSV, like so:
```
Search Term,First Web Result
automation,https://en.wikipedia.org/wiki/Automation
boteconomy,http://www.economist.com/news/business-and-finance/21696477-market-apps-maturing-now-one-text-based-services-or-chatbots-looks-poised
coffee,https://en.wikipedia.org/wiki/Coffee
house of cards,https://en.wikipedia.org/wiki/House_of_Cards_(U.S._TV_series)
```

How does it work? [Read the tutorial](blob/master/tutorial.md).

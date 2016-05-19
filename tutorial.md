# Are Your Feeling Lucky? Bulk Google Search from CSV Files

For many of us, Google is the source of truth. Not only is it the top search engine, its users trust its rankings. Despite many other links, ads, and results, the top result gets 33% of the traffic. Google realized the gravitational pull of the top rank early on and provided an "I'm Feeling Lucky" button to bypass the list of results.

In this tutorial, we'll take a CSV of search terms and add a new field with the top Google result for each term. Essentially, we're building a bulk, automated way to retrieve the best--at at least the luckiest--result for every term.

First, ensure you have Python installed on your system, along with these libraries that will make the code shorter and easier to write: `sys, urllib, requests, csv`.

## Prepare the Python Script

Now we're ready to write some code. Here is the basic framework of the solution, which will read through a CSV one line at a time, look up the search result, then write is all back to the CSV:
import sys, urllib, requests, csv

```
import sys, urllib, requests, csv

# Find the top result for search terms in CSV
def process_file(fn):
  return

# Save the search results in CSV
def write_file(fn, results):
  return

# Use Google's I'm Feeling Lucky option to retrieve the top search result
def lucky_search(q):
  return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: lucky.py filename.csv"
    else:
        process_file(sys.argv[1])
```

You can save this code as `lucky.py` and run it with `python lucky.py terms.csv`

This barebones version will check for a filename argument, then pass it to the `process_file` function. At this point, all of the functions are empty, so let's add in the code to do the heavy lifting.

## Read the CSV File

Our search terms are stored in a CSV with each term on a new line. We need to read in the file, extract each term, and run a search.

The `process_file` function kicks off the fun:
```
# Find the top result for search terms in CSV
def process_file(fn):
    results = []
    with open(fn, 'rb') as f:
        rd = csv.reader(f)
        header = rd.next()
        results.append(header)
        for row in rd:
            row[1] = lucky_search(row[0])
            results.append(row)
    f.close()
    write_file(fn, results)
    print "Processed " + str(len(results)-1) + " search terms"
```

Here we open the CSV file and create a `csv.reader` that knows how to handle that file type. After storing the headers from the first row, we iterate through the remaining rows. Each term is in the first column (the "zeroth" index), so we pass `row[0]` to the search function and store the result in the second column (the first index, `row[1]`).

Now we've looped through every line of the file, but we handed off the most important part to another function. Let's check that out.

## Performing the Google Search

These days it seems like there is an API for everything. You'd think there would be a programmatic interface for the world's biggest search engine. Unfortunately, Google has closed two search APIs and no longer makes its results available outside of a browser.

For retrieving our top results, we're left with two options:
1. Screen scrape HTML to extract the first result, which is messy and legally questionable.
2. Intercept the HTTP redirect for I'm Feeling Lucky searches.

Based on the name of this tutorial, you can probably guess I chose the second. This choice has the added benefits of more maintainable code and a clear conscience.

Here is the short code to accompish each search:
```
# Use Google's I'm Feeling Lucky option to retrieve the top search result
def lucky_search(q):
    url = "https://www.google.com/search?btnI&q=" + urllib.quote_plus(q)
    user_agent = "Feeling Lucky/0.1"

    headers = {'user-agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=True)
    return r.url
```

The Python `requests` library handles our call to Google search. To get results we do have to provide a user agent. I chose to create my own, `Feeling Lucky/0.1`, though you *could* choose your favorite existing browser.

Our Google search URL includes the query term (q) and the I'm Feeling Lucky button name (btnI). When we execute the request, Python calls Google and follows the Location redirect. The response URL now is the top result, which we return to the `process_file` function.

### Google Recommending Google

The only downside I've discovered to the I'm Feeling Lucky method is that Google sometimes considers its own search results to be the top result for some searches. This seems most likely when searching for something that could be considered a location-based query, such as a restaurant type.

In these cases, if you aren't satisfied with a link to Google results, you'd need to use the screen scraping option as a backup plan. A Python library, such as Beautiful Soup, can help you easily parse HTML.

## Save the Results to the CSV

Remember that our `process_file` function acts as the conductor of our script, calling other functions as necessary. The final function it calls is `write_file`, which stores results to the same CSV file.

Here is the entirety of this final function:
```
# Save the search results in CSV
def write_file(fn, results):
    with open(fn, 'wb') as f:
        wt = csv.writer(f)
        for row in results:
            wt.writerow(row)
    f.close()
```

Here we create a `csv.writer` that knows how to handle the file type. For each of the results (an array of arrays stored appended each time through the original file) we write it to the CSV file.

Consider this example CSV file:
```
Search Term,First Web Result
automation,
boteconomy,
coffee,
house of cards,
```

When we call `python lucky.py terms.csv` the CSV file will now contain our top results:
```
Search Term,First Web Result
automation,https://en.wikipedia.org/wiki/Automation
boteconomy,http://www.economist.com/news/business-and-finance/21696477-market-apps-maturing-now-one-text-based-services-or-chatbots-looks-poised
coffee,https://en.wikipedia.org/wiki/Coffee
house of cards,https://en.wikipedia.org/wiki/House_of_Cards_(U.S._TV_series)
```

Try it out for yourself:
* `git clone https://github.com/adamd/feeling-lucky.git`
* Or download [lucky.py](https://raw.githubusercontent.com/adamd/feeling-lucky/master/lucky.py) to your machine.

**Got improvements? Happily accepting pull requests and issues.**

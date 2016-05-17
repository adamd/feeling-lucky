import sys, urllib, requests, csv

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

# Save the search results in CSV
def write_file(fn, results):
    with open(fn, 'wb') as f:
        wt = csv.writer(f)
        for row in results:
            wt.writerow(row)
    f.close()

# Use Google's I'm Feeling Lucky option to retrieve the top searh result
def lucky_search(q):
    url = "https://www.google.com/search?btnI&q=" + urllib.quote_plus(q)
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0"

    headers = {'user-agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=True)
    return r.url

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: lucky.py filename.csv"
    else:
        process_file(sys.argv[1])

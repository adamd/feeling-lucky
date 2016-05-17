import sys, urllib, requests

# Use Google's I'm Feeling Lucky option to retrieve the top searh result
def lucky_search(q):
    url = "https://www.google.com/search?btnI&q=" + urllib.quote_plus(q)
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0"

    headers = {'user-agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=True)
    print r.url

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: lucky.py filename.csv"
    else:
        #process_file(sys.argv[1])
        lucky_search(sys.argv[1])

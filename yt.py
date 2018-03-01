import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

def yt_search(search_terms):
    query = urllib.parse.quote(search_terms)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    return ["https://youtube.com{}".format(n['href']) for n in soup.findAll(attrs={'class':'yt-uix-tile-link'}) if ('watch' in n['href'] and 'googleads' not in n['href']) ]

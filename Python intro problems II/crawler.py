import requests


url = 'https://www.tocilar.ro/sitemaps/referate2.txt'


def crawl(url, n):
    resp = requests.get(url)
    text = resp.content.decode()
    if n == 0:
        return
    for url in text.split('\n'):
        if 'https://' == url[:8] or 'http://' == url[:7]:
            print(n, url)
            crawl(url, n-1)

crawl(url, 2)

            

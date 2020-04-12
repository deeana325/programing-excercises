import requests


url = 'https://www.tocilar.ro/sitemaps/referate2.txt'

text = requests.get(url)
text = text.content.decode()

def crawl(url, n):
    if n == 0:
        return
    for word in text.split(' '):
        if 'https://' in word:
            print(n, word)
            crawl(word, n-1)

crawl(url, 2)

            

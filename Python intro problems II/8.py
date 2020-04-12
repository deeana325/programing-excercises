#8. Write a Python program to get the top stories from Google news.
import requests


url = 'https://www.tocilar.ro/sitemaps/referate2.txt'

text = requests.get(url)

text = text.content.decode()

for line in text.split('\n'):
    print(len(line), line)


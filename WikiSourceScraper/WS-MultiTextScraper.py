from bs4 import BeautifulSoup
import requests
import re

with open("links500.txt") as f:
    urls = f.readlines()

with open("results.txt", "w") as outfile:
    for i, url in enumerate(urls):
        soup = BeautifulSoup(requests.get(url.strip()).text, 'html.parser')

        # eliminate undesirable contents
        for tag in soup(['style']):
            tag.decompose()
        for tag in soup.find_all('span', class_='numeroriga'):
            tag.decompose()

        # find the right title and content
        title = soup.find('h1', {'id': 'firstHeading'})
        if title is None:
            title = soup.find('div', class_=re.compile(r'testi\b'))

        content = soup.find('div', class_=re.compile(r'testi\b'))

        if title is not None:
            outfile.write(f"{title.get_text()}\n")
        else:
            outfile.write(f"Title not found for URL: {url}\n")

        if content is not None:
            content_text = re.sub(r'\[.*?\]', '', content.get_text())
            outfile.write(f"{content_text}\n")
        else:
            outfile.write(f"Content not found for URL: {url}, tag 'div class=testi' not found\n")

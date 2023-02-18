# import the required libraries
from bs4 import BeautifulSoup
import requests
import re

# Define a function to check if a URL is valid
def is_valid(url):
    # Check if the URL exists
    if url:
        # Check if the URL starts with '/wiki/'
        if url.startswith('/wiki/'):
            # Check if the URL does not contain a forward slash followed by any word character followed by a colon
            if not re.compile('/\w+:').search(url):
                # If all conditions are met, return True
                return True
    # If any of the above conditions fail, return False
    return False

# Define the URL to scrape
random_url = 'https://it.wikisource.org/w/index.php?title=Categoria:Testi_del_XIII_secolo&pagefrom=Di+settembre+vi+do+diletti+tanti%0ADi+settembre+vi+do+diletti+tanti#mw-pages'

# Send an HTTP request to the URL and store the response
r = requests.get(random_url)

# Print the URL of the page that was actually loaded
print('url:', r.url)

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(r.text, 'html.parser')

# Find the title of the page using its class
title = soup.find('h1', {'class': 'firstHeading'})

# Print the URL of the page and its title
print('starting website:', r.url)
print('titled:', title.text)
print()

# Create an empty list to store valid URLs
valid_urls = []

# Loop through all the links on the page
for link in soup.find_all('a'):
    # Get the URL of the link
    url = link.get('href', '')
    # Check if the URL is valid and has not been seen before
    if url not in valid_urls and is_valid(url):
        # If the URL is valid, add it to the list of valid URLs
        valid_urls.append(url)

# Generate a list of full URLs by appending the valid URLs to the base URL
full_urls = [f'https://it.wikisource.org{url}' for url in valid_urls]

# Write the full URLs to a txt file
with open("links.txt", "w") as file:
    for url in valid_urls:
        full_url = "https://it.wikisource.org" + url
        file.write(full_url + "\n")

# Print the full URLs to the console
print('\n'.join(full_urls))

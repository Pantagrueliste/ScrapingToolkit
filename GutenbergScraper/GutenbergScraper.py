import requests
import json
import csv
import os
from pathlib import Path

# Function to download a file
def download_file(url, local_path):
    response = requests.get(url)
    with open(local_path, 'wb') as f:
        f.write(response.content)

# Function to get word count of a file
def get_word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = f.read().split()
        return len(words)

# Load JSON data from a local file (change the name of 'books.json' accordingly)
with open('books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a directory to store downloaded files
Path("downloaded_files").mkdir(parents=True, exist_ok=True)

# Prepare the CSV file (change the name of 'books.csv' accordingly)
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['filename', 'id', 'title', 'authors', 'century', 'word_count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through the JSON entries (as created by the Gutendex web API)
    for entry in data['results']:
        # Get the txt file URL
        txt_file_url = entry['formats'].get('text/plain') or entry['formats'].get('text/plain; charset=utf-8')
        if txt_file_url:
            # Download the .txt file
            file_name = f"downloaded_files/{entry['id']}.txt"
            download_file(txt/_file_url, file_name)

            # Get the century format
            if entry['authors'][0]['death_year']:
                century = (entry['authors'][0]['death_year'] - 1) // 100 * 100 + 100
            else:
                century = 'Unknown'

            # Get the word count of the downloaded file
            word_count = get_word_count(file_name)

            # Write to the CSV file
            writer.writerow({
                'filename': file_name,
                'id': entry['id'],
                'title': entry['title'],
                'authors': ', '.join([author['name'] for author in entry['authors']]),
                'century': century,
                'word_count': word_count
            })

        else:
            print(f"Error: No txt file found for book ID {entry['id']}")
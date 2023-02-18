# Scrapingtoolkit 
`Scrapingtoolkit` is a collection of scripts I developed to scrape databases in the digital humanities. The scripts have been used for very specific purposes and chances are you will need to adapt them in order to obtain what you want. To adapt the code, feel free to fork this repository. 
As of 10/01/2023, `Scrapingtoolkit` includes two folders:
 - `MIAscraper`
 - `Wikisource scraper` (coming soon)

# MIAscraper
`MIAscraper` is a Python script that requests data from the MIA database API and saves it in a CSV file.

## Description
### The MIA Database
The MIA database is a collaborative platform where scholars can share their photographs of documents found in the [State Archives of Florence](https://archiviodistatofirenze.cultura.gov.it/asfi/home), transcribe them and catrgorize them. MIA has been created by the [Medici Archive Project](https://www.medici.org), one of the oldest digital humanities projects still in existence. The depth and breadth of this database is truly impressive and its contents are growing everyday. 
It is highly recommended you familiarize with the database before attempting any scraping. Note that you also need to obtain credentials to access the database.  

### The Script 
`MIAscraper` makes a POST request to the MIA API, extracts specific data from the response, and writes the data to a CSV file. The script uses the requests and csv modules, as well as the json module to work with JSON data.

## Getting Started
To use MIAscraper, you will need to install the required Python modules. You can do this using pip:

```
pip install requests
```

You will also need to replace the login and password information in the script with your own credentials.

### Usage

To use `MIAscraper`, simply run the script using Python:

```
python MIAscraper.py
```

The script will make a request to the MIA API and write the extracted data to a CSV file named `results.csv`.

## Wikisource Scraper (coming soon)
`Wikisource scraper` is a collection of scripts aimed at scraping vast amounts of texts stored in Wikisource. The script was designed to help me create a large corpus of Italian texts for training purposes. To adapt the code, feel free to fork this repository. 

As of 15/02/2023, Wikisource scraper contains 3 scripts:

### `WS-MultiTextScraper`
`WS-MultiTextScraper` scrapes all the text available on Wikisource. In this case, the code is adapted to the Italian Wikisource (i.e.: it scrapes contents under div classes starting with "testi"). You might need to adapt it to your specific needs, especially if you want to adapt to other languages. The script needs a text file with all the urls to scrape. To build this file, you can use the two scripts below.

### `CreateLinksList`
`CreateLinksList` generates lists of links to books stored in Wikisource. This list of links will be stored in a text file, that you can subsequently use with `WS-MultiTextScraper`. Choose a wiki category and paste the url on "random_url". Make sure the "full_url" line is correct.  

### `MultiBookLinksExtractor`
Some books on Wikisource are structured differently and contain multiple chapters. To help scraping each of these chapters, `MultiBookLinksExtractor` creates an additional list of links related to multi chapter books. Once this list is complete, you can add it the list created with `CreateLinksList`. This consolidated list of links will enable you to scrape all the contents of the category you initially chose.

# Contributing
Contributions to `MIAscraper` and `WikiScraper` and are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes. You can also submit bug reports or feature requests by creating an issue in the repository.

# License
`Scrapingtoolkit` is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.

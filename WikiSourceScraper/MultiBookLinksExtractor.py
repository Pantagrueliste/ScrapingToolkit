from bs4 import BeautifulSoup
import requests

# Base URL for the website
base_url = "https://it.wikisource.org"

# Open the file with the urls
with open("links700.txt", "r") as file:
    urls = file.readlines()

# Create a file to store the links
file_name = "links700-mb.txt"
with open(file_name, "w") as file:
    # Iterate over each url
    for url in urls:
        url = url.strip() # remove newline character

        try:
            # Make a request to the url
            response = requests.get(url)
            content = response.content

            # Print out the response status code
            print(f"Response status code: {response.status_code}")

            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(content, "html.parser")

            # Find the h2 header with the id "Indice"
            Indice = soup.find("span", id="Indice")

            # Check if the h2 header exists
            if Indice:
                # This is a multichapter book
                title = soup.title.string.split("-")[0].strip() # extract the title of the book
                print("Multichapter book detected:", title)

                # Find the list of links in the book
                links_list = Indice.find_next("ul").find_all("li")

                # Extract and write the complete URLs to the file
                for li in links_list:
                    link = base_url + li.a["href"]
                    if "/w/index.php" not in link:
                        file.write(link + "\n")
        except Exception as e:
            print("Error while processing url:", url)
            print("Error message:", e)

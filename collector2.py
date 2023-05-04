import requests
from bs4 import BeautifulSoup

# Collecting data from a website
url = "http://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Storing data in a text file
with open('website_data.txt', 'w') as file:
    file.write(soup.prettify())
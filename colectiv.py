import os
import time
import threading
from pathlib import Path
from bs4 import BeautifulSoup
import requests

# Reading all types of files
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

# Listing all files and directories
def list_files_and_directories(path):
    return os.listdir(path)

# Searching Google
def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("div", class_="tF2Cxc")
    results = []

    for result in search_results:
        title = result.find("h3", class_="LC20lb DKV0Md").text
        url = result.find("a")["href"]
        results.append({"title": title, "url": url})

    return results

# Main function that uses other functions
def main():
    # Task 1: List all files and directories
    path = "C:/"
    files_and_dirs = list_files_and_directories(path)
    print(f"Files and directories in {path}:")
    for item in files_and_dirs:
        print(item)

    # Task 2: Read a file
    file_path = "example.txt"
    content = read_file(file_path)
    print(f"\nContent of {file_path}:")
    print(content)

    # Task 3: Search Google
    query = "Python programming"
    results = search_google(query)
    print("\nGoogle search results:")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print()

# Run the main function
if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

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
        snippet = result.find("div", class_="IsZvec")
        if snippet:
            snippet = snippet.find("span", class_="aCOpRe")
            if snippet:
                snippet = snippet.text

        results.append({"title": title, "url": url, "snippet": snippet})

    return results

if __name__ == "__main__":
    query = "Python programming"
    results = search_google(query)

    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Snippet: {result['snippet']}")
        print()
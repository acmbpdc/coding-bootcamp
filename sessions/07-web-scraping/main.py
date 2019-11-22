import requests
from bs4 import BeautifulSoup
import re


def wiki(title):
    """Returns a URL on https://en.wikipedia.org based on a title

    Arguments:
        title {str} -- desired page

    Returns:
        str -- URL on https://en.wikipedia.org based on title
    """
    return f"https://en.wikipedia.org/wiki/{title}"


def get_pages(page):
    respose = requests.get(wiki(page))
    soup = BeautifulSoup(respose.content, "html.parser")

    pages = set()
    for link in soup.find_all("a", attrs={"href": re.compile("^/wiki/")}):
        href = link.get("href")[6:]

        if any([x in href for x in[".", ":", "#"]]):
            continue

        pages.add(href)

    return pages



if __name__ == "__main__":
    src = "Barack_Obama"
    target = "Keanu_Reeves"

    pages = []
    current = src
    counter = 1
    while True:
        subs = get_pages(current)
        if target in subs:
            print(f"Found in {counter} steps")
            break
        else:
            pages.extend(subs)
            current = pages.pop(0)
            counter += 1

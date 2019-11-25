# Web Scraping

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.

It involves fetching a web page and extracting information from it.

## Motivation

*   Websites have a lot of data. This data, if extracted properly, can be very useful in the realm of Machine Learning
*   Search engine engineering relies a lot on Web Scraping and other forms of Information Retrieval
*   It can be used to automate mundane tasks
*   Learning how to web scrape involves exploring many related domains, such as Cybersecurity, Web Development, Web Services, & Natural Language Processing

## Setup

We will be using the following Python libraries:

*   [`requests`](https://pypi.org/project/requests/) - *HTTP Requests for Humans*
*   [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) - *Scraping Library*

```bash
pip3 install requests beautifulsoup4 # installs the libraries
```

Create the following project layout:

```
web-scraping
└── main.py
```

## Scraper

We will build a crawler that surfs across [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) and finds the shortest directed path between two articles.

```python
import argparse
from bs4 import BeautifulSoup
from collections import deque
import re
import requests


def wiki(title):
    """Takes a title and wraps it to form a https://en.wikipedia.org URL

    Arguments:
        title {str} -- Title of Wikipedia Article

    Returns:
        {str} -- URL on wikipedia
    """
    return f"https://en.wikipedia.org/wiki/{title}"
```

Let us define a function that retrieves a page, and returns a list of titles for all articles that appear as links on the page.


```python
def get_pages(title):
    """Returns a set of wikipedia articles linked in a wikipedia article

    Arguments:
        title {str} -- Article title

    Returns:
        {set()} -- A set of wikipedia articles
    """
    response = requests.get(wiki(title))
    soup = BeautifulSoup(response.content, "html.parser")
```

>   *   `requests.get(url)` retrieves the resource at the `url` using an `HTTP GET Request`
>
>
>       You can try the following lines of code in the `python` shell environment
>       ```python
>       import requests
>       response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
>       print(resonse.content)
>       ```
>
>   *   `BeautifulSoup(content, "html.parser")` returns an object that has information regarding the `<html>` tag, with all of its descendants and text content.

```python
    pages = set()

    for link in soup.find_all("a", attrs={"href": re.compile("^/wiki/")}):
        page = link.get("href")[len("/wiki/"):]

        if any([x in page for x in[".", ":", "#"]]):
            continue

        pages.add(page)

    return pages
```

>   *   `soup.find_all("a", attrs={"href": re.compile("^/wiki/")})` returns a list of `<a>` tags, which have `href`s that start with `/wiki/`
>   *   `page` is set to the rest of the link
>   *   check if `page` has any special characters:
>       *   `.` : indicates a url for a media file
>       *   `:` : indicates a url for a Wikipedia meta page
>       *   `#` : indicates a url for a page with an anchor attached. We choose to not include these

## Crawler

The crawler uses a Breadth-First Search traversal to *crawl* across the site.

```python
def shortest_path(start, end):
	"""
	Finds the shortest path in Wikipedia from start page to end page

	Arguments:
		start {str} -- start page in /wiki/name format
		end {str} -- end page in /wiki/name format
	"""
	i = 1
	seen = set()
	d = deque([start])
	tree = {start: None}
	level = {start: 1}

	while d:
		# Get element in front
		topic = d.pop()
		seen.add(topic)
		print(f'{i}) Parsed: {topic}, Deque: {len(d)}, Seen: {len(seen)}, Level: {level[topic]}')

		urls = get_pages(topic)
		urls -= seen

		# Update structures with new urls
		seen |= urls
		d.extendleft(urls)
		for child in urls:
			tree[child] = topic
			level[child] = level[topic] + 1

		# Check if page found
		if end in urls:
			topic = end
			break
		i += 1

	# Get path from start to end
	path = []
	while topic in tree:
		path.append(topic)
		topic = tree[topic]
	print(' \u2192 '.join(reversed(path)))
	print(f'Length: {len(path)-1}')
```

## Interface

Let us create an interface for our functions

```python
def main():
    """Command line interface for the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', '-s', help='Exact name of start page', required=True)
    parser.add_argument('--end', '-e', help='Exact name of end page', required=True)
    args = parser.parse_args()

    start = '_'.join(args.start.split())
    end = '_'.join(args.end.split())
    shortest_path(start, end)

if __name__ == "__main__":
    main()
```

You can find the complete source code [here](src/main.py)

## Usage

To learn how to use the command

```bash
python main.py -h
```

```
usage: main.py [-h] --start START --end END

optional arguments:
  -h, --help            show this help message and exit
  --start START, -s START
                        Exact name of start page
  --end END, -e END     Exact name of end page
```

Try the program

```bash
python main.py -s Web_Scraping -e Hell
```

```
Ouput placeholder
```

## Summary

We covered:

*	[Motivation](#motivation)
*	[Setup](#setup)
*	[Scrapper](#scrapper)
*	[Crawler](#crawler)
*	[Interface](#interface)
*	[Usage](#usage)

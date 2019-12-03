# Web Scraping

Web scraping, web harvesting, or web data extraction is data scraping used for quickly and efficiently extracting data from websites. It involves fetching a web page and extracting information from it.

## Motivation

*   Websites have a lot of data. If extracted properly, this data  can be very useful in the realm of [Machine Learning](https://github.com/acmbpdc/coding-bootcamp/tree/master/sessions/07-machine-learning).
*   Search engine engineering relies a lot on Web Scraping and other forms of [Information Retrieval](https://github.com/acmbpdc/openlib.cs/tree/master/courses/CSF469).
*   It can be used to automate mundane search tasks.
*   Learning how to web scrape involves exploring many related domains, such as Cybersecurity, Web Development, Web Services, & Natural Language Processing.

## Setup

We will be using the following Python libraries:

*   [`requests`](https://pypi.org/project/requests/) - [*HTTP Requests*](https://www.w3schools.com/tags/ref_httpmethods.asp) *for Humans*
	
	Allows to navigate and access resources on the web.

*   [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) - *Scraping Library*

	Allows to parse and extract certain information from a resource.

<p align="center"><img src="assets/beautiful.gif" height="200"></p>

```bash
pip3 install requests bs4	# install the libraries
```

Create the following project layout:

```
web-scraping
└── main.py
```

## Scraper

We will build a crawler that surfs across [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) and finds the [shortest directed path](https://brilliant.org/wiki/shortest-path-algorithms/) between two articles.

Import the dependencies

```python
import re
import requests
import argparse
from bs4 import BeautifulSoup
from collections import deque
```

<p align="center"><img src="assets/later.gif" height="200"></p>


<!-- 
Where would you like to add these?

>   *   `requests.get(url)` retrieves the resource at the `url` using an `HTTP GET Request`
>
>   *   `BeautifulSoup(content, "html.parser")` returns an object that has information regarding the `<html>` tag, with all of its descendants and text content. 

>   *   `soup.find_all("a", attrs={"href": re.compile("^/wiki/")})` returns a list of `<a>` tags, which have `href`s that start with `/wiki/`
>   *   `page` is set to the rest of the link
-->

Using the `get` function in the requests module, you can access a webpage

```python
response = requests.get('https://en.wikipedia.org/wiki/Batman')	# pass the webpage url as an argument to the function
```

```python
print(response.status_code)	# 200 OK response if the webpage is present
print(response.headers)		# contains the date, size, information about the server and type of file the server is sending to the client
print(resonse.content)		# page content or the html source
```

>	#### Status Codes
>
>	There are five classes of response status codes:
>	*	1xx informational - relatively new, only indicates the request has been received
>	*	2xx successful - request received and accepted successfully
>	*	3xx redirection - client must take some action in order to complete the request
>	*	4xx client error - request from client contains bad syntax or access to invalid resources
>	*	5xx server error - server incapable of fulfilling the request
>
>	For more information, you can refer to [this](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) Wikipedia page.

To parse the content or the page source, we will use the `BeautifulSoup` module. To do so, first create a `BeautifulSoup` object

```python
soup = BeautifulSoup(response.content, 'html.parser')
```

We can now access specific information directly. To get the first link in the page

```python
link = soup.a
```

To get all the links on the page

```python
links = soup.find_all('a')	# anchor tag contains a link
```

Let's work on the last link in the page

```python
link = links[-1]	# get the last anchor tag
```

The link is a `Tag` object corresponding to the anchor tag. Each `Tag` object contains a few properties

```python
print(link.name)	# name of the tag
print(link.attrs)	# attributes of the tag
```

The anchor tag or `<a>` has an `href` attribute which contains the actual link to the page

```python
print(link.attrs['href'])	# accessing directly using attrs
print(link['href'])			# accessing by treating like a dict
```

Trying to access an attribute that does not exist causes an error. A better way is to use the `get` method

```python
print(link['id'])		# error
print(link.get('id'))	# returns value if exists else None and does not throw an error
```

To find only those anchor tags that contain the `href` attribute

```python
links = soup.find_all('a', href=True)	# anchor tag contains a href attribute
```

You can also specify a regex to match links that fit a requirement. In our case, we only want to keep links to Wikipedia pages. We also want to exclue the links that point to some documentation (such as the _Help_ or _About_ page). If you notice, the links have a specific format. 

Links we need since they point to other Wikipedia pages

```
/wiki/DC_Thomson
/wiki/Chris_KL-99
/wiki/Wing_(DC_Comics)
```

Links we don't need since they contain documentation, media or point to other websites

```
/wiki/Category:American_culture
/wiki/File:Batman_DC_Comics.png
www.wikimediafoundation.org
```

Hence, we can use the following regex `^/wiki/[^.:#]*$`. This is explained below:

*	`^` denotes the start of the string
*	`^/wiki/` the link _starts_ with `/wiki/`
*	`[]` denotes a character set that is allowed, `[^]` denotes a character set that is *not* allowed. The `^` symbol negates the character set if present at the start
*	`[c]*` denotes 0 or more occurrences of a character c, `[^c]*` denotes 0 or more occurrences of _all_ characters except c
*	`$` denotes the end of the string

The above regex means the link starts with `/wiki/` has 0 or more characters that are not `.` or `:` or `#` symbol till the end of the string.

```python
links = soup.find_all('a', href=re.compile('^/wiki/[^.:#]*$'))	# find all anchor tags that contain the href attribute with the specified regex
```

>	#### Special characters
>
>	*   `.` - indicates a url for a media file. For example, '/wiki/url/to/file/batman.jpg'.
>	*   `:` - indicates a url for a Wikipedia meta page. For example, '/wiki/Help:Contents'.
>	*   `#` - indicates a url for a page with an anchor attached, we chose to not include these.

Don't forget, we still have to extract the title from the `href` link since the above returns all the anchor tags

```python
pages = set([link.get('href')[len("/wiki/"):] for link in links])
```

## Code Modularity

Let's add a helper function to return the entire url given a title

```python
def wiki(title):
    """Takes a title and wraps it to form a https://en.wikipedia.org URL

    Arguments:
        title {str} -- Title of Wikipedia Article

    Returns:
        {str} -- URL on wikipedia
    """
    return f"https://en.wikipedia.org/wiki/{title}"
```

<p align="center"><img src="assets/scan.gif" height="200"></p>

Let us organize our code into a function that retrieves a page, and returns a list of titles for all articles that appear as links on the page

```python
def get_pages(title):
	"""Returns a set of wikipedia articles linked in a wikipedia article

	Arguments:
		title {str} -- Article title

	Returns:
		{set()} -- A set of wikipedia articles
	"""
	response = requests.get(wiki(title))
	soup = BeautifulSoup(response.content, 'html.parser')
	links = soup.find_all('a', href=re.compile('^/wiki/[^.:#]*$'))
	pages = set([link.get('href')[len("/wiki/"):] for link in links])

	return pages
```

<p align="center"><img src="assets/fight.gif" height="200"></p>

## Crawler

The crawler uses a [Breadth-First Search](https://brilliant.org/wiki/breadth-first-search-bfs/) traversal to *crawl* across the site.

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
<p align="center"><img src="assets/flip.gif" height="200"></p>

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

<p align="center"><img src="assets/reconstruction.gif" height="200"></p>

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

<p align="center"><img src="assets/end.gif" height="200"></p>

## Summary

We covered:

*	[Motivation](#motivation)
*	[Setup](#setup)
*	[Scraper](#scrapper)
*	[Code Modularity](#code-modularity)
*	[Crawler](#crawler)
*	[Interface](#interface)
*	[Usage](#usage)
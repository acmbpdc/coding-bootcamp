import re
import requests
import argparse
from bs4 import BeautifulSoup
from collections import deque



def wiki(title):
	"""Takes a title and wraps it to form a https://en.wikipedia.org URL

	Arguments:
		title {str} -- Title of Wikipedia Article

	Returns:
		{str} -- URL on wikipedia
	"""
	return f"https://en.wikipedia.org/wiki/{title}"



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
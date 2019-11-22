import re
import requests
import argparse
from collections import deque



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
	base_url = "https://en.wikipedia.org"
	
	while d:
		# Get element in front
		topic = d.pop()
		seen.add(topic)
		print(f'{i}) Parsed: {topic}, Deque: {len(d)}, Seen: {len(seen)}, Level: {level[topic]}')

		# Parse the url
		url = base_url + topic
		html = requests.get(url).text

		# Get urls and add if not seen
		urls = re.findall(r'/wiki/[^"]*', html)
		urls = set([url for url in urls if ':' not in url]) - seen

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
		path.append(topic[len('/wiki/'):])
		topic = tree[topic]
	print(' \u2192 '.join(reversed(path)))
	print(f'Length: {len(path)}')



# Adding the keyword arguments
parser = argparse.ArgumentParser()
parser.add_argument('--start', '-s', help='Exact name of start page', required=True)
parser.add_argument('--end', '-e', help='Exact name of end page', required=True)
args = parser.parse_args()

start = '/wiki/ ' + '_'.join(args.start.split())
end = '/wiki/' + '_'.join(args.end.split())
shortest_path(start, end)
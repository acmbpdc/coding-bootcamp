import re
import requests
import argparse
import matplotlib.pyplot as plt
from collections import deque



def shortest_path(start, end):
	"""
	Finds the shortest path in Wikipedia from start page to end page
	
	Arguments:
		start {str} -- start page in /wiki/name format
		end {str} -- end page in /wiki/name format
	"""
	i = 1
	x = []
	y_d = []
	y_s = []
	seen = set()
	d = deque([start])
	nodes = {1: 1}
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
			nodes[level[child]] = nodes.get(level[child], 0) + 1
		
		# Graph plots
		x.append(i)
		y_d.append(len(d))
		y_s.append(len(seen))

		# iterations vs. size of deque
		plt.plot(x, y_d)
		plt.xlabel('Iterations')
		plt.ylabel('Size of Deque')
		plt.savefig('deque.png')
		plt.clf()
		
		# iterations vs. size of seen
		plt.plot(x, y_s)
		plt.xlabel('Iterations')
		plt.ylabel('Size of Seen')
		plt.savefig('seen.png')
		plt.clf()

		# level vs. number of nodes
		plt.plot(list(nodes.keys()), list(nodes.values()))
		plt.xlabel('Level')
		plt.ylabel('Number of nodes')
		plt.savefig('level.png')
		plt.clf()

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
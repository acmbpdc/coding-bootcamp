import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import deque
from main import wiki, get_pages



def store_details(title, csv):
	"""
	Parse the webpage and store the details from the table into a CSV file if it has all the columns
	
	Arguments:
		title {str} -- celebrity title
		csv {str} -- path to csv file
	"""
	# Create a bs4 object for the webpage
	response = requests.get(wiki(title))
	soup = BeautifulSoup(response.content, 'html.parser')
	
	# Information to be extracted
	header = ['Name', 'Nickname', 'Born', 'Birthplace', 'Residence', 'Occupation', 'Father', 'Mother', 'Website']

	try:
		# Get the table of celebrity details
		body = soup.find('table', class_='infobox').tbody

		# Extract information by unique class names
		# Attributes present in personalities
		born = body.find(class_='bday').text
		name = body.find(class_='fn').text
		nickname = body.find(class_='nickname').text
		residence = body.find(class_='label').text

		# Optional
		birthplace = body.find(class_='birthplace')
		birthplace = birthplace.text if birthplace else None
		occupation = body.find(class_='role')
		if not occupation:
			occupation = None
		else:
			if occupation.find('li'):
				occupation = occupation.li
			occupation = occupation.text
		url = body.find(class_='url')
		url = url.text if url else None

		# Extract information by searching a string and getting the parent tag
		parent = body.find('th', string='Parent(s)')
		if not parent:
			father, mother = [None, None]
		else:
			father, mother = [li.text for li in parent.parent.find_all('li')]

		# Append details to CSV file
		row = [name, nickname, born, birthplace, residence, occupation, father, mother, url]
		df = pd.DataFrame(row).T
		if not os.path.isfile(csv):
			df.to_csv(csv, header=header, index=False)
		else:
			df.to_csv(csv, mode='a', header=False, index=False)
	except:	# does not contain any one or more attributes
		pass



def celebrity_to_csv(csv):
	"""
	Keep storing details of celebrities into one csv file unless suspended
	"""
	i = 1
	seen = set()
	d = deque(['Bill_Gates'])

	while d:
		# Get element in front
		title = d.pop()
		seen.add(title)
		store_details(title, csv)
		print(f'{i}) Parsed: {title}, Deque: {len(d)}, Seen: {len(seen)}')

		urls = get_pages(title)
		urls -= seen

		# Update structures with new urls
		seen |= urls
		d.extendleft(urls)
		i += 1



if __name__ == '__main__':
	celebrity_to_csv('celebrity_details.csv')
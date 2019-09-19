# Bootcamp Orientation

Over the course of this workshop, you will be introduced to various technologies.

The learning is interaction based.
You will be shown how to use the different tools and how you can apply them to solve different problems.

Today's session is a little different from what is to follow.
We will be showcasing a few projects that we developed using the technologies that you will learn through this bootcamp.


## Python and Command Line workflow

Since [Python](https://www.python.org/) has a simple structure, it is very beginner friendly.

It is also perhaps why it has a large collection of libraries maintained by an ever growing community.

One such library is [OpenCV](https://opencv.org/), which is used for image processing.

This library was used in creating [image-to-ascii](https://github.com/aarondecosta/image-to-ascii), a simple command line tool that can convert images to text based art.

```
usage: python converter.py [-h] [-o] [-v] [-c] [-b] [-s  | -w ] image_path

Convert an Image to ASCII Art

positional arguments:
  image_path      Path to Image File

optional arguments:
  -h, --help      show this help message and exit
  -o , --output   Path to Output File
  -v, --verbose   Print Verbose
  -c, --color     Color
  -b, --braille   Braille
  -s , --scale    Scale Factor
  -w , --width    New Width
```

![Stranger Things](./stranger-things.jpg)
![Stranger Things, Text](./stranger-things-text.png)

Using the `write` command for [Unix](https://en.wikipedia.org/wiki/Unix) systems, we can send anyone logged in on a server a picture this way.

## Automation

The following script spams a website that rewards users based on a referral program.

It creates referrals by generating random names and email ids.

```python
# spam.py
import json
import names
import random
import string
import requests



def random_email():
    ''' Returns a string representing a random email '''
    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com", "outlook.com"]
    letters = string.ascii_lowercase[:12]
    email = ''.join(random.choice(letters) for i in range(random.randint(5, 10)))
    email = email + ''.join(random.choice(string.digits) for i in range(random.randint(1, 5)))
    email = email + ''.join(random.choice(letters) for i in range(random.randint(1, 6)))
    email = email + '@' + random.choice(domains)
    return email



def spam_user():
    ''' Spams HOPI's website with random username '''
    # Generating a random user
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    email = random_email()

    # POST request parameters
    url = 'https://app.viral-loops.com/api/v2/events'

    headers = { 'Content-Type': 'application/json',
                'Origin': 'https://behopi.com',
                'Referer': 'https://behopi.com/?referralCode=Wx3CF6G&refSource=copy',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                'X-BC': '[{"key":"language","value":"en-US"},{"key":"color_depth","value":24},{"key":"pixel_ratio","value":1},{"key":"resolution","value":[1366,768]},{"key":"available_resolution","value":[1366,728]},{"key":"timezone_offset","value":-240},{"key":"session_storage","value":1},{"key":"local_storage","value":1},{"key":"indexed_db","value":1},{"key":"open_database","value":1},{"key":"cpu_class","value":"unknown"},{"key":"navigator_platform","value":"Win32"},{"key":"do_not_track","value":"unknown"}]',
                'X-FP': '40e037351d7d82c641288ba002b5aa96',
                'X-UCID': 'M3LqOT76h1NebJ5Pb4lvVfDDW6s' }

    payload = {
                "params": {
                    "event":"registration",
                    "user": {
                        "firstname": firstname,
                        "lastname": lastname,
                        "email": email
                    },
                    "referrer": {"referralCode":"Wx3CF6G"},
                    "refSource":"copy"
                },
                "publicToken":"M3LqOT76h1NebJ5Pb4lvVfDDW6s" }

    # Sending the request
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Spammed for user {} with email {}".format(firstname, email))



for x in range(10):
    spam_user()
```

This script runs only for 10 users. This can be circumvented by using the `watch` Unix command.

## Web Development

We can use Python as a backend for websites too.

The [Django Web Framework](https://www.djangoproject.com/) was used in creating [mouseless](https://github.com/acmbpdc/mouseless), a website for a quiz like competition.


## Competitive Programming

The concept of sorting algorithms is a good example to demonstrate the core idea behind competitive programming.

The [p5.js](https://p5js.org/) graphic library was used to create [p5-gallery](https://github.com/bagofbolts/p5-gallery) to visualize these algorithms


## Machine Learning

One of the most simple projects to understand and implement is a digit recognizer, trained on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/).

Although [Digit-Recognizer](https://github.com/Mohammed-Shoaib/Digit-Recognizer) was built in JavaScript, the main model was trained using Python.


We can implement the latest state-of-the-art algorithms using Python.

The [UMAP algorithm](https://umap-learn.readthedocs.io/en/latest/#) was implemented in [Genomic Data Visualization Pipeline
](https://github.com/kelvindecosta/genomic-data-visualization-pipeline), which found patterns in genomic data for different population mappings.
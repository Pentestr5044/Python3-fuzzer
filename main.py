from bs4 import BeautifulSoup as bs
import httpx
import os
import argparse as arg



parser = arg.ArgumentParser(description="This is a python fuzzer for multiple uses", prog="FuzzyWuzzy")
parser.add_argument('-u', '--url', help="url list to pass through")
parser.add_argument('-us', '--username', help="file that holds usernames to fuzz")
parser.add_argument('-pw', '--password', help="this is the file that holds passwords to fuzz")
parser.add_argument('-d', '--domains', help="domains to check for validity")

args = parser.parse_args()
url=args.url
user=args.username
passw=args.password
domain=args.domains

if url:
    with open(url) as file:
        for lines in file:
            try:
                client = httpx.Client(follow_redirects=True)
                r = client.get("http://"+lines+"/")
                r1 = client.get("https://"+lines+"/")
            finally:
                if r.status_code == 200:
                    print(r.url)
                elif r1.status_code == 200:
                    print(r1.url)
                else:
                    exit()
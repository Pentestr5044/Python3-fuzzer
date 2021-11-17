from bs4 import BeautifulSoup as bs
import httpx
import os
import argparse as arg
import re


parser = arg.ArgumentParser(description="This is a python fuzzer for multiple uses", prog="FuzzyWuzzy")
parser.add_argument('-u', '--url', help="enter FUZZ to fuzz the url of your choice")
parser.add_argument('-us', '--username', help="file that holds usernames to fuzz")
parser.add_argument('-pw', '--password', help="this is the file that holds passwords to fuzz")
parser.add_argument('-d', '--domains', help="domains to check for validity")
parser.add_argument('-w', '--wordlist', help="This is the flag for adding your wordlist")

args = parser.parse_args()
url=args.url
w = args.wordlist
user=args.username
passw=args.password
domain=args.domains

if domain:
    with open(domain) as file:
        for lines in file:
            try:
                client = httpx.Client(follow_redirects=True)
                r = client.get("http://"+lines+"/")
                r1 = client.get("https://"+lines+"/")
            except httpx.ConnectError:
                print("!!!Can't reach website!!!")
            finally:
                if r.status_code == 200:
                    print(r.url)
                elif r1.status_code == 200:
                    print(r1.url)
                else:
                    exit()
if url:
    with open(w) as word:
        for w in word:
            try:
                newurl = url.replace("FUZZ", w)
                furl = newurl.strip('\n')
                client = httpx.Client()
                r = client.get(furl)
            except httpx.ConnectError:
                print("TEST!!!@#!@#!@#$!@#$%!$%@#$%")
            finally:
                try:
                    if r.status_code == 200:
                        print(r.url)
                except:
                    print('Take A DAB!!!!@!')
                    print(furl)

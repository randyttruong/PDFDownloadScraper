"""
Powerpoint and PDF Scraper 
Author: Randy Truong 
Date: 15 November 2022

Description:  
This program is just made to take different webpages and scrape all of their hyperlinks,
and then with the hyperlinks, download their contents.

This program is mainly just a resource for me to download all of the slides/worksheets for different CS courses online. 
"""

from bs4 import BeautifulSoup as bs
import requests as rq
import os 
import sys 
import wget 

# Retrieve Command-Line Arguments 
# print(f"The passed in arguments are: {sys.argv}. There are a total of {len(sys.argv)} arguments") 

sysArgs = sys.argv[1:]
    
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def pretty_folders(): 
    current_directory = os.listdir()
    print("The current folders in your directory are:")
    for each in current_directory: 
        if os.path.isdir(each): 
            print(each) 

def get_all_links(soup):
    ''' 
    Parameters-- 
    soup: soup object of the current link 
    '''
    urls = []
    all_urls = soup.find_all("a")
    for url in all_urls:
        if "href" in url.attrs and ".pdf" in url.attrs["href"]: 
            urls.append(url.attrs["href"])
    return urls

def download_links(url, directory=(f"{os.getcwd()}/downloads")): 
    page_id = "https://www.cs.cmu.edu/~charlie/courses/17-214/2021-spring/"
    req = rq.get(url, headers) 
    soup = bs(req.content, 'html.parser')
    links = get_all_links(soup)
    user_in = input(f"Would you like to download all {len(links)}? [Y/n] ")
    if user_in.lower() == "y": 
        for link in links: 
            final_url = (page_id + link)
            print(f"Getting {final_url}")
            wget.download(page_id + link, out=directory)
    elif user_in.lower() == "n":
        None 
    else:
        print("Please try again.") 
        download_links(url)

print(os.getcwd())
pretty_folders()
for url in sysArgs: 
    download_links(url)
    


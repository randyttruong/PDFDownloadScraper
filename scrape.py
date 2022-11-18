"""
Powerpoint Scraper 
Author: Randy Truong 
Date: 15 November 2022

Description:  
This program is just made to take different webpages and scrape all of their hyperlinks,
and then with the hyperlinks, download their contents.

This program is mainly just a resource for me to download all of the slides/worksheets
for different CS courses online. 
"""

from bs4 import BeautifulSoup as bs
from urllib.request import (
	urlopen, urlparse, urlunpause, urlretrieve) 
import os 
import sys 
import re 
from treelib import Node, Tree  

def get_all_links(soup):
    ''' 
    Parameters-- 
    soup: soup object of the current link 
    '''
    
    urls = []
    all_urls = soup.find_all("a")
    for url in all_urls:
        if "href" in url.attrs and url.attrs["href"] == "pdf":
            urls.append(url.attrs["href"])
    return urls

class WebPage:
	def __init__(self, page_directory, page_id): 
		self.page_id = page_id 
		self.WebPageSoup = soup()
        self.links = get_all_links(self.WebPageSoup)



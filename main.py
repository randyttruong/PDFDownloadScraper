"""
PDF Scraper 
Author: Randy Truong 
Date: 15 November 2022

Description:  
This program is just made to take different webpages and scrape all of their hyperlinks,
and then with the hyperlinks, download their contents.

This program is mainly just a resource for me to download all of the slides/worksheets for different CS courses online. 
"""

from bs4 import BeautifulSoup as bs
import requests as rq
import os, sys, wget, typer 

# Retrieve Command-Line Arguments 
# print(f"The passed in arguments are: {sys.argv}. There are a total of {len(sys.argv)} arguments") 

sysArgs = sys.argv[1:]

app = typer.Typer()
    
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


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

def y_or_n(response, links, page_id, directory): 
    if response.lower() == "y": 
        os.system('cls')
        os.system('clear')
        for link in links: 
            final_url = (page_id + link)
            print(f"Getting {final_url}")
            wget.download(page_id + link, out=directory)
    elif response.lower() == "n":
        return None  
    else:
        print("Please try again.") 


@app.command()
def main(
        url: str= typer.Argument(...), 
        page_id: str= typer.Argument(...),
        directory: str= typer.Option("./downloads", help="Change output directory")
        ): 
    """
    Args: \n 
    URL: URL of page to be scraped (whole link) \n 
    Page_ID: The directory of the current page (just the root directory)
    """
    request = rq.get(url, headers)
    soup = bs(request.content, 'html.parser')
    links = get_all_links(soup)
    user_in = input(f"Are you sure you want to download {len(links)} to {directory}? [Y/n] ")
    y_or_n(user_in, links, page_id, directory)

    
if __name__ == "__main__":
    app()

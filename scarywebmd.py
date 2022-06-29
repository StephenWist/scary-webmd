# user inputs string of conditions to search clinvar
# e.g. "inflamed thyroid"
# and is given the link to/abstract of all relevant publications
# from the clinvar results
import argparse
import sys
import requests
import subprocess
from bs4 import BeautifulSoup

class argParser:
    # parse user given string

    def __init__(self):
        self.args = None

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Search ClinVar Like It\'s WebMD.')
        parser.add_argument('query', type=str, nargs='+', help='Search Query')
        self.args = parser.parse_args()
        
        return self.args.query

class searchClinVar:
    # handles requests of and parsing of clinvar html
    
    def __init__(self, query):
        self.ncbi_url = 'https://www.ncbi.nlm.nih.gov'
        self.base_url = 'https://www.ncbi.nlm.nih.gov/clinvar/?term='
        self.search_url = self.base_url
        self.entrez_cmd = ['efetch', '-db', 'pubmed', '-format', 'abstract', '-id']
        self.query = query
        self.pubs = []
        self.pub_count = 0

    def build_query(self):
        # URL built for querying ClinVar
        for q in self.query:
            # add '+' to previous query term
            if self.search_url[-1] != '=':
                self.search_url += '+'
            self.search_url += q
        self.query_cv()
        return True

    def query_cv(self):
        # get main page results
        r = requests.get(self.search_url)
        r = r.text

        if self.parse_main(r):
            print(f'Publications Found: {self.pub_count}')
        else:
            print(f'Error parsing {self.search_url}. Exiting...')
            sys.exit()
        return True

    def parse_main(self, r):
        # parse main page results and get links to sub pages
        soup = BeautifulSoup(r, 'html.parser')
        links = soup.find_all('a', {'class': 'blocklevelaintable variant_title'})
        
        # build urls to  subpages
        for l in links:
            link = l['href']
            sub_url = self.ncbi_url + link
            self.query_sub(sub_url)

        return True

    def query_sub(self, url):
        # get subpage html
        r = requests.get(url)
        r = r.text

        if self.parse_sub(r):
            pass
        else:
            print(f'Error parsing subpage {url}. Exiting...')
            sys.exit()
        return True

    def parse_sub(self, r):
        # parse subpage and get links to pubmed publications
        # add these links/abstracts to self.pubs
        soup = BeautifulSoup(r, 'html.parser')
        citations = soup.find_all('a', {'data-ga-action':'PMID citation'})
        # get citation pubmed id
        # it will be used to get abstracts
        for c in citations:
            link = c.contents
            self.pubs.append(link) 
            self.pub_count += 1

        self.get_abstracts()
        return True

    def get_abstracts(self):
        # use entrez direct to get abstract of papers
        for p in self.pubs:
            self.entrez_cmd += p
        subprocess.run(self.entrez_cmd)
        return True



if __name__ == '__main__':
    
    args = argParser()
    a = args.parse_args()

    searcher = searchClinVar(a)
    searcher.build_query()
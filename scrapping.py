
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/'

quote_from_good_read = urllib.request.urlopen(url)

soup = BeautifulSoup(quote_from_good_read)

div_tags = soup.find("div",class_='featureTeaserBox__quotesBox').find("div",class_="featureTeaserBox__quotesBoxQuote")

all_quotes = div_tags.findAll("div",class_="quoteText")

list_of_quotes = []

list_of_author = []


final_data = []
for i in all_quotes:
    q = i.find(text=True)
    q = q.replace("\n",'')
    q = q.lstrip()
    q = q.rstrip()
    a = i.find("span",class_="authorOrTitle").find(text=True)
    a = a.replace("\n",'')
    a = a.lstrip()
    a = a.rstrip()
    data = {
        "quote":q,
        "author":a
    }
    final_data.append(data)
'''
import requests
# print("list of authors-->",final_data)    
len_list = len(final_data)

for k in range(0,len_list):
    quote = final_data[k]["quote"]
    author = final_data[k]["author"]
    data = {
        "quote":quote,
        "author":author
    }
    
    quote_post = requests.post("http://127.0.0.1:8000/post/",data=data)
    print("posted successfully")
'''
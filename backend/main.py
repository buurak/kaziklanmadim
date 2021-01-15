from typing import Optional
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()


@app.get("/{search_variable}")
def read_root(search_variable:str):
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    url = 'https://www.cimri.com/' + search_variable
    req = requests.get(url, headers)
    
    soup = BeautifulSoup(req.content, 'html.parser')
    myscdivs = soup.find_all('div',{"class":"z7ntrt-0 cLlfW s1a29zcm-9 jvSenz"})
    title = ''
    price = ''
    products = {}
    for text in myscdivs:
        title = text.find("h3",{"class":"product-title"}).text
        price = text.find("div",{"class":"top-offers"}).text
        products.update({title:price.split('TL')[0]})
    print(products)

    return products



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
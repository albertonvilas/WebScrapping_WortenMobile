__author__ = "Alberto Neto Vilas"
__email__ = "anv7345@gmail.com"

from bs4 import BeautifulSoup
import requests
from pandas import DataFrame
import datetime

page = requests.get("http://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones?page=1&vendido-por=Worten")
soup = BeautifulSoup(page.content, 'html.parser')

def getpages():
    pageblock = soup.find('div', class_='w-pagination-block')
    pages = soup.find_all('a', rel='next')
    nrpage=int(pages[len(pages)-1].get_text())
    return nrpage


dictNamePrice=dict()

def retrive_products(nrpage):

    for i in range(nrpage+1):      # Number of pages plus one
        url = "http://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones?page={}&vendido-por=Worten".format(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_products = soup.find_all('div', class_='w-product__content')
        for product in all_products:
            product_name = product.find('h3', class_='w-product__title')
            product_price = product.find('span', class_='w-currentPrice iss-current-price')
            product_price = product_price.get_text()[1:]
            dictNamePrice[product_name.get_text()]=product_price
    date = str(datetime.date.today())
    df = DataFrame({'Modelo': list(dictNamePrice.keys()), 'Preço': list(dictNamePrice.values())})
    df.to_excel('PrecosWorten'+date+'.xlsx', sheet_name='sheet1', index=False)


if __name__ == '__main__':
    retrive_products(getpages())

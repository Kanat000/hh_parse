import requests as req
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
db_name = 'company_db'

path_to_driver = "C:/tools/chromedriver/chromedriver.exe"


def get_soup(url):
    res = req.get(url, headers=headers)
    return BeautifulSoup(res.text, 'lxml')


item_code='005930'
page_no=1

url= f"https://finance.naver.com/item/board.naver?code={item_code}&page={page_no}"



import requests

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

response = requests.get(url, headers=headers)

response.text


from bs4 import BeautifulSoup as bs

html = bs(response.text,'lxml')
bs_table=html.select('table')
bs_table


import pandas as pd

table = pd.read_html(str(bs_table))

temp=table[1]


temp

temp.drop('Unnamed: 6',axis=1)


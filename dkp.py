import requests 
from bs4 import BeautifulSoup as bs


header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

}

a = requests.get('https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code=4399900000&mdiv=1099700000-bt_0_957_01-&ctype=B',headers=header)
b = bs(a.text,'lxml')

c = b.select('div.TabContentD ul li p span')

print(c)
# for i in c:
#     print(i.get_text())



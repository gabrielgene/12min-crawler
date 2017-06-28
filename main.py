import requests
from bs4 import BeautifulSoup
import os


s = requests.session()
url = 'https://app.12min.com.br/users/sign_in'
login_response = s.get(url)
token_soup = BeautifulSoup(login_response.text, 'lxml')
token = token_soup.find('input', {'name': 'authenticity_token'}).get('value')

data = {
  'utf8':'✓',
  'authenticity_token':token,
  'user[email]':'YOUREMAIL',
  'user[password]':'YOURLOGIN',
  'commit':'Entrar'
}

login_response = s.post(url, data)
book_page = s.get('https://app.12min.com.br')
html_soup = BeautifulSoup(book_page.text, 'lxml')
div_list = html_soup.select('div.my-books div.tabs-content div.tab-pane div div')
for div in div_list:
  x = div.select('p')
  if x:
    a = x[0].find_next_sibling('a').get('href')
    print(a)
    book_response = s.get('https://app.12min.com.br'+a)
    book_soup = BeautifulSoup(book_response.text, 'lxml')
    book = book_soup.select('div.book-reading-content')
    name = a
    file_n = name.replace('/', '')
    file_name = file_n+'.html'
    x = open(file_name, 'w')
    x.write('<meta charset="UTF-8">')
    x.write('<link rel="stylesheet" href="style.css">')
    x.write(str(book[0]))
    x.close()

print('----finish-----')

import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://ridibooks.com/category/books/123?page=1")
soup = bs(page.text, "html.parser")

elements = soup.select('a.thumbnail_btn')

for index, element in enumerate(elements, 1):
    book_uri = element["href"]
    book_page = requests.get("https://ridibooks.com"+book_uri)
    book_soup = bs(book_page.text, "html.parser")
    book_element = book_soup.select("p.introduce_paragraph")
    print(book_element[0].text)

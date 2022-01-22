import requests
import bs4

"""https://books.toscrape.com/ 
 Title of the books which has 2 star rating
 """

two_star = []
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

for pages in range(1, 51):

    scrape_url = base_url.format(pages)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star.append(book.select('a')[1]['title'])

print(two_star)


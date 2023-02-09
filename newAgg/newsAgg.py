import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news"
res = requests.get(url)
html_content = res.text
soup = BeautifulSoup(html_content, "html.parser")
articles = soup.find_all("a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")

for article in articles:
    print(article.text.strip())

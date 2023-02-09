import requests
from bs4 import BeautifulSoup
url = "https://www.example.com"


def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text
    print(title)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    scraper(url)


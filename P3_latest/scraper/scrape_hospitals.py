from splinter import Browser
from bs4 import BeautifulSoup

    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url = "http://www.hospitalsafetygrade.org/search?findBy=state&zip_code=&city=&state_prov=CA&hospital="
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["headline"] = soup.find("a", class_="result-title").get_text()
    listings["price"] = soup.find("span", class_="result-price").get_text()
    listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings

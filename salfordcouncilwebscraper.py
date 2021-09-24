import mechanicalsoup
import re
from bs4 import BeautifulSoup as BS

browser = mechanicalsoup.StatefulBrowser()

customerPostCode = ""
customerAddress = ""

url = "https://www.salford.gov.uk/bins-and-recycling/bin-collection-days/"

page = browser.open(url)

browser.select_form('form[action="#propertylist"]')
browser["prop"] = customerPostCode
browser.form.print_summary()
browser.submit_selected()

propertySearchResults = browser.page.find_all(
    "a")

for propertySearchResult in propertySearchResults:
    if propertySearchResult.find(text=re.compile(customerAddress)):
        addressLink = propertySearchResult
        break

print(addressLink)

browser.follow_link(addressLink)

binDataPage = browser.page.find_all('div', attrs={'class': 'waste'})

print(binDataPage)

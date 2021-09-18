from urllib.request import urlopen

url = "https://www.salford.gov.uk/bins-and-recycling/bin-collection-days/"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

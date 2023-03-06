from requests_html import HTMLSession

url = "https://jiji.co.ke/computers-and-laptops"

session = HTMLSession()
results = session.get(url)
results.html.render(sleep=1)

products = results.html.xpath('//*[@id="js-advert-listing-wrapper"]/div/div', first = True)
print(products.absolute_links)
for item in products.absolute_links :
    results = session.get(item)
    name = results.find('div.b-advert-title-outer', first = True).text
    print(name)
    print(name)
    print(name)
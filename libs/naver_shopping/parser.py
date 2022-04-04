from bs4 import BeautifulSoup

def getProductInfo(li):
    img = li.find("img")
    alt = img['alt']
    price = li.find("strong", {"class":"basicList_price__2r23_"}).find('span')
    a_tit = li.find("a", {"class":"basicList_link__1MaTN"})
    href = a_tit['href']
    thumbnail_link = li.find('div', {'class':'thumbnail_thumb_wrap__1pEkS'}).find('a')

    return {"name":alt, "price":price.text.replace(",", ""), "link":href}

def parse(pageString):
    bs_obj = BeautifulSoup(pageString, "html.parser")
    ul = bs_obj.find("ul", {"class":"list_basis"})
    lis = ul.findAll("li", {"class":"basicList_item__2XT81"})

    products = []
    for li in lis:
        try:
            products.append(getProductInfo(li))
        except Exception as e:
            print("--error--", e)

    return products


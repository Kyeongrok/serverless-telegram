from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse

keyword = '핸드백'
page_string = crawl(keyword)
products = parse(page_string)
print(products[0])

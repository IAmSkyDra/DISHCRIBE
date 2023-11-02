# Thu thập dữ liệu web với thư viện selenium và lxml
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import os
class product:
    def __init__(self, name, price, unit, scale):
        self.name = name
        self.price = int(str(price).replace(".", "", 1))
        self.unit = unit
        self.scale = scale
    def json(self):
        return "{" + f'"name" : "{self.name}", "price" : "{self.price}", "unit" : "{self.unit}", "scale" : "{self.scale}"' + "}"
def createList(NAME): # Tạo danh sách sản phẩm đã thu thập từ trang web
    driver = webdriver.Chrome()
    driver.get(f"https://www.bachhoaxanh.com/{NAME}")
    # Xác định các đường dẫn cố định trên cây HTML, để dễ dàng sử dụng XPath để điều hướng trong mã sau này
    PRODUCT_BOX = "mt-[4px] flex h-full w-full flex-col px-[6px] pb-[4px]"
    PRODUCT_NAME = "product_name mb-2 line-clamp-2 h-[28px] text-[12px] leading-[14px] text-[#9DA7BC] lg:h-[35px] lg:text-14 lg:leading-[17.5px]"
    PRODUCT_PRICE = 'product_price mt-0.5 flex text-15 font-bold leading-4 text-[#192038] lg:text-16 lg:leading-[18px]'
    PRODUCT_UNIT = 'mt-0.5 line-clamp-1 text-11 font-normal text-[#9DA7BC] lg:text-12'
    time.sleep(10)  # Chờ để đảm bảo trang web được tải hoàn toàn, chỉ khi đó thì mã này mới thu thập toàn bộ dữ liệu từ nguồn HTML
    # Bắt đầu điều hướng bằng cách sử dụng XPath
    tree = etree.HTML(driver.page_source)
    element = tree.xpath(f'//div[@class="flex flex-wrap content-stretch bg-[#fff] px-[2px] pt-[4px]"]//div[@class="{PRODUCT_BOX}"]')
    def fix(x):
        if len(x) == 0:
            return "cái"
        return x[0][1:]
    LIST = []
    for x in element:
        name = x.xpath(f".//span[@class='{PRODUCT_NAME}']//text()")[0]
        y = x.xpath(f".//div[@class='{PRODUCT_PRICE}']")
        price = y[0].text
        temp = y[0].xpath(f".//div[@class='{PRODUCT_UNIT}']/text()")
        unit = fix(temp)
        if len(temp) == 0:
            LIST.append(product(name, price, 1, unit))
        else:
            def reFormat(u): # Hàm này giúp tách các đơn vị văn bản đã thu thập từ "/g" thành "/" và "g"
                u = str(u).lstrip().rstrip()
                unt = ""
                scl = ""
                for i in range(len(u)):
                    if u[i].isdigit():
                        unt = unt + u[i]
                    else:
                        break
                for i in reversed(range(len(u))):
                    if u[i].isalpha():
                        scl = u[i] + scl
                    else:
                        break
                return [unt, scl]
            re_format = reFormat(unit)
            LIST.append(product(name, price, re_format[0], re_format[1]))
    driver.quit()
    return LIST
def outFile(link, NAME): # Xuất danh sách đã tạo ra file .json
    LIST_OF_PRODUCT = createList(link)
    for x in LIST_OF_PRODUCT:
        print(x.json())
    with open(f"list_{NAME}.json", "w", encoding="utf-8") as f:
        f.write("{\n\t" + f'"name":"{NAME}",\n\t"product":[\n')
        i = 0
        for x in LIST_OF_PRODUCT: # Chỉ in danh sách vào file
            i += 1
            send = ""
            if i == len(LIST_OF_PRODUCT):
                send = '\n'
            else:
                send = ', \n'
            f.write("\t\t" + x.json() + send)
        f.write("\t]\n}")
    
outFile('thit-heo', "pork")
        
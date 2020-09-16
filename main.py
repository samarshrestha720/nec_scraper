from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get(
    "http://nec.edu.np/index.php?option=com_content&view=category&id=47&Itemid=74"
)

whole_page = driver.find_element_by_tag_name("html")
page = whole_page.find_element_by_xpath("//tbody")
first_elem = page.find_element_by_xpath("//tr[@class='sectiontableentry1']/td[3]").text
link = page.find_element_by_xpath("//tr[@class='sectiontableentry1']")

hits = int(first_elem)

if hits < 100:
    link.click()
    
else:
    print("NO NEW NOTICES!!")
    driver.close()

print("HITS: ", hits)


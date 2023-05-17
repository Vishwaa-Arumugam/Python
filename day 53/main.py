
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

GOOGLE_SHEET_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSc86LAkKROjEkhdvnSs4ptAtkBFr1wdq3fOpeIdiI7i7nvmDg/viewform?usp=sf_link"

ZILLOW_LINK = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(ZILLOW_LINK, headers=headers)
website_html = response.text

link_soup = BeautifulSoup(website_html, "html.parser")
all_link = link_soup.find_all("a",
                              {"class": "StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link"})

final_link = []

for i in all_link:
    link = i["href"]
    if "https" not in link:
        full_link = f"https://www.zillow.com/b/argenta-san-francisco-ca-5Xj7m7/{link}"
        final_link.append(full_link)

price = link_soup.find_all("span", {"data-test": "property-card-price"})

all_price = []

for p in price:
    all_price.append(p.getText().split("+")[0])
del all_price[-2:]

address = link_soup.find_all("address", {"data-test": "property-card-addr"})

all_addresses = []

for a in address:
    all_addresses.append(a.getText())
del all_addresses[-2:]

# ------------SELENIUM

driver = webdriver.Chrome()

sleep(2)
count = 0

for i in range(len(all_link)):
    driver.get(GOOGLE_SHEET_LINK)

    driver.maximize_window()

    address_text = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_text = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_text = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_text.send_keys(all_addresses[i])
    price_text.send_keys(all_price[i])
    link_text.send_keys(final_link[i])

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    count += 1
    if count == len(all_addresses):
        driver.quit()




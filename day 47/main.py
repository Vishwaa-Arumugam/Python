import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
URl = "https://www.amazon.in/Armani-Exchange-Analog-Black-Watch-AX2164/dp/B00VB71TVU/ref=sxin_26?asc_contentid=amzn1.osa.8fbc9648-47b5-4a87-bbf6-28cb637ddf80.A21TJRUUN4KGV.en_IN&asc_contenttype=article&ascsubtag=amzn1.osa.8fbc9648-47b5-4a87-bbf6-28cb637ddf80.A21TJRUUN4KGV.en_IN&content-id=amzn1.sym.feb2b32b-0085-4665-973c-36b431684408%3Aamzn1.sym.feb2b32b-0085-4665-973c-36b431684408&creativeASIN=B00VB71TVU&cv_ct_cx=watches+for+men&cv_ct_id=amzn1.osa.8fbc9648-47b5-4a87-bbf6-28cb637ddf80.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&keywords=watches+for+men&linkCode=oas&pd_rd_i=B00VB71TVU&pd_rd_r=4d0197fa-dbf9-41eb-bb43-5592222d8dd6&pd_rd_w=v6HdG&pd_rd_wg=kcUiI&pf_rd_p=feb2b32b-0085-4665-973c-36b431684408&pf_rd_r=RATPJSJH47ZZENS3S938&qid=1679154321&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=watch%2Caps%2C200&sr=1-2-c84eb971-91f2-4a4d-acce-811265c24254&tag=sm-content-21"

my_email = "05451"
password = ""

response = requests.get(URl, headers=headers)
response.raise_for_status()
website_html = response.text


amazon_soup = BeautifulSoup(website_html, "html.parser")

price_list = amazon_soup.find_all(name="span", class_="a-price-whole")
print(price_list)
price = [product_price.getText() for product_price in price_list[0]]
price = price[0].replace(",", "")

name = amazon_soup.find_all(name="span", id="productTitle",
                            class_="a-size-large product-title-word-break")
product_name = [name.text for name in name]
for name in product_name:
    amazon_product_name = name
print(amazon_product_name)

if price < "20000":
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vishwaa1528@gmail.com",
            msg=f"Subject:Amazon Price Alert\n\n{amazon_product_name} is now {price}"
        )
        print("mail sent successfully")

else:
    print("Mail has not sent successfully")

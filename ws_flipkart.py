from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as Ureq

my_url = "https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_2&otracker1=AS_Query_HistoryAutoSuggest_0_2&as-pos=0&as-type=HISTORY&as-backfill=on"
uClient = Ureq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"_1-2Iqu row"})
print(len(containers))

# print(soup.prettify(containers[0]))

container = containers[0]
# name = container.findALL("div", {"class":"col col-7-12"})
# print(name[0])
# name =container.div("div",{"class":"_3wU53n"})
name1 =container.findAll("div",{"class":"_3wU53n"})
# print(name1[0].text,end="\n")

price1 = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
# print(price1[0].text,end="\n")

rating1 = container.findAll("div",{"class":"niH0FQ"})
# print(rating1[0].text, end ="\n")

#Extracting data from website to File
filename ="mob_products.csv"
f = open(filename,"w")

headers ="Product_Name,Pricing,Rating\n"
f.write(headers)

for container in containers:
    product_name_container = container.findAll("div",{"class":"_3wU53n"})
    product_name = product_name_container[0].text

    price_container = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div",{"class":"niH0FQ"})
    rating = rating_container[0].text

    print("Product Name :",product_name,"\nPrice :",price,"\nRatings :",rating)


    #String Parsing
    trim_price = ''.join(price.split(','))
    rm_rupees = trim_price.split("₹")
    add_rs_price = "Rs." + rm_rupees[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(",")
    final_rating = split_rating[0]

    print(product_name.replace(",","|")+"," + final_price + "," +final_rating +"\n")
    f.write(product_name.replace(",","|")+"," + final_price + "," +final_rating +"\n")
f.close()
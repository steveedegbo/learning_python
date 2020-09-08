from bs4 import BeautifulSoup
import requests

# html_file = open("index.html", "r")

# html_data = html_file.read()


# soup = BeautifulSoup(html_data, features="html.parser")


# # print(soup)


# filtering = soup.find("h3")

# print(filtering.text)



#USING BEAUTIFUL SOUP WITH RESOURCES ON THE INTERNET

# jumia_url = "https://www.jumia.com.ng/smartphones/"

# jumia_request = requests.get(jumia_url)

# jumia_html = jumia_request.content


# # print(jumia_html)

# jumia_soup = BeautifulSoup(jumia_html, features = "html.parser")


# h3_filter = jumia_soup.find_all("h3")

# for product in h3_filter:

#     print(product.text)
    
#     print()
    

#ASSIGNMENT SCRAPE WIKI NIGERIA, capital to government

wiki_url = "https://en.wikipedia.org/wiki/Nigeria"

wiki_request = requests.get(wiki_url)

wiki_html = wiki_request.content

# print(wiki_html)

wiki_soup = BeautifulSoup(wiki_html, features = "html.parser")

rows = wiki_soup.find_all(['tr', 'th'])

# print(rows)

for row in rows:

    print(row.text)

    print()

    if row.text == "Government":
        break
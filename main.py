#import the libraries
import requests
from bs4 import BeautifulSoup

#putting the url of our scraping website
url = "https://www.w3schools.com/"
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content

#print(htmlContent)	or parsing html
soup=BeautifulSoup(htmlContent, 'html.parser')
#we can well arange or prettyfy the HTML content 
print(soup.prettify)

#get the title of html page
print(type(title))

#get all the paragraphs pf the page
paras = soup.find_all('p')
print(paras)

#print(anchors)
#step to get the first para
print(soup.find('p'))

#step to get the first para & class
print(soup.find('p')['class'])

#find all the elements with class 'lead'
#print(soup.find_all('p', class_="lead"))

#get the text from tag/soup
print(soup.find('p').get_text())
print(soup.get_text())

#get all the anchor tags pf the page
anchors = soup.find_all('a')
all_links= set()
for link in anchors:
    if(link.get('href') !='#'):
        linktext = 'https://www.w3schools.com/' +link.get('href')
        all_links.add(link)
        print(linktext)


#contents= A tag's children are available as a list 
#children= A tag's children are available as a generators 
#navbarSupportedContent=soup.find(id='navbarSupportedContent')
#for elem in navbarSupportedContent:
    #print(elem)

#to get the string from selected id
#for item in navbarSupportedContent.stripped_strings:
    #print(item)
#print(navbarSupportedContent.previous_sibling.previous_sibling) 







#From these steps we can scrap the desired data from given url and convert it toa csv file

import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find_all('table')[1]

    rows = table.select('tbody > tr')

    header = [th.text.rstrip() for th in rows[0].find_all('th')]

    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)


if __name__=="__main__":
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    scrape_data(url)




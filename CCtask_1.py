# code for python web scraping
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.coreyms.com').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary'])


for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div',class_='entry-content').p.text
    print(summary)



#print(article.prettify())

#
#
#

    vid_src = article.find('iframe',class_='youtube-player')['src']
#print(vid_src)





try:
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    print(vid_id)
except Exception as e :
    ytube_link = None



csv_writer.writerow([headline,summary])


csv_file.close()

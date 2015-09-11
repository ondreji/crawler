import os

__author__ = 'haibo'
from pyquery import PyQuery as pq
import requests

# for num in range(1340,1349):

url = "http://jandan.net/ooxx/page-"+str(num)

html_content = pq(url)
# print(html_content)

for anchor in html_content('img'):
    # print(anchor)
    anchor = html_content(anchor)

    jpeg_link= anchor.attr('src')
    print(jpeg_link)


    r = requests.get(jpeg_link)

    filename =os.path.basename(jpeg_link)
    with open(filename, "wb") as pic:
        pic.write(r.content)

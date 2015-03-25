import os

__author__ = 'haibo'
from pyquery import PyQuery as pq
import requests

# def jiandan():
#     for num in range(1300,1356):
#
#         url = "http://jandan.net/ooxx/page-"+str(num)
#         html_content = pq(url)
#     # print(html_content)
#
#         for anchor in html_content('#comments p>img'):
#             # print(anchor)
#             anchor = html_content(anchor)
#
#             jpeg_link= anchor.attr('src')
#             print(jpeg_link)
#
#
#             r = requests.get(jpeg_link)
#
#             filename =os.path.basename(jpeg_link)
#             with open(filename, "wb") as pic:
#                 pic.write(r.content)
#
#         # time.sleep(2)

def downloadfile(url):
    r = requests.get(url)
    filename =os.path.basename(url)
    with open(filename, "wb") as pic:
        pic.write(r.content)
# al
#
#
def douban(albumurl,photosPerPage,pageCount):
    for num in range(0,pageCount):
        url = albumurl+str(num*photosPerPage)
        print(url)
        html_content = pq(url)
        for anchor in html_content('div.photolst.clearfix a>img'):
            anchor = html_content(anchor)

            jpeg_link= anchor.attr('src')
            print(jpeg_link)
            downloadfile(jpeg_link.replace('thumb','photo'))
if __name__ == '__main__':
    print("main")
    # douban(u'http://www.douban.com/photos/album/127493069/?start=',18,22)
    # pass
    douban(u'http://www.douban.com/photos/album/152360818/?start=',18,2)
    # http://www.douban.com/photos/album/105181925/

from bs4 import BeautifulSoup as BS
from optparse import OptionParser
import urllib2


parser = OptionParser()
parser.add_option("-m", "--manga", dest="manga",
                          help="Name of the manga")
parser.add_option("-c", "--chapter", dest="chapter",
                          help="Chapter number")

(options, args) = parser.parse_args()


"""
data = urllib2.urlopen(url)

"""

chap_pages = []
url = 'http://mangareader.net' + '/' +options.manga +'/'+ options.chapter
base_url = 'http://mangareader.net'
   

def validate_url(url):
    """
        Test if an url opened with urllib2 return a 200 code or 404
    """
    if url.code == 200:
        return True
    else:
        return False


def get_chapter_pages(source):
    """
    'source' is the result of urllib2.urlopen funct 
    a valid page of the chapter can be used for retrieving it
    retrieve the page number and the url of the different page in the chapter
    """
    content = source.read()
    data = BS(content, 'html')
    tmp = data.find(id='pageMenu')
    for option in tmp.find_all('option'):
        chap_pages.append(option['value'])


def download_page_img():
    num_page = 1
    for url in chap_pages:
        page_url = base_url + url
        page = urllib2.urlopen(page_url)
        file = 'page'+str(num_page)+'.jpg'
        down = base_url + url
        resp = urllib2.urlopen(down)
        img = BS(resp.read(), 'html')
        img_data = img.find(id='imgholder').find('img')['src']
        resp = urllib2.urlopen(img_data)
        fh = open(file, 'w')
        fh.write(resp.read())
        fh.close()
        num_page+= 1 


data = urllib2.urlopen(url)
if validate_url(data):
    get_chapter_pages(data)
    download_page_img()



__author__ = 'nmtsylla'

from bs4 import BeautifulSoup as BS
import urllib2
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--manga", dest="manga",
                  help="Name of the manga")
parser.add_option("-c", "--chapter", dest="chapter",
                  help="Chapter number")
parser.set_defaults(m='one-piece')
parser.set_defaults(c='654')

(options, args) = parser.parse_args()

chap_pages = []
url = 'http://mangareader.net' + '/' + options.manga + '/' + options.chapter
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
    slct = data.find(id='pageMenu')
    for option in slct.find_all('option'):
        chap_pages.append(option['value'])


def download_page(page_url):
    link = base_url + page_url
    page_data = urllib2.urlopen(link)
    img = BS(page_data.read(), 'html')
    return img


def extract_img(img):
    img_src = img.find(id='img')['src']
    img_data = urllib2.urlopen(img_src)
    return img_data


def write_to_file(img_data, page):
    fh = open(page, 'w')
    fh.write(img_data.read())
    fh.close()


def save_img(num_page, page_url):
    page = options.manga + '_' + options.chapter + '_' + str(num_page) + '.jpg'
    img = download_page(page_url)
    img_data = extract_img(img)
    write_to_file(img_data, page)


def download_chapter():
    num_page = 1
    for page_url in chap_pages:
        save_img(num_page, page_url)
        num_page += 1



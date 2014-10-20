__author__ = 'nmtsylla'
from function import *

data = urllib2.urlopen(url)
if validate_url(data):
    get_chapter_pages(data)
    download_chapter()
else:
    print 'Le chapitre ou le manga que vous chercher est disponible'


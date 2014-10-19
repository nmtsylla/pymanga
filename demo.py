import urllib2
from bs4 import BeautifulSoup as BS
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-m", "--manga", dest="manga",
                          help="Name of the manga")
parser.add_option("-c", "--chapter", dest="chapter",
                          help="Chapter number")

(options, args) = parser.parse_args()

print args, options

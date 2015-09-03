from urllib2 import urlopen
print 1
xml = urlopen("https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml")

#Found out that urllib is totally different in Python 3. TODO
def fetchxml():
    from urllib2 import urlopen
    import xml.etree.ElementTree as ET
    print 1
    xml = urlopen("https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml")
        
    #The tree is the entire XML tree, and its root is the top level of the tree. In the TfL case, 'stations'. 
    tree = ET.parse(xml)
    root = tree.getroot()

    return root
    #Found out that urllib is totally different in Python 3. TODO as soon as I get my hands on ArcGIS Pro
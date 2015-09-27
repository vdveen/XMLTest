def fetchxml():
    import requests
    import json
    import xml.etree.ElementTree as ET

    url = "https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml"
    http = requests.get(url) 
    root = ET.fromstring(http.text) #fromstring returns the root of the xml directly
    return root

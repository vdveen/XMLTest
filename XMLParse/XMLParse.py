#Goal: 
#Import XML file 
#Put info from XML in a neat class with attributes

import xml.etree.ElementTree as ET


#The tree is the entire XML tree, and its root is the top level of the tree. In this case, 'stations'. 
tree = ET.parse('E:\OneDrive\GIS\Expe\Visual Studio App\livecyclehireupdates.xml')
root = tree.getroot()

#List all the stations
for station in root:
    print station[1].tag, station[1].text


